from pysmt.logics import QF_LRA, QF_NRA
from pysmt.shortcuts import Portfolio, write_smtlib, Solver
from typing import Set, List, Dict

from z3 import Optimize

from src.pddl.NumericPlan import NumericPlan
from src.plan.PDDL2SMT import PDDL2SMT
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self, pddl2smt: PDDL2SMT = None, maximize=False):
        self.variables: Set[SMTVariable] = set()
        self.variablesByName: Dict[str, SMTVariable] = dict()
        self.assertions: List[SMTExpression] = list()
        self.softAssertions: List[SMTExpression] = list()
        self.pddl2smt: PDDL2SMT = pddl2smt
        self.maximize = maximize

        self.z3: Solver = Solver("z3",
                                 logic=QF_LRA,
                                 incremental=True,
                                 generate_models=True)
        self.portfolio: Portfolio = Portfolio(["z3"],
                                              logic=QF_LRA,
                                              incremental=True,
                                              generate_models=True)
        self.solver = Optimize() if self.maximize else self.portfolio

        if self.pddl2smt:
            self.addAssertions(self.pddl2smt.rules)
            self.addSoftAssertions(self.pddl2smt.softRules)

    def addAssertion(self, expr: SMTExpression, push=True):
        self.assertions.append(expr)
        self.variables.update(expr.variables)
        for v in expr.variables:
            self.variablesByName[str(v).replace("'", "")] = v

        z3Expr = self.z3.converter.convert(expr.expression) if self.maximize else expr.expression

        if self.maximize:
            self.solver.add(z3Expr)
        else:
            self.solver.add_assertion(z3Expr)

        if push:
            self.solver.push()

    def addAssertions(self, exprs: [SMTExpression], push=True):
        for expr in exprs:
            self.addAssertion(expr, push=False)

        if push:
            self.solver.push()

    def addSoftAssertion(self, expr: SMTExpression, push=True):

        if not self.maximize:
            return

        self.softAssertions.append(expr)
        self.variables.update(expr.variables)
        for v in expr.variables:
            self.variablesByName[str(v)] = v
        z3Expr = self.z3.converter.convert(expr.expression)
        self.solver.add_soft(z3Expr)

        if push:
            self.solver.push()

    def addSoftAssertions(self, exprs: [SMTExpression], push=True):
        if not self.maximize:
            return

        for expr in exprs:
            self.addSoftAssertion(expr, push=False)

        if push:
            self.solver.push()

    def popLastAssertion(self):
        self.assertions.pop()
        self.solver.pop()
        self.solver.push()  # I repush to keep the stack with the last actions

    def exit(self):
        self.z3.exit()
        self.portfolio.exit()
        pass

    def getSolution(self) -> SMTSolution or bool:

        if self.maximize:
            res = self.solver.check()

            if str(res) != "sat":
                return False
        else:
            found = self.solver.solve()
            if not found:
                return False

        solution = SMTSolution()
        if self.maximize:
            model = self.solver.model()
            for v in model:
                varName = str(v)
                if varName not in self.variablesByName:
                    continue
                solution.addVariable(self.variablesByName[varName], model[v])
        else:
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
            print(f"Found plan with quality {lastPlanFound.quality}. Improving...")
            self.addAssertion(self.pddl2smt.getMetricExpression(lastPlanFound.quality))

            plan = self.solve()
            if not plan or plan.quality == lastPlanFound.quality:
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
        print(f"Searching plan with quality {half}.")
        plan = self.__solveBelowQuality(half)
        if plan and plan.quality != lastPlan.quality:
            print(f"Plan FOUND with quality {plan.quality}.")
            if onSolutionFound:
                onSolutionFound(plan)
            return self.__searchBetween(plan.quality, lb, error, plan, onSolutionFound)
        if not plan or plan.quality == lastPlan.quality:
            print(f"Plan NOT FOUND with quality {half}.")
            return self.__searchBetween(ub, half, error, lastPlan, onSolutionFound)

    def optimizeBinary(self, error=1, onSolutionFound=None) -> NumericPlan or bool:

        lastPlanFound: NumericPlan = self.solve()
        if not lastPlanFound:
            return False
        if onSolutionFound:
            onSolutionFound(lastPlanFound)

        return self.__searchBetween(lastPlanFound.quality, 0, error, lastPlanFound, onSolutionFound)
