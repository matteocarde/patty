from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPatternPrecedenceGraph import ICEPatternPrecedenceGraph
from src.ices.ICETask import ICETask
from src.ices.ICETransitionVariables import ICETransitionVariables


class ICEEncoding:
    task: ICETask
    pattern: ICEPattern
    ppg: ICEPatternPrecedenceGraph

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task = task
        self.pattern = pattern
        self.tVars = ICETransitionVariables(task, pattern)
        self.ppg = ICEPatternPrecedenceGraph(pattern, self.tVars)
