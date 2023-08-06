"""Options shared between the commands."""

from os.path import isfile

from functools import wraps
from typing import Callable
import click

from escape_cli.static.constants import CONFIG_FILENAME, DISCOVER_NAMESPACE
from escape_cli.utils.config import get_config


def config_option(func: Callable) -> Callable:
    """Option to give the path of the escape config file."""

    return click.option('-c', '--config', 'config_path', default=CONFIG_FILENAME, help='Path of the escape config file.')(func)


def extract_config(func: Callable) -> Callable:
    """Extract the config given the config path."""

    @wraps(func)
    @config_option
    def wrapped(*args, **kwargs):  # type: ignore

        config_path = kwargs['config_path']
        config = get_config(config_path, DISCOVER_NAMESPACE)
        if not config:
            raise ValueError(f'Cannot read the config in the file {config_path}')

        del kwargs['config_path']
        kwargs['config'] = config

        return func(*args, **kwargs)

    return wrapped


def extract_as_module(func: Callable) -> Callable:
    """Check if the entrypoint correspond to a file in the cwd."""

    @wraps(func)
    def wrapped(*args, **kwargs):  # type: ignore

        kwargs['as_module'] = not isfile(kwargs['entrypoint'][0])
        return func(*args, **kwargs)

    return wrapped
