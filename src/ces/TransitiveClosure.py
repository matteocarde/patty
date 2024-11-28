import signal
from typing import List

from pyeda.boolalg.bdd import bddvar

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.pddl.Atom import Atom


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self, t: ActionStateTransitionFunction):
        super().__init__(t)

    @staticmethod
    def setOrder(action, order, reflexive):
        for v in order:
            bddvar(f"{action}_{v}_0")
            bddvar(f"{action}_{v}_1")
            bddvar(f"{action}_{v}_2")

    @classmethod
    def fromActionStateTransitionFunction(cls, t: ActionStateTransitionFunction, atomsOrder: List[Atom],
                                          reflexive=True, maxTime: None or int = None) -> List[TransitionFunctionBDD]:

        bdds = []
        i = 0
        TransitiveClosure.setOrder(t.action, atomsOrder, reflexive)
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t, atomsOrder)
        bdds.append(currentBDD)

        print(currentBDD.bdd.to_dot())

        if maxTime:
            signal.alarm(maxTime)

        def handler(signum, frame):
            raise Exception("Timeout!!!")

        signal.signal(signal.SIGALRM, handler)
        try:
            while True:
                i += 1
                nextBDD: TransitionFunctionBDD = currentBDD.computeTransition(reflexive=reflexive)
                if currentBDD.isEquivalent(nextBDD):
                    nextBDD.__class__ = TransitiveClosure
                    signal.alarm(0)
                    return bdds
                bdds.append(nextBDD)
                currentBDD = nextBDD
        except:
            print(len(bdds))
            print(f"Timeout when computing transitive closure of {t.action} at step {i}, i.e., {2 ** i} steps")
            return bdds
