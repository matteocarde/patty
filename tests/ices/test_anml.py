import unittest
from unittest import TestCase

import unified_planning.model
from unified_planning.engines import CompilationKind
from unified_planning.io import ANMLReader
from unified_planning.shortcuts import Compiler

from src.ices.ICEEncoding import ICEEncoding
from src.ices.ICEPattern import ICEPattern
from src.ices.ICEPlan import ICEPlan
from src.ices.ICETask import ICETask
from src.smt.SMTSolver import SMTSolver


class TestAnml(TestCase):

    def setUp(self) -> None:
        self.domainFile = "./domain.anml"
        self.problemFile = "./instance_2_2.anml"
        pass

    def test_read_with_unified_planning(self):
        reader = ANMLReader()

        anml = reader.parse_problem([self.domainFile, self.problemFile])
        with Compiler(problem_kind=anml.kind, compilation_kind=CompilationKind.GROUNDING) as grounder:
            grounding_result = grounder.compile(anml, CompilationKind.GROUNDING)
            groundAnml = grounding_result.problem

        self.assertIsInstance(anml, unified_planning.model.Problem)
        self.assertIsInstance(groundAnml, unified_planning.model.Problem)

    pass

    def test_translate_into_icetask(self):
        icetask: ICETask = ICETask.fromANML(self.domainFile, self.problemFile)
        self.assertIsInstance(icetask, ICETask)

    pass

    def test_plan(self):
        task: ICETask = ICETask.fromANML(self.domainFile, self.problemFile)
        pattern = ICEPattern.fromSnap(task)
        print(pattern)
        bound = 2

        if bound > 1:
            pattern = pattern.multiply(bound)

        self.encoding: ICEEncoding = ICEEncoding(task, pattern)

        solver: SMTSolver = SMTSolver(self.encoding)

        self.solution = solver.getSolution()
        self.assertTrue(self.solution)

        plan: ICEPlan = ICEPlan.fromSMTSolution(self.encoding, self.solution)

        plan.print()

        print(f"Plan is {'valid' if plan.isValid() else 'invalid'}")

        self.assertTrue(plan.isValid())

        pass


if __name__ == '__main__':
    unittest.main()
