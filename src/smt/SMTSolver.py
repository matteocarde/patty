from pysmt.logics import QF_LRA
from pysmt.shortcuts import Portfolio
from typing import Set, List

from src.pddl.NumericPlan import NumericPlan
from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self, pddl2smt: PDDL2SMT = None):
        self.variables: Set[SMTVariable] = set()
        self.assertions: List[SMTExpression] = list()
        self.pddl2smt: PDDL2SMT = pddl2smt

        self.solver: Portfolio = Portfolio(["yices"],
                                           logic=QF_LRA,
                                           incremental=True,
                                           generate_models=True)

        if self.pddl2smt:
            self.addAssertions(self.pddl2smt.rules)

    def addAssertion(self, expr: SMTExpression, push=True):
        self.assertions.append(expr)
        self.variables.update(expr.variables)
        self.solver.add_assertion(expr.expression)

        if push:
            self.solver.push()

    def addAssertions(self, exprs: [SMTExpression], push=True):
        for expr in exprs:
            self.addAssertion(expr, push=False)

        if push:
            self.solver.push()

    def popLastAssertion(self):
        self.assertions.pop()
        self.solver.pop()
        self.solver.push()  # I repush to keep the stack with the last actions

    def exit(self):
        self.solver.exit()
        pass

    def getSolution(self) -> SMTSolution or bool:
        found = self.solver.solve()
        if not found:
            return False

        solution = SMTSolution()
        for variable in self.variables:
            value = self.solver.get_value(variable.expression)
            solution.addVariable(variable, value)

        return solution

    def solve(self) -> NumericPlan or bool:

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.pddl2smt.getPlanFromSolution(solution)
        plan.quality = plan.getMetric(self.pddl2smt.problem)

        return plan

    # Linear Optimization
    def optimize(self) -> NumericPlan or bool:

        lastPlanFound: NumericPlan = self.solve()
        if not lastPlanFound:
            return False

        while True:
            assert lastPlanFound.validate(self.pddl2smt.problem)
            # print(f"Found plan with quality {lastPlanFound.quality}. Improving...")
            self.addAssertion(self.pddl2smt.getMetricExpression(lastPlanFound.quality))

            plan = self.solve()
            if not plan:
                lastPlanFound.optimal = True
                return lastPlanFound

            lastPlanFound = plan
            self.popLastAssertion()

    def __solveBelowQuality(self, quality: float):
        # print("Searching below", quality)
        self.addAssertion(self.pddl2smt.getMetricExpression(quality), push=False)
        plan = self.solve()
        self.popLastAssertion()
        return plan

    def __searchBetween(self, ub: float, lb: float, error: float, lastPlan: NumericPlan,
                        onSolutionFound=None) -> NumericPlan:
        if abs(ub - lb) < error:
            lastPlan.optimal = True
            return lastPlan

        half = lb + (ub - lb) / 2
        # print(f"Searching plan with quality {half}.")
        plan = self.__solveBelowQuality(half)
        if plan:
            # print(f"Plan FOUND with quality {plan.quality}.")
            if onSolutionFound:
                onSolutionFound(plan)
            return self.__searchBetween(plan.quality, lb, error, plan, onSolutionFound)
        if not plan:
            # print(f"Plan NOT FOUND with quality {half}.")
            return self.__searchBetween(ub, half, error, lastPlan, onSolutionFound)

    def optimizeBinary(self, error=1, onSolutionFound=None) -> NumericPlan or bool:

        lastPlanFound: NumericPlan = self.solve()
        if not lastPlanFound:
            return False
        if onSolutionFound:
            onSolutionFound(lastPlanFound)

        return self.__searchBetween(lastPlanFound.quality, 0, error, lastPlanFound, onSolutionFound)
