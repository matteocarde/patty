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
        pass

    def addAssertion(self, expr: SMTExpression):
        satExpr = expr.getPropositionalFormula(memodict=self.memodict)
        self.assertions.append(satExpr)
        self.variables.update(expr.variables)

    def addAssertions(self, exprs: [SMTExpression]):
        for i, expr in enumerate(exprs):
            self.addAssertion(expr)

    @staticmethod
    def satisfies_cnf(cnf, model) -> bool:
        model_set = set(model)

        return all(
            any(literal in model_set for literal in clause)
            for clause in cnf
        )

    def getSolution(self) -> SMTSolution or bool:
        formula = And(*self.assertions, merge=True)
        with Solver(name='glucose4', bootstrap_with=formula) as s:
            if not s.solve():
                return False
            model = s.get_model()
            solution = SMTSolution()
            vpool: IDPool = Formula.export_vpool()
            assignment = dict([(abs(lit), lit > 0) for lit in model])
            for v in self.variables:
                r = vpool.obj2id[v.atom]
                solution.addVariable(v, assignment[r])
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

    def exit(self):
        Formula.cleanup()
