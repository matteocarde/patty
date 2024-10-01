from typing import List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from pyeda.boolalg.bdd import _NODES

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
            print(f"Step {i} of the transitive closure")
            nextBDD: TransitionFunctionBDD = currentBDD.computeTransition()
            if currentBDD.isEquivalent(nextBDD):
                print(f"Transitive Closure found at {i}-th iteration")
                nextBDD.__class__ = TransitiveClosure
                return nextBDD
            del currentBDD
            currentBDD = nextBDD
