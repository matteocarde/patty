from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from pyeda.boolalg.bdd import _NODES


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self, t: ActionStateTransitionFunction):
        super().__init__(t)

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction):
        i = 1
        print("Computing first step")
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t)
        print(f"Step 1: {currentBDD.bdd.to_dot()}")
        while (True):
            i += 1
            nextBDD: TransitionFunctionBDD = currentBDD.computeTransition()
            print(len(_NODES))
            if currentBDD.isEquivalent(nextBDD):
                print(f"Transitive Closure found at {i}-th iteration")
                nextBDD.__class__ = TransitiveClosure
                return nextBDD
            currentBDD = nextBDD
