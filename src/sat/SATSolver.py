from typing import Dict, List, Set

from pysat.examples.rc2 import RC2
from pysat.formula import And, Formula, Atom, PYSAT_TRUE, PYSAT_FALSE, IDPool, WCNF
from pysat.solvers import Solver

from src.pddl.Plan import Plan
from src.plan.Encoding import Encoding
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.TrueExpression import TrueExpression
from src.utils.LogPrint import LogPrint, LogPrintLevel, console
from src.utils.TimeStat import TimeStat


class SATSolver:
    encoding: Encoding
    variables: Set[SMTVariable]
    memodict: Dict
    assertions: List[Formula]
    phases: List[SMTVariable]

    def __init__(self, encoding: Encoding):
        self.memodict = dict()
        self.encoding = encoding
        self.assertions = list()
        self.variables = set()
        self.phases = list()
        self.addAssertions(self.encoding.rules)
        # if self.encoding.softRules:
        #     for g in self.encoding.softRules:
        #         if not isinstance(g, SMTBoolVariable):
        #             raise Exception(f"I cannot deal with a conjunction of formulae in the goal like {g}")
        #         self.phases.append(g)
        pass

    def addAssertion(self, expr: SMTExpression):
        if isinstance(expr, TrueExpression):
            return
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

    # def getSolution(self) -> SMTSolution or bool:
    #     formula = And(*self.assertions, merge=True)
    #     formula.clausify()
    #
    #     # Export the pool only after clausification, since Tseitin variables
    #     # may have been introduced.
    #     vpool: IDPool = Formula.export_vpool()
    #
    #     wcnf = WCNF()
    #
    #     # Original formula clauses are hard.
    #     for clause in formula:
    #         wcnf.append(list(clause))
    #
    #     # Each unit soft clause [p] expresses:
    #     # "prefer p to be True".
    #     for preferred in self.phases:
    #         preferred_id = vpool.obj2id[preferred.atom]
    #         wcnf.append([preferred_id], weight=1)
    #
    #     with RC2(wcnf, solver="kissat404") as rc2:
    #         model = rc2.compute()
    #
    #         # None means that the hard clauses are inconsistent.
    #         if model is None:
    #             return False
    #
    #         assignment = {
    #             abs(literal): literal > 0
    #             for literal in model
    #         }
    #
    #         solution = SMTSolution()
    #
    #         for variable in self.variables:
    #             variable_id = vpool.obj2id[variable.atom]
    #
    #             solution.addVariable(
    #                 variable,
    #                 assignment[variable_id],
    #             )
    #
    #         return solution

    @staticmethod
    def printFormulaStats(f: Formula):
        before = len(f.atoms())

        f.clausify()

        vpool = Formula.export_vpool()
        after = vpool.top

        console.log(f"Variables Before CNF: {before}", LogPrintLevel.STATS)
        console.log(f"Variables After CNF: {after}", LogPrintLevel.STATS)

    def getSolution(self) -> SMTSolution or bool:
        formula: Formula = And(*self.assertions, merge=True)
        SATSolver.printFormulaStats(formula)
        t = TimeStat.startHolder("Constructing solver formula")
        with Solver(name='kissat', bootstrap_with=formula) as s:
            # phases = [vpool.obj2id[p.atom] for p in self.phases]
            # s.set_phases(phases)
            t.endHolderMilliseconds()
            t = TimeStat.startHolder("Actual SAT Solving time")
            res = s.solve()
            t.endHolderMilliseconds()

            t = TimeStat.startHolder("Retrieving solution")
            vpool = Formula.export_vpool()
            if not res:
                return False
            model = s.get_model()
            solution = SMTSolution()
            assignment = dict([(abs(lit), lit > 0) for lit in model])
            for v in self.variables:
                r = vpool.obj2id[v.atom]
                solution.addVariable(v, assignment[r])
            t.endHolderMilliseconds()
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
