import math
from typing import Dict, List, Tuple

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.plan.Encoding import Encoding
from src.plan.Pattern import Pattern
from src.relaxed.classical.ClassicalLevelVariables import ClassicalLevelVariables
from src.relaxed.classical.ClassicalLevelVariablesDL import ClassicalLevelVariablesDL
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class RelaxedClassicalEncodingDL(Encoding):

    def __init__(self,
                 domain: GroundedDomain,
                 problem: Problem,
                 heuristic: str,
                 stateVars: Dict[Atom, SMTVariable],
                 minimize: bool = True,
                 c: float = float("inf")
                 ):
        super().__init__()
        self.domain = domain
        self.problem = problem
        self.heuristic = heuristic
        self.stateVars = stateVars
        self.L = 0

        self.literals = domain.getAllLiterals()

        self.levelVariables = ClassicalLevelVariablesDL(self.domain)

        self.rules = []

        self.rules += self.__getEffRules()
        self.rules += self.__getPreRules()
        self.rules += self.__getBoundRules()
        self.rules += self.__getGoalRules()

        if c < float("inf"):
            self.rules += self.__getCountRules(c)

        if minimize:
            self.minimize = self.__getMinimizeGoal()

        pass

    def __getBoundRules(self) -> List[SMTExpression]:
        rules = []
        LA = self.levelVariables.actions

        for a, la in LA.items():
            rules.append(la >= 0)
        return rules

    def __getEffRules(self) -> List[SMTExpression]:
        rules = SMTConjunction()
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals

        for lit in self.literals:
            affectingActions = [LA[a] for a in self.domain.actions if lit in a.effects.assignments]
            trueLit = self.stateVars[lit.atom] if lit.sign == "+" else ~self.stateVars[lit.atom]
            effects = SMTExpression.bigor([la.equal(LC[lit]) for la in affectingActions])
            r = (LC[lit] >= 1).implies(trueLit | effects)
            rules.append(r)

        return rules

    def __getPreRules(self) -> List[SMTExpression]:

        rules: List[SMTExpression] = list()
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals
        lg = self.levelVariables.goal

        els: List[Tuple[SMTVariable, List[SMTVariable]]] = list()
        for a in self.domain.actions:
            els.append((LA[a], [LC[lit] for lit in a.preconditions if isinstance(lit, Literal)]))
        els.append((lg, [LC[lit] for lit in self.problem.goal if isinstance(lit, Literal)]))

        for la, preconditions in els:
            andGt = SMTExpression.bigand([lv >= la + 1 for lv in preconditions])
            orEqual = SMTExpression.bigor([lv.equal(la + 1) for lv in preconditions])
            r = (la >= 1).implies(andGt & orEqual)
            rules.append(r)

        return rules

    def __getGoalRules(self) -> List[SMTExpression]:

        rules = SMTConjunction()
        LC = self.levelVariables.literals
        lg = self.levelVariables.goal

        rules.append(lg.equal(1))

        return rules

    def __getCountRules(self, c):
        LA = self.levelVariables.actions

        return [MaxExpression(*[la for la in LA.values()]) < c]

    def __getMinimizeGoal(self):
        LA = self.levelVariables.actions

        minimize = sum([la for la in LA.values()])
        return [minimize]

    def getPattern(self, solution: SMTSolution, incomplete: bool = False) -> Pattern:
        LA = self.levelVariables.actions
        order = sorted([(-solution.getVariable(LA[a]), a) for a in self.domain.actions])
        if incomplete:
            order = [(la, a) for (la, a) in order if -la >= 1]
        return Pattern.fromOrder([a for (la, a) in order])

    def getGoalValueFunction(self, solution: SMTSolution):
        LA = self.levelVariables.actions

        goalLevel = max([solution.getVariable(la) for la in LA.values()])
        return goalLevel
