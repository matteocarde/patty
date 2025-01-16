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

    def __init__(self, domain: GroundedDomain, maxTime: None or int = None, relaxed=True):

        self.closures = dict()
        self.reachability = dict()

        for a in domain.actions:
            if a.isIdempotent():
                continue

            T_a = ActionStateTransitionFunction(a, domain)
            bddorder = BDDVariableOrder(a)
            order = bddorder.getOrder()
            # print(f"Order {a}: {bddorder.toDot()}")
            print(f"Computing Transitive Closure of {a}")
            Ts = TransitiveClosure.fromTransitionFunction(T_a, order,
                                                          relaxed=relaxed,
                                                          reflexive=True,
                                                          maxTime=maxTime)

            # print(a, Ts[-1].bdd.to_dot())
            self.closures[a] = Ts

            print(f"Computing Reachability of {a}")
            Rs = TransitiveClosure.fromTransitionFunction(T_a,
                                                          order,
                                                          relaxed=relaxed,
                                                          reflexive=False,
                                                          maxTime=maxTime,
                                                          maxReachabilityIndex=len(Ts))
            self.reachability[a] = Rs

        pass
