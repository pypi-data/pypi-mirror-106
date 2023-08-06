""" main """
from pathlib import Path

import QLog
from QLog import QLogHighlight, QLogDebug, QLogInfo, QLogWarning, QLogError, LogLevel
from QLog.azure_system_logger import AzureSystemLogger
from QLog.console_logger import ConsoleLogger
from QLog.file_logger import FileLogger
from QLog.system_logger import SystemLogger


def main():
    """ main """

    QLog.loggers = [AzureSystemLogger(log_level=LogLevel.INFO), ConsoleLogger(), FileLogger(log_level=LogLevel.DEBUG, path=Path('log/test.log')), SystemLogger(log_level=LogLevel.INFO)]
    QLogHighlight('Highlight')
    QLogDebug('Debug')
    QLogInfo('Info')
    QLogWarning('Warning')
    QLogError('Error')


if __name__ == '__main__':
    main()
