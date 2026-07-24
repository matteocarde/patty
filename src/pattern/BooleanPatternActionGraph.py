from typing import List, Dict, Set, Tuple, Iterator

from src.pattern.BooleanPatternAction import BooleanPatternAction
from src.pattern.PatternAction import PatternAction
from src.pattern.PatternActionGraph import PatternActionGraph
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.utils.TimeStat import TimeStat


class BooleanPatternActionGraph(PatternActionGraph):
    graphDict: Dict[BooleanPatternAction, List[BooleanPatternAction]]
    action2patternAction: Dict[Action, BooleanPatternAction]
    patternAction2action: Dict[BooleanPatternAction, Action]

    def __init__(self, actionList: Set[Action]):
        super().__init__(actionList)

        t = TimeStat.startHolder("--- Initializing PatternActionGraph")
        self.action2patternAction = dict((a, BooleanPatternAction.fromAction(a)) for a in actionList)
        self.patternAction2action = dict((pa, a) for (a, pa) in self.action2patternAction.items())
        patternActions = sorted([self.action2patternAction[a] for a in actionList])

        prePos: Dict[Atom, Set[Action]] = dict()
        preNeg: Dict[Atom, Set[Action]] = dict()
        adding: Dict[Atom, Set[Action]] = dict()
        deleting: Dict[Atom, Set[Action]] = dict()

        for a in actionList:
            for v in a.getPredicates():
                prePos.setdefault(v, set())
                preNeg.setdefault(v, set())
                adding.setdefault(v, set())
                deleting.setdefault(v, set())
                if v in a.prePos:
                    prePos[v].add(a)
                if v in a.preNeg:
                    preNeg[v].add(a)
                if v in a.addedAtoms:
                    adding[v].add(a)
                if v in a.deletedAtoms:
                    deleting[v].add(a)

        self.graphDict = dict()
        for a in patternActions:
            self.graphDict[a] = list()

        t.endHolderMilliseconds()

        t = TimeStat.startHolder("--- Constructing PatternActionGraph")
        c = 0
        cu = 0
        print(f"--- Number of actions: {len(actionList)}")
        for a in actionList:
            activeBlocking = set()
            activeSupporting = set()
            passiveBlocking = set()

            for v in a.addedAtoms:
                activeBlocking.update(preNeg[v])
                activeSupporting.update(prePos[v])

            for v in a.deletedAtoms:
                activeBlocking.update(prePos[v])
                activeSupporting.update(preNeg[v])

            for v in a.prePos:
                passiveBlocking.update(deleting[v])
            for v in a.preNeg:
                passiveBlocking.update(adding[v])

            pass
            # 17640/32100
            for b in ((activeBlocking - passiveBlocking) | activeSupporting) - {a}:
                pa = self.action2patternAction[a]
                pb = self.action2patternAction[b]
                if a <= b:
                    continue
                c += 1
                comp = pa.compare(pb)

                if comp != 0:
                    cu += 1
                if comp < 0:
                    self.graphDict[pb].append(pa)
                if comp > 0:
                    self.graphDict[pa].append(pb)
        print(f"--- Number of compares: {cu}/{c}")

        t.endHolderMilliseconds()

        t = TimeStat.startHolder("--- Sorting neighbours of PatternActionGraph")
        for a in patternActions:
            self.graphDict[a] = sorted(self.graphDict[a])
        t.endHolderMilliseconds()
