
import logging
import socket
from select import select
from threading import Thread
from typing import Optional, Tuple, Union

from .command import Command
from .message import Message
from .message_info import StatusInfo, SettingsInfo


logger = logging.getLogger(__name__)


class ToloServer(object):
    def __init__(self, address: Optional[str] = None, port: int = 51500) -> None:
        self._address = address
        self._port = port

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((address, port))
        self._thread: Optional[Thread] = None
        self._keep_running = False

    def start(self) -> None:
        """Initialize and start the server loop thread.

        Initializes and starts a thread in the background, which handles incoming messages and updates local variables
        accordingly.
        """
        if self._thread is not None:
            raise RuntimeError('server thread already initialized!')

        self._thread = Thread(target=self._thread_loop)
        self._keep_running = True
        self._thread.start()

    def join(self, timeout: Optional[float] = None) -> None:
        """Join the background thread and wait until it is finished.

        Args:
            timeout (float): timeout in seconds
        """
        if self._thread is None:
            raise RuntimeError('server does not have a running thread - did you call start() before?')

        self._thread.join(timeout)

    def run(self) -> None:
        """Shortcut method calling start() and join()"""
        self.start()
        self.join()

    def receive_message(self) -> Tuple[Message, str]:
        """Receive, decode and return a single control message.

        Blocks until a message has received.

        Returns:
            A decoded Message object which contains the received control message.
        """
        raw_bytes, sender = self._socket.recvfrom(4096)
        return Message.from_bytes(raw_bytes), sender

    def send_message(self, message: Message, recipient: Union[Tuple[str, int], str]) -> int:
        raw_bytes = bytes(message)
        return self._socket.sendto(raw_bytes, recipient)

    def _thread_loop(self) -> None:
        logger.debug('server thread loop started')
        while self._keep_running:
            incoming_data = select([self._socket], [], [], 0.2)
            if incoming_data[0]:
                message, sender = self.receive_message()
                logger.debug('received message %s' % str(message))

                if message.command == Command.STATUS:
                    status_info = StatusInfo()
                    self.send_message(Message(Command.STATUS, 0, status_info), sender)
                elif message.command == Command.SETTINGS:
                    settings_info = SettingsInfo()
                    self.send_message(Message(Command.SETTINGS, 0, settings_info), sender)

    def stop(self) -> None:
        self._keep_running = False

    def close(self) -> None:
        self._socket.close()

    def __del__(self) -> None:
        self.close()
