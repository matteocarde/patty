from typing import Dict

import time

from src.utils.LogPrint import LogPrint, LogPrintLevel, console

TIMINGS_GROUP = {}


class TimeHolder:

    def __init__(self, message: str):
        self.__start = time.time()
        self.__message = message

    def endHolder(self):
        console.log(f"{self.__message}: {round(time.time() - self.__start, 2)}s", LogPrintLevel.TIMES)

    def getCheckPointTime(self):
        return round(time.time() - self.__start, 2)

    def endHolderMilliseconds(self, group: str or None = None):
        val = (time.time() - self.__start) * 1000
        console.log(f"Ended {self.__message}: {int(val)}", LogPrintLevel.TIMES)
        if group:
            TIMINGS_GROUP.setdefault(group, 0)
            TIMINGS_GROUP[group] += val
        return val


class TimeStat:

    def __init__(self):
        self.__timings: Dict[str, int] = dict()
        self.__results: Dict[str, int] = dict()

    @staticmethod
    def now() -> int:
        return round(time.perf_counter() * 1000)

    @staticmethod
    def timeCall(call):
        a = time.time()
        # print(f"Start {call.__name__}")
        x = call()
        b = time.time()
        console.log(f"{call.__name__} = {b - a}s - {len(x)} rules", LogPrintLevel.TIMES)
        return x

    @staticmethod
    def startHolder(message: str):
        # print("Starting", message)
        return TimeHolder(message)

    def start(self, name: str):
        self.__timings[name] = TimeStat.now()
        if console:
            console.log(f"Started {name}", LogPrintLevel.STEPS)

    def end(self, name: str, group: str or None = None):
        self.__results[name] = TimeStat.now() - self.__timings[name]
        if console:
            console.log(f"Ended {name}: {self.__results[name]}", LogPrintLevel.STEPS)

        if group:
            TIMINGS_GROUP.setdefault(group, 0)
            TIMINGS_GROUP[group] += self.__results[name]

    def get(self, name: str) -> int:
        return self.__results[name]

    def __str__(self):
        str = ""
        for (key, value) in self.__results.items():
            str += f"{key}: {value}ms\n"
        return str

    @staticmethod
    def printGroups():
        print(TIMINGS_GROUP)
