import itertools
from graphlib import TopologicalSorter, CycleError
from typing import List, Dict, Set, Tuple, Iterator

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
                    comp = a.compare(b)
                    if comp < 0:
                        self.graphDict[b].append(a)
                    if comp > 0:
                        self.graphDict[a].append(b)

        for a in patternActions:
            self.graphDict[a] = sorted(self.graphDict[a])

        pass

    def getSorted(self) -> List[Action]:
        """
        Return a topological ordering after ignoring DFS back edges.

        graphDict[node] contains the predecessors of `node`, matching the
        representation expected by graphlib.TopologicalSorter.
        """
        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        state: Dict[PatternAction, int] = {}
        order: List[PatternAction] = []

        # Include nodes that appear only as predecessors.
        # Using a dict preserves the insertion order.
        nodes: Dict[PatternAction, None] = {
            node: None for node in self.graphDict
        }

        for predecessors in self.graphDict.values():
            for predecessor in predecessors:
                nodes.setdefault(predecessor, None)

        for start in nodes:
            if state.get(start, UNSEEN) != UNSEEN:
                continue

            state[start] = VISITING

            stack: List[
                Tuple[PatternAction, Iterator[PatternAction]]
            ] = [
                (start, iter(self.graphDict.get(start, ())))
            ]

            while stack:
                node, predecessors = stack[-1]

                try:
                    predecessor = next(predecessors)
                except StopIteration:
                    stack.pop()
                    state[node] = VISITED
                    order.append(node)
                    continue

                predecessor_state = state.get(predecessor, UNSEEN)

                if predecessor_state == UNSEEN:
                    state[predecessor] = VISITING
                    stack.append(
                        (
                            predecessor,
                            iter(self.graphDict.get(predecessor, ())),
                        )
                    )

                elif predecessor_state == VISITING:
                    # predecessor -> node closes a cycle.
                    # Ignore this edge.
                    continue

                # If it is VISITED, it is already correctly placed before node.

        return [
            self.patternAction2action[pattern_action]
            for pattern_action in order
        ]
