
from typing import Union

from .command import Command, CommandTypeHint
from .const import MESSAGE_PREFIX, MESSAGE_SUFFIX


class Message(object):
    PREFIX = MESSAGE_PREFIX
    SUFFIX = MESSAGE_SUFFIX

    def __init__(self, command: Command, data: CommandTypeHint, info: Union[bytes, bytearray] = b''):
        self._command = command
        self._data = data
        self._info = bytes(info)

    @property
    def command(self) -> Command:
        return self._command

    @property
    def data(self) -> CommandTypeHint:
        return self._data

    @property
    def info(self) -> bytes:
        return self._info

    def __str__(self) -> str:
        return '<%s: cmd: %s, data: %d, info: %s>' % (
            self.__class__.__name__,
            self._command.name,
            self._command.data_container.to_int(self._command.data_container.normalize(self._data)),
            self._info.hex()
        )

    def __bytes__(self) -> bytes:
        data = self.PREFIX + bytes([
            self._command.code,
            self._command.data_container.to_int(self._data)
        ]) + self._info + self.SUFFIX
        return data + bytes([self.generate_crc(data)])

    @staticmethod
    def from_bytes(b: bytes) -> 'Message':
        if not Message.validate_meta(b):
            raise ValueError('invalid meta information')

        command = Command.from_code(b[2])
        data = command.data_container.normalize(b[3])

        return Message(
            command=command,
            data=data,
            info=b[4:-3]
        )

    @staticmethod
    def generate_crc(data: bytes) -> int:
        crc = 0x00
        for b in data:
            crc = crc ^ b
        return crc

    @staticmethod
    def validate_crc(raw_bytes: bytes) -> bool:
        return Message.generate_crc(raw_bytes[:-1]) == raw_bytes[-1]

    @classmethod
    def validate_meta(cls, raw_bytes: bytes) -> bool:
        """Validates meta data of message bytes.

        The validation will check for prefix, suffix and CRC.
        It will NOT check for valid code or payload.

        Args:
            raw_bytes (bytes): binary data to be checked

        Returns:
            True if the check was successful and the meta data is as expected, False otherwise.
        """
        if not raw_bytes.startswith(cls.PREFIX):
            return False
        if not raw_bytes[:-1].endswith(cls.SUFFIX):
            return False
        return cls.validate_crc(raw_bytes)
