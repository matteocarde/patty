from typing import Dict, List

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.plan.Encoding import Encoding
from src.relaxed.ClassicalLevelVariables import ClassicalLevelVariables
from src.smt.SMTConjunction import SMTConjunction
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTVariable import SMTVariable
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

        self.infty = 2 ** min(len(self.domain.actions), len(self.domain.predicates))
        self.literals = domain.getAllLiterals()

        self.levelVariables = ClassicalLevelVariables(self.domain)

        self.rules = []

        self.rules += self.__getEffRules()
        self.rules += self.__getPreRules()
        self.rules += self.__getGoalRules()

        pass

    def __getEffRules(self) -> List[SMTExpression]:
        rules = SMTConjunction()
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals

        for lit in self.literals:
            affectingActions = [LA[a] for a in self.domain.actions if lit in a.effects.assignments]
            trueLit = self.stateVars[lit.atom] if lit.sign == "+" else ~self.stateVars[lit.atom]
            falseLit = ~self.stateVars[lit.atom] if lit.sign == "+" else self.stateVars[lit.atom]

            rules.append(trueLit.implies(LC[lit].equal(0)))
            minAffecting = MinExpression.fromList(affectingActions + [self.infty])
            rules.append(falseLit.implies(LC[lit].equal(minAffecting)))

        return rules

    def __getPreRules(self) -> List[SMTExpression]:
        if self.heuristic == "hmax":
            return self.__getPreRulesHMAX()
        if self.heuristic == "hadd":
            return self.__getPreRulesHADD()
        if self.heuristic == "h+":
            return self.__getPreRulesHPLUS()

    def __getPreRulesHMAX(self):
        rules = SMTConjunction()
        LA = self.levelVariables.actions
        LC = self.levelVariables.literals

        for a in self.domain.actions:
            maxPrecondition = MaxExpression.fromList([LC[lit] for lit in a.preconditions if isinstance(lit, Literal)] + [0])
            rules.append((LA[a] < self.infty).implies(LA[a].equal(maxPrecondition + 1)))
            orPrecondition = SMTExpression.bigor([LA[a].equal(LC[lit]) for lit in a.preconditions if isinstance(lit, Literal)])
            rules.append((LA[a] >= self.infty).implies(orPrecondition))

        return rules
