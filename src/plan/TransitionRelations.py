from typing import Dict, List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Domain import Domain


class TransitionRelations:
    closures: Dict[Action, List[TransitionFunctionBDD]]
    reachability: Dict[Action, List[TransitionFunctionBDD]]

    def __init__(self, domain: Domain):

        self.closures = dict()
        self.reachability: Dict[Action, List[TransitionFunctionBDD]] = dict()
        for a in domain.actions:
            T_a = ActionStateTransitionFunction(a)
            atomsOrder = list(reversed(sorted(a.predicates)))
            if a.isIdempotent():
                bdd = TransitionFunctionBDD.fromActionStateTransitionFunction(T_a, atomsOrder)
                self.closures[a] = [bdd]
                self.reachability[a] = [bdd]
                continue
            print(f"Computing Transitive Closure of {a}")
            self.closures[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, atomsOrder, reflexive=True)
            print(f"Computing Reachability of {a}")
            self.reachability[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, atomsOrder, reflexive=False)
