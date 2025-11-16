import unittest
from unittest import TestCase

import unified_planning.model
from unified_planning.engines import CompilationKind
from unified_planning.io import ANMLReader
from unified_planning.shortcuts import Compiler

from src.ices.ICETask import ICETask


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
        reader = ANMLReader()

        anml = reader.parse_problem([self.domainFile, self.problemFile])
        with Compiler(problem_kind=anml.kind, compilation_kind=CompilationKind.GROUNDING) as grounder:
            grounding_result = grounder.compile(anml, CompilationKind.GROUNDING)
            groundAnml = grounding_result.problem

        icetask: ICETask = ICETask.fromUnifiedPlanning(groundAnml)
        self.assertIsInstance(icetask, ICETask)

    pass


if __name__ == '__main__':
    unittest.main()
