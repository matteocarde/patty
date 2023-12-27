from __future__ import annotations

import copy
from typing import Dict, Set, Tuple, List

from sympy import Expr

from src.pddl.Atom import Atom
from src.pddl.Constant import Constant
from src.pddl.Predicate import Predicate
from src.pddl.TypedPredicate import TypedPredicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Literal(Predicate):
    sign: str
    atom: Atom
    funct: str

    def __init__(self):
        super().__init__()

    def __deepcopy__(self, m=None) -> Literal:
        m = {} if m is None else m
        l = Literal()
        l.sign = self.sign
        l.atom = copy.deepcopy(self.atom, m)
        l.funct = self.funct
        return l

    @classmethod
    def fromAtom(cls, atom: Atom, sign: str):
        lit = cls()
        lit.atom = atom
        lit.sign = sign
        lit.funct = lit.atom.toFunctionName()
        lit.alphaFunct = lit.atom.toAlphaFunctionName()
        return lit

    def replace(self, atom: Atom, w: Predicate):
        if self.atom != atom:
            return copy.deepcopy(self)
        if self.sign != "+":
            raise Exception(f"Cannot replace {atom} with {w} since it appears as negated")
        return copy.deepcopy(w)

    def replaceDict(self, r: Dict[Atom, Predicate]):
        if self.atom in r:
            return copy.deepcopy(r[self.atom])
        return copy.deepcopy(self.atom)

    def isLinearIncrement(self):
        return False



    @classmethod
    def fromNode(cls, node: p.PositiveLiteralContext or p.NegativeLiteralContext) -> Literal:
        literal = cls()

        literal.sign = "+" if isinstance(node, p.PositiveLiteralContext) else "-"
        positiveLiteralNode = node.getChild(2) if literal.sign == "-" else node
        atomNode = positiveLiteralNode.getChild(1)

        literal.atom = Atom.fromNode(atomNode)
        literal.string = f"({literal.atom})"
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def getPredicates(self) -> Set[Atom]:
        return {self.atom}

    def getFunctions(self) -> Set[Atom]:
        return {self.atom}

    def getAtom(self) -> Atom:
        return self.atom

    def getLiterals(self) -> Set[Predicate]:
        return {self}

    def ground(self, subs: Dict[str, str], delta=1) -> Literal:

        literal = Literal()
        literal.sign = self.sign

        literal.atom = self.atom.ground(subs)
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def __str__(self):
        if self.sign == "+":
            return f"({self.atom})"
        else:
            return f"(not ({self.atom}))"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromPositiveString(cls, string: str) -> Literal:
        return cls.fromNode(Utilities.getParseTree(string).positiveLiteral())

    @classmethod
    def fromNegativeString(cls, string: str) -> Literal:
        return cls.fromNode(Utilities.getParseTree(string).negativeLiteral())

    def toLatex(self) -> str:
        if self.sign == "+":
            return self.atom.toLatex()
        return f"(\\neg {self.atom.toLatex()})"

    def __hash__(self):
        return hash(self.sign + str(self.atom))

    def __eq__(self, other):
        if not isinstance(other, Literal):
            return False
        return self.sign == other.sign and self.atom == other.atom

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        if self.atom not in subs and default is None:
            return self
        if self.atom not in subs and default is not None:
            return Constant(default)
        if self.atom in subs:
            return Constant(subs[self.atom])

    def canHappen(self, subs: Dict[Atom, float], default=None) -> bool:
        return True

    def canHappenLifted(self, sub: Tuple, params: List[str], problem) -> bool:
        if not problem.isPredicateStatic[self.atom.name]:
            return True
        attSet = set(self.atom.attributes)
        subStr = ",".join([sub[i] for i, p in enumerate(params) if p in attSet])
        atomStr = f"{self.atom.name}({subStr})"
        if self.sign == "+":
            return atomStr in problem.canHappenValue
        if self.sign == "-":
            return atomStr not in problem.canHappenValue

    def canHappenLiftedPartial(self, item: Tuple, params: List[str], problem) -> bool:
        if not problem.isPredicateStatic[self.atom.name]:
            return True

        if not set(params).intersection(set(self.atom.attributes)):
            return True

        if not self.atom.name in problem.assignmentsTree:
            return False

        from src.pddl.Problem import Problem
        problem: Problem
        totalItems = []
        root = problem.assignmentsTree[self.atom.name]
        for i in range(len(item)):
            if params[i] not in self.atom.attributes:
                continue
            indexOfParam = self.atom.attributes.index(params[i])
            if indexOfParam not in root or item[i] not in root[indexOfParam]:
                totalItems.append(set())
                continue
            totalItems.append(root[indexOfParam][item[i]])

        if not totalItems:
            return False

        if len(totalItems) == 1:
            return True

        finalSet: Set = totalItems[0]
        for itemSet in totalItems[1:]:
            finalSet = finalSet.intersection(itemSet)

        return len(finalSet) > 0

    def isDynamicLifted(self, problem) -> bool:
        return not problem.isPredicateStatic[self.atom.name]

    def getLinearIncrement(self) -> float:
        return 0

    def toExpression(self) -> Expr:
        return self.atom.toExpression()

    def expressify(self, symbols: Dict[Atom, Expr]) -> Expr:
        return symbols[self.atom]

    def comesFromTypedPredicate(self, tp: TypedPredicate) -> bool:
        return tp.name == self.atom.name and len(tp.parameters) == len(self.atom.attributes)

    def expressifyWithEquation(self, symbols: Dict[Atom, Expr]) -> Expr:
        # return Eq(self.expressify(symbols), 1) if self.sign == "+" else Eq(self.expressify(symbols), -1)
        return self.expressify(symbols) - 1 if self.sign == "+" else self.expressify(symbols) + 1
