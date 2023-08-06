__all__ = ["read", "load"]

import contextlib
import mmap
import io

import awkward as ak
import numpy as np
from awkward.forth import ForthMachine32


EVENT_PROGRAM_TEMPLATE = """
        begin
            ( read header )
            data {endian}H-> stack
            data {endian}H-> stack

            ( error when first item is not magic )
            swap 65535 = invert
            if halt then

        ( check we have length )
        dup while
            ( the actual length of payload excludes header )
            4 -

            ( have we have started reading? )
            should_read_next @
            if
                ( have we just stopped reading )
                event @ stop @ >=
                if
                    exit
                else
                    ( convert bytes to n events )
                    4 /

                    ( read events )
                    dup 0 do
                        data {endian}B-> channel
                        data {endian}B-> adc
                        data {endian}H-> value
                    loop

                    ( write number of data in event )
                    num <- stack
                then
            else
                ( update reading flag )
                event @ 1 +
                start @ >= 
                should_read_next !

                data skip
            then

            ( increment event counter )
            1 event +!
        repeat
        drop
"""


# In[6]:


MIDAS_PROGRAM = f"""
input data
input range

variable start
variable stop
variable event
variable should_read_next

output adc uint8
output channel uint8
output value uint16
output num uint16

( assign read range )
range i-> stack start !
range i-> stack stop !

( initialise reading flag )
0 start @ = 
should_read_next !

( main loop )
begin
    begin
        ( see if header is not EBYEDATA )
        data B-> stack 69 =
        data B-> stack 66 =
        data B-> stack 89 =
        data B-> stack 69 =
        data B-> stack 68 =
        data B-> stack 65 =
        data B-> stack 84 =
        data B-> stack 65 =
        and and and and and and and
        invert
    while
        ( find start of current read )
        data pos
        8 -

        ( calculate next aligned location )
        0x3FF invert
        and 0x400 +

        ( exit when out of bounds )
        dup data len >=
        if
            drop exit
        then

        ( seek to new location )
        data seek
    repeat

    ( skip to data endianness because we don't read any fields )
    4 data skip
    2 data skip
    2 data skip
    2 data skip

    ( read data endianness )
    data H-> stack

    ( skip length field )
    4 data skip

    ( convert endianness to bool )
    1 =
    ( process events according to endianness )
    if
        {EVENT_PROGRAM_TEMPLATE.format(endian="")}
    else
        {EVENT_PROGRAM_TEMPLATE.format(endian="!")}
    then
again
"""


def load(buffer, entry_start: int = None, entry_stop: int = None) -> ak.Array:
    """Load MIDAS data from a buffer and return the ragged array.

    :param buffer: object supporting buffer protocol
    :param entry_start: the first entry to include. If None, start at 0.
    :param entry_stop: the first entry to exclude. If None, stop at the end of the file.
    """
    if entry_start is None:
        entry_start = 0
    if entry_stop is None:
        entry_stop = np.iinfo(np.int32).max

    if entry_start < 0:
        raise ValueError("Start entry must be positive")
    if entry_stop < 0:
        raise ValueError("Stop entry must be positive")
    if entry_stop < entry_start:
        raise ValueError("Stop entry must not be less than the start entry")

    # Create a view over the memory map
    data = np.frombuffer(buffer, dtype="<B")

    # Run the VM
    vm = ForthMachine32(MIDAS_PROGRAM)
    vm.run({"data": data, "range": np.array([entry_start, entry_stop], dtype=np.int32)})

    # Create the result
    outputs = vm.outputs.copy()
    num = outputs.pop("num")
    return ak.unflatten(ak.zip(outputs), num)


def read(
    source: io.IOBase, entry_start: int = None, entry_stop: int = None
) -> ak.Array:
    """Read a MIDAS tape file and return the ragged array.

    :param source: open MIDAS file source
    :param entry_start: the first entry to include. If None, start at 0.
    :param entry_stop: the first entry to exclude. If None, stop at the end of the file.
    """

    with contextlib.ExitStack() as stack:
        memory = stack.enter_context(
            mmap.mmap(source.fileno(), 0, flags=mmap.ACCESS_READ, prot=mmap.PROT_READ)
        )

        # We will be searching linearly, so advise the kernel
        memory.madvise(mmap.MADV_SEQUENTIAL)
        return load(memory)
