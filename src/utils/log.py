import logging
import sys

from src.config.settings import api_log_config

FORMATTER = logging.Formatter(
    fmt='[%(levelname)s] %(asctime)s,%(msecs)03d %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
)

_logger = logging.getLogger('python_api_tests')
_logger.setLevel(logging.DEBUG)

info = _logger.info

_logger.propagate = False

if api_log_config.CONSOLE:
    def _console_handler() -> logging.StreamHandler:
        """Collect API calls stdout to console"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    _logger.addHandler(_console_handler())

if api_log_config.FILE:
    def _file_handler() -> logging.FileHandler:
        """Collect API calls stdout to file tests/cream_py/python_tests_api_calls.log"""
        file_handler = logging.FileHandler('python_tests_api_calls.log', mode='w')
        file_handler.setFormatter(FORMATTER)
        file_handler.setLevel(logging.DEBUG)
        return file_handler

    _logger.addHandler(_file_handler())