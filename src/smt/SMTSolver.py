import datetime
import sys
from typing import Set, List, Dict, Callable

from pysmt.logics import QF_LRA, QF_NRA
from pysmt.shortcuts import Portfolio, Solver
from z3 import Optimize, Bool

from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self, encoding: Encoding = None, trySoftAsHard=False):
        self.variables: Set[SMTVariable] = set()
        self.variablesByName: Dict[str, SMTVariable] = dict()
        self.assertions: List[SMTExpression] = list()
        self.softAssertions: List[SMTExpression] = list()
        self.encoding: Encoding = encoding
        self.onImprovedModel: Callable or None = None
        self.trySoftAsHard = trySoftAsHard
        self.toMinimize: List[SMTExpression] = []

        self.maximize = self.encoding and (bool(self.encoding.softRules) or bool(self.encoding.minimize))
        if self.maximize:
            self.solver: Optimize = Optimize()

            self.z3: Solver = Solver("z3",
                                     logic=QF_LRA,
                                     incremental=True,
                                     generate_models=True)
        else:
            self.solver: Portfolio = Portfolio(["z3"],
                                               logic=QF_LRA,
                                               incremental=True,
                                               generate_models=True)

        if self.encoding:
            self.addAssertions(self.encoding.rules)
            self.addSoftAssertions(self.encoding.softRules)
            self.setMinimize(self.encoding.minimize)

        # signal.signal(signal.SIGTERM, self.z3.exit)
        # signal.signal(signal.SIGINT, self.z3.exit)

    def addAssertion(self, expr: SMTExpression, push=True):
        self.assertions.append(expr)
        self.variables |= expr.getVariables()
        z3Expr = self.z3.converter.convert(expr.getExpression()) if self.maximize else expr.getExpression()

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

        self.variables.update(expr.getVariables())
        z3Expr = self.z3.converter.convert(expr.getExpression())
        self.softAssertions.append(z3Expr)
        if not self.trySoftAsHard:
            self.solver.add_soft(z3Expr)

        if push:
            self.solver.push()

    def setMinimize(self, expr: [SMTExpression]):
        if not expr:
            return

        for e in expr:
            z3Expr = self.z3.converter.convert(e.getExpression())
            self.toMinimize.append(z3Expr)
            if not self.trySoftAsHard:
                self.solver.minimize(z3Expr)

    def addSoftAssertions(self, exprs: [SMTExpression], push=True):

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

    def getSolutionFromModel(self, model) -> SMTSolution:
        solution = SMTSolution()
        variablesByName = dict()
        for v in self.variables:
            variablesByName[str(v).replace("'", "")] = v
        for v in model:
            varName = str(v)
            if varName not in variablesByName:
                continue
            solution.addVariable(variablesByName[varName], model[v])
        return solution

    def tryWithSoftAsHard(self):
        self.solver.push()
        for i, expr in enumerate(self.softAssertions):
            self.solver.add(expr)
        print(f"Starting checking without contraints [{datetime.datetime.now()}]")
        res = self.solver.check()
        print(f"Ended checking without contraints [{datetime.datetime.now()}]")
        if str(res) == "sat":
            return "sat"

        self.solver.pop()
        # for i, expr in enumerate(self.softAssertions):
        #     self.solver.add_soft(expr)
        #     # if Bool(f"r{i}") in core:
        #     #     self.solver.add_soft(expr)
        #     # else:
        #     #     self.solver.add(expr)
        for expr in self.toMinimize:
            self.solver.minimize(expr)
        self.solver.push()

        return self.solver.check()

    def getSolution(self) -> SMTSolution or bool:
        if self.maximize:

            if not self.trySoftAsHard:
                res = self.solver.check()
            else:
                res = self.tryWithSoftAsHard()

            if str(res) != "sat":
                return False
        else:
            found = self.solver.solve()
            if not found:
                return False

        solution = SMTSolution()
        if self.maximize:
            model = self.solver.model()
            solution = self.getSolutionFromModel(model)
        else:
            for variable in self.variables:
                value = self.solver.get_value(variable.getSymbol())
                solution.addVariable(variable, value)

        return solution

    def registerOnImprovedModel(self, onImprovedModel: Callable):
        self.onImprovedModel = onImprovedModel

    def __wrappedOnImprovedModel(self, model):
        try:
            solution = self.getSolutionFromModel(model)
            self.onImprovedModel(solution)
        except:
            print("ERROR ON IMPROVED MODEL")

    def solve(self, relaxed=False) -> Plan or bool:

        if self.onImprovedModel:
            self.solver.set_on_model(self.__wrappedOnImprovedModel)

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.encoding.getPlanFromSolution(solution, relaxed=relaxed)
        # plan.quality = plan.getMetric(self.encoding.problem)

        return plan
