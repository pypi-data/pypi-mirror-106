
from typing import Any, Optional
from unittest import TestCase

from tololib import ToloClient, ToloServer
from tololib.message_info import StatusInfo, SettingsInfo


class ClientTest(TestCase):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._server: Optional[ToloServer] = None

    def setUp(self) -> None:
        self._server = ToloServer('localhost', 0)
        self._server.start()

    def tearDown(self) -> None:
        if self._server is not None:
            self._server.stop()
            self._server.join()
            self._server = None

    def _get_port(self) -> int:
        if self._server is None:
            raise RuntimeError('server not set up')

        port = self._server.get_socket_info()[1]

        if not isinstance(port, int):
            raise RuntimeError('not an int value')

        return port

    def test_get_status_info(self) -> None:
        client = ToloClient('localhost', self._get_port())
        response = client.get_status_info()
        self.assertIsInstance(response, StatusInfo)

    def test_get_settings_info(self) -> None:
        client = ToloClient('localhost', self._get_port())
        response = client.get_settings_info()
        self.assertIsInstance(response, SettingsInfo)
