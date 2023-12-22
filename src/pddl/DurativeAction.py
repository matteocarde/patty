from __future__ import annotations

from typing import Dict, List
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.Operation import Operation
from src.pddl.Parameter import Parameter
from src.pddl.Preconditions import Preconditions
from src.pddl.Predicate import Predicate
from src.pddl.TimePredicate import TimePredicate, TimePredicateType
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser as p

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.pddl.SnapAction import SnapAction


class DurativeAction(Operation):
    name: str

    def __init__(self):
        super().__init__()
        self.name: str
        self.parameters = list()
        self.duration: Predicate

    @classmethod
    def fromNode(cls, node: p.DurativeActionContext, types: Dict[str, Type]):
        da = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                da.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                da.setParameters(child.getChild(1), types)
            elif isinstance(child, p.OpDurationContext):
                da.__setDuration(child.getChild(1))
            elif isinstance(child, p.OpDurativeConditionContext):
                da.addPreconditions(child)
            elif isinstance(child, p.OpDurativeEffectContext):
                da.addEffects(child)
        return da

    def __setDuration(self, node: p.DurationAssignmentContext):
        op = node.op.getChild(0)
        if isinstance(op, p.OperationContext):
            self.duration = BinaryPredicate.fromNode(op)
        elif isinstance(op, p.PositiveLiteralContext):
            self.duration = Literal.fromNode(op)
        elif isinstance(op, p.ConstantContext):
            self.duration = Constant.fromNode(op)

    def ground(self, problem, delta=1) -> List[DurativeAction]:
        groundOps: List = []
        toGroundOps = self.getGroundedOperations(problem, delta=delta)
        for op in toGroundOps:
            op.__class__ = DurativeAction
            groundOps.append(op)
        return groundOps
