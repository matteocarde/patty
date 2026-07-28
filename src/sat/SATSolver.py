from typing import Dict, List, Set

from pysat.formula import Formula
from pysat.solvers import Solver

from src.pddl.Plan import Plan
from src.plan.ClassicEncoding import ClassicEncoding
from src.sat.CNFVariable import CNFVariable
from src.sat.SATSolution import SATSolution
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.utils.TimeStat import TimeStat


class SATSolver:
    encoding: ClassicEncoding
    variables: Set[SMTVariable]
    memodict: Dict
    assertions: List[Formula]
    phases: List[SMTVariable]

    def __init__(self, encoding: ClassicEncoding):
        self.memodict = dict()
        self.encoding = encoding
        self.cnf = self.encoding.cnf

    def getSolution(self) -> SMTSolution or bool:
        t = TimeStat.startHolder("Loading clauses to PYSAT solver")
        with Solver(name="g42", bootstrap_with=self.cnf.clauses) as s:
            if self.encoding.phases:
                s.set_phases(self.encoding.phases)
            t.endHolderMilliseconds()
            t = TimeStat.startHolder("Actual SAT Solving time")
            res = s.solve()
            t.endHolderMilliseconds(group="SOlVING")

            t = TimeStat.startHolder("Retrieving solution")
            if not res:
                return False
            model = s.get_model()
            solution = SATSolution()
            assignment = dict([(abs(lit), lit > 0) for lit in model])
            for varId, value in assignment.items():
                var = CNFVariable.ID2VAR[varId]
                solution.addVariable(var, value)
            t.endHolderMilliseconds(group="POSTPROCESSING")
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
        CNFVariable.reset()
