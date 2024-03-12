from __future__ import annotations

from src.pddl.Domain import GroundedDomain


class DomainStats:
    nOfFunctions: int
    nOfPredicates: int
    nOfSnapActions: int

    def __init__(self):
        pass

    @classmethod
    def fromGroundedDomain(cls, gDomain: GroundedDomain) -> DomainStats:
        ds = cls()

        ds.nOfFunctions = len(gDomain.functions)
        ds.nOfPredicates = len(gDomain.predicates)
        ds.nOfSnapActions = len(gDomain.actions)

        return ds

    def toJSON(self):
        return {
            "nOfFunction": self.nOfFunctions,
            "nOfPredicates": self.nOfPredicates,
            "nOfSnapActions": self.nOfSnapActions
        }
