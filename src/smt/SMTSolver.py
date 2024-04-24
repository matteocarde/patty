from pysmt.logics import QF_LRA, QF_NRA
from pysmt.shortcuts import Portfolio, write_smtlib, Solver
from typing import Set, List, Dict

from z3 import Optimize, z3

from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.plan.NumericEncoding import NumericEncoding
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self, encoding: Encoding = None, maximize=False):
        self.variables: Set[SMTVariable] = set()
        self.variablesByName: Dict[str, SMTVariable] = dict()
        self.assertions: List[SMTExpression] = list()
        self.softAssertions: List[SMTExpression] = list()
        self.encoding: Encoding = encoding
        self.maximize = True

        if self.maximize:
            self.solver = Optimize()
            self.z3: Solver = Solver("z3",
                                     logic=QF_LRA,
                                     incremental=True,
                                     generate_models=True)
        else:
            self.solver: Portfolio = Portfolio(["z3"],
                                               logic=QF_NRA,
                                               incremental=True,
                                               generate_models=True)

        if self.encoding:
            self.addAssertions(self.encoding.rules)
            self.addSoftAssertions(self.encoding.softRules)

    def addAssertion(self, expr: SMTExpression, push=True):
        self.assertions.append(expr)
        self.variables.update(expr.variables)

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
        if self.maximize:
            self.z3.exit()
        else:
            self.solver.exit()
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
            variablesByName = dict()
            for v in self.variables:
                variablesByName[str(v).replace("'", "")] = v
            for v in model:
                varName = str(v)
                if varName not in variablesByName:
                    continue
                solution.addVariable(variablesByName[varName], model[v])
        else:
            for variable in self.variables:
                value = self.solver.get_value(variable.expression)
                solution.addVariable(variable, value)

        return solution

    def solve(self) -> Plan or bool:

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.encoding.getPlanFromSolution(solution)
        # plan.quality = plan.getMetric(self.encoding.problem)

        return plan

    # Linear Optimization
    def optimize(self) -> NumericPlan or bool:

        lastPlanFound: NumericPlan = self.solve()
        if not lastPlanFound:
            return False

        while True:
            assert lastPlanFound.validate(self.encoding.problem)
            print(f"Found plan with quality {lastPlanFound.quality}. Improving...")
            self.addAssertion(self.encoding.getMetricExpression(lastPlanFound.quality))

            plan = self.solve()
            if not plan or plan.quality == lastPlanFound.quality:
                lastPlanFound.optimal = True
                return lastPlanFound

            lastPlanFound = plan
            self.popLastAssertion()

    def __solveBelowQuality(self, quality: float):
        # print("Searching below", quality)
        self.addAssertion(self.encoding.getMetricExpression(quality), push=False)
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
