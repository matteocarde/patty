from __future__ import annotations

from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal


class DomainStats:
    nOfFunctions: int
    nOfPredicates: int
    nOfSnapActions: int
    nOfBooleanEffects: int
    nOfNumericEffects: int
    nOfAtMostOnceActions: int

    def __init__(self):
        pass

    @classmethod
    def fromGroundedDomain(cls, gDomain: GroundedDomain) -> DomainStats:
        ds = cls()

        ds.nOfFunctions = len(gDomain.functions)
        ds.nOfPredicates = len(gDomain.predicates)
        ds.nOfSnapActions = len(gDomain.operations)

        ds.nOfBooleanEffects = 0
        ds.nOfNumericEffects = 0
        atMostOnceActions = set()

        for op in gDomain.operations:
            for e in op.effects:
                if isinstance(e, BinaryPredicate):
                    ds.nOfNumericEffects += 1
                elif isinstance(e, Literal):
                    ds.nOfBooleanEffects += 1
            if not op.couldBeRepeated():
                atMostOnceActions.add(op)

        ds.nOfAtMostOnceActions = len(atMostOnceActions)
        return ds

    def toJSON(self):
        return {
            "nOfFunctions": self.nOfFunctions,
            "nOfPredicates": self.nOfPredicates,
            "nOfSnapActions": self.nOfSnapActions,
            "nOfBooleanEffects": self.nOfBooleanEffects,
            "nOfNumericEffects": self.nOfNumericEffects,
            "nOfAtMostOnceActions": self.nOfAtMostOnceActions
        }
