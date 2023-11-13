from enum import Enum
import sys


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    NONE = 2


class Log:
    logLevel: LogLevel

    def __init__(self, logLevel: LogLevel) -> None:
        self.logLevel = logLevel

    def debug(self, message: str):
        if self.logLevel in [LogLevel.DEBUG, LogLevel.INFO]:
            print(f"DEBUG: {message}")

    def info(self, message):
        if self.logLevel in [LogLevel.INFO]:
            print(f"INFO:  {message}")

    def error(self, message):
        print(f"ERROR: {message}")


class Main:
    log: Log

    def __init__(self, filename: str, logLevel=LogLevel.DEBUG) -> None:
        self.log = Log(logLevel)
        self.log.debug(filename)


if len(sys.argv) != 2:
    raise Exception("Invalid arguments. Usage: python main.py dataFile.txt")

runner = Main(sys.argv[1])
