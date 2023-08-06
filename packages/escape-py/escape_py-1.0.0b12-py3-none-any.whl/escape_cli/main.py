"""Main."""

import sys
import click
from loguru import logger

from . import __version__, commands
from .utils import title, format_logs

logger.remove()
logger.add(sys.stderr, format=format_logs)  #type: ignore

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option('-V', '--version', 'version', default=False, is_flag=True)
def main(version: bool) -> None:
    """Starting point of the Python CLI."""

    if version:
        print(__version__)
        sys.exit(0)

    title()


main.add_command(commands.init)
main.add_command(commands.discover)  # type: ignore
main.add_command(commands.cover)
