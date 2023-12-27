# Ciao

from __future__ import annotations

import copy
from typing import List, Dict, Set, cast

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.MooreInterval import MooreInterval
from src.pddl.Operation import Operation
from src.pddl.OperationType import OperationType
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Supporter import Supporter, SupporterEffect
from src.pddl.Type import Type
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Action(Operation):

    def __init__(self):
        self.isFake = False
        super().__init__()

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        a = copy.deepcopy(super(), m)
        a.__class__ = Action
        a.isFake = self.isFake
        return cast(Action, a)

    @classmethod
    def fromNode(cls, node: p.ActionContext, types: Dict[str, Type]):
        return super().fromNode(node, types)

    @classmethod
    def fromProperties(cls, name, parameters, preconditions, effects, planName, duration=None) -> Action:
        return super().fromProperties(name, parameters, preconditions, effects, planName, duration=duration)

    @classmethod
    def fromString(cls, string: str, types: Dict[str, Type]) -> Action:
        return cls.fromNode(Utilities.getParseTree(string).action(), types)

    @property
    def type(self):
        return OperationType.ACTION

    def ground(self, problem, delta=1) -> List[Action]:
        groundOps: List = []
        toGroundOps = self.getGroundedOperations(problem, delta=delta)
        for op in toGroundOps:
            op.__class__ = Action
            groundOps.append(op)
        return groundOps

    def getSupporters(self) -> Set[Supporter]:
        supporters: Set[Supporter] = set()

        if not self.effects.getFunctions():
            supporters.add(Supporter(self, self.preconditions, None))

        simpleIntervals: Dict[Atom, MooreInterval] = dict()
        for c in self.preconditions:
            if not isinstance(c, BinaryPredicate) or len(c.getFunctions()) > 1:
                continue
            atom = c.getFunctions().pop()
            interval = c.getIntervalFromSimpleCondition()
            if not interval:
                continue
            if atom in simpleIntervals:
                other = simpleIntervals[atom]
                simpleIntervals[atom] = other.intersecate(interval)
            else:
                simpleIntervals[atom] = interval

        for effect in self.effects:
            if not isinstance(effect, BinaryPredicate):
                continue
            if effect.operator == "assign" and isinstance(effect.rhs, Constant):
                s = Supporter(self, self.preconditions, SupporterEffect(effect.lhs.getAtom(), effect.rhs.value))
                supporters.add(s)
                continue

            # Additive Effects Transformation
            if effect.operator == "assign":
                effect = BinaryPredicate.additiveEffectsTransformation(effect)

            atom = effect.getAtom()
            interval = MooreInterval()

            if atom in simpleIntervals and len(effect.rhs.getFunctions()) == 0:
                interval = simpleIntervals[atom]
                if effect.operator == "increase":
                    interval.ub = float(interval.ub + effect.rhs.toExpression())
                if effect.operator == "decrease":
                    interval.lb = float(interval.lb - effect.rhs.toExpression())

            dir_plus = interval.ub if effect.operator == "increase" else interval.lb
            dir_minus = interval.lb if effect.operator == "increase" else interval.ub

            if not isinstance(effect.rhs, Constant) or effect.rhs.value > 0:
                pre_plus = self.preconditions + [effect.rhs > 0]
                e_plus = Supporter(self, pre_plus, SupporterEffect(atom, dir_plus))
                supporters.add(e_plus)

            if not isinstance(effect.rhs, Constant) or effect.rhs.value < 0:
                pre_minus = self.preconditions + [effect.rhs < 0]
                e_minus = Supporter(self, pre_minus, SupporterEffect(atom, dir_minus))
                supporters.add(e_minus)

        return supporters

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        name = self.name
        preconditions = self.preconditions.substitute(sub, default)
        effects = self.effects.substitute(sub, default)
        planName = self.planName
        action = Action.fromProperties(name, [], preconditions, effects, planName)
        return action

    def canHappen(self, sub: Dict[Atom, float], default=None) -> bool:
        return self.preconditions.canHappen(sub, default)

    def getBinaryOperation(self, i: int) -> Action:
        a_i = super().getBinaryOperation(i)
        a_i.__class__ = Action
        return a_i

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(f"(:action {self.name}")
        pw.increaseTab()
        parameters = " ".join([str(p) for p in self.parameters])
        pw.write(f":parameters ({parameters})")
        self.preconditions.toPDDL(pw)
        self.effects.toPDDL(pw)

        pw.decreaseTab()
        pw.write(")")
        pass

    def toSnapActions(self):

        from src.pddl.DurativeAction import DurativeAction
        dAction = DurativeAction.fromProperties(self.name, self.parameters, self.preconditions, self.effects,
                                                self.planName, duration=0)
        from src.pddl.SnapAction import SnapAction
        start = SnapAction.fromProperties(self.name + "")

        pass
