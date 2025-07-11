from typing import Set, Dict, Tuple

from classes.utils.Constants import EPSILON
from src.ices.Happening import Happening, ACTION_START, ACTION_END, IEFF, ICOND_START, ICOND_END
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETransitionVariables import ICETransitionVariables
from src.smt.SMTExpression import SMTExpression


class ICEPatternPrecedenceGraph:
    nodes: Set[Happening]
    edges: Dict[Happening, Set[Happening]]
    delta: Dict[Tuple[Happening, Happening], SMTExpression or float]

    def __init__(self, pattern: ICEPattern, tVars: ICETransitionVariables):

        self.nodes = set()
        self.edges = dict()
        self.predecessors = dict()
        self.delta = dict()

        for i, h_i in enumerate(pattern):
            self.nodes.add(h_i)
            self.edges[h_i] = set()
            self.predecessors[h_i] = set()

        for i, h_i in enumerate(pattern):

            for h_j in pattern[i + 1:]:

                if i == 0:
                    # self.setDelta(h_i, h_j, EPSILON)
                    pass
                elif h_i.type == ACTION_START and h_j.type == ACTION_END and h_i.action == h_j.action:
                    self.setDelta(h_i, h_j, tVars.durVariables[h_i])
                elif h_i.type == ACTION_START and h_j.type == ACTION_START and h_i.action == h_j.action:
                    self.setDelta(h_i, h_j, tVars.durVariables[h_i])
                elif h_i.type == ACTION_END and h_j.type == ACTION_END and h_i.action == h_j.action:
                    self.setDelta(h_i, h_j, EPSILON)
                elif h_i.type == ACTION_END and h_j.type == ACTION_START and h_i.action == h_j.action:
                    self.setDelta(h_i, h_j, 0)
                elif (h_i.type == ICOND_START or h_i.type == ICOND_END) and h_j.type == IEFF and h_i.inMutexWith(h_j):
                    self.setDelta(h_i, h_j, 0)
                elif h_i.type == IEFF and (h_j.type == ICOND_START or h_j.type == ICOND_END) and h_i.inMutexWith(h_j):
                    self.setDelta(h_i, h_j, EPSILON)
                elif h_i.type == IEFF and h_j.type == IEFF and h_i.inMutexWith(h_j):
                    self.setDelta(h_i, h_j, EPSILON)
        pass

    def setDelta(self, h_i: Happening, h_j: Happening, value: SMTExpression or float):
        assert (h_i, h_j) not in self.delta
        self.edges[h_i].add(h_j)
        self.predecessors[h_j].add(h_i)
        self.delta[h_i, h_j] = value

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
