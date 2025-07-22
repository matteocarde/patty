from typing import Set, Dict, Tuple, List

from classes.utils.Constants import EPSILON
from src.ices.Happening import Happening, ACTION_START, ACTION_END, IEFF, ICOND_START, ICOND_END, HappeningEffect, \
    HappeningAction, HappeningActionStart
from src.ices.ICEAction import ICEAction
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETransitionVariables import ICETransitionVariables
from src.smt.SMTExpression import SMTExpression


class ICEPatternPrecedenceGraphInstradi:
    nodes: Set[Happening]
    edges: Dict[Happening, Set[Happening]]
    delta: Dict[Tuple[Happening, Happening], SMTExpression or float]
    forced: Dict[Tuple[Happening, Happening], SMTExpression or float]
    forcedPredecessors: Dict[Happening, Set[Happening]]
    forcedSuccessors: Dict[Happening, Set[Happening]]

    def __init__(self, pattern: ICEPattern, tVars: ICETransitionVariables):

        self.nodes = set()
        self.edges = dict()
        self.predecessors = dict()
        self.delta = dict()

        self.forced = dict()
        self.forcedPredecessors = dict()
        self.forcedSuccessors = dict()

        actionHappenings: Dict[ICEAction, HappeningActionStart] = dict()
        actionEffectHappenings: Dict[ICEAction, List[HappeningEffect]] = dict()
        self.happeningParentAction: Dict[Happening, HappeningActionStart] = dict()

        for i, h_i in enumerate(pattern):
            self.nodes.add(h_i)
            self.edges[h_i] = set()
            self.predecessors[h_i] = set()

            if isinstance(h_i, HappeningActionStart):
                actionHappenings[h_i.action] = h_i
                actionEffectHappenings[h_i.action] = list()

            if hasattr(h_i, "parent") and isinstance(h_i.parent, ICEAction):
                self.happeningParentAction[h_i] = actionHappenings[h_i.parent]

            if isinstance(h_i, HappeningEffect) and isinstance(h_i.parent, ICEAction):
                actionEffectHappenings[h_i.parent].append(h_i)

        for action, h_i in actionHappenings.items():
            if len(actionEffectHappenings[action]) <= 1:
                continue
            for h_p, h_q in zip(actionEffectHappenings[action][:-1], actionEffectHappenings[action][1:]):
                # delta = h_q.effect - h_p.effect
                # if delta > 0:
                #     self.forced[h_p, h_q] = delta
                self.forcedPredecessors.setdefault(h_q, set())
                self.forcedPredecessors.setdefault(h_p, set())
                self.forcedPredecessors[h_q].add(h_p)
                self.forcedPredecessors[h_p].add(h_q)

        for i, h_i in enumerate(pattern):

            for h_j in pattern[i + 1:]:

                if i == 0:
                    # self.setDelta(h_i, h_j, EPSILON)
                    pass
                elif ((h_i.type == ICOND_END) and h_j.type == IEFF and
                      h_i.parent != h_j.parent and h_i.inMutexWith(h_j)):
                    self.setDelta(h_i, h_j, 0)
                elif (h_i.type == IEFF and (h_j.type == ICOND_START) and
                      h_i.parent != h_j.parent and h_i.inMutexWith(h_j)):
                    self.setDelta(h_i, h_j, EPSILON)
                elif h_i.type == IEFF and h_j.type == IEFF and h_i.inMutexWith(h_j) and h_i.parent != h_j.parent:
                    self.setDelta(h_i, h_j, EPSILON)
        pass

    def setDelta(self, h_i: Happening, h_j: Happening, value: SMTExpression or float):
        assert (h_i, h_j) not in self.delta

        # for h_p in self.forcedPredecessors.get(h_j, []):
        #     if (h_i, h_p) in self.delta:
        #         return
        #
        # for h_p in self.forcedPredecessors.get(h_i, []):
        #     if (h_p, h_j) in self.delta:
        #         del self.delta[h_p, h_j]
        #         self.edges[h_p].remove(h_j)
        #         self.predecessors[h_j].remove(h_p)

        if h_i in self.happeningParentAction:
            value += Happening.computeTime(h_i)
            h_i = self.happeningParentAction[h_i]

        if h_j in self.happeningParentAction:
            value -= Happening.computeTime(h_j)
            h_j = self.happeningParentAction[h_j]

        if (h_i, h_j) in self.delta and self.delta[h_i, h_j] > value:
            return

        # assert (h_i, h_j) not in self.delta
        self.edges[h_i].add(h_j)
        self.predecessors[h_j].add(h_i)
        self.delta[h_i, h_j] = value

        # print("SET_DELTA: ", h_i, h_j, value)

        # for p in self.predecessors[h_i]:
        #     if (p, h_j) in self.delta and self.delta[p, h_j] < self.delta[p, h_i] + self.delta[h_i, h_j]:
        #         del self.delta[p, h_j]
        #         self.edges[p].remove(h_j)
        #         self.predecessors[h_j].remove(p)

    def printDot(self):
        print("digraph {")
        for h_i in self.nodes:
            print(f"\t\"{h_i}\"")
            for h_j in self.edges[h_i]:
                print(f"\t\"{h_i}\" -> \"{h_j}\" [label=\"{self.delta[h_i, h_j]}\"]")
        print("}")
