import unittest
from unittest import TestCase

from sympy import Symbol

from src.pddl.Atom import Atom


class TestAtom(TestCase):

    def setUp(self) -> None:
        pass

    def test_shouldCreateAndGroundAnAtom(self):
        atom1 = Atom.fromString("a ?x ?y ?z")
        self.assertIsInstance(atom1, Atom)
        self.assertEqual(atom1.name, "a")
        self.assertEqual(atom1.attributes, ["?x", "?y", "?z"])

        atom2 = Atom.fromString("a x1 y1 z1")
        self.assertIsInstance(atom2, Atom)
        self.assertEqual(atom2.name, "a")
        self.assertEqual(atom2.attributes, ["x1", "y1", "z1"])

        gAtom = atom1.ground({"?x": "x1", "?y": "y1", "?z": "z1"})
        self.assertEqual(gAtom, atom2)

        # Idempotence
        self.assertEqual(atom1.attributes, ["?x", "?y", "?z"])

    def test_shouldReturnSymbol(self):
        atom = Atom.fromString("a x1 y1 z1")
        self.assertEqual(atom.toExpression(), Symbol("a(x1,y1,z1)"))


if __name__ == '__main__':
    unittest.main()
