from typing import List
from unittest import TestCase

import unittest

from Action import Action
from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Problem import Problem

ACTION1 = """
(:action move_block_down
    :parameters (?b - block)
    :precondition (and 
        (>= (- (y ?b) 1) (min_y) )
        (not (isBroken ?b))
        (isOutside ?b)
    )
    :effect (and
        (decrease (y ?b) (+ 5 7))
        (increase (x ?b) 1)
        (assign (z ?b) (+ (x ?b) (y ?b)))
        (not (delList1 ?b))
        (not (delList2 ?b))
        (addList ?b)
    ))
"""

ACTION2 = """
(:action multiple_parameter
     :parameters (?a - block ?b - block ?c - other)
     :precondition (and 
        (>= (y ?b) (y ?a))
        (>= (y ?c) (y ?b))
     )
     :effect (and
        (decrease (y ?a) 1)
        (decrease (y ?b) 1)
        (decrease (y ?c) 1)
    ))
"""

PROBLEM = """
(define (problem instance_5_5_2_1)
    (:domain mt-block-grouping)
    (:objects
        b1 b2 b3 - block
        o1 o2 o3 - other
    )

    (:init
        (= (y b1) 5) 
        (= (y b2) 5) 
        (= (y b3) 5) 
    )

    (:goal
        (and 
            (< (y b1) 5) 
            (< (y b2) 5) 
            (< (y b3) 5)
        ) 
    )

)
"""


class TestAction(TestCase):

    def setUp(self) -> None:
        self.action1 = Action.fromString(ACTION1)
        self.action2 = Action.fromString(ACTION2)
        self.problem = Problem.fromString(PROBLEM)
        pass

    def test_shouldHaveCreatedAnAction(self):
        self.assertIsInstance(self.action1, Action)
        self.assertIsInstance(self.action2, Action)
        self.assertIsInstance(self.problem, Problem)

    def test_shouldHaveRightStructure(self):
        self.assertEqual(self.action1.name, "move_block_down")
        self.assertEqual(len(self.action1.parameters), 1)
        self.assertEqual(self.action1.parameters[0].name, "?b")
        self.assertEqual(self.action1.parameters[0].type, "block")
        self.assertEqual(len(self.action1.preconditions), 3)
        self.assertEqual(len(self.action1.effects), 6)

    def test_combinations(self):
        combinations1 = self.action1.getCombinations(self.problem)
        self.assertEqual(len(combinations1), 3)
        for i, c in enumerate(combinations1):
            self.assertEqual(len(c.items()), 1)
            self.assertIn("?b", c)
            self.assertEqual(c["?b"], "b" + str(i + 1))

        combinations2 = self.action2.getCombinations(self.problem)

        self.assertEqual(len(combinations2), 3 * 3 * 3)
        for i, c in enumerate(combinations2):
            self.assertEqual(len(c.items()), 3)
            self.assertIn("?a", c)
            self.assertIn(c["?a"], {"b1", "b2", "b3"})
            self.assertIn("?b", c)
            self.assertIn(c["?b"], {"b1", "b2", "b3"})
            self.assertIn("?c", c)
            self.assertIn(c["?c"], {"o1", "o2", "o3"})

    def test_grounding(self):

        gActions1 = self.action1.ground(self.problem)
        self.assertEqual(len(gActions1), 3)
        self.assertIsInstance(gActions1[0], Action)

        gActions2 = self.action2.ground(self.problem)
        self.assertEqual(len(gActions2), 3 * 3 * 3)
        self.assertIsInstance(gActions2[0], Action)

        for a1 in gActions1:
            self.assertIn(a1.name, {"move_block_down b1", "move_block_down b2", "move_block_down b3"})

        for a2 in gActions2:
            nameParts = a2.name.split(" ")
            self.assertIn(nameParts[1], {"b1", "b2", "b3"})
            self.assertIn(nameParts[2], {"b1", "b2", "b3"})
            self.assertIn(nameParts[3], {"o1", "o2", "o3"})

    def test_components(self):

        gAction1 = self.action1.ground(self.problem)[0]
        functions = gAction1.getFunctions()
        self.assertEqual(len(functions), 4)
        self.assertIn(Atom.fromString("y b1"), functions)
        self.assertIn(Atom.fromString("min_y"), functions)
        self.assertIn(Atom.fromString("x b1"), functions)
        self.assertIn(Atom.fromString("z b1"), functions)

        predicates = gAction1.getPredicates()
        self.assertEqual(len(predicates), 5)
        self.assertIn(Atom.fromString("isBroken b1"), predicates)
        self.assertIn(Atom.fromString("isOutside b1"), predicates)
        self.assertIn(Atom.fromString("delList1 b1"), predicates)
        self.assertIn(Atom.fromString("delList2 b1"), predicates)
        self.assertIn(Atom.fromString("addList b1"), predicates)

        preB = gAction1.getPreB()
        self.assertEqual(len(preB), 2)
        self.assertIn(Atom.fromString("isBroken b1"), preB)
        self.assertIn(Atom.fromString("isOutside b1"), preB)

        addList = gAction1.getAddList()
        self.assertEqual(len(addList), 1)
        self.assertIn(Atom.fromString("addList b1"), addList)

        delList = gAction1.getDelList()
        self.assertEqual(len(delList), 2)
        self.assertIn(Atom.fromString("delList1 b1"), delList)
        self.assertIn(Atom.fromString("delList2 b1"), delList)

        assList = gAction1.getAssList()
        self.assertEqual(len(assList), 1)
        self.assertIn(Atom.fromString("z b1"), assList)

        influencedAtoms = gAction1.getInfluencedAtoms()
        self.assertEqual(len(influencedAtoms), 6)
        self.assertIn(Atom.fromString("x b1"), influencedAtoms)
        self.assertIn(Atom.fromString("y b1"), influencedAtoms)
        self.assertIn(Atom.fromString("z b1"), influencedAtoms)
        self.assertIn(Atom.fromString("addList b1"), influencedAtoms)
        self.assertIn(Atom.fromString("delList1 b1"), influencedAtoms)
        self.assertIn(Atom.fromString("delList2 b1"), influencedAtoms)

        increases = gAction1.getIncreases()
        self.assertEqual(len(increases), 1)
        self.assertIn(Atom.fromString("x b1"), increases)
        self.assertEqual(increases[Atom.fromString("x b1")],
                         BinaryPredicate.fromModificationString("(increase (x b1) 1)").rhs)

        decreases = gAction1.getDecreases()
        self.assertEqual(len(decreases), 1)
        self.assertIn(Atom.fromString("y b1"), decreases)
        self.assertEqual(decreases[Atom.fromString("y b1")],
                         BinaryPredicate.fromModificationString("(decrease (y b1) (+ 5 7)").rhs)

        assignments = gAction1.getAssignments()
        self.assertEqual(len(assignments), 1)
        self.assertIn(Atom.fromString("z b1"), assignments)
        self.assertEqual(assignments[Atom.fromString("z b1")],
                         BinaryPredicate.fromModificationString("(assign (z b1) (+ (x b1) (y b1))").rhs)

    def test_substitute(self):
        gAction1 = self.action1.ground(self.problem)[0]

        subAction1 = gAction1.substitute(sub={Atom.fromString("min_y"): 5})

        self.assertIsInstance(subAction1, Action)

        gFunctions = gAction1.getFunctions()
        self.assertEqual(len(gFunctions), 4)
        self.assertIn(Atom.fromString("y b1"), gFunctions)
        self.assertIn(Atom.fromString("min_y"), gFunctions)
        self.assertIn(Atom.fromString("x b1"), gFunctions)
        self.assertIn(Atom.fromString("z b1"), gFunctions)

        subFunctions = subAction1.getFunctions()
        self.assertEqual(len(subFunctions), 3)
        self.assertIn(Atom.fromString("y b1"), subFunctions)
        self.assertIn(Atom.fromString("x b1"), subFunctions)
        self.assertIn(Atom.fromString("z b1"), subFunctions)

        pass


if __name__ == '__main__':
    unittest.main()
