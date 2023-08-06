"""Logger to log into azure system logger"""

import logging

from QLog.log_entry import LogEntry
from QLog.log_level import LogLevel
from QLog.logger import Logger


class AzureSystemLogger(Logger):
    """Logger to log into system logger"""

    def __init__(self, log_level=LogLevel.INFO):
        self.log_level = log_level
        if self.log_level is LogLevel.INFO:
            logging.getLogger().setLevel(logging.INFO)
        if self.log_level is LogLevel.WARNING:
            logging.getLogger().setLevel(logging.WARNING)
        if self.log_level is LogLevel.ERROR:
            logging.getLogger().setLevel(logging.ERROR)
        else:
            logging.getLogger().setLevel(logging.DEBUG)

    def do_log(self, log_entry: LogEntry):
        text = log_entry.log_level.text + ' ' + log_entry.azure_meta_text + log_entry.text
        if log_entry.log_level is LogLevel.INFO:
            return logging.info(text)
        if log_entry.log_level is LogLevel.WARNING:
            return logging.warning(text)
        if log_entry.log_level is LogLevel.ERROR:
            return logging.error(text)
        return logging.debug(text)
