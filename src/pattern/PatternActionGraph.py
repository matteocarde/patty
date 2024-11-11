import itertools
from graphlib import TopologicalSorter, CycleError
from typing import List, Dict, Set

from src.pattern.PatternAction import PatternAction
from src.pddl.Action import Action


class PatternActionGraph:
    graphDict: Dict[PatternAction, List[PatternAction]]
    action2patternAction: Dict[Action, PatternAction]
    patternAction2action: Dict[PatternAction, Action]

    def __init__(self, actionList: Set[Action]):

        self.action2patternAction = dict((a, PatternAction.fromAction(a)) for a in actionList)
        self.patternAction2action = dict((pa, a) for (a, pa) in self.action2patternAction.items())
        patternActions = sorted([self.action2patternAction[a] for a in actionList])

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

    def getSorted(self) -> List[Action]:
        while True:
            try:
                ts = TopologicalSorter(self.graphDict)
                return [self.patternAction2action[pa] for pa in ts.static_order()]
            except CycleError as e:
                cycle = e.args[1]
                self.graphDict[cycle[1]].remove(cycle[0])
