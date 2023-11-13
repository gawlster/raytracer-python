from enum import Enum
import sys
from typing import List


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    NONE = 2


class Log:
    logLevel: LogLevel

    def __init__(self, logLevel: LogLevel) -> None:
        self.logLevel = logLevel

    def debug(self, message: str) -> None:
        if self.logLevel in [LogLevel.DEBUG, LogLevel.INFO]:
            print(f"DEBUG: {message}")

    def info(self, message) -> None:
        if self.logLevel in [LogLevel.INFO]:
            print(f"INFO:  {message}")

    def warn(self, message) -> None:
        if self.logLevel in [LogLevel.INFO, LogLevel.DEBUG]:
            print(f"WARN:  {message}")

    def error(self, message) -> None:
        print(f"ERROR: {message}")

    def formatListForString(self, list: List) -> str:
        formattedList = "\n".join(list).replace("\n", "\n\t")
        return f"""
    [
    \t{formattedList}
    ]
    """


class Main:
    fileLines: List[str] = []

    def __init__(self, filename: str) -> None:
        log.debug(f"Initing new raytracer based on data in {filename}")

        with open(filename, "r") as fd:
            self.fileLines = fd.readlines()
            for i, line in enumerate(self.fileLines):
                self.fileLines[i] = line.rstrip()

        log.debug(f"Read file into list: {log.formatListForString(self.fileLines)}")


if len(sys.argv) != 2:
    raise Exception("Invalid arguments. Usage: python main.py dataFile.txt")

log = Log(LogLevel.DEBUG)
runner = Main(sys.argv[1])
