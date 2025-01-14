import signal
from typing import List, Dict

from pyeda.boolalg.bdd import bddvar, BDDVariable

from src.ces.ActionStateTransitionFunction import ActionStateTransitionFunction
from src.ces.TransitionFunctionBDD import TransitionFunctionBDD
from src.pddl.Atom import Atom


class TransitiveClosure(TransitionFunctionBDD):

    def __init__(self):
        super().__init__()

    @staticmethod
    def getOrder(action, order) -> Dict[Atom, Dict[int, BDDVariable]]:
        d = dict()
        for v in order:
            d[v] = dict()
            d[v][0] = bddvar(f"{action}_{v}_0")
            d[v][1] = bddvar(f"{action}_{v}_1")
            d[v][2] = bddvar(f"{action}_{v}_2")
        return d

    @classmethod
    def fromTransitionFunction(cls, t: ActionStateTransitionFunction,
                               atomsOrder: List[Atom],
                               reflexive=True,
                               relaxed=True,
                               maxTime: None or int = None,
                               maxReachabilityIndex=0) -> List[TransitionFunctionBDD]:

        bdds = []
        i = 0
        variables = TransitiveClosure.getOrder(t.action, atomsOrder)
        currentBDD: TransitionFunctionBDD = super().fromActionStateTransitionFunction(t, atomsOrder, variables)
        bdds.append(currentBDD)

        print("Transitive" if reflexive else "Reachability", t.action, i, currentBDD.bdd.to_dot())

        if maxTime:
            signal.alarm(maxTime)

        def handler(signum, frame):
            raise TimeoutError("Timeout!!!")

        signal.signal(signal.SIGALRM, handler)
        try:
            while True:
                i += 1
                nextBDD: TransitionFunctionBDD = currentBDD.computeTransition(
                    reflexive=reflexive,
                    relaxed=relaxed
                )
                print("Transitive" if reflexive else "Reachability", t.action, i, nextBDD.bdd.to_dot())
                if not reflexive and i > maxReachabilityIndex:
                    return bdds
                if currentBDD.isEquivalent(nextBDD):
                    nextBDD.__class__ = TransitiveClosure
                    signal.alarm(0)
                    print(nextBDD.bdd.satisfy_count())
                    return bdds
                bdds.append(nextBDD)
                currentBDD = nextBDD
        except TimeoutError:
            print(len(bdds))
            print(f"Timeout when computing transitive closure of {t.action} at step {i}, i.e., {2 ** i} steps")
            return bdds
