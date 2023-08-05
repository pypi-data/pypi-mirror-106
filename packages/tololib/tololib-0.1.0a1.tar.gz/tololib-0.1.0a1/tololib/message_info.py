
from typing import Optional

from .command import Command
from .const import AromaTherapy, Calefaction, LampMode, Model
from .data_container import BooleanContainer, EnumContainer, IntContainer


class MessageInfo(bytearray):
    LENGTH = -1

    def __init__(self, initial_value: Optional[bytes] = None) -> None:
        if initial_value is None:
            super().__init__(b'\x00' * self.LENGTH)
        elif len(initial_value) == self.LENGTH:
            super().__init__(initial_value)
        else:
            raise ValueError('initial value must have length %d, %d given' % (self.LENGTH, len(initial_value)))


class StatusInfo(MessageInfo):
    """
      * 0: int(self._power_on),
      * 1: self._current_temperature,
      * 2: 61 if self._power_timer is None else self._power_timer,
      * 3: (64 if self._flow_in else 0) + (16 if self._flow_out else 0) + self._calefaction.value,
     4: int(self._aroma_therapy_on),
     5: int(self._sweep_on),
     6: 0,  # TODO descaling - what is this?
     7: int(self._lamp_on),
     8: self._water_level,
     9: int(self._fan_on),
    10: 61 if self._fan_timer is None else self._fan_timer,
    11: self._current_humidity,
    12: self._tank_temperature,
    13: 0,  # TODO unused?
    14: self._model.value,
    15: self._salt_bath_on,
    16: 0 if self._salt_bath_timer is None else self._salt_bath_timer
    """
    LENGTH = 17

    @property
    def power_on(self) -> bool:
        return self[0] != 0

    @power_on.setter
    def power_on(self, power_on: bool) -> None:
        container = BooleanContainer()
        self[0] = container.to_int(container.normalize(power_on))

    @property
    def current_temperature(self) -> int:
        return self[1]

    @current_temperature.setter
    def current_temperature(self, current_temperature: int) -> None:
        container = IntContainer(0, 255)
        self[1] = container.to_int(container.normalize(current_temperature))

    @property
    def power_timer(self) -> Optional[int]:
        if self[2] == 61:
            return None
        else:
            return self[2]

    @power_timer.setter
    def power_timer(self, power_timer: Optional[int]) -> None:
        container = IntContainer(1, 60, 61)
        self[2] = container.to_int(container.normalize(power_timer))

    @property
    def flow_in(self) -> bool:
        return bool(self[3] & 64)

    @flow_in.setter
    def flow_in(self, flow_in: bool) -> None:
        self[3] = (self[3] & 191) | (64 if flow_in else 0)

    @property
    def flow_out(self) -> bool:
        return bool(self[3] & 16)

    @flow_out.setter
    def flow_out(self, flow_out: bool) -> None:
        self[3] = (self[3] & 239) | (16 if flow_out else 0)

    @property
    def calefaction(self) -> Calefaction:
        return Calefaction(self[3] & 3)

    @calefaction.setter
    def calefaction(self, calefaction: Calefaction) -> None:
        container = EnumContainer[Calefaction](Calefaction)

        if not isinstance(calefaction, int) or calefaction < 0 or calefaction > 3:
            raise ValueError('expecting int from 0 to 3')
        self[3] = (self[3] & 252) | container.to_int(container.normalize(calefaction))

    @property
    def aroma_therapy_on(self) -> bool:
        return self[4] != 0

    @aroma_therapy_on.setter
    def aroma_therapy_on(self, aroma_therapy_on: bool) -> None:
        self[4] = bool(aroma_therapy_on)

    @property
    def sweep_on(self) -> bool:
        return self[5] != 0

    @sweep_on.setter
    def sweep_on(self, sweep_on: bool) -> None:
        self[5] = bool(sweep_on)

    @property
    def lamp_on(self) -> bool:
        return self[7] != 0

    @lamp_on.setter
    def lamp_on(self, lamp_on: bool) -> None:
        container = BooleanContainer()
        self[7] = container.to_int(container.normalize(lamp_on))

    @property
    def water_level(self) -> int:
        return self[8]

    @water_level.setter
    def water_level(self, water_level: int) -> None:
        container = IntContainer(0, 3)
        self[8] = container.to_int(container.normalize(water_level))

    @property
    def fan_on(self) -> bool:
        return self[9] != 0

    @fan_on.setter
    def fan_on(self, fan_on: bool) -> None:
        self[9] = bool(fan_on)

    @property
    def fan_timer(self) -> Optional[int]:
        return None if self[10] == 61 else self[10]

    @fan_timer.setter
    def fan_timer(self, fan_timer: Optional[int]) -> None:
        container = IntContainer(1, 60, 61)
        self[10] = container.to_int(container.normalize(fan_timer))

    @property
    def current_humidity(self) -> int:
        return self[11]

    @current_humidity.setter
    def current_humidity(self, current_humidity: int) -> None:
        container = IntContainer(0, 100)
        self[11] = container.to_int(container.normalize(current_humidity))

    @property
    def tank_temperature(self) -> int:
        return self[12]

    @tank_temperature.setter
    def tank_temperature(self, tank_temperature: int) -> None:
        container = IntContainer(0, 255)
        self[12] = container.to_int(container.normalize(tank_temperature))

    @property
    def model(self) -> Model:
        return Model(self[14])

    @model.setter
    def model(self, model: Model) -> None:
        container = EnumContainer[Model](Model)
        self[14] = container.to_int(container.normalize(model))

    @property
    def salt_bath_on(self) -> bool:
        return bool(self[15])

    @salt_bath_on.setter
    def salt_bath_on(self, salt_bath_on: bool) -> None:
        container = BooleanContainer()
        self[15] = container.to_int(container.normalize(salt_bath_on))

    @property
    def salt_bath_timer(self) -> Optional[int]:
        return None if self[16] == 0 else self[16]

    @salt_bath_timer.setter
    def salt_bath_timer(self, salt_bath_timer: Optional[int]) -> None:
        container = IntContainer(1, 60, 0)
        self[16] = container.to_int(container.normalize(salt_bath_timer))

    def __str__(self) -> str:
        return '\n'.join([
            'Power:               %s' % ('ON' if self.power_on else 'OFF'),
            'Current Temperature: %d' % self.current_temperature,
            'Power Timer:         %s' % self.power_timer,
            'Flow in:             %s' % ('YES' if self.flow_in else 'NO'),
            'Flow out:            %s' % ('YES' if self.flow_out else 'NO'),
            'Calefaction:         %s' % self.calefaction.name,
            'Aroma Therapy:       %s' % ('ON' if self.aroma_therapy_on else 'OFF'),
            'Sweep:               %s' % ('ON' if self.sweep_on else 'OFF'),
            # 'Descaling:           %s' % ('YES' if self.descaling else 'NO'), TODO what is this?
            'Lamp:                %s' % ('ON' if self.lamp_on else 'OFF'),
            'Water Level:         %s' % self.water_level,
            'Fan:                 %s' % ('ON' if self.fan_on else 'OFF'),
            'Fan Timer:           %s' % ('OFF' if self.fan_timer is None else str(self.fan_timer)),
            'Current Humidity:    %s' % self.current_humidity,
            'Tank Temperature:    %s' % self.tank_temperature,
            'Model:               %s' % self.model.name,
            'Salt Bath On:        %s' % ('ON' if self.salt_bath_on else 'OFF'),
            'Salt Bath Timer:     %s' % ('OFF' if self.salt_bath_timer is None else str(self.salt_bath_timer))
        ])


class SettingsInfo(MessageInfo):
    """
    0: self._target_temperature,
    1: 255 if self._power_timer is None else self._power_timer,
    2: self._aroma_therapy.value,
    3: self._sweep_timer,
    4: 61 if self._fan_timer is None else self._fan_timer,
    5: self._target_humidity,
    6: 255 if self._salt_bath_timer is None else self._salt_bath_timer,
    7: self._lamp_mode.value

    """
    LENGTH = 8

    @property
    def target_temperature(self) -> int:
        return self[0]

    @target_temperature.setter
    def target_temperature(self, target_temperature: int) -> None:
        container = IntContainer(-20, 60)
        self[0] = container.to_int(container.normalize(target_temperature))

    @property
    def power_timer(self) -> Optional[int]:
        return None if self[1] else self[1]

    @power_timer.setter
    def power_timer(self, power_timer: Optional[int]) -> None:
        container = Command.POWER_TIMER.data_container
        self[1] = container.to_int(container.normalize(power_timer))

    @property
    def aroma_therapy(self) -> AromaTherapy:
        return AromaTherapy(self[2])

    @aroma_therapy.setter
    def aroma_therapy(self, aroma_therapy: AromaTherapy) -> None:
        container = Command.AROMA_THERAPY_SELECT1.data_container
        self[2] = container.to_int(container.normalize(aroma_therapy))

    @property
    def sweep_timer(self) -> int:
        return self[3]

    @sweep_timer.setter
    def sweep_timer(self, sweep_timer: int) -> None:
        container = Command.SWEEP_TIMER.data_container
        self[3] = container.to_int(container.normalize(sweep_timer))

    @property
    def fan_timer(self) -> Optional[int]:
        return None if self[4] == 61 else self[4]

    @fan_timer.setter
    def fan_timer(self, fan_timer: Optional[int]) -> None:
        container = Command.FAN_TIMER.data_container
        self[4] = container.to_int(container.normalize(fan_timer))

    @property
    def target_humidity(self) -> int:
        return self[5]

    # TODO setter for target_humidty

    @property
    def salt_bath_timer(self) -> Optional[int]:
        return None if self[6] == 255 else self[6]

    # TODO setter for salt bath timer

    @property
    def lamp_mode(self) -> LampMode:
        return LampMode(self[7])

    # TODO setter for lamp mode

    def __str__(self) -> str:
        return '\n'.join([
            'Target Temperature: %d' % self.target_temperature,
            'Power Timer:        %s' % self.power_timer,
            'Aroma Therapy:      %s' % self.aroma_therapy,
            'Sweep Timer:        %s' % self.sweep_timer,
            'Fan Timer:          %s' % self.fan_timer,
            'Target Humidity:    %s' % self.target_humidity,
            'Salt Bath Timer:    %s' % self.salt_bath_timer,
            'Lamp Mode:          %s' % self.lamp_mode
        ])
