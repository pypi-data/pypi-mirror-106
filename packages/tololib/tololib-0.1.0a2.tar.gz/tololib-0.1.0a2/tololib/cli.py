
import argparse
import logging
import signal
import sys
from types import FrameType

from .client import ToloClient
from .command import Command
from .const import DEFAULT_PORT
from .message_info import SettingsInfo, StatusInfo
from .message import Message
from .server import ToloServer


logger = logging.getLogger(__name__)

SETTINGS_COMMAND_MAP = {
    # main panel
    'power': Command.POWER_SWITCH,
    'fan': Command.FAN_SWITCH,
    'aroma-therapy': Command.AROMA_THERAPY_SWITCH,
    'lamp': Command.LAMP_SWITCH,
    'sweep': Command.SWEEP_SWITCH,
    'salt-bath': Command.SALT_BATH_TIMER,
    # settings panel
    'target-temperature': Command.TEMPERATURE,
    'target-humidity': Command.HUMIDITY,
    'power-timer': Command.POWER_TIMER,
    'salt-bath-timer': Command.SALT_BATH_TIMER,
    'aroma-therapy-slot': Command.AROMA_THERAPY_SELECT1,
    'sweep-timer': Command.SWEEP_TIMER,
    'lamp-mode': Command.LAMP_MODE,
    'fan-timer': Command.FAN_TIMER
}


def main() -> int:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-l', '--log-level', choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
                                 default='INFO')

    argument_sub_parser = argument_parser.add_subparsers(title='command', dest='command', required=True)

    server_argument_parser = argument_sub_parser.add_parser('server')
    server_argument_parser.add_argument('-l', '--listen-address', default='')
    server_argument_parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)

    discover_argument_parser = argument_sub_parser.add_parser('discover')
    discover_argument_parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)

    show_settings_argument_parser = argument_sub_parser.add_parser('show-settings')
    show_settings_argument_parser.add_argument('-a', '--address', type=str)
    show_settings_argument_parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)
    show_settings_argument_parser.add_argument('--resend-timeout', type=float, default=1)
    show_settings_argument_parser.add_argument('--retries', type=int, default=3)

    set_argument_parser = argument_sub_parser.add_parser('set')
    set_argument_parser.add_argument('-a', '--address', type=str)
    set_argument_parser.add_argument('-p', '--port', type=int, default=DEFAULT_PORT)
    set_argument_parser.add_argument('--resend-timeout', type=float, default=1)
    set_argument_parser.add_argument('--retries', type=int, default=3)
    set_argument_parser.add_argument('key', choices=SETTINGS_COMMAND_MAP.keys())
    set_argument_parser.add_argument('value')

    args = argument_parser.parse_args()

    library_logger = logging.getLogger(__package__)
    log_handler = logging.StreamHandler(sys.stderr)
    log_formatter = logging.Formatter(fmt='%(asctime)s %(name)-20s [%(levelname)s] %(message)s')
    log_handler.setFormatter(log_formatter)
    library_logger.addHandler(log_handler)
    library_logger.setLevel(logging.getLevelName(args.log_level))

    if args.command == 'server':
        return cmd_server(args)
    elif args.command == 'discover':
        return cmd_discover(args)
    elif args.command == 'show-settings':
        return cmd_show_settings(args)
    elif args.command == 'set':
        return cmd_set(args)
    else:
        return 1


def cmd_server(args: argparse.Namespace) -> int:
    server = ToloServer(address=args.listen_address, port=args.port)

    def stop_on_signal(s: signal.Signals, t: FrameType) -> None:
        logger.debug('received signal %d, shutting down...' % s)
        server.stop()

    signal.signal(signal.SIGINT, stop_on_signal)
    server.run()
    return 0


def cmd_discover(args: argparse.Namespace) -> int:
    # TODO use args
    for message, address in ToloClient.discover():
        info = StatusInfo(message.info)
        print('=== Address: %s:%s' % (address[0], address[1]))
        print(info)
    return 0


def cmd_show_settings(args: argparse.Namespace) -> int:
    message = Message(Command.SETTINGS, Command.SETTINGS.default_value, b'\xFF')
    client = ToloClient(args.address, args.port)
    response = client.send_wait_response(message, resend_timeout=args.resend_timeout, retries=args.retries)
    if response is None:
        print('Did not get response')
        return 1
    else:
        info = SettingsInfo(response.info)
        print(info)
        return 0


def cmd_set(args: argparse.Namespace) -> int:
    command = SETTINGS_COMMAND_MAP.get(args.key)
    if command is None:
        raise ValueError('command not supported')  # TODO change error type

    data = command.data_container.normalize(args.value)

    message = Message(command, data, b'\xFF')

    client = ToloClient(args.address, args.port)
    response = client.send_wait_response(message, resend_timeout=args.resend_timeout, retries=args.retries)
    if response is None:
        return 1
    else:
        print(response)
        return 0
