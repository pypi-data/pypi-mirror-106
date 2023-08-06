"""
Lump 35 - Game Lump
===================

This lump contains a single :any:`dgamelumpheader_t`. This is only the gamelump headers and not the gamelump data. for gamelump data, :ref:`see gamelumps<gamelumps>`.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from construct import *  # NOQA: #402
from valvebsp.structs.common import *  # NOQA #402

dgamelump_flags = FlagsEnum(
    Int16ul,
    GAMELUMPFLAG_COMPRESSED=1)

dgamelump_t = Struct(
    'id' / PaddedString(4, "ascii"),
    'flags' / dgamelump_flags,
    'version' / Int16ul,
    'fileofs' / Int32sl,
    'filelen' / Int32sl,
)

dgamelumpheader_t = Struct(
    'lumpCount' / Int32sl,
    'gamelump' / dgamelump_t[this.lumpCount],
)


@lump_struct
@lump_version(0)
def lump_35(header, profile=None):
    return dgamelumpheader_t
