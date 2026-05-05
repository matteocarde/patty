from enum import IntEnum


class LogPrintLevel(IntEnum):
    ALL = 0
    INFO = 1  # The timings of the various part of the plan
    TIMES = 2  # The timings of the various part of the plan
    STATS = 3  # All the stats of the planning
    STEPS = 4  # The steps that compose the planning (e.g. "Grounding...", "Solving...")
    PLAN = 5  # The solution

    @staticmethod
    def getLevels():
        return """See the code at LogPrint"""

    @staticmethod
    def getDefault():
        return LogPrintLevel.ALL


class LogPrint:

    # Level: 1 -> Everything
    # Level: 2 ->
    def __init__(self):
        self.__level = LogPrintLevel.getDefault()

    def setLogLevel(self, lvl: LogPrintLevel):
        self.__level = lvl

    def log(self, log: str, level: LogPrintLevel):
        if level >= self.__level:
            print(log)
        pass


console: LogPrint = LogPrint()
