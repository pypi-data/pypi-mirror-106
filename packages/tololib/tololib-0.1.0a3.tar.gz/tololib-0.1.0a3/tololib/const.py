
from enum import IntEnum


DEFAULT_PORT = 51500

MESSAGE_PREFIX = b'\xAA\xAA'
MESSAGE_SUFFIX = b'\x55\x55'


class AromaTherapy(IntEnum):
    A = 0
    B = 1


class Calefaction(IntEnum):
    HEAT = 0
    INACTIVE = 1
    UNCLEAR2 = 2  # TODO find correct meaning
    KEEP = 3


class LampMode(IntEnum):
    MANUAL = 0
    AUTOMATIC = 1


class Model(IntEnum):
    DOMESTIC = 0
    COMMERCIAL = 1
