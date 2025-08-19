import unittest
from unittest import TestCase

from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Problem import Problem
from src.search.AStarSearchMax import AStarSearchMax
from src.search.BDCSearch import BDCSearch
from src.search.GDSearch import GDSearch
from src.search.JairSearch import JairSearch
from src.utils.Arguments import Arguments
from z3 import *


class TestZ3(TestCase):

    def setUp(self) -> None:
        pass

    def test_solve(self):
        print(z3.get_full_version())
        x, y, z = Reals('x y z')

        s = Optimize()
        s.set("opt.priority", "lex")
        s.add_soft(x < 30)
        s.add_soft(y > 60)
        s.add_soft(z < 100)
        h = s.minimize(x+y+z)

        def onImprovedModel(model):
            print("Improved:", model)

        s.set_on_model(onImprovedModel)

        print(s.check())
        print(s.model())
        print(s.objectives())
        print(h.value())


if __name__ == '__main__':
    unittest.main()
