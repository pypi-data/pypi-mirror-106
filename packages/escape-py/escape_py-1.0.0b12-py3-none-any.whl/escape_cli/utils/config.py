"""Handle .escaperc config file."""

import os
import json

from typing import Union
from loguru import logger

from escape_cli.static.constants import ESCAPE_DIR, TRANSACTIONS_PATH, ENDPOINTS_PATH, METHODS_PATH
from escape_cli.patchs import patch_app


def get_config(config_filename: str, discover_namespace: str) -> Union[dict, None]:
    """Get configuration to correctly patch the application."""

    if not os.path.isfile(config_filename):
        logger.error(f'Config file at path {config_filename} not found. Did you run `escape-py init`?')
        return None

    with open(config_filename, 'r') as f:
        config = json.load(f)
        f.close()

        if not isinstance(config, dict) or discover_namespace not in config.keys():
            logger.error(f'Config file at path {config_filename} has a wrong format. Did you run `escape-py init`?')
            return None

        return config


def init_logs(escape_dir: str, transactions_path: str, endpoints_path: str, methods_path: str) -> None:
    """Reset the escape config directory where logs will be saved."""

    if not os.path.isdir(escape_dir):
        os.mkdir(escape_dir)

    # Instead of writing and opening the JSON each time in the middleware, we simply append to the end of file the serialized dict.
    with open(transactions_path, 'w+') as f:
        f.write('[')
        logger.success(f'Transactions have been reset: {transactions_path}')

    with open(endpoints_path, 'w+') as f:
        logger.success(f'Endpoints have been reset: {endpoints_path}')

    with open(methods_path, 'w+') as f:
        json.dump({}, f)
        logger.success(f'Methods have been reset: {methods_path}')


def close_json(char: str, file: str) -> None:
    """Properly end the json file."""

    def move_backward() -> None:
        """Move one char backward in the file."""
        fb.seek(-1, os.SEEK_END)

    with open(file, 'rb+') as fb:
        move_backward()

        # Remove the last comma if it exists
        if fb.read(1) == b',':
            move_backward()
            fb.truncate()

        # Add the final char such as right bracket or parenthesis
        fb.write(bytes(char, 'utf-8'))


def close_logs(transactions_path: str, endpoints_path: str) -> tuple[list, list]:
    """Once completed format logs to make them readable."""

    # Since the middleware is appending "json.dumps(result)," at the end of the file, we have to delete the last "," and close the list bracket ].
    close_json(']', transactions_path)

    with open(transactions_path, 'r') as f:
        transactions = json.load(f)

    try:
        with open(endpoints_path, 'r') as f:
            patterns = json.load(f)
    except json.JSONDecodeError as error:  # Handle the case where no endpoints have been saved
        raise ValueError('Unable to parse the endpoints. You may need to make at least one request to the API.') from error

    return transactions, patterns


def patch_and_run(entrypoint: str, config: dict, as_module: bool, manual: bool = False) -> dict:
    """Patch the app and run the entrypoint."""

    result: dict = {}

    # Initialize logs
    init_logs(ESCAPE_DIR, TRANSACTIONS_PATH, ENDPOINTS_PATH, METHODS_PATH)

    try:
        # Patch the app and run the entrypoint
        patch_app(config, entrypoint, as_module)
    except KeyboardInterrupt as error:
        if manual:
            logger.warning('KeyboardInterrupt exception detected, but the flag `--manual` is enabled,  so we\'ll send results anyway.')
        else:
            raise error

    # Close logs file and return result
    result['transactions'], result['endpoints'] = close_logs(TRANSACTIONS_PATH, ENDPOINTS_PATH)
    return result
