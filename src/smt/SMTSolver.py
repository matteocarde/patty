from typing import Set, List, Dict

from pysmt.logics import QF_LRA, QF_NRA
from pysmt.shortcuts import Portfolio, Solver
from z3 import Optimize

from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class SMTSolver:
    solver: Portfolio
    variables: Set[SMTVariable]

    def __init__(self, encoding: Encoding = None):
        self.variables: Set[SMTVariable] = set()
        self.variablesByName: Dict[str, SMTVariable] = dict()
        self.assertions: List[SMTExpression] = list()
        self.softAssertions: List[SMTExpression] = list()
        self.encoding: Encoding = encoding

        self.maximize = self.encoding and (bool(self.encoding.softRules) or bool(self.encoding.minimize))
        if self.maximize:
            self.solver = Optimize()
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

        self.softAssertions.append(expr)
        self.variables.update(expr.variables)
        z3Expr = self.z3.converter.convert(expr.expression)
        self.solver.add_soft(z3Expr)

        if push:
            self.solver.push()

    def setMinimize(self, expr: SMTExpression):
        if not expr:
            return

        z3Expr = self.z3.converter.convert(expr.expression)
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
