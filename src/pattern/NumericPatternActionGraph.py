from typing import List, Dict, Set, Tuple, Iterator

from src.pattern.PatternAction import PatternAction
from src.pattern.PatternActionGraph import PatternActionGraph
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.utils.TimeStat import TimeStat


class NumericPatternActionGraph(PatternActionGraph):
    graphDict: Dict[PatternAction, List[PatternAction]]
    action2patternAction: Dict[Action, PatternAction]
    patternAction2action: Dict[PatternAction, Action]

    def __init__(self, actionList: Set[Action]):
        super().__init__(actionList)

        t = TimeStat.startHolder("Initializing PatternActionGraph")
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

        t.endHolderMilliseconds()

        t = TimeStat.startHolder("Constructing PatternActionGraph")
        c = 0
        for aa in actionList:
            for v in aa.getPredicates():
                for ab in self.affected[v]:
                    c += 1
                    a = self.action2patternAction[aa]
                    b = self.action2patternAction[ab]
                    if a <= b:
                        continue
                    comp = a.compare(b)
                    if comp < 0:
                        self.graphDict[b].append(a)
                    if comp > 0:
                        self.graphDict[a].append(b)
        t.endHolderMilliseconds()

        t = TimeStat.startHolder("Sorting neighbours of PatternActionGraph")
        for a in patternActions:
            self.graphDict[a] = sorted(self.graphDict[a])
        t.endHolderMilliseconds()
