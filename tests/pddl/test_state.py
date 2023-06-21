from unittest import TestCase

import unittest
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Formula import Formula
from src.pddl.InitialCondition import InitialCondition
from src.pddl.State import State

INITIAL_CONDITION = """
(:init
    (at x y)
    (= (number x) 10)
    (= (number y) 20)
)
"""

ACTION1 = """
(:action action-1
    :parameters ()
    :precondition (and 
        (at x y)
    )
    :effect (and
        (not (at x y))
        (at z w)
    ))
"""

ACTION2 = """
(:action action-2
    :parameters ()
    :precondition (and 
        (<= (number x) 5)
    )
    :effect (and
        (increase (number x) 10)
        (decrease (number y) 20)
    ))
"""

ACTION3 = """
(:action action-3
    :parameters ()
    :precondition (and 
        (>= (number y) 5)
    )
    :effect (and
        (decrease (number x) 10)
        (increase (number y) 20)
    ))
"""

ACTION_AND = """
(:action action-3
    :parameters ()
    :precondition (and 
        (at x y)
        (at z w)
    )
    :effect (and
        (decrease (number x) 10)
        (increase (number y) 20)
    ))
"""

ACTION_OR = """
(:action action-3
    :parameters ()
    :precondition (or 
        (at x y)
        (at z w)
    )
    :effect (and
        (decrease (number x) 10)
        (increase (number y) 20)
    ))
"""

ACTION_NOT = """
(:action action-3
    :parameters ()
    :precondition (or 
        (at x y)
        (not (at z w))
    )
    :effect (and
        (decrease (number x) 10)
        (increase (number y) 20)
    ))
"""


class TestState(TestCase):

    def setUp(self) -> None:
        self.init = InitialCondition.fromString(INITIAL_CONDITION)
        self.action1 = Action.fromString(ACTION1, dict())
        self.action2 = Action.fromString(ACTION2, dict())
        self.action3 = Action.fromString(ACTION3, dict())
        self.actionAnd = Action.fromString(ACTION_AND, dict())
        self.actionOr = Action.fromString(ACTION_OR, dict())
        self.actionNot = Action.fromString(ACTION_NOT, dict())

    def test_shouldUpdateStatesCorrectly(self):
        state0 = State.fromInitialCondition(self.init)
        state1 = state0.applyAction(self.action1)
        state1_3 = state1.applyAction(self.action3)
        state1_3_2 = state1_3.applyAction(self.action2)

        self.assertEqual(state0.getAtom(Atom.fromString("at x y")), True)
        self.assertEqual(state0.getAtom(Atom.fromString("at z w")), False)
        self.assertEqual(state0.getAtom(Atom.fromString("number x")), 10)
        self.assertEqual(state0.getAtom(Atom.fromString("number y")), 20)
        self.assertEqual(state0.satisfies(self.action1.preconditions), True)
        self.assertEqual(state0.satisfies(self.action2.preconditions), False)
        self.assertEqual(state0.satisfies(self.action3.preconditions), True)
        self.assertEqual(state0.satisfies(self.actionNot.preconditions), True)

        self.assertEqual(state1.getAtom(Atom.fromString("at x y")), False)
        self.assertEqual(state1.getAtom(Atom.fromString("at z w")), True)
        self.assertEqual(state1.getAtom(Atom.fromString("number x")), 10)
        self.assertEqual(state1.getAtom(Atom.fromString("number y")), 20)
        self.assertEqual(state1.satisfies(self.action1.preconditions), False)
        self.assertEqual(state1.satisfies(self.action2.preconditions), False)
        self.assertEqual(state1.satisfies(self.action3.preconditions), True)

        self.assertEqual(state1_3.getAtom(Atom.fromString("at x y")), False)
        self.assertEqual(state1_3.getAtom(Atom.fromString("at z w")), True)
        self.assertEqual(state1_3.getAtom(Atom.fromString("number x")), 0)
        self.assertEqual(state1_3.getAtom(Atom.fromString("number y")), 40)
        self.assertEqual(state1_3.satisfies(self.action1.preconditions), False)
        self.assertEqual(state1_3.satisfies(self.action2.preconditions), True)
        self.assertEqual(state1_3.satisfies(self.action3.preconditions), True)

        self.assertEqual(state1_3_2.getAtom(Atom.fromString("at x y")), False)
        self.assertEqual(state1_3_2.getAtom(Atom.fromString("at z w")), True)
        self.assertEqual(state1_3_2.getAtom(Atom.fromString("number x")), 10)
        self.assertEqual(state1_3_2.getAtom(Atom.fromString("number y")), 20)
        self.assertEqual(state1_3_2.satisfies(self.action1.preconditions), False)
        self.assertEqual(state1_3_2.satisfies(self.action2.preconditions), False)
        self.assertEqual(state1_3_2.satisfies(self.action3.preconditions), True)

        self.assertEqual(state0.satisfies(self.actionAnd.preconditions), False)
        self.assertEqual(state0.satisfies(self.actionOr.preconditions), True)

        f = Formula.fromString("(and (or (at x y) (at z w)) (or (>= (number x) 5) (<= (number y) 0)))")
        self.assertEqual(state0.satisfies(f), True)


if __name__ == '__main__':
    unittest.main()
