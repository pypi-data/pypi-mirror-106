# pylint: skip-file
from escape_cli.static.constants import DISCOVER_NAMESPACE
from .django import django_patch
from .flask import flask_patch

from loguru import logger


def patch_app(config: dict, entrypoint: str, as_module: bool) -> None:

    logger.info(f'> {entrypoint}')

    if config[DISCOVER_NAMESPACE]['httpLib'].lower() == 'django':
        django_patch(entrypoint, as_module)

    elif config[DISCOVER_NAMESPACE]['httpLib'].lower() == 'flask':
        flask_patch(entrypoint, as_module)
