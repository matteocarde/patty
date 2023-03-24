from pysmt.oracles import get_logic
from typing import Set, List

import yicespy

from pysmt.logics import QF_LIA, QF_LRA
from pysmt.shortcuts import Portfolio, And, to_smtlib

from classes.smt.SMTExpression import SMTExpression
from classes.smt.SMTSolution import SMTSolution
from classes.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self):
        self.variables: Set[SMTVariable] = set()
        self.assertions: List[SMTExpression] = list()

    def addAssertion(self, expr: SMTExpression):
        # self.solver.add_assertion(expr.expression)
        # self.solver.push()
        self.assertions.append(expr)
        self.variables.update(expr.variables)

    def addAssertions(self, exprs: [SMTExpression]):
        for expr in exprs:
            # print(expr, get_logic(expr.expression))
            self.addAssertion(expr)

    def solve(self) -> SMTSolution:

        with Portfolio(["yices"],
                       logic=QF_LRA,
                       incremental=False,
                       generate_models=True) as solver:
            totalAssertion = And([f.expression for f in self.assertions])
            simplifiedAssertion = totalAssertion.simplify()

            solver.add_assertion(simplifiedAssertion)
            solver.push()

            result = solver.solve()
            solution = SMTSolution()
            for variable in self.variables:
                value = solver.get_value(variable.expression)
                solution.addVariable(variable, value)

            return solution
