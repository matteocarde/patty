import json
from typing import Dict, Set

from src.pddl.Domain import Domain
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.Predicate import Predicate
from src.pddl.TypedPredicate import TypedPredicate


class DeltaKnowledge:

    def __init__(self):
        self.variables: Set[TypedPredicate] = set()
        self.initial: Dict[Literal, int] = dict()
        self.jTck: Dict[Operation, Literal] = dict()
        self.jDelta: Dict[Operation, Literal] = dict()
        self.Nabla: Dict[Operation, Predicate] = dict()
        pass

    @classmethod
    def fromFile(cls, filename: str, domain: Domain):
        kdelta = cls()

        with open(filename, 'r') as f:
            kJson = json.load(f)

        for (var, value) in kJson["vars"].items():
            tPredicate = TypedPredicate.fromString(var, domain.types)
            kdelta.variables.add(tPredicate)
            kdelta.initial[tPredicate] = value

        signatures = domain.getSignatures()
        for (signature, variables) in kJson["J"].items():
            signature = signature.replace(" ", "")
            if signature not in signatures:
                raise Exception(f"No operation {signature} in domain")
            operation = signatures[signature]
            tckVar = Literal.fromPositiveString(variables[0])
            deltaVar = Literal.fromPositiveString(variables[1])
            kdelta.jTck[operation] = tckVar
            kdelta.jDelta[operation] = deltaVar

        pass
