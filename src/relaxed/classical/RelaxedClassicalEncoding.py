from typing import Dict, List, Tuple

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.plan.Encoding import Encoding
from src.plan.Pattern import Pattern
from src.relaxed.classical.ClassicalLevelVariables import ClassicalLevelVariables
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.MaxExpression import MaxExpression
from src.smt.expressions.MinExpression import MinExpression


class RelaxedClassicalEncoding(Encoding):

    def __init__(self,
                 domain: GroundedDomain,
                 problem: Problem,
                 heuristic: str,
                 stateVars: Dict[Atom, SMTVariable]
                 ):
        super().__init__()
        self.domain = domain
        self.problem = problem
        self.heuristic = heuristic
        self.stateVars = stateVars

        self.literals = domain.getAllLiterals()

        self.levelVariables = ClassicalLevelVariables(self.domain)

        self.rules = []

        self.rules += self.__getEffRules()
        self.rules += self.__getPreRules()
        self.rules += self.__getBoundRules()
        self.rules += self.__getGoalRules()

        self.minimize = self.__getMinimize()

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
            minAffecting = MinExpression.fromList(affectingActions + [linfty])
            rules.append(falseLit.implies(LC[lit].equal(minAffecting)))

        return rules

    def __getPreRules(self) -> List[SMTExpression]:

        LA = self.levelVariables.actions
        LC = self.levelVariables.literals

        els: List[Tuple[SMTVariable, List[SMTVariable]]] = list()
        for a in self.domain.actions:
            els.append((LA[a], [LC[lit] for lit in a.preconditions if isinstance(lit, Literal)]))

        if self.heuristic == "hmax":
            return self.__getPreRulesHMAX(els)
        if self.heuristic == "hadd":
            return self.__getPreRulesHADD(els)
        if self.heuristic == "h+":
            return self.__getPreRulesHPLUS(els)

    def __getGoalRules(self) -> List[SMTExpression]:

        rules = SMTConjunction()
        LC = self.levelVariables.literals
        linfty = self.levelVariables.infty

        for c in self.problem.goal:
            print(self.problem.goal, c)
            rules.append(LC[c] < linfty)

        return rules

    def __getPreRulesHMAX(self, els: List[Tuple[SMTVariable, List[SMTVariable]]]):
        rules = SMTConjunction()
        linfty = self.levelVariables.infty

        for (la, lcs) in els:
            maxPrecondition = MaxExpression.fromList(lcs + [0]) + 1
            rules.append((la < linfty).implies(la.equal(maxPrecondition)))
            orPrecondition = SMTExpression.bigor([la.equal(lc) for lc in lcs])
            rules.append((la >= linfty).implies(orPrecondition))

        return rules

    def __getPreRulesHADD(self, els: List[Tuple[SMTVariable, List[SMTVariable]]]):
        rules = SMTConjunction()
        linfty = self.levelVariables.infty

        for (la, lcs) in els:
            sumPrecondition = sum(lcs) + 1
            rules.append((la < linfty).implies(la.equal(sumPrecondition)))
            orPrecondition = SMTExpression.bigor([la.equal(lc) for lc in lcs])
            rules.append((la >= linfty).implies(orPrecondition))

        return rules

    def __getPreRulesHPLUS(self, els: List[Tuple[SMTVariable, List[SMTVariable]]]):
        rules = SMTConjunction()
        linfty = self.levelVariables.infty

        for (la, lcs) in els:
            maxPrecondition = MaxExpression.fromList(lcs) + 1
            rules.append((la < linfty).implies(la.equal(maxPrecondition)))

        return rules

    def __getMinimize(self):
        if self.heuristic != "h+":
            return []
        linfty = self.levelVariables.infty
        LA = self.levelVariables.actions
        minimize = sum([ITEExpression(LA[a] < linfty, 1, 0) for a in self.domain.actions])
        return [minimize]

    def getPattern(self, solution: SMTSolution) -> Pattern:
        LA = self.levelVariables.actions
        order = sorted([(solution.getVariable(LA[a]), a) for a in self.domain.actions])
        return Pattern.fromOrder([a for (la, a) in order])
