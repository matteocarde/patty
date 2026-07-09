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
        # self.rules += self.__getUsageRules()
        self.rules += self.__getBoundRules()
        self.rules += self.__getGoalRules()

        # if c < float("inf"):
        #     self.rules += self.__getCountRules(c)

        if minimize:
            self.minimize = self.__getMinimizeGoal()

        pass

    def __getBoundRules(self) -> List[SMTExpression]:
        rules = []
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals
        linfty = self.levelVariables.infty

        for a, la in LA.items():
            rules.append(la <= linfty)
            rules.append(la >= 0)
        for lit, lc in LC.items():
            rules.append(lc <= linfty)
            rules.append(lc >= 0)
        return rules

    def __getEffRules(self) -> List[SMTExpression]:
        rules = SMTConjunction()
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals
        linfty = self.levelVariables.infty

        for lit in self.literals:
            affectingActions = [LA[a] for a in self.domain.actions if lit in a.effects.assignments]
            trueLit = self.stateVars[lit.atom] if lit.sign == "+" else ~self.stateVars[lit.atom]
            falseLit = ~self.stateVars[lit.atom] if lit.sign == "+" else self.stateVars[lit.atom]

            rules.append(trueLit.implies(LC[lit].equal(0)))
            bigor = SMTExpression.bigor([LC[lit] > la for la in affectingActions] + [LC[lit].equal(linfty)])
            rules.append(falseLit.implies(bigor))

        return rules

    def __getPreRules(self) -> List[SMTExpression]:

        LA = self.levelVariables.actions
        LC = self.levelVariables.literals

        els: List[Tuple[SMTVariable, List[SMTVariable]]] = list()
        for a in self.domain.actions:
            els.append((LA[a], [LC[lit] for lit in a.preconditions if isinstance(lit, Literal)]))

        if self.heuristic == "hmax":
            return self.__getPreRulesHMAX(els)
        if self.heuristic == "h+":
            return self.__getPreRulesHPLUS(els)

    def __getPreRulesHMAX(self, els: List[Tuple[SMTVariable, List[SMTVariable]]]):
        rules = SMTConjunction()
        linfty = self.levelVariables.infty

        for (la, lcs) in els:
            bigand = SMTExpression.bigand([la > lc for lc in lcs])
            rules.append((la < linfty).implies(bigand))
            orPrecondition = SMTExpression.bigor([la.equal(lc) for lc in lcs])
            rules.append((la >= linfty).implies(orPrecondition))

        return rules

    def __getPreRulesHPLUS(self, els: List[Tuple[SMTVariable, List[SMTVariable]]]):
        rules = SMTConjunction()
        linfty = self.levelVariables.infty

        for (la, lcs) in els:
            bigand = SMTExpression.bigand([la > lc + self.L for lc in lcs])
            r = (la < linfty).implies(bigand)
            rules.append(r)

        return rules

    def __getGoalRules(self) -> List[SMTExpression]:

        rules = SMTConjunction()
        LC = self.levelVariables.literals
        linfty = self.levelVariables.infty

        for c in self.problem.goal:
            rules.append(LC[c] < linfty)

        return rules

    def __getMinimize(self):
        # if self.heuristic != "h+":
        #     return []
        linfty = self.levelVariables.infty
        LA = self.levelVariables.actions
        minimize = sum([ITEExpression(LA[a] < linfty, 1, 0) for a in self.domain.actions])
        # minimize = sum([LA[a] - linfty for a in self.domain.actions])
        return [minimize]

    def __getMinimizeGoal(self):
        LC = self.levelVariables.literals

        minimize = MaxExpression(*[LC[c] for c in self.problem.goal])
        return [minimize]

    def __getMinimizeUsage(self):
        LU = self.levelVariables.usage
        minimize = sum([LU[a] for a in self.domain.actions])
        return [minimize]

    def __getCountRules(self, c: float):
        LC = self.levelVariables.literals
        minimize = MaxExpression(*[LC[c] for c in self.problem.goal]) <= c
        return [minimize]

    # def __getUsageRules(self):
    #     linfty = self.levelVariables.infty
    #     LA = self.levelVariables.actions
    #     LU = self.levelVariables.usage
    #     rules = []
    #     for a in self.domain.actions:
    #         rules.append((LA[a] < linfty).implies(LU[a].equal(1)))
    #         rules.append((LA[a] >= linfty).implies(LU[a].equal(0)))
    #     return rules

    def __getSoftRules(self):
        linfty = self.levelVariables.infty
        LA = self.levelVariables.actions
        return [LA[a] >= linfty for a in self.domain.actions]

    def getPattern(self, solution: SMTSolution, removeBeyondInfinite: bool = False) -> Pattern:
        LA = self.levelVariables.actions
        linfty = self.levelVariables.infty
        order = sorted([(solution.getVariable(LA[a]), a) for a in self.domain.actions])
        if removeBeyondInfinite:
            order = [(la, a) for (la, a) in order if la < solution.getVariable(linfty)]
        return Pattern.fromOrder([a for (la, a) in order])

    def getGoalValueFunction(self, solution: SMTSolution):
        LC = self.levelVariables.literals
        goalLevel = max([solution.getVariable(LC[c]) for c in self.problem.goal])
        # print(f"Goal level: {goalLevel}")
        # goalLevel = math.floor(goalLevel / self.L) * self.L - self.L
        # print(f"Goal level after: {goalLevel}")
        return goalLevel

    def getPatternGoal(self, solution: SMTSolution):
        LA = self.levelVariables.actions
        goalLevel = self.getGoalValueFunction(solution)
        order = sorted([(solution.getVariable(LA[a]), a) for a in self.domain.actions])
        order = [(la, a) for (la, a) in order if la < goalLevel]
        return Pattern.fromOrder([a for (la, a) in order])
