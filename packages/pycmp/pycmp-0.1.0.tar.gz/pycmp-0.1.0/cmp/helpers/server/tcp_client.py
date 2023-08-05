import asyncio
import logging
import os
from argparse import ArgumentParser, Namespace
from typing import Optional

logger = logging.getLogger(__name__)
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.INFO)
logger.addHandler(s_handler)


class TCPClient(ArgumentParser):
    """Simple TCP client for sending in MATLAB compiler"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.address = os.environ.get("HOSTNAME", '127.0.0.1')
        self.port = os.environ.get("PORT", 8888)
        self.description = 'TCP client for server MATLAB compiler'
        self.command_group = self.add_mutually_exclusive_group(required=True)
        self.command_group.add_argument(
            '-d',
            '--data',
            type=str,
            help='input data for compiler from console'
        )
        self.command_group.add_argument(
            '-f',
            '--file',
            type=str,
            help='input data for compiler from file'
        )
        self.add_argument(
            '-p',
            '--port',
            required=False,
            type=int,
            help='Port of connection server'
        )
        self.add_argument(
            '-a',
            '--address',
            required=False,
            type=str,
            help='Address of connection server'
        )

    def execute(self) -> None:
        """Start TCP client in CLI"""
        args = self.parse_args()  # type: Namespace

        message = self._get_text(args)
        address = args.address or self.address  # type: str
        port = args.port or self.port  # type: int

        response = asyncio.run(self._send_data(message, address, port))
        logger.info(response)

    @staticmethod
    def _validate_file(path: str) -> bool:
        return os.path.isfile(path)

    def _get_text(self, args: Namespace) -> Optional[str]:
        if args.data:
            return str(args.data)
        else:
            if not self._validate_file(args.file):
                logger.error('Incorrect path file')
                return None
            with open(args.file, "r") as file:
                content = file.read()
            return content

    @staticmethod
    async def _send_data(message: str, host: str, port: int) -> str:
        reader, writer = await asyncio.open_connection(host, port)

        writer.write(message.encode())
        writer.write_eof()
        await writer.drain()

        data = await reader.read()
        writer.close()
        await writer.wait_closed()

        return data.decode(encoding='utf-8')


def main() -> None:
    client = TCPClient()
    client.execute()


if __name__ == '__main__':
    main()
