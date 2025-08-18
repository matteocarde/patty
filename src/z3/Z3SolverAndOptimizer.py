from pysmt.logics import QF_LRA
from pysmt.shortcuts import Portfolio, Solver
from z3 import Optimize, Bool

from src.smt.SMTSolution import SMTSolution


class Z3SolverAndOptimizer:
    optimizer: Optimize
    solver: Solver

    def __init__(self):
        self.optimizer: Optimize = Optimize()
        self.optimizer.set("opt.priority", "lex")

        self.solver: Solver = Solver("z3",
                                     logic=QF_LRA,
                                     incremental=True,
                                     generate_models=True)

    def push(self):
        self.optimizer.push()
        self.solver.push()

    def pop(self):
        self.optimizer.pop()
        self.solver.pop()

    def exit(self):
        self.solver.exit()

    def convert(self, expr):
        return self.solver.converter.convert(expr)

    def add(self, expr):
        self.optimizer.add(self.convert(expr))
        self.solver.add_assertion(expr)

    def add_soft(self, expr):
        self.solver.add_assertion(expr)
        self.optimizer.add_soft(self.convert(expr))

    def minimize(self, expr):
        self.optimizer.minimize(self.convert(expr))

    def getSolutionFromOptimizer(self, variables) -> SMTSolution:
        model = self.optimizer.model()
        solution = SMTSolution()
        variablesByName = dict()
        for v in variables:
            variablesByName[str(v).replace("'", "")] = v
        for v in model:
            varName = str(v)
            if varName not in variablesByName:
                continue
            solution.addVariable(variablesByName[varName], model[v])
        return solution

    def getSolutionFromSolver(self, variables) -> SMTSolution:
        solution = SMTSolution()
        for variable in variables:
            value = self.solver.get_value(variable.getSymbol())
            solution.addVariable(variable, value)
        return solution

    def optimize(self, variables):
        res = self.optimizer.check()

        if str(res) != "sat":
            return False

        return self.getSolutionFromOptimizer(variables)

    def solve(self, variables):
        found = self.solver.solve()
        if not found:
            return False

        return self.getSolutionFromSolver(variables)

    def setOnModel(self, onModel):
        self.optimizer.set_on_model(onModel)
