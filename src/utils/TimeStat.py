from typing import Dict

import time

from src.utils.LogPrint import LogPrint, LogPrintLevel


class TimeStat:

    def __init__(self):
        self.__timings: Dict[str, int] = dict()
        self.__results: Dict[str, int] = dict()

    @staticmethod
    def now() -> int:
        return round(time.perf_counter() * 1000)

    def start(self, name: str, console: LogPrint or None = None):
        self.__timings[name] = TimeStat.now()
        if console:
            console.log(f"Started {name}", LogPrintLevel.STEPS)

    def end(self, name: str, console: LogPrint or None = None):
        self.__results[name] = TimeStat.now() - self.__timings[name]
        if console:
            console.log(f"Ended {name}", LogPrintLevel.STEPS)

    def get(self, name: str) -> int:
        return self.__results[name]

    def __str__(self):
        str = ""
        for (key, value) in self.__results.items():
            str += f"{key}: {value}ms\n"
        return str
