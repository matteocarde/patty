from typing import Dict, List, Set

from pysat.formula import And, Formula, Atom, PYSAT_TRUE, PYSAT_FALSE, IDPool
from pysat.solvers import Solver

from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.utils.TimeStat import TimeStat


class SATSolver:
    encoding: Encoding
    variables: Set[SMTVariable]
    memodict: Dict
    assertions: List[Formula]

    def __init__(self, encoding: Encoding):
        self.memodict = dict()
        self.encoding = encoding
        self.assertions = list()
        self.variables = set()
        self.addAssertions(self.encoding.rules)

        self.cnf = []
        t = TimeStat.startHolder("Converting formula into CNF")
        for assertion in self.assertions:
            if assertion == PYSAT_TRUE:
                pass
            elif assertion == PYSAT_FALSE:
                self.cnf.append([])
            else:
                assertion.clausify()
                self.cnf += assertion.clauses
        t.endHolderMilliseconds(group="PREPROCESSING")
        pass

    def addAssertion(self, expr: SMTExpression):
        satExpr = expr.getPropositionalFormula(memodict=self.memodict)
        self.assertions.append(satExpr)
        self.variables.update(expr.variables)

    def addAssertions(self, exprs: [SMTExpression]):
        for i, expr in enumerate(exprs):
            self.addAssertion(expr)

    def getSolution(self) -> SMTSolution or bool:
        with Solver(name='cadical195', bootstrap_with=self.cnf) as s:
            if not s.solve():
                return False
            model = s.get_model()
            solution = SMTSolution()
            vpool: IDPool = Formula.export_vpool()
            for v in self.variables:
                r = vpool.obj2id[v.atom]
                solution.addVariable(v, model[r] > 0)
            return solution

    def solve(self) -> Plan or bool:

        solution = self.getSolution()
        if not solution:
            return False
        plan = self.encoding.getPlanFromSolution(solution)
        # plan.quality = plan.getMetric(self.encoding.problem)
        if not plan:
            raise Exception("Solution was found but conversion to plan failed")

        return plan
