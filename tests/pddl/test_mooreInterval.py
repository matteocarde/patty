import unittest
from unittest import TestCase

from sympy import Symbol

from Atom import Atom
from Formula import Formula
from InitialCondition import InitialCondition
from MooreInterval import MooreInterval


class TestMooreInterval(TestCase):

    def setUp(self) -> None:
        pass

    def test_shouldOperateWithMooreIntervals(self):
        i = MooreInterval(5, 10)
        self.assertEqual(i.lb, 5)
        self.assertEqual(i.ub, 10)

        i = MooreInterval()
        self.assertEqual(i.lb, float("-inf"))
        self.assertEqual(i.ub, float("+inf"))

        i = MooreInterval(5, 10) + MooreInterval(-5, 20)
        self.assertEqual(i.lb, 0)
        self.assertEqual(i.ub, 30)

        i = MooreInterval(-2, 10) - MooreInterval(-5, -2)
        self.assertEqual(i.lb, 0)
        self.assertEqual(i.ub, 15)

        i = MooreInterval(-2, 10) * MooreInterval(-5, -2)
        self.assertEqual(i.lb, -50)
        self.assertEqual(i.ub, 10)

        i = MooreInterval(5, 10) / MooreInterval(1, 30)
        self.assertEqual(i.lb, 5 / 30)
        self.assertEqual(i.ub, 10)

        i = MooreInterval(-10, 0).merge(MooreInterval(2, 40))
        self.assertEqual(i.lb, -10)
        self.assertEqual(i.ub, 40)

        i = MooreInterval(-10, 5).intersecate(MooreInterval(2, 40))
        self.assertEqual(i.lb, 2)
        self.assertEqual(i.ub, 5)

        i = MooreInterval(1, 10)
        self.assertTrue(i.exists(">", 4))
        self.assertTrue(i.exists(">", -4))
        self.assertFalse(i.exists(">", 11))
        self.assertFalse(i.exists(">", 10))
        self.assertTrue(i.exists(">=", 10))
        self.assertTrue(i.exists("<", 4))
        self.assertTrue(i.exists("<", 40))
        self.assertFalse(i.exists("<", 1))
        self.assertTrue(i.exists("<=", 1))
        self.assertTrue(i.exists("=", 5))
        self.assertTrue(i.exists("=", 1))
        self.assertTrue(i.exists("=", 10))
        self.assertFalse(i.exists("=", 16))

        self.assertTrue(i.exists("!=", 20))
        self.assertTrue(i.exists("!=", -2))
        self.assertFalse(i.exists("!=", 5))


if __name__ == '__main__':
    unittest.main()
