from typing import Dict

from src.pddl.Action import Action
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.smt.SMTNumericVariable import SMTIntVariable, SMTRealVariable

LAMBDA = "λ"


class ClassicalLevelVariablesDL:
    actions: Dict[Action, SMTIntVariable]
    literals: Dict[Literal, SMTIntVariable]
    goal: SMTIntVariable

    def __init__(self, domain: GroundedDomain):
        self.actions = dict()
        self.usage = dict()
        self.literals = dict()
        self.goal = SMTIntVariable(f"λ(G)")
        # self.infty = SMTRealVariable(f"λ(∞)")

        for a in domain.actions:
            self.actions[a] = SMTRealVariable(f"λ({a})")

        for v in domain.predicates:
            self.literals[Literal.pos(v)] = SMTRealVariable(f"λ({v} = T)")
            self.literals[Literal.neg(v)] = SMTRealVariable(f"λ({v} = F)")
