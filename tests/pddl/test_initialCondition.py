from unittest import TestCase

import unittest
from src.pddl.Atom import Atom
from src.pddl.InitialCondition import InitialCondition

INITIAL_CONDITION = """
(:init
    (= (x b3) 1)
    (= (y b3) 3)
    (= (x b4) 3)
    (= (y b4) 4)
    (= (x b2) 7)
    (= (y b2) 2)
    (= (x b1) 5)
    (= (y b1) 1)
    (= (x b5) 5)
    (= (y b5) 5)
    (= (max_x) 5)
    (= (min_x) 1)
    (= (max_y) 5)
    (= (min_y) 1)
)
"""


class TestInitialContidition(TestCase):

    def setUp(self) -> None:
        pass

    def test_shouldCreateAnInitialCondition(self):
        ic = InitialCondition.fromString(INITIAL_CONDITION)
        self.assertEqual(len(ic.assignments), 14)
        self.assertEqual(ic.numericAssignments[Atom.fromString("x b2")], 7)


if __name__ == '__main__':
    unittest.main()
