from typing import Dict

from src.pddl.Action import Action
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.smt.SMTNumericVariable import SMTIntVariable
from src.smt.SMTVariable import SMTVariable

LAMBDA = "λ"


class ClassicalLevelVariables:
    actions: Dict[Action, SMTVariable]
    literals: Dict[Literal, SMTVariable]

    def __init__(self, domain: GroundedDomain):
        self.actions = dict()
        self.literals = dict()
        self.goalLevel = SMTIntVariable(f"λ(G)")

        for a in domain.actions:
            self.actions[a] = SMTIntVariable(f"λ({a})")

        for v in domain.predicates:
            self.literals[Literal.pos(v)] = SMTIntVariable(f"λ({v} = T)")
            self.literals[Literal.neg(v)] = SMTIntVariable(f"λ({v} = F)")
