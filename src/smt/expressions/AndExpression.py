from typing import Dict, List

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from pyeda.boolalg.expr import AndOp, Variable, Complement, OrOp
from pysmt.fnode import FNode
from pysmt.shortcuts import And as SMTAnd

from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class AndExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(rhs, FalseExpression) or isinstance(lhs, FalseExpression):
            return FalseExpression()
        if isinstance(lhs, TrueExpression):
            return rhs
        if isinstance(rhs, TrueExpression):
            return lhs
        return cls(lhs, rhs)

    def __andOfSubClauses(self, clauses):
        if len(clauses) == 1:
            return clauses[0]
        elif len(clauses) == 0:
            return 1

        mid = len(clauses) // 2

        # Recursively compute the sum of each half
        left = self.__andOfSubClauses(clauses[:mid])
        right = self.__andOfSubClauses(clauses[mid:])

        # Combine the results
        return left & right

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses: List[BinaryDecisionDiagram] = [e.toBDDExpression(map) for e in self.children]
        return self.__andOfSubClauses(clauses)

    def getExpression(self) -> FNode:
        return SMTAnd([x.getExpression() for x in self.children])

    @classmethod
    def fromBDDExpression(cls, bdd: AndOp, subs: Dict[str, SMTExpression]):
        from src.smt.expressions.OrExpression import OrExpression
        assert isinstance(bdd, AndOp)
        conjunction = []
        for x in bdd.xs:
            if isinstance(x, Variable):
                conjunction.append(subs[x.name])
            if isinstance(x, Complement):
                conjunction.append(~subs[x.top.name])
            if isinstance(x, OrOp):
                conjunction.append(OrExpression.fromBDDExpression(x, subs))
        return SMTExpression.bigand(conjunction)

    def replace(self, sub):
        return SMTExpression.bigand([c.replace(sub) for c in self.children])

    def evaluate(self, solution):
        for c in self.children:
            if not c.evaluate(solution):
                return False
        return True
