from pysmt.oracles import get_logic
from typing import Set

from pysmt.logics import QF_LIA, QF_LRA
from pysmt.shortcuts import Portfolio

from classes.smt.SMTExpression import SMTExpression
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self):
        self.variables: Set[SMTVariable] = set()
        self.solver = Portfolio(["z3"],
                                logic=QF_LRA,
                                incremental=True,
                                generate_models=True)

    def addAssertion(self, expr: SMTExpression):
        self.solver.add_assertion(expr.expression)
        self.solver.push()
        self.variables.update(expr.variables)

    def addAssertions(self, exprs: [SMTExpression]):
        for expr in exprs:
            # print(expr, get_logic(expr.expression))
            self.addAssertion(expr)

    def solve(self) -> SMTSolution:
        self.solver.solve()
        solution = SMTSolution()
        for variable in self.variables:
            solution.addVariable(variable, self.solver.get_value(variable.expression))

        return solution
