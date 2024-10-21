from typing import List, Dict

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.ces.TransitiveClosure import TransitiveClosure
from src.pddl.Action import Action
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.Problem import Problem
from src.utils.Arguments import Arguments


class TransitiveClosureSolver:

    def __init__(self, domain: Domain, problem: Problem, gDomain: GroundedDomain, args: Arguments):
        self.domain = domain
        self.problem = problem
        self.gDomain = gDomain
        self.args = args

        self.transitions: Dict[Action, List[TransitionFunctionBDD]] = dict()
        self.reachability: Dict[Action, List[TransitionFunctionBDD]] = dict()
        for a in self.domain.actions:
            T_a = ActionStateTransitionFunction(a)
            atomsOrder = list(reversed(sorted(a.predicates)))
            print(f"Non-Idempotent {a}: {a.isNonIdempotent()}")
            if a.isIdempotent():
                bdd = TransitionFunctionBDD.fromActionStateTransitionFunction(T_a, atomsOrder)
                self.transitions[a] = [bdd]
                self.reachability[a] = [bdd]
                continue
            print(f"Computing Transitive Closure of {a}")
            self.transitions[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, atomsOrder, reflexive=True)
            print(f"Computing Reachability of {a}")
            self.reachability[a] = TransitiveClosure.fromActionStateTransitionFunction(T_a, atomsOrder, reflexive=False)

        pass
