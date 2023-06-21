from unittest import TestCase

import unittest
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula


class TestFormula(TestCase):

    def setUp(self) -> None:
        pass

    def test_shouldCreateAFormula(self):
        f = Formula.fromString("()")
        self.assertIsInstance(f, Formula)

        f = Formula.fromString("(atHome x y)")
        self.assertIsInstance(f, Formula)
        self.assertEqual(f.type, "AND")
        self.assertEqual(len(f.conditions), 1)

        f = Formula.fromString("(>= (bricks x y) 10)")
        self.assertIsInstance(f, Formula)
        self.assertEqual(f.type, "AND")
        self.assertEqual(len(f.conditions), 1)

        f = Formula.fromString("(and (>= (bricks x y) 10) (<= (cost) 5))")
        self.assertIsInstance(f, Formula)
        self.assertEqual(f.type, "AND")
        self.assertEqual(len(f.conditions), 2)

        f = Formula.fromString("(and (>= (bricks x y) 10) (or (<= (cost) 5) (>= (cost) 20)))")
        self.assertIsInstance(f, Formula)
        self.assertEqual(f.type, "AND")
        self.assertEqual(len(f.conditions), 2)
        orF = f.conditions[1]
        self.assertIsInstance(orF, Formula)
        self.assertEqual(orF.type, "OR")
        self.assertEqual(len(orF.conditions), 2)

    def test_shouldGround(self):
        f = Formula.fromString("(and (>= (bricks ?x ?y) 10.0) (or (<= (cost ?x) 5.0) (>= (cost ?y) 20.0)))")
        gF = f.ground({"?x": "x1", "?y": "y2"})
        self.assertEqual(gF, Formula.fromString(
            "(and (>= (bricks x1 y2) 10.0) (or (<= (cost x1) 5.0) (>= (cost y2) 20.0)))"))
        self.assertIn(Atom.fromString("bricks ?x ?y"), f.getFunctions())
        self.assertIn(Atom.fromString("bricks x1 y2"), gF.getFunctions())


if __name__ == '__main__':
    unittest.main()
