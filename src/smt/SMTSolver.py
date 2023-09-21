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

        if self.pddl2smt:
            self.addAssertions(self.pddl2smt.rules)
            self.addSoftAssertions(self.pddl2smt.softRules)

    def addAssertion(self, expr: SMTExpression, push=True):
        self.assertions.append(expr)
        self.variables.update(expr.variables)
        for v in expr.variables:
            self.variablesByName[str(v).replace("'", "")] = v

    def addAssertions(self, exprs: [SMTExpression], push=True):
        for expr in exprs:
            self.addAssertion(expr, push=False)

    def addSoftAssertion(self, expr: SMTExpression, push=True):

        if not self.maximize:
            return

        self.softAssertions.append(expr)
        self.variables.update(expr.variables)
        for v in expr.variables:
            self.variablesByName[str(v)] = v

    def addSoftAssertions(self, exprs: [SMTExpression], push=True):
        if not self.maximize:
            return

        for expr in exprs:
            self.addSoftAssertion(expr, push=False)

    def popLastAssertion(self):
        self.assertions.pop()
        self.solver.pop()
        self.solver.push()  # I repush to keep the stack with the last actions

    def exit(self):
        # self.z3.exit()
        # self.portfolio.exit()
        pass

    def getSolutionViaPortfolio(self) -> SMTSolution or bool:
        solution = SMTSolution()

        with Portfolio(["z3"],
                       logic=QF_LRA,
                       incremental=False,
                       generate_models=True) as solver:

            for ass in self.assertions:
                solver.add_assertion(ass.expression)
            found = solver.solve()
            if not found:
                return False

            for variable in self.variables:
                value = solver.get_value(variable.expression)
                solution.addVariable(variable, value)

            solver.exit()

            return solution

    def getSolutionViaOptimize(self) -> SMTSolution or bool:

        solution = SMTSolution()
        convertedHard = []
        convertedSoft = []

        with Solver("z3", logic=QF_LRA, incremental=True, generate_models=True) as z3:
            for ass in self.assertions:
                z3Expr = z3.converter.convert(ass.expression)
                convertedHard.append(z3Expr)
            for ass in self.softAssertions:
                z3Expr = z3.converter.convert(ass.expression)
                convertedSoft.append(z3Expr)

        solver = Optimize()

        for ass in convertedHard:
            solver.add(ass)

        for ass in convertedSoft:
            solver.add_soft(ass)

        res = solver.check()

        if str(res) != "sat":
            return False

        model = solver.model()
        for v in model:
            varName = str(v)
            if varName not in self.variablesByName:
                continue
            solution.addVariable(self.variablesByName[varName], model[v])

        return solution

    def getSolution(self) -> SMTSolution or bool:
        return self.getSolutionViaOptimize() if self.maximize else self.getSolutionViaPortfolio()

    def solve(self) -> NumericPlan or bool:

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.pddl2smt.getPlanFromSolution(solution)
        plan.quality = plan.getMetric(self.pddl2smt.problem)

        return plan
    #
    # # Linear Optimization
    # def optimize(self) -> NumericPlan or bool:
    #
    #     lastPlanFound: NumericPlan = self.solve()
    #     if not lastPlanFound:
    #         return False
    #
    #     while True:
    #         assert lastPlanFound.validate(self.pddl2smt.problem)
    #         print(f"Found plan with quality {lastPlanFound.quality}. Improving...")
    #         self.addAssertion(self.pddl2smt.getMetricExpression(lastPlanFound.quality))
    #
    #         plan = self.solve()
    #         if not plan or plan.quality == lastPlanFound.quality:
    #             lastPlanFound.optimal = True
    #             return lastPlanFound
    #
    #         lastPlanFound = plan
    #         self.popLastAssertion()
    #
    # def __solveBelowQuality(self, quality: float):
    #     # print("Searching below", quality)
    #     self.addAssertion(self.pddl2smt.getMetricExpression(quality), push=False)
    #     plan = self.solve()
    #     self.popLastAssertion()
    #     return plan
    #
    # def __searchBetween(self, ub: float, lb: float, error: float, lastPlan: NumericPlan,
    #                     onSolutionFound=None) -> NumericPlan:
    #     if abs(ub - lb) < error:
    #         lastPlan.optimal = True
    #         return lastPlan
    #
    #     half = lb + (ub - lb) / 2
    #     print(f"Searching plan with quality {half}.")
    #     plan = self.__solveBelowQuality(half)
    #     if plan and plan.quality != lastPlan.quality:
    #         print(f"Plan FOUND with quality {plan.quality}.")
    #         if onSolutionFound:
    #             onSolutionFound(plan)
    #         return self.__searchBetween(plan.quality, lb, error, plan, onSolutionFound)
    #     if not plan or plan.quality == lastPlan.quality:
    #         print(f"Plan NOT FOUND with quality {half}.")
    #         return self.__searchBetween(ub, half, error, lastPlan, onSolutionFound)
    #
    # def optimizeBinary(self, error=1, onSolutionFound=None) -> NumericPlan or bool:
    #
    #     lastPlanFound: NumericPlan = self.solve()
    #     if not lastPlanFound:
    #         return False
    #     if onSolutionFound:
    #         onSolutionFound(lastPlanFound)
    #
    #     return self.__searchBetween(lastPlanFound.quality, 0, error, lastPlanFound, onSolutionFound)
