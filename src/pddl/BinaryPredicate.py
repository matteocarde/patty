from __future__ import annotations

import copy
from enum import Enum
from typing import Dict, Set

from sympy import Expr, diff

from src.pddl.Atom import Atom
from src.pddl.Constant import Constant
from src.pddl.Literal import Literal
from src.pddl.MooreInterval import MooreInterval
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class BinaryPredicateType(Enum):
    MODIFICATION = "modification"
    OPERATION = "operation"
    COMPARATION = "comparation"


class BinaryPredicate(Predicate):
    operator: str
    lhs: BinaryPredicate or Literal or Constant
    rhs: BinaryPredicate or Literal or Constant
    type: BinaryPredicateType

    def __init__(self):
        super().__init__()
        self.__functions = None

    def __deepcopy__(self, m=None) -> BinaryPredicate:
        m = {} if m is None else m
        bp = BinaryPredicate()
        bp.operator = self.operator
        bp.lhs = copy.deepcopy(self.lhs, m)
        bp.rhs = copy.deepcopy(self.rhs, m)
        bp.type = copy.deepcopy(self.type, m)
        return bp

    @classmethod
    def fromNode(cls, node: p.ModificationContext or p.ComparationContext or p.OperationContext) -> BinaryPredicate:
        bp = cls()

        if isinstance(node, p.NegatedComparationContext):
            bp = BinaryPredicate.fromNode(node.getChild(2))
            bp.operator = Utilities.inverted(bp.operator)
            return bp

        if type(node) not in {p.ModificationContext, p.ComparationContext, p.OperationContext, p.AssignmentContext}:
            raise Exception("Incorrect Binary Predicate Type: ", type(node))

        bp.operator = node.getChild(1).getText()
        bp.rhs = bp.__assignClass(node.getChild(3))
        lhsNode = node.getChild(2)

        bp.lhs = bp.__assignClass(lhsNode) if type(node) in {p.ComparationContext,
                                                             p.OperationContext} else Literal.fromNode(lhsNode)

        if type(node) in {p.ModificationContext, p.AssignmentContext}:
            bp.type = BinaryPredicateType.MODIFICATION
        elif isinstance(node, p.ComparationContext):
            bp.type = BinaryPredicateType.COMPARATION
        elif isinstance(node, p.OperationContext):
            bp.type = BinaryPredicateType.OPERATION
        else:
            raise Exception("I don't know what this is")

        return bp

    @staticmethod
    def __assignClass(node: p.OperationSideContext):
        child = node.getChild(0)
        if isinstance(child, p.OperationContext):
            return BinaryPredicate.fromNode(child)
        elif isinstance(child, p.PositiveLiteralContext):
            return Literal.fromNode(child)
        elif isinstance(child, p.ConstantContext):
            return Constant.fromNode(child)
        elif isinstance(child, p.NumberContext):
            return Constant.fromNode(child)
        else:
            raise NotImplemented()

    def ground(self, subs: Dict[str, str], delta=1) -> BinaryPredicate:
        bp = BinaryPredicate()
        bp.operator = self.operator
        bp.lhs = self.lhs.ground(subs, delta)
        bp.rhs = self.rhs.ground(subs, delta)
        bp.type = self.type

        return bp

    def replace(self, atom: Atom, w: BinaryPredicate):
        bp = BinaryPredicate()
        bp.operator = self.operator
        bp.lhs = self.lhs.replace(atom, w)
        bp.rhs = self.rhs.replace(atom, w)
        bp.type = self.type

        return bp

    def isLinearIncrement(self):
        return self.operator in {"increase", "decrease"} and self.rhs.getFunctions()

    def getAtom(self) -> Atom:
        if not isinstance(self.lhs, Literal):
            raise Exception("Cannot get atom from Binary Predicate", self)
        return self.lhs.atom

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        if not self.__functions:
            self.__functions = self.lhs.getFunctions() | self.rhs.getFunctions()
        return self.__functions

    def getLiterals(self) -> Set[Predicate]:
        return {self}

    def getFunctionsOverwrite(self) -> Set[Atom]:
        self.__functions = self.lhs.getFunctions() | self.rhs.getFunctions()
        return self.__functions

    def __str__(self):
        if self.operator == "!=":
            return f"(not (= {self.lhs} {self.rhs}))"
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, BinaryPredicate):
            return False
        return str(self) == str(other)

    def toLatex(self) -> str:
        if self.operator == "/":
            return r"\frac{" + self.lhs.toLatex() + "}{" + self.rhs.toLatex() + "}"
        return f"({self.lhs.toLatex()} {Utilities.latexOp(self.operator)} {self.rhs.toLatex()})"

    @staticmethod
    def additiveEffectsTransformation(effect: BinaryPredicate):
        x = BinaryPredicate()
        x.lhs = effect.lhs
        x.operator = "increase"
        x.rhs = effect.rhs - effect.lhs
        x.type = effect.type
        return x

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        x = BinaryPredicate()
        x.type = self.type
        x.lhs = self.lhs.substitute(subs, default) if x.type != BinaryPredicateType.MODIFICATION else self.lhs
        x.operator = self.operator
        x.rhs = self.rhs.substitute(subs, default)

        x.__functions = x.getFunctionsOverwrite()

        if not x.__functions:
            if x.type == BinaryPredicateType.OPERATION:
                return x.toConstant()
            else:
                return None

        return x

    def canHappen(self, subs: Dict[Atom, float], default=None) -> bool:
        x = BinaryPredicate()
        x.type = self.type
        x.lhs = self.lhs.substitute(subs, default) if x.type != BinaryPredicateType.MODIFICATION else self.lhs
        x.operator = self.operator
        x.rhs = self.rhs.substitute(subs, default)

        x.__functions = x.getFunctionsOverwrite()

        if x.getFunctions() or x.getPredicates():
            return True
        else:
            result = Utilities.compare(x.operator, x.lhs.value, x.rhs.value)
            return result

    def canHappenLifted(self, sub, problem, isPredicateStatic: Dict[str, bool]) -> bool:
        # if all([not isPredicateStatic[f.name] for f in self.getFunctions()]):
        #     return False
        return True

    def canHappenLiftedPartial(self, sub, problem, isPredicateStatic: Dict[str, bool]) -> bool:
        # if all([not isPredicateStatic[f.name] for f in self.getFunctions()]):
        #     return False
        return True

    def isDynamicLifted(self, problem) -> bool:
        return True

    def toConstant(self) -> Constant:
        if self.getFunctions():
            raise Exception(f"Cannot transform {self} into a Constant")
        c = Constant(float(self.toExpression()))
        return c

    def getLinearIncrement(self) -> float:
        if self.type != BinaryPredicateType.OPERATION:
            raise Exception("Cannot get linear increment since Binary Predicate is not an operation")

        if len(self.lhs.getFunctions()) > 0 and len(self.rhs.getFunctions()) > 0 and self.operator in {"*", "/"}:
            raise Exception("Cannot get linear increment in a non linear function ", self)

        return Utilities.op(self.operator, self.lhs.getLinearIncrement(), self.rhs.getLinearIncrement())

    def simplify(self):
        if self.type == BinaryPredicateType.MODIFICATION:
            raise Exception("Cannot simplify a modification of the form", self)
        if self.type == BinaryPredicateType.COMPARATION:
            bp = BinaryPredicate()
            bp.type = self.type
            bp.lhs = (self.lhs - self.rhs).simplify()
            bp.rhs = Constant(0)
            bp.operator = self.operator
            return bp
        if self.type == BinaryPredicateType.OPERATION:
            raise NotImplemented("TODO")

    def toExpression(self) -> Expr:
        if self.type != BinaryPredicateType.OPERATION:
            raise Exception("Cannot transform", self, " to expression ", self.type)
        return Utilities.op(self.operator, self.lhs.toExpression(), self.rhs.toExpression())

    def expressify(self, symbols: Dict[Atom, Expr]) -> Expr:
        if self.type == BinaryPredicateType.OPERATION:
            return Utilities.op(self.operator, self.lhs.expressify(symbols), self.rhs.expressify(symbols))
        elif self.type == BinaryPredicateType.COMPARATION:
            if self.operator == "=":
                return self.lhs.expressify(symbols) - self.rhs.expressify(symbols)
            return Utilities.compareExpr(self.operator, self.lhs.expressify(symbols), self.rhs.expressify(symbols))
        else:
            raise Exception("Cannot expressify assignment")

    def getIntervalFromSimpleCondition(self) -> MooreInterval or None:
        if len(self.getFunctions()) > 1:
            return None

        var = self.getFunctions().pop().toExpression()
        func = self.lhs - self.rhs

        # f = mx + q
        f: Expr = func.toExpression()

        m = diff(f, var)  # m = df/dx
        q = f.subs(var, 0)  # q = f | 0

        lb = float(-q / m) if self.operator in {">=", ">", "=", "!="} else float("-inf")
        ub = float(-q / m) if self.operator in {"<=", "<", "=", "!="} else float("+inf")

        return MooreInterval(lb, ub)

    @classmethod
    def fromAssignment(cls, atom: Atom, value: float):
        bp = cls()
        bp.operator = "="
        bp.lhs = Literal.fromAtom(atom, "+")
        bp.rhs = Constant(value)
        bp.type = BinaryPredicateType.MODIFICATION
        return bp

    @classmethod
    def fromOperationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).operation())

    @classmethod
    def fromModificationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).modification())

    @classmethod
    def fromAssignmentString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).assignment())

    @classmethod
    def fromComparationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).comparation())

    @classmethod
    def fromNegatedComparationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).negatedComparation())
