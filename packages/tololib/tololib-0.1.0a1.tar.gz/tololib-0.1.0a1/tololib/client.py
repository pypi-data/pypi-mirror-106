
import logging
import socket
from select import select
from typing import List, Optional, Tuple, Union

from .command import Command
from .message import Message


logger = logging.getLogger(__name__)


class ToloClient(object):
    def __init__(self, address: str, port: int = 51500) -> None:
        self._address = address
        self._port = port

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message: Message) -> int:
        """Send a message to the server.

        Args:
            message (Message): The message to be send to the server.

        Returns:
            Number of bytes sent.
        """
        raw_bytes = bytes(message)
        logger.debug('sending %s to %s' % (raw_bytes.hex(), (self._address, self._port)))
        return self._socket.sendto(raw_bytes, (self._address, self._port))

    def receive_message(self, wait_timeout: Optional[float] = None) -> Optional[Message]:
        incoming = select([self._socket], [], [], wait_timeout)
        if incoming[0]:
            raw_bytes, sender = self._socket.recvfrom(4096)
            logger.debug('received %s from %s' % (raw_bytes.hex(), sender))
            return Message.from_bytes(raw_bytes)
        else:
            return None

    def send_wait_response(self, message: Message, resend_timeout: Optional[float] = None,
                           retries: int = 3) -> Optional[Message]:
        for _ in range(retries):
            self.send_message(message)
            response = self.receive_message(wait_timeout=resend_timeout)
            if response is not None:
                return response
        return None

    @staticmethod
    def discover(address: str = '255.255.255.255', port: int = 51500,
                 wait_timeout: float = 1) -> List[Tuple[Message, Union[str, Tuple[str, int]]]]:
        devices = []

        discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        discovery_socket.sendto(bytes(Message(Command.STATUS, 0, b'\xFF')), (address, port))

        while True:
            incoming_data = select([discovery_socket], [], [], wait_timeout)
            if incoming_data[0]:
                raw_bytes, sender = discovery_socket.recvfrom(4096)
                message = Message.from_bytes(raw_bytes)
                devices.append((message, sender))
            else:
                discovery_socket.close()
                return devices
