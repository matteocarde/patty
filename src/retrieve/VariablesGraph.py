from __future__ import annotations

from typing import Dict, List, Set

from sympy import symbols, Expr

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Trace import Trace


class VariablesGraph:
    class Node:
        def __init__(self, atom: Atom, i: int):
            replaced = str(atom).replace(' ', '\_')
            self.name = f"{replaced}_{{{i}}}"
            self.var = symbols(self.name)
            self.value = self.var
            self.index = i
            self.connectedWith: Set[VariablesGraph.Node] = set()

        def __hash__(self):
            return hash(self.name)

        def __repr__(self):
            return str(self.value)

        def addConnection(self, node: VariablesGraph.Node):
            # print(f"{self.var} -- {node.var}")
            self.connectedWith.add(node)
            node.connectedWith.add(self)
            if node.index < self.index:
                self.var = node.var
                self.value = node.value
            if self.index < node.index:
                node.var = self.var
                node.value = self.value

        def setValue(self, value):
            if self.value == value:
                return
            if not self.value.free_symbols:
                raise Exception("Something wrong. It is overwriting a variable")
            self.value = value
            for n in self.connectedWith:
                n.setValue(value)
            pass

    def __init__(self, domain: GroundedDomain, trace: Trace):
        self.Xis: Dict[int, Dict[Atom, VariablesGraph.Node]] = dict()
        self.m = len(trace)
        self.__fixedXi: Dict[int, Dict[Atom, Expr]] = dict()

        for i in range(0, self.m + 1):
            Xi: Dict[Atom, VariablesGraph.Node] = dict()
            self.Xis[i] = Xi
            for atom in domain.allAtoms:
                Xi[atom] = VariablesGraph.Node(atom, i)

        pass

    def __repr__(self):
        return str(self.Xis)

    def getNode(self, i: int, atom: Atom) -> VariablesGraph.Node:
        return self.Xis[i][atom]

    def fixXi(self):
        for i in self.Xis.keys():
            self.__fixedXi[i] = self.getXi(i)

    def getXi(self, i: int) -> Dict[Atom, Expr]:
        if i in self.__fixedXi:
            return self.__fixedXi[i]
        return dict([(atom, node.value) for (atom, node) in self.Xis[i].items()])
