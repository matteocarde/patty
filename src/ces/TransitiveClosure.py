from typing import List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from pyeda.boolalg.bdd import _NODES, bddvar

from src.pddl.Atom import Atom


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self, t: ActionStateTransitionFunction):
        super().__init__(t)

    @staticmethod
    def setOrder(action, order, reflexive):
        p = 1 if reflexive else 0
        for v in order:
            bddvar(f"{action}_{v}_0")
            bddvar(f"{action}_{v}_1")
            bddvar(f"{action}_{v}_2")

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom],
                                          reflexive=True) -> List[TransitionFunctionBDD]:

        bdds = []
        i = 1
        TransitiveClosure.setOrder(t.action, atomsOrder, reflexive)
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t, atomsOrder)
        bdds.append(currentBDD)
        while (True):
            i += 1
            nextBDD: TransitionFunctionBDD = currentBDD.computeTransition(reflexive=reflexive)
            if currentBDD.isEquivalent(nextBDD):
                nextBDD.__class__ = TransitiveClosure
                return bdds
            bdds.append(nextBDD)
            currentBDD = nextBDD
