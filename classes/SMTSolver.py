from typing import Dict, Set

from pysmt.logics import QF_LIA, get_logic
from pysmt.shortcuts import Portfolio

from classes.SMTExpression import SMTExpression
from classes.SMTBoolVariable import SMTBoolVariable
from classes.SMTSolution import SMTSolution
from classes.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self):
        self.variables: Set[SMTVariable] = set()
        self.solver = Portfolio(["z3"],
                                logic=QF_LIA,
                                incremental=False,
                                generate_models=True)

    def addAssertion(self, expr: SMTExpression):
        self.solver.add_assertion(expr.expression)
        self.solver.push()
        self.variables.update(expr.variables)

    def addAssertions(self, exprs: [SMTExpression]):
        for expr in exprs:
            self.addAssertion(expr)

    def solve(self) -> SMTSolution:
        self.solver.solve()
        solution = SMTSolution()
        for variable in self.variables:
            solution.addVariable(variable, self.solver.get_value(variable.expression))

        return solution
