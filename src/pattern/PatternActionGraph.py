import itertools
from graphlib import TopologicalSorter, CycleError
from typing import List, Dict, Set

from src.pattern.PatternAction import PatternAction
from src.pddl.Action import Action
from src.pddl.Atom import Atom


class PatternActionGraph:
    graphDict: Dict[PatternAction, List[PatternAction]]
    action2patternAction: Dict[Action, PatternAction]
    patternAction2action: Dict[PatternAction, Action]

    def __init__(self, actionList: Set[Action]):

        self.action2patternAction = dict((a, PatternAction.fromAction(a)) for a in actionList)
        self.patternAction2action = dict((pa, a) for (a, pa) in self.action2patternAction.items())
        patternActions = sorted([self.action2patternAction[a] for a in actionList])

        self.affected: Dict[Atom, Set[Action]] = dict()
        for a in actionList:
            for v in a.getPredicates():
                self.affected.setdefault(v, set())
                self.affected[v].add(a)

        self.graphDict = dict()
        for a in patternActions:
            self.graphDict[a] = list()
        # pairs = itertools.combinations_with_replacement(patternActions, 2)

        c = 0
        for aa in actionList:
            for v in aa.getPredicates():
                for ab in self.affected[v]:
                    c += 1
                    a = self.action2patternAction[aa]
                    b = self.action2patternAction[ab]
                    if a <= b:
                        continue
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
