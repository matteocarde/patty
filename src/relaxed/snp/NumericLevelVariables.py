from typing import Dict, Tuple, Set, List

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.smt.SMTNumericVariable import SMTIntVariable

LAMBDA = "λ"


class NumericLevelVariables:
    actionsLevel: Dict[Action, SMTIntVariable]
    conditionsLevel: Dict[Literal, SMTIntVariable]
    Ac_plus: Set[Tuple[Action, Atom, float]]
    Ac_minus: Set[Tuple[Action, Atom, float]]
    goalLevel: SMTIntVariable

    def __init__(self, domain: GroundedDomain):
        self.actionsLevel = dict()
        self.actions = dict()
        self.conditionsLevel = dict()
        self.goalLevel = SMTIntVariable(f"λ(G)")

        conditions: List[BinaryPredicate] = list()
        self.Ac_plus = set()
        self.Ac_minus = set()

        for a in domain.actions:
            self.actionsLevel[a] = SMTIntVariable(f"λ({a})")
            self.actions[a] = SMTIntVariable(f"r({a})")
            for c in a.preconditions.normalize():
                self.conditionsLevel[c] = SMTIntVariable(f"λ({c})")
                conditions.append(c)

        for c in conditions:
            if not isinstance(c, BinaryPredicate):
                continue
            coeffs = c.getCoefficients()
            for (x, kx) in coeffs.items():
                for a in domain.actions:
                    k = a.getConstantIncrement(x)
                    if not isinstance(k, BinaryPredicate):
                        continue
                    assert isinstance(k.rhs, Constant)
                    k = k.rhs.value
                    t = (a, x, k)
                    if (kx > 0 and k > 0) or (kx < 0 and k < 0):
                        self.Ac_plus.add(t)
                    if (kx > 0 > k) or (kx < 0 < k):
                        self.Ac_minus.add(t)

        pass
