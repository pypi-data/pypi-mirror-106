"""The formatter that will be passed to loguru."""


def format_logs(record: dict) -> str:
    """Format loguru records properly."""
    if record['level'].name == 'SUCCESS':
        return '<bold><blue>escape</blue></bold> | <bold><green>{level}</green></bold> | <green>{message}</green>\n'
    if record['level'].name == 'WARNING':
        return '<bold><blue>escape</blue></bold> | <bold><yellow>{level}</yellow></bold> | <yellow>{message}</yellow>\n'
    if record['level'].name == 'ERROR':
        return '<bold><blue>escape</blue></bold> | <bold><red>{level}</red></bold> | <red>{message}</red>\n'
    return '<bold><blue>escape</blue></bold> | <bold><blue>{level}</blue></bold> | {message}\n'
