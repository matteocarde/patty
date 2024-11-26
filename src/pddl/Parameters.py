from typing import List, Dict

from src.pddl.Parameter import Parameter
from src.pddl.Problem import Problem
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser


class Parameters(List[Parameter]):
    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.ParametersContext, types: Dict[str, Type]):
        p = cls()
        for child in node.children:
            if not isinstance(child, pddlParser.TypedAtomParameterContext):
                continue
            varNames = []
            varType = types[child.atomsType.getText().lower()]

            for x in child.children:
                if isinstance(x, pddlParser.LiftedAtomParameterContext):
                    varNames.append(x.getText())

            for name in varNames:
                p.append(Parameter(name, varType))
        return p

    def getCombinations(self, problem: Problem):
        subs: List[List[str]] = list()
        for parameter in self:
            pSubs = list()
            for childType in parameter.type.getMeAndMyChildren():
                if childType.name not in problem.objectsByType:
                    continue
                pSubs += problem.objectsByType[childType.name]
            subs.append(pSubs)

        return subs  # list(itertools.product(*subs))
