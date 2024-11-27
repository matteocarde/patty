from typing import Dict, List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.BDDVariableOrder import BDDVariableOrder
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Domain import Domain, GroundedDomain


class TransitionRelations:
    closures: Dict[Action, List[TransitionFunctionBDD]]
    reachability: Dict[Action, List[TransitionFunctionBDD]]

    def __init__(self, domain: GroundedDomain, maxTime: None or int = None):

        self.closures = dict()
        self.reachability = dict()
        for a in domain.actions:
            if a.isIdempotent():
                continue

            T_a = ActionStateTransitionFunction(a)
            order = BDDVariableOrder(a).getOrder()
            print(f"Computing Transitive Closure of {a}")
            self.closures[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, order, reflexive=True,
                                                                                   maxTime=maxTime)
            print(f"Computing Reachability of {a}")
            self.reachability[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, order, reflexive=False,
                                                                                       maxTime=maxTime)
