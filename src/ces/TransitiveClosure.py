from typing import List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.pddl.Atom import Atom


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self, t: ActionStateTransitionFunction):
        super().__init__(t)

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom]):
        i = 1
        print("Computing first step")
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t, atomsOrder)
        print(f"Step 1: {currentBDD.bdd.to_dot()}")
        while (True):
            i += 1
            nextBDD: TransitionFunctionBDD = currentBDD.computeTransition()
            print(f"Step {i}: {nextBDD.bdd.to_dot()}")
            if currentBDD.isEquivalent(nextBDD):
                print(f"Transitive Closure found at {i}-th iteration")
                nextBDD.__class__ = TransitiveClosure
                return nextBDD
            del currentBDD
            currentBDD = nextBDD
