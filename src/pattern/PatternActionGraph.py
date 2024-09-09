import itertools
from graphlib import TopologicalSorter, CycleError
from typing import List, Dict, Set

from src.pattern.PatternAction import PatternAction
from src.pddl.Action import Action


class PatternActionGraph:
    graphDict: Dict[PatternAction, List[PatternAction]]

    def __init__(self, actionList: Set[Action]):

        patternActions = sorted([PatternAction.fromAction(a) for a in actionList])

        self.graphDict = dict()
        for a in patternActions:
            self.graphDict[a] = list()
        for a, b in itertools.combinations_with_replacement(patternActions, 2):
            if a.compare(b) < 0:
                self.graphDict[b].append(a)
            if a.compare(b) > 0:
                self.graphDict[a].append(b)

        for a in patternActions:
            self.graphDict[a] = sorted(self.graphDict[a])

        pass

    def getSorted(self) -> List[PatternAction]:
        while True:
            try:
                ts = TopologicalSorter(self.graphDict)
                return list(ts.static_order())
            except CycleError as e:
                cycle = e.args[1]
                self.graphDict[cycle[1]].remove(cycle[0])
