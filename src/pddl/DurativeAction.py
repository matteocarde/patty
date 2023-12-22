from typing import Dict, List

from src.pddl.Action import Action
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.Parameter import Parameter
from src.pddl.Preconditions import Preconditions
from src.pddl.Predicate import Predicate
from src.pddl.TimePredicate import TimePredicate
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser as p


class DurativeAction:

    def __init__(self):
        self.name: str
        self.parameters = list()
        self.duration: BinaryPredicate
        self.timedPreconditions: List[TimePredicate] = list()
        self.timedEffects: List[TimePredicate] = list()

    @classmethod
    def fromNode(cls, node: p.DurativeActionContext, types: Dict[str, Type]):
        da = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                da.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                da.__setParameters(child.getChild(1), types)
            elif isinstance(child, p.OpDurationContext):
                da.__setDuration(child.getChild(1))
            elif isinstance(child, p.OpDurativeConditionContext):
                da.__addPreconditions(child)
            elif isinstance(child, p.OpDurativeEffectContext):
                da.__addEffects(child)
        return da

    def __setDuration(self, node: p.DurationAssignmentContext):
        op = node.op.getChild(0)
        if isinstance(op, p.OperationContext):
            self.duration = BinaryPredicate.fromNode(op)
        elif isinstance(op, p.PositiveLiteralContext):
            self.duration = Literal.fromNode(op)
        elif isinstance(op, p.ConstantContext):
            self.duration = Constant.fromNode(op)

    def __addPreconditions(self, node: p.OpDurativeConditionContext):

        child = node.c.getChild(0)
        if isinstance(child, p.EmptyPreconditionContext):
            return

        if type(child) in {p.AtStartPreContext, p.AtEndPreContext, p.OverAllPreContext}:
            self.timedPreconditions.append(TimePredicate.fromNode(child))
        elif isinstance(child, p.AndDurClauseContext):
            for pre in child.children:
                if type(pre) in {p.AtStartPreContext, p.AtEndPreContext, p.OverAllPreContext}:
                    self.timedPreconditions.append(TimePredicate.fromNode(pre))

    def __addEffects(self, node: p.OpDurativeEffectContext):
        eff = node.e.getChild(0)
        if isinstance(eff, p.DurativeEffectContext):
            self.timedEffects.append(TimePredicate.fromNode(eff.getChild(0)))
        elif isinstance(eff, p.AndDurativeEffectContext):
            for c in eff.children:
                if isinstance(c, p.DurativeEffectContext):
                    self.timedEffects.append(TimePredicate.fromNode(c.getChild(0)))

        pass

    def __setParameters(self, node: p.ParametersContext, types: Dict[str, Type]):
        for child in node.children:
            if not isinstance(child, p.TypedAtomParameterContext):
                continue
            varNames = []
            varType = types[child.atomsType.getText()]

            for x in child.children:
                if isinstance(x, p.LiftedAtomParameterContext):
                    varNames.append(x.getText())

            for name in varNames:
                self.parameters.append(Parameter(name, varType))
