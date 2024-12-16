import unittest
from typing import List
from unittest import TestCase

from pyeda.boolalg.bdd import BinaryDecisionDiagram, bddvar, BDDVariable


def smooth(func: BinaryDecisionDiagram, vars: List[BDDVariable],
           var: BDDVariable or None = None):
    if not var:
        return smooth(func, vars[1:], vars[0])

    sFunc = smooth(func, vars[1:], vars[0]) if vars else func
    left = sFunc.restrict({var: 0})
    right = sFunc.restrict({var: 1})
    join = left | right
    return join


def closure(X0, X1, X2, T):
    prev01 = T(X0, X1)
    prev12 = T(X1, X2)
    prev02 = T(X0, X2)

    while True:
        now = smooth(((prev01 & prev12) | prev02), list(X1.values()))
        if now.equivalent(prev02):
            return now
        prev02 = now
        prev01 = now.compose(dict([(X2[i], X1[i]) for i in range(1, len(X0) + 1)]))
        prev12 = now.compose(dict([(X0[i], X1[i]) for i in range(1, len(X0) + 1)]))


def closureRelaxed(X0, X1, X2, T, C):
    prev01 = T(X0, X1)
    prev12 = T(X1, X2)
    prev02 = T(X0, X2)

    while True:
        trans = (C(X0) & (C(X1) | C(X2))) >> (prev01 & C(X1) & prev12)
        now = smooth(trans | prev02, list(X1.values()))
        if now.equivalent(prev02):
            return now
        prev02 = now
        prev01 = now.compose(dict([(X2[i], X1[i]) for i in range(1, len(X0) + 1)]))
        prev12 = now.compose(dict([(X0[i], X1[i]) for i in range(1, len(X0) + 1)]))


def models(X0, X2, T: BinaryDecisionDiagram):
    ms = []
    for mu in T.satisfy_all():
        s0 = ""
        s2 = ""
        for i in range(1, len(X0.items()) + 1):
            s0 += str(mu[X0[i]]) if X0[i] in mu else "-"
        for i in range(1, len(X2.items()) + 1):
            s2 += str(mu[X2[i]]) if X2[i] in mu else "-"
        ms.append(s0 + " -> " + s2)
    return ms


class TestCES(TestCase):

    def setUp(self) -> None:
        pass

    def test_solver(self):
        n = 4
        X0 = dict()
        X1 = dict()
        X2 = dict()
        for i in range(1, n + 1):
            X0[i] = bddvar(f"x{i}")
            # for i in range(1, n + 1):
            X1[i] = bddvar(f"x{i}'")
            # for i in range(1, n + 1):
            X2[i] = bddvar(f"x{i}''")

        T = lambda X0, X1: \
            X1[1].iff(X0[4]) & \
            X1[2].iff(X0[1]) & \
            X1[3].iff(X0[2]) & \
            X1[4].iff(X0[3]) & \
            (X0[1] | X0[2] | X0[3] | X0[4]) & \
            (~X0[1] | ~X0[2]) & \
            (~X0[2] | ~X0[3]) & \
            (~X0[3] | ~X0[4]) & \
            (~X0[4] | ~X0[1])
        C = lambda X: (~X[1] | ~X[2]) & \
                      (~X[1] | ~X[3]) & \
                      (~X[1] | ~X[4]) & \
                      (~X[2] | ~X[3]) & \
                      (~X[2] | ~X[4]) & \
                      (~X[3] | ~X[4]) & \
                      (X[1] | X[2] | X[3] | X[4])

        T_and = lambda X0, X1: T(X0, X1) & C(X0) & C(X1)

        # print("T", T(X0, X1).to_dot())
        # print("T_iff", T_iff(X0, X1).to_dot())
        # print("T_and", T_and(X0, X1).to_dot())
        # print("T_or", T_or(X0, X1).to_dot())

        print("T models: ", models(X0, X2, T(X0, X2)))
        print("T_and models: ", models(X0, X2, T_and(X0, X2)))

        T_plus: BinaryDecisionDiagram = closure(X0, X1, X2, T)
        T_and_plus: BinaryDecisionDiagram = closure(X0, X1, X2, T_and)
        T_hat_plus: BinaryDecisionDiagram = closureRelaxed(X0, X1, X2, T, C)

        # print("T^+", T_plus.to_dot())
        # print("T_iff^+", T_iff_plus.to_dot())
        # print("T_and^+", T_and_plus.to_dot())
        # print("T_or^+", T_or_plus.to_dot())

        print("T^+ models: ", models(X0, X2, T_plus))
        print("T_and^+ models: ", models(X0, X2, T_and_plus))
        print("T_hat^+ models: ", models(X0, X2, T_hat_plus))

        print("T_and^+", T_and_plus.to_dot())
        print("T_hat^+", T_hat_plus.to_dot())

        print("C(X) & C(X'') models: ", models(X0, X2, C(X0) & C(X2)))

        self.assertTrue(T_and_plus.equivalent((C(X0) & C(X2))))
        self.assertTrue(T_and_plus.equivalent((C(X0) & C(X2) & T_hat_plus)))
        self.assertTrue(T_hat_plus.is_one())

        # self.assertTrue((T_hat_plus & C(X0) & C(X2)).equivalent((T_hat1_plus & C(X0) & C(X2))))

        # self.assertTrue((T_hat1_plus & C(X0) & C(X2)).equivalent((C(X0) & C(X2))))

        if __name__ == '__main__':
            unittest.main()
