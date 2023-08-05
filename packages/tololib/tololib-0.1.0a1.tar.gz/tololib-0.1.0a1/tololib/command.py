
from enum import Enum
from typing import Any, NamedTuple, Type, Union

from .const import AromaTherapy, LampMode
from .data_container import DataContainer, BooleanContainer, IntContainer, FixedIntContainer, EnumContainer


CommandTypeHint = Union[Type[int], Type[bool], int, None]


class CommandDefinition(NamedTuple):
    code: int
    default_value: Any
    data_container: DataContainer[Any]


class Command(CommandDefinition, Enum):
    POWER_SWITCH = CommandDefinition(14, False, BooleanContainer())
    LAMP_SWITCH = CommandDefinition(30, False, BooleanContainer())
    LAMP_MODE = CommandDefinition(60, LampMode.MANUAL, EnumContainer[LampMode](LampMode))
    LAMP_CHANGE_COLOR = CommandDefinition(62, 1, FixedIntContainer(1))
    FAN_SWITCH = CommandDefinition(34, False, BooleanContainer())
    FAN_TIMER = CommandDefinition(36, None, IntContainer(1, 60, 61))
    SWEEP_SWITCH = CommandDefinition(26, False, BooleanContainer())
    SWEEP_TIMER = CommandDefinition(28, None, IntContainer(0, 8))
    SALT_BATH_SWITCH = CommandDefinition(54, False, BooleanContainer())
    AROMA_THERAPY_SWITCH = CommandDefinition(18, False, BooleanContainer())
    AROMA_THERAPY_SELECT1 = CommandDefinition(20, AromaTherapy.A, EnumContainer[AromaTherapy](AromaTherapy))
    AROMA_THERAPY_SELECT2 = CommandDefinition(21, AromaTherapy.A, EnumContainer[AromaTherapy](AromaTherapy))
    TEMPERATURE = CommandDefinition(4, 40, IntContainer(-20, 60))
    HUMIDITY = CommandDefinition(38, 95, IntContainer(60, 99))
    POWER_TIMER = CommandDefinition(8, None, IntContainer(0, 100, 255))
    SALT_BATH_TIMER = CommandDefinition(56, None, IntContainer(0, 100, -1))
    STATUS = CommandDefinition(97, 0, IntContainer())
    SETTINGS = CommandDefinition(99, 0, IntContainer())
    # TODO learn command code 61

    @classmethod
    def from_code(cls, code: int) -> 'Command':
        for command in cls:
            if command.code == code:
                return command
        else:
            raise ValueError('unknown command code %s' % code)
