import logging

from abstraction.constants import DEFAULT_LOG_LEVEL
from abstraction.constants import LIBRARY_NAME

"""
Logging setup for plotly helper. 
"""

logger = logging.getLogger(LIBRARY_NAME.upper())
logger.setLevel(DEFAULT_LOG_LEVEL)


def change_log_level(log_level: int) -> None:
    logger.setLevel(log_level)


class logging_level:
    @property
    def INFO(self):
        logger.setLevel(logging.INFO)

    @property
    def DEBUG(self):
        logger.setLevel(logging.DEBUG)
