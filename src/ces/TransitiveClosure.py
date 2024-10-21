from typing import List

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from pyeda.boolalg.bdd import _NODES, bddvar

from src.pddl.Atom import Atom


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self, t: ActionStateTransitionFunction):
        super().__init__(t)

    @staticmethod
    def setOrder(order):
        for v in order:
            bddvar(f"{v}_0")
            bddvar(f"{v}_1")
            bddvar(f"{v}_2")

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom],
                                          reflexive=True) -> List[TransitionFunctionBDD]:

        bdds = []
        i = 1
        TransitiveClosure.setOrder(atomsOrder)
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t, atomsOrder)
        bdds.append(currentBDD)
        while (True):
            i += 1
            nextBDD: TransitionFunctionBDD = currentBDD.computeTransition(reflexive=reflexive)
            bdds.append(nextBDD)
            if currentBDD.isEquivalent(nextBDD):
                nextBDD.__class__ = TransitiveClosure
                return bdds
            del currentBDD
            currentBDD = nextBDD
