from typing import Dict, Tuple

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from pysmt.fnode import FNode
from pysmt.shortcuts import Iff as SMTIff
from pysat.formula import Formula, Equals as SATEquals

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.BinaryExpression import BinaryExpression
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NotExpression import NotExpression
from src.smt.expressions.TrueExpression import TrueExpression

IFF_CACHE: Dict[Tuple[SMTExpression, SMTExpression], SMTExpression] = dict()


class IffExpression(BinaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(rhs, FalseExpression) and isinstance(lhs, FalseExpression):
            return TrueExpression()
        if isinstance(rhs, TrueExpression) and isinstance(lhs, TrueExpression):
            return TrueExpression()
        if isinstance(lhs, FalseExpression):
            return NotExpression.simplify(rhs)
        if isinstance(rhs, FalseExpression):
            return NotExpression.simplify(lhs)
        if isinstance(lhs, TrueExpression):
            return rhs
        if isinstance(rhs, TrueExpression):
            return lhs
        if (lhs, rhs) in IFF_CACHE:
            return IFF_CACHE[lhs, rhs]
        IFF_CACHE[lhs, rhs] = cls(lhs, rhs)
        return IFF_CACHE[lhs, rhs]

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        lhs: BinaryDecisionDiagram = self.lhs.toBDDExpression(map)
        rhs: BinaryDecisionDiagram = self.rhs.toBDDExpression(map)
        return lhs.iff(rhs)

    def getExpression(self, memodict=dict()) -> FNode:
        if self in memodict:
            return memodict[self]
        expr = SMTIff(self.lhs.getExpression(memodict=memodict), self.rhs.getExpression(memodict=memodict))
        memodict[self] = expr
        return expr

    def getPropositionalFormula(self, memodict=dict()) -> Formula:
        if self in memodict:
            return memodict[self]
        lhs = self.lhs.getPropositionalFormula(memodict)
        rhs = self.rhs.getPropositionalFormula(memodict)
        expr = SATEquals(lhs, rhs)
        memodict[self] = expr
        return expr

    def evaluate(self, solution):
        return self.lhs.evaluate(solution) == self.rhs.evaluate(solution)
