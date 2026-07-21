import datetime
import traceback
from typing import Set, List, Dict, Callable

from pysmt.shortcuts import Portfolio

from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.utils.LogPrint import console, LogPrintLevel
from src.utils.TimeStat import TimeStat
from src.z3.Z3SolverAndOptimizer import Z3SolverAndOptimizer


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

        self.solver = Z3SolverAndOptimizer()
        # self.maximize = self.encoding and (bool(self.encoding.softRules) or bool(self.encoding.minimize))

        if self.encoding:
            memodict = dict()
            if self.encoding.softRules or self.encoding.minimize:
                self.addAssertions(self.encoding.rules, solver=False, optimizer=True, memodict=memodict)
            # with open("./memodict.txt", "w") as f:
            #     for k in memodict.keys():
            #         f.write(str(k) + "\n")
            # self.addAssertions(self.encoding.rules, solver=True, optimizer=False, memodict=memodict)
            console.log(f"memodict size: {len(memodict)}", LogPrintLevel.STATS)
            self.addSoftAssertions(self.encoding.softRules)
            self.setMinimize(self.encoding.minimize)
            pass

        # signal.signal(signal.SIGTERM, self.z3.exit)
        # signal.signal(signal.SIGINT, self.z3.exit)

    def addAssertion(self, expr: SMTExpression, push=True, solver=True, optimizer=True, memodict=dict()):
        self.assertions.append(expr)
        self.variables |= expr.getVariables()
        expr = expr.getExpression(memodict=memodict)
        self.solver.add(expr, solver=solver, optimizer=optimizer)

        if push:
            self.solver.push()

    def addAssertions(self, exprs: [SMTExpression], push=True, solver=True, optimizer=True, memodict=dict()):
        for i, expr in enumerate(exprs):
            self.addAssertion(expr, push=False, solver=solver, optimizer=optimizer, memodict=memodict)

        if push:
            self.solver.push()

    def addSoftAssertion(self, expr: SMTExpression, push=True):

        self.variables.update(expr.getVariables())
        self.solver.add_soft(expr.getExpression())

        if push:
            self.solver.push()

    def setMinimize(self, expr: [SMTExpression]):

        if not expr:
            return

        console.log(f"Adding minimize", LogPrintLevel.STATS)

        for e in expr:
            self.solver.minimize(e.getExpression())

    def addSoftAssertions(self, exprs: [SMTExpression], push=True):
        if not exprs:
            return

        console.log(f"Adding {len(exprs)} soft-assert", LogPrintLevel.STATS)
        for expr in exprs:
            self.addSoftAssertion(expr, push=False)

        if push and self.trySoftAsHard:
            self.solver.push()

    def popLastAssertion(self):
        self.assertions.pop()
        self.solver.pop()
        self.solver.push()  # I repush to keep the stack with the last actions

    def exit(self):
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
        console.log(f"Starting checking without constraints [{datetime.datetime.now()}]", LogPrintLevel.TIMES)
        solveRes = self.solver.solve(self.variables)
        console.log(f"Ended checking without constraints [{datetime.datetime.now()}]", LogPrintLevel.TIMES)
        if solveRes:
            return solveRes

        return self.solver.optimize(self.variables)

    def getSolution(self) -> SMTSolution or bool:
        if self.onImprovedModel:
            self.solver.setOnModel(self.__wrappedOnImprovedModel)
        if not self.trySoftAsHard:
            if self.encoding.minimize or self.encoding.softRules:
                return self.solver.optimize(self.variables)
            else:
                return self.solver.solve(self.variables)
        else:
            return self.tryWithSoftAsHard()

    def registerOnImprovedModel(self, onImprovedModel: Callable):
        self.onImprovedModel = onImprovedModel

    def __wrappedOnImprovedModel(self, model):
        try:
            solution = self.getSolutionFromModel(model)
            self.onImprovedModel(solution)
        except:
            print("ERROR ON IMPROVED MODEL")
            print(traceback.format_exc())

    def solve(self, relaxed=False) -> Plan or bool:

        if self.onImprovedModel:
            self.solver.setOnModel(self.__wrappedOnImprovedModel)

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.encoding.getPlanFromSolution(solution, relaxed=relaxed)
        # plan.quality = plan.getMetric(self.encoding.problem)
        # if not plan:
        #     raise Exception("Solution was found but conversion to plan failed")

        return plan
