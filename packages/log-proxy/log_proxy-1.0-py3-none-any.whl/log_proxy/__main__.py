#!/usr/bin/env python3
import argparse
import asyncio
import logging
import sys
from typing import Tuple

from . import utils
from .handlers import JSONSocketHandler
from .server import LogServer

DEFAULT_PORT = 3773
LOG_LEVELS = {
    "critical": logging.CRITICAL,
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "info": logging.INFO,
    "warn": logging.WARN,
    "warning": logging.WARNING,
}


class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action: argparse.Action) -> str:
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)

        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return f"{'/'.join(action.option_strings)} {args_string}"


def parse_args(args: Tuple[str] = None) -> None:
    parser = argparse.ArgumentParser(
        formatter_class=CustomHelpFormatter,
        prog="",
        description="",
    )

    group = parser.add_argument_group("Basic configuration")
    group.add_argument(
        "--log-file",
        help="File to use for logging. If not set logs will be put to stdout.",
    )
    group.add_argument(
        "--log-level",
        choices=sorted(LOG_LEVELS),
        default="info",
        help="Set the log level to use. (default: %(default)s)",
    )
    group.add_argument(
        "--log-stdin",
        default=False,
        action="store_true",
        help="Pipe the stdin into the log",
    )
    group.add_argument(
        "--log-format",
        default=utils.DEFAULT_LOG_FORMAT,
        help="Configure the log format using the { style formatting",
    )
    group.add_argument(
        "--no-server",
        default=False,
        action="store_true",
        help="Disable the server part",
    )

    group = parser.add_argument_group("Server configuration")
    group.add_argument(
        "-l",
        "--listen",
        dest="listen",
        default=("", DEFAULT_PORT),
        metavar="[host[,host]*][:port]",
        type=lambda x: utils.parse_address(
            x,
            host="",
            port=DEFAULT_PORT,
            multiple=True,
        ),
        help=f"The address to listen on. If host is not given the server will "
        f"listen for connections from all IPs. If you want to listen on multiple "
        f"interfaces you can separate them by comma. If the port is not given "
        f"the server will listen on port {DEFAULT_PORT}.",
    )
    group.add_argument(
        "--ca",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="CA certificate to use. Will enforce client certificates.",
    )
    group.add_argument(
        "--cert",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="Certificate to use for establishing the connection.",
    )
    group.add_argument(
        "--key",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="Private key for the certificate.",
    )
    group.add_argument(
        "--cipher",
        default=None,
        help="Ciphers to use for the TLS connection.",
    )

    group = parser.add_argument_group("Forwarding configuration")
    group.add_argument(
        "-f",
        "--forward",
        dest="forward",
        metavar="host[:port]",
        default=None,
        type=lambda x: utils.parse_address(x, port=DEFAULT_PORT),
        help=f"Connect to a different log server to forward the log messages further."
        f" (default: {DEFAULT_PORT})",
    )
    group.add_argument(
        "--forward-ca",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="CA certificate to use.",
    )
    group.add_argument(
        "--forward-cert",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="Certificate to use for establishing the connection. Required if the "
        "target server enforces the client certificates.",
    )
    group.add_argument(
        "--forward-key",
        default=None,
        metavar="FILE",
        type=utils.valid_file,
        help="Private key for the certificate. Required if the target server enforces "
        "the client certificates.",
    )
    group.add_argument(
        "--forward-cipher",
        default=None,
        help="Ciphers to use for the TLS connection.",
    )
    group.add_argument(
        "--no-verify-hostname",
        action="store_true",
        default=False,
        help="Disable the hostname verification. Only useful for forwarding.",
    )

    return parser.parse_args(args)


def configure(args):
    """Configure the logger using the arguments"""
    level = LOG_LEVELS.get(args.log_level, logging.INFO)
    if not args.forward:
        return utils.configure_logging(args.log_file, level, None, args.log_format)

    if not args.forward_ca:
        handler = JSONSocketHandler(*args.forward)
        return utils.configure_logging(args.log_file, level, handler, args.log_format)

    sc = utils.generate_ssl_context(
        ca=args.forward_ca,
        cert=args.forward_cert,
        key=args.forward_key,
        ciphers=args.forward_cipher,
        check_hostname=not args.no_verify_hostname,
    )

    handler = JSONSocketHandler(*args.forward, sc)
    return utils.configure_logging(args.log_file, level, handler, args.log_format)


async def run(args):
    if not args.no_server:
        # Server SSL context
        if args.cert and args.key:
            ssl_context = utils.generate_ssl_context(
                cert=args.cert,
                ca=args.ca,
                key=args.key,
                ciphers=args.cipher,
                server=True,
            )
        else:
            ssl_context = None

        server = LogServer(*args.listen, ssl_context)

        if args.log_stdin:
            asyncio.create_task(utils.stdin_to_log())

        await server.run()

    elif args.log_stdin:
        # Only log the stdin
        await utils.stdin_to_log()


def main(args: Tuple[str] = None) -> None:
    args = parse_args(args)

    configure(args)

    asyncio.run(run(args))


if __name__ == "__main__":
    main(sys.argv)
