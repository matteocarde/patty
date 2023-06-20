from unittest import TestCase

import copy
import unittest

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Effects import Effects
from src.pddl.Preconditions import Preconditions
from src.pddl.Problem import Problem
from src.pddl.Type import Type

ACTION1 = """
(:action exch
    :parameters ()
    :precondition (and
      (p)
      (>= (qL) (q))
      (>= (qR) (* -1 (q)))
    )
    :effect (and
      (decrease (qL) (q))
      (increase (qR) (q))
    )
  )
"""


class TestAction(TestCase):

    def setUp(self) -> None:
        self.action = Action.fromString(ACTION1, dict())
        pass

    def test_shouldLinearize(self):
        self.assertTrue(self.action.hasNonSimpleLinearIncrement())

        linearize = self.action.getBinaryOperation(3)
        self.assertIsInstance(linearize, Action)




if __name__ == '__main__':
    unittest.main()
