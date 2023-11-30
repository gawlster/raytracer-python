from enum import Enum
from typing import List
from inspect import getframeinfo, stack


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    NONE = 2


class Log:
    logLevel: LogLevel

    def __init__(self, logLevel: LogLevel) -> None:
        self.logLevel = logLevel

    def debug(self, message: str) -> None:
        if self.logLevel in [LogLevel.DEBUG]:
            print(f"DEBUG {self._getLogLineNumber()}: {message}")

    def info(self, message) -> None:
        if self.logLevel in [LogLevel.INFO, LogLevel.DEBUG]:
            print(f"INFO {self._getLogLineNumber()}:  {message}")

    def warn(self, message) -> None:
        if self.logLevel in [LogLevel.INFO, LogLevel.DEBUG]:
            print(f"WARN {self._getLogLineNumber()}:  {message}")

    def error(self, message) -> None:
        print(f"ERROR {self._getLogLineNumber()}: {message}")

    def formatListForString(self, list: List) -> str:
        formattedList = "\n".join(list).replace("\n", "\n\t")
        return f"""
    [
    \t{formattedList}
    ]
    """

    def _getLogLineNumber(self) -> str:
        caller = getframeinfo(stack()[2][0])
        return f"[file: {caller.filename.split('/').pop()}, line: {caller.lineno}]"


log = Log(LogLevel.INFO)
