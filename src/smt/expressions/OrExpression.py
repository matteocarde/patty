from typing import Dict, List

from pysmt.fnode import FNode
from pysmt.shortcuts import Or as SMTOr

from libs.pyeda.pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram
from libs.pyeda.pyeda.boolalg.expr import OrOp, Variable, Complement, AndOp
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression, BOOLEAN
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.NaryExpression import NaryExpression
from src.smt.expressions.TrueExpression import TrueExpression


class OrExpression(NaryExpression):

    def __init__(self, *xs: SMTExpression):
        super().__init__(*xs)
        self.type = BOOLEAN

    @classmethod
    def simplify(cls, lhs, rhs):
        if isinstance(rhs, TrueExpression) or isinstance(lhs, TrueExpression):
            return TrueExpression()
        if isinstance(lhs, FalseExpression):
            return rhs
        if isinstance(rhs, FalseExpression):
            return lhs
        return cls(lhs, rhs)

    def __orOfSubClauses(self, clauses):
        if len(clauses) == 1:
            return clauses[0]
        elif len(clauses) == 0:
            return 1

        mid = len(clauses) // 2

        # Recursively compute the sum of each half
        left = self.__orOfSubClauses(clauses[:mid])
        right = self.__orOfSubClauses(clauses[mid:])

        # Combine the results
        return left | right

    def toBDDExpression(self, map: Dict[SMTBoolVariable, BDDVariable]):
        clauses: List[BinaryDecisionDiagram] = [e.toBDDExpression(map) for e in self.children]
        return self.__orOfSubClauses(clauses)

    def getExpression(self) -> FNode:
        return SMTOr([x.getExpression() for x in self.children])

    @classmethod
    def fromBDDExpression(cls, bdd: OrOp, subs: Dict[str, SMTExpression]):
        from src.smt.expressions.AndExpression import AndExpression
        assert isinstance(bdd, OrOp)
        conjunction = []
        for x in bdd.xs:
            if isinstance(x, Variable):
                conjunction.append(subs[x.name])
            if isinstance(x, Complement):
                conjunction.append(~subs[x.top.name])
            if isinstance(x, AndOp):
                conjunction.append(AndExpression.fromBDDExpression(x, subs))
        return SMTExpression.bigor(conjunction)

    def replace(self, sub):
        return SMTExpression.bigor([c.replace(sub) for c in self.children])

    def evaluate(self, solution):
        for c in self.children:
            if c.evaluate(solution):
                return True
        return False
