import unittest
from unittest import TestCase

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate as BP, BinaryPredicateType
from src.pddl.Constant import Constant
from src.pddl.Literal import Literal
from src.pddl.MooreInterval import MooreInterval

OPERATION = "(+ 5 (- (+ 20 10) (* 20 (/ (x ?a1) (x ?a2)))))"

TYPED_COMPARATION = "(not (= ?x1 ?x2))"


class TestFormula(TestCase):

    def setUp(self) -> None:
        pass

    def test_shouldCreateOperation(self):
        bp1 = BP.fromOperationString(OPERATION)
        self.assertEqual(bp1.operator, "+")
        self.assertEqual(bp1.lhs, Constant(5))
        self.assertEqual(bp1.type, BinaryPredicateType.OPERATION)
        node = bp1.rhs
        self.assertEqual(node.type, BinaryPredicateType.OPERATION)
        self.assertEqual(node, BP.fromOperationString("(- (+ 20 10) (* 20 (/ (x ?a1) (x ?a2))))"))
        self.assertEqual(node.operator, "-")
        self.assertEqual(node.lhs.operator, "+")
        self.assertEqual(node.lhs.lhs, Constant(20))
        self.assertEqual(node.lhs.rhs, Constant(10))
        node = node.rhs
        self.assertEqual(node.type, BinaryPredicateType.OPERATION)
        self.assertEqual(node, BP.fromOperationString("(* 20 (/ (x ?a1) (x ?a2)))"))
        self.assertEqual(node.operator, "*")
        self.assertEqual(node.lhs, Constant(20))
        node = node.rhs
        self.assertEqual(node.type, BinaryPredicateType.OPERATION)
        self.assertEqual(node, BP.fromOperationString("(/ (x ?a1) (x ?a2))"))
        self.assertEqual(node.operator, "/")
        self.assertIsInstance(node.lhs, Literal)
        self.assertEqual(node.lhs.sign, "+")
        self.assertEqual(node.lhs.atom, Atom.fromString("x ?a1"))
        self.assertIsInstance(node.rhs, Literal)
        self.assertEqual(node.rhs.sign, "+")
        self.assertEqual(node.rhs.atom, Atom.fromString("x ?a2"))

        functions = bp1.getFunctions()
        self.assertEqual(len(functions), 2)
        self.assertIn(Atom.fromString("x ?a1"), functions)
        self.assertIn(Atom.fromString("x ?a2"), functions)
        self.assertEqual(len(bp1.getPredicates()), 0)

    def test_ground(self):
        bp = BP.fromOperationString("(+ 5 (- (+ 20 10) (* 20 (/ (x ?a1) (x ?a2)))))")
        gBp = bp.ground({"?a1": "a", "?a2": "b"})
        self.assertEqual(gBp, BP.fromOperationString("(+ 5 (- (+ 20 10) (* 20 (/ (x a) (x b)))))"))
        self.assertIn(Atom.fromString("x ?a1"), bp.getFunctions())
        self.assertIn(Atom.fromString("x a"), gBp.getFunctions())

    def test_shouldCreateModification(self):
        for op in {"assign", "increase", "decrease"}:
            bp1 = BP.fromModificationString(f"({op} (y ?a ?b) {OPERATION})")
            self.assertEqual(bp1.type, BinaryPredicateType.MODIFICATION)
            self.assertEqual(bp1.operator, op)
            self.assertEqual(bp1.lhs, Literal.fromPositiveString("(y ?a ?b)"))
            self.assertEqual(bp1.getAtom(), Atom.fromString("y ?a ?b"))
            self.assertEqual(bp1.type, BinaryPredicateType.MODIFICATION)
            self.assertEqual(bp1.rhs, BP.fromOperationString(OPERATION))

    def test_shouldCreateComparation(self):
        for op in {">=", ">", "<", "<=", "="}:
            bp1 = BP.fromComparationString(f"({op} (y ?a ?b) {OPERATION})")
            self.assertEqual(bp1.type, BinaryPredicateType.COMPARATION)
            self.assertEqual(bp1.operator, op)
            self.assertEqual(bp1.lhs, Literal.fromPositiveString("(y ?a ?b)"))
            self.assertEqual(bp1.getAtom(), Atom.fromString("y ?a ?b"))
            self.assertEqual(bp1.rhs, BP.fromOperationString(OPERATION))

    def test_shouldCreateBinaryPredicateWithNotEqual(self):
        bp1 = BP.fromNegatedComparationString(f"(not (= (y ?a ?b) {OPERATION}))")
        self.assertEqual(bp1.type, BinaryPredicateType.COMPARATION)
        self.assertEqual(bp1.operator, "!=")
        self.assertEqual(bp1.lhs, Literal.fromPositiveString("(y ?a ?b)"))
        self.assertEqual(bp1.getAtom(), Atom.fromString("y ?a ?b"))
        self.assertEqual(bp1.rhs, BP.fromOperationString(OPERATION))

    def test_additiveEffectTransformation(self):
        bp1 = BP.fromModificationString("(assign (x) (+ (y) 10))")
        bp2 = BP.additiveEffectsTransformation(bp1)
        self.assertEqual(bp2, BP.fromModificationString("(increase (x) (- (+ (y) 10.0) (x)))"))

    def test_substitute(self):
        bp = BP.fromModificationString("(increase (x ?a) (+ (y) (- (a) (+ 10 (w a b c))))")
        y = Atom.fromString("y")
        a = Atom.fromString("a")
        w = Atom.fromString("w a b c")
        subBp = bp.substitute(subs={y: 1, a: 10, w: 5})

        self.assertEqual(len(bp.getFunctions()), 4)
        self.assertEqual(len(subBp.getFunctions()), 1)

        self.assertEqual(subBp, BP.fromModificationString("(increase (x ?a) -4.0)"))

    def test_linearIncrement(self):

        # 5x + 6y + 12z + 5 -> 5
        bp = BP.fromOperationString("(+(* 5 (x)) (+ (* 6 (y) (+ (* 12 (z)) 5))))")
        self.assertEqual(bp.getLinearIncrement(), 5)

        # 5x + 6y + 12z -> 0
        bp = BP.fromOperationString("(+(* 5 (x)) (+ (* 6 (y) (* 12 (z)))))")
        self.assertEqual(bp.getLinearIncrement(), 0)

        # 5x + 6y + 12z + 5*3 -> 15
        bp = BP.fromOperationString("(+(* 5 (x)) (+ (* 6 (y) (+ (* 12 (z)) (* 5 3)))))")
        self.assertEqual(bp.getLinearIncrement(), 15)

    def test_intervalFromSimpleCondition(self):

        # x > 10 -> [10, +inf]
        bp = BP.fromComparationString("(>= (x) 10)")
        int: MooreInterval = bp.getIntervalFromSimpleCondition()
        self.assertEqual(int.lb, 10)
        self.assertEqual(int.ub, float("+inf"))

        # x < 10 -> [-inf, 10]
        bp = BP.fromComparationString("(<= (x) 10)")
        int: MooreInterval = bp.getIntervalFromSimpleCondition()
        self.assertEqual(int.lb, float("-inf"))
        self.assertEqual(int.ub, 10)

        # 2x < 10 -> [-inf, 5]
        bp = BP.fromComparationString("(<= (* 2 (x)) 10)")
        int: MooreInterval = bp.getIntervalFromSimpleCondition()
        self.assertEqual(int.lb, float("-inf"))
        self.assertEqual(int.ub, 5)

        # (3+2)x > (23 + 2) * 2 -> [10, +inf]
        bp = BP.fromComparationString("(>= (* (+ 3 2) (x)) (* (+ 23 2) 2))")
        int: MooreInterval = bp.getIntervalFromSimpleCondition()
        self.assertEqual(int.lb, 10)
        self.assertEqual(int.ub, float("+inf"))


if __name__ == '__main__':
    unittest.main()
