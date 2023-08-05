
from enum import IntEnum
from typing import Any, Generic, Optional, Type, TypeVar


E = TypeVar('E', bound=IntEnum)
T = TypeVar('T')


class DataContainer(Generic[T]):
    def to_int(self, value: T) -> int:
        raise NotImplementedError()

    def validate(self, value: Any, raise_error: bool = True) -> bool:
        try:
            self.normalize(value)
            return True
        except ValueError as e:
            if raise_error:
                raise e
            else:
                return False

    def normalize(self, value: Any) -> T:
        raise NotImplementedError()


class BooleanContainer(DataContainer[bool]):
    def to_int(self, value: bool) -> int:
        return 1 if value else 0

    def normalize(self, value: Any) -> bool:
        if isinstance(value, bool):
            return value
        elif isinstance(value, int):
            return bool(value)
        elif isinstance(value, str):
            if value.lower() in ('false', '0', 'off', 'no'):
                return False
            elif value.lower() in ('true', '1', 'on', 'yes'):
                return True
            else:
                raise ValueError('cannot interpret %s as boolean value' % value)
        else:
            raise ValueError('unsupported type for normalization')


class IntContainer(DataContainer[Optional[int]]):
    def __init__(self, min_value: Optional[int] = None, max_value: Optional[int] = None,
                 none_int: Optional[int] = None) -> None:
        self._min = min_value
        self._max = max_value
        self._none_int = none_int

    def to_int(self, value: Optional[int]) -> int:
        if value is None:
            if self._none_int is None:
                raise ValueError('None not allowed by container definition')
            else:
                return self._none_int
        elif self._min is not None and value < self._min:
            raise ValueError('value must be >= %d' % self._min)
        elif self._max is not None and value > self._max:
            raise ValueError('value must be <= %d' % self._max)
        else:
            return value

    def normalize(self, value: Any) -> Optional[int]:
        if value is None:
            return None
        elif isinstance(value, int):
            return value
        elif isinstance(value, str):
            return int(value)
        else:
            raise ValueError('cannot parse %s as int' % str(value))


class FixedIntContainer(DataContainer[int]):
    def __init__(self, fixed_value: int):
        self._fixed_value = fixed_value

    def to_int(self, value: int) -> int:
        return value

    def normalize(self, value: Any) -> int:
        if value is None:
            raise ValueError('None value not allowed')
        elif not isinstance(value, int) or value != self._fixed_value:
            raise ValueError('value does not equal fixed value %d' % self._fixed_value)
        else:
            return value


class EnumContainer(Generic[E], DataContainer[IntEnum]):
    def __init__(self, enum_type: Type[E]):
        self._enum_type = enum_type

    def to_int(self, value: IntEnum) -> int:
        return value.value

    def normalize(self, value: Any) -> E:
        if isinstance(value, self._enum_type):
            return value
        elif isinstance(value, int):
            return self._enum_type(value)
        elif isinstance(value, str):
            return self._enum_type[value.upper()]
        else:
            raise ValueError('unsupported type')
