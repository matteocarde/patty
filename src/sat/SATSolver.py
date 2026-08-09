from typing import Dict, List, Set, Union

from pysat.examples.rc2 import RC2
from pysat.formula import Formula, WCNF
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

    def __getSolutionMAXSAT(self) -> SMTSolution or bool:
        t = TimeStat.startHolder("Building MaxSAT formula")

        wcnf = WCNF()

        # Original constraints must always be satisfied.
        for clause in self.cnf.clauses:
            wcnf.append(clause)

        # Each phase is a preferred assignment.
        # A positive literal p prefers p=True.
        # A negative literal -p prefers p=False.
        for phase in self.encoding.phases:
            wcnf.append([phase], weight=1)

        t.endHolderMilliseconds()

        t = TimeStat.startHolder("Loading clauses to RC2 MaxSAT solver")

        # RC2 uses an internal SAT solver. "g42" preserves your previous choice.
        with RC2(wcnf, solver="g42") as maxsat:
            t.endHolderMilliseconds()

            t = TimeStat.startHolder("Actual MaxSAT solving time")
            model = maxsat.compute()
            t.endHolderMilliseconds(group="SOLVING")

            if model is None:
                # The hard clauses are unsatisfiable.
                return False

            # Number of preferred phases that could not be respected.
            maxsat_cost = maxsat.cost

            t = TimeStat.startHolder("Retrieving solution")

            solution = SATSolution()

            for literal in model:
                var_id = abs(literal)

                # RC2 may introduce auxiliary relaxation variables.
                # Ignore IDs that do not correspond to your CNFVariable objects.
                var = CNFVariable.ID2VAR.get(var_id)
                if var is not None:
                    solution.addVariable(var, literal > 0)

            t.endHolderMilliseconds(group="POSTPROCESSING")

            return solution

    def __getSolutionSAT(self) -> SMTSolution or bool:
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

    def getSolution(self):
        return self.__getSolutionMAXSAT()

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
