import unittest
from unittest import TestCase

from BinaryPredicate import BinaryPredicate
from MooreInterval import MooreInterval
from Problem import Problem

PROBLEM = """
(define (problem instance_4_1_1)
    (:domain mt-plant-watering-constrained)
    (:objects
        agent1 - agent
        tap1 - tap
        plant1 - plant
    )

    (:init
        (= (max_int) 20)
        (boolean)
    )

    (:goal (and 
        (boolean)
        (= (poured plant1) 4)
        (= (total_poured) (poured plant1) )
    )

    (:metric minimize (+ (* 4 (poured plant2)) (* 5 (poured plant2))))
)

"""

PROBLEM_2 = """
(define (problem instance_4_1_1)
    (:domain mt-plant-watering-constrained)
    (:objects
        agent1 - agent
        tap1 - tap
        plant1 - plant
    )

    (:init
        (= (max_int) 20)
        (boolean)
    )

    (:goal (and 
        (boolean)
        (= (poured plant1) 4)
        (= (total_poured) (poured plant1) )
    )

    (:metric minimize (poured plant2))
)

"""


class TestProblem(TestCase):

    def setUp(self) -> None:
        self.problem1 = Problem.fromString(PROBLEM)
        self.problem2 = Problem.fromString(PROBLEM_2)
        pass

    def test_metric(self):
        self.assertEqual(self.problem1.metric,
                         BinaryPredicate.fromOperationString("(+ (* 4 (poured plant2)) (* 5 (poured plant2)))"))


if __name__ == '__main__':
    unittest.main()
