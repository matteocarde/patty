from enum import IntEnum


class LogPrintLevel(IntEnum):
    STEPS = 1  # The steps that compose the planning (e.g. "Grounding...", "Solving...")
    STATS = 2  # All the stats of the planning
    TIMES = 3  # The timings of the various part of the plan
    PLAN = 4  # The solution

    @staticmethod
    def getLevels():
        return """
         LEVEL 0 - Muted
         LEVEL 1 - Steps (The steps that compose the planning (e.g. "Grounding...", "Solving...") + Previous levels 
         LEVEL 2 - Stats (All the stats of the planning) + Previous levels 
         LEVEL 3 - Timings (The timings of the various part of the plan) + Previous levels 
         LEVEL 4 (Default) - Plan (the solution) + Previous levels 
        """

    @staticmethod
    def getDefault():
        return 4


class LogPrint:

    # Level: 1 -> Everything
    # Level: 2 ->
    def __init__(self, verboseLevel: LogPrintLevel):
        self.__level = verboseLevel

    def log(self, log: str, level: LogPrintLevel):
        if self.__level >= level:
            print(log)
        pass
