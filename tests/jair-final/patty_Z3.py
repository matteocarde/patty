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
        s.add(x > y)
        s.add(y > z)
        s.add(z > 0)
        s.add_soft(x > y + 1)
        h = s.minimize(x)
        print(s.check())
        print(s.model())
        print(h.value())



if __name__ == '__main__':
    unittest.main()
