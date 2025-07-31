from typing import Set, Dict, Tuple, List

from classes.instradi.Instradi import Instradi
from classes.instradi.station.Route import Route
from classes.planning.actions.MoveAction import MoveAction
from classes.planning.actions.OverlapAction import OverlapAction
from classes.utils.Constants import EPSILON
from src.ices.Happening import Happening, ACTION_START, ACTION_END, IEFF, ICOND_START, ICOND_END, HappeningEffect, \
    HappeningAction, HappeningActionStart, HappeningConditionStart, HappeningConditionEnd
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

    def __init__(self, pattern: ICEPattern, tVars: ICETransitionVariables, instradi: Instradi):

        self.instradi = instradi

        self.nodes = set()
        self.edges = dict()
        self.predecessors = dict()
        self.delta = dict()

        self.forced = dict()
        self.forcedPredecessors = dict()
        self.forcedSuccessors = dict()

        self.useless: List[Tuple[Happening, Happening]] = list()

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

        tByEffects = pattern.getTouchedAtomsIndexes()
        tByConditionStart = pattern.getTouchedByConditionStart()

        for i, h_i in enumerate(pattern):
            if i == 0:
                # self.setDelta(h_i, h_j, EPSILON)
                pass

            ps = set()
            if isinstance(h_i, HappeningConditionEnd):
                for v in h_i.condition.conditions.atoms:
                    for j in tByEffects.get(v, []):
                        if j > i:
                            ps.add(j)
                for j in ps:
                    self.setDelta(h_i, pattern[j], 0)

            if isinstance(h_i, HappeningEffect):
                for e in h_i.effect.effects:
                    v = e.getAtom()
                    for j in tByEffects.get(v, []) + tByConditionStart.get(v, []):
                        if j > i:
                            ps.add(j)
                for j in ps:
                    self.setDelta(h_i, pattern[j], EPSILON)

            # for h_j in pattern[i + 1:]:
            #
            #     if h_i.type == ICOND_END and h_j.type == IEFF and h_i.inMutexWith(h_j):
            #         self.setDelta(h_i, h_j, 0)
            #     elif h_i.type == IEFF and h_j.type == ICOND_START and h_i.inMutexWith(h_j):
            #         self.setDelta(h_i, h_j, EPSILON)
            #     elif h_i.type == IEFF and h_j.type == IEFF and h_i.inMutexWith(h_j):
            #         self.setDelta(h_i, h_j, EPSILON)
        pass

    def isUseless(self, h_i: Happening, h_j: Happening):
        if hasattr(h_i, "parent") and hasattr(h_j, "parent"):
            if h_i.parent == h_j.parent:
                return True

            if not isinstance(h_i.parent, ICEAction) or not isinstance(h_j.parent, ICEAction):
                return False

            a_i: ICEAction = h_i.parent
            a_j: ICEAction = h_j.parent

            if a_i.originalName == a_j.originalName:
                return "mutex"

            if hasattr(a_i, "train") and hasattr(a_j, "train"):
                t_i = a_i.train
                t_j = a_j.train

                if t_i != t_j:
                    return False

                if hasattr(a_i, "route") and hasattr(a_j, "route"):
                    r_i: Route = a_i.route
                    r_j: Route = a_j.route

                    if r_i == r_j:
                        return False

                    if not self.instradi.stationGraph.areConnected(r_i, r_j):
                        # print("Is useless to constrain", h_i, h_j)
                        return "mutex" if type(a_i) == type(a_j) else True

                if hasattr(a_i, "toRoute") and hasattr(a_j, "fromRoute"):
                    r_i: Route = a_i.toRoute
                    r_j: Route = a_j.fromRoute

                    if r_i == r_j:
                        return False

                    if not self.instradi.stationGraph.areConnected(r_i, r_j):
                        # print("Is useless to constrain", h_i, h_j)

                        return True

                # if hasattr(a_i, "route") and isinstance(a_j, OverlapAction):
                #     if a_i.route != a_j.fromRoute:
                #         return True
                # if isinstance(a_i, OverlapAction) and hasattr(a_j, "route"):
                #     if a_j.route != a_i.fromRoute:
                #         return True

            return False

    def setDelta(self, h_i: Happening, h_j: Happening, value: SMTExpression or float):
        assert (h_i, h_j) not in self.delta

        isUseless = self.isUseless(h_i, h_j)
        if isUseless == "mutex":
            self.useless.append((h_i, h_j))

        if isUseless:
            return

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
