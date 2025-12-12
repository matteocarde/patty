from __future__ import annotations

from typing import List, Set, Tuple, Dict

from unified_planning.model.action import DurativeAction as UPDurativeAction

from src.pddl.Action import Action
from src.utils.Constants import EPSILON
from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect
from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.PlanRelativeTime import PlanRelativeTimeAnchor
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Constant import Constant
from src.pddl.DurativeAction import DurativeAction
from src.pddl.Literal import Literal
from src.pddl.TimePredicate import TimePredicate

START = ActionRelativeTimeAnchor.START
END = ActionRelativeTimeAnchor.END
BEGIN = PlanRelativeTimeAnchor.BEGIN
FINISH = PlanRelativeTimeAnchor.FINISH
ALPHA = PlanRelativeTimeAnchor.BEGIN
OMEGA = PlanRelativeTimeAnchor.FINISH


class ICEAction:
    name: str
    originalName: str
    icond: List[ActionIntermediateCondition]
    ieff: List[ActionIntermediateEffect]
    duration: float
    isSnap: bool

    def __init__(self):
        self.icond = list()
        self.ieff = list()
        self.isSnap = False

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        # In reality, for two actions to be equal they should also have the same icond and ieff. In the plan,
        # if they have the same name they are undistinguishable. Thus we check only the name.
        return isinstance(other, ICEAction) and self.name == other.name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if not isinstance(other, ICEAction):
            return False
        return self.name < other.name

    @classmethod
    def fromProperties(cls, name: str, duration: int) -> ICEAction:
        a = cls()
        a.name = name
        a.originalName = name
        a.duration = duration
        return a

    def isEligibleForRolling(self):
        added: Set[Atom] = set()
        deleted: Set[Atom] = set()
        lhs: Set[Atom] = set()
        rhs: Set[Atom] = set()
        hasLinearIncrements = False
        for eff in [eff for e in self.ieff for eff in e.effects]:
            if isinstance(eff, Literal):
                v = eff.getAtom()
                if eff.sign == "+":
                    added.add(v)
                if eff.sign == "-":
                    deleted.add(v)
            if isinstance(eff, BinaryPredicate):
                hasLinearIncrements = eff.isLinearIncrementNew()
                lhs.add(eff.getAtom())
                rhs.update(eff.getRHSAtoms())
                if lhs & rhs:
                    return False

        for cond in [cond for c in self.icond for cond in c.conditions]:
            if isinstance(cond, Literal):
                v = cond.getAtom()
                if cond.sign == "+" and v in deleted:
                    return False
                if cond.sign == "-" and v in added:
                    return False

        return hasLinearIncrements

    def isWellOrderable(self):
        return True

    @classmethod
    def fromSnapActionNOICEs(cls, action: Action):
        iceAction = cls()
        iceAction.name = action.name
        iceAction.originalName = action.originalName
        iceAction.duration = 1
        ic = ActionIntermediateCondition.fromProperties(START + 0, START + 0)
        iceAction.icond.append(ActionIntermediateCondition.fromProperties(END - 0, END - 0))
        # ic.conditions = action.preconditions
        for c in action.preconditions:
            ic.addCondition(c)
        iceAction.icond.append(ic)
        ie = ActionIntermediateEffect.fromProperties(START + 0)
        for e in action.effects:
            ie.addEffect(e)
        iceAction.ieff.append(ie)
        iceAction.ieff.append(ActionIntermediateEffect.fromProperties(END - 0))
        iceAction.isSnap = True
        return iceAction

    @classmethod
    def fromDurativeActionNOICEs(cls, action: DurativeAction):
        iceAction = cls()
        iceAction.name = action.name
        iceAction.originalName = action.originalName
        if not isinstance(action.duration, Constant):
            raise Exception("Cannot translate durative action w/o ICEs if duration is not constant")
        iceAction.duration = action.duration.value

        for type, pres in TimePredicate.group(action.preconditions.conditions):
            iceAction.icond.append(IntermediateCondition.fromTimePredicateSet(type, pres))

        for type, effs in TimePredicate.group(action.effects.assignments):
            iceAction.ieff.append(IntermediateEffect.fromTimePredicateSet(type, effs))

        return iceAction

    def getEpsilonB(self) -> float:
        start = ({c for c in self.icond if c.fromTime.anchor == START and c.fromTime.k == 0} |
                 {e for e in self.ieff if e.time.anchor == START and e.time.k == 0})
        end = ({c for c in self.icond if c.fromTime.anchor == END and c.fromTime.k == 0} |
               {e for e in self.ieff if e.time.anchor == END and e.time.k == 0})
        for s in start:
            for e in end:
                if s.inMutexWith(e):
                    return EPSILON
        return 0

    @classmethod
    def fromUnifiedPlanning(cls, a: UPDurativeAction, atomDict: Dict[str, Atom]) -> ICEAction:
        iceAction = cls()
        iceAction.name = a.name
        iceAction.originalName = a.name
        if a.duration.lower != a.duration.upper:
            raise NotImplementedError("I have yet to implement actions with not fixed durations")
        iceAction.duration = float(a.duration.lower.constant_value())

        hasStart = False
        hasEnd = False
        hasIntermediate = False

        for time, cond in a.conditions.items():
            ic = ActionIntermediateCondition.fromUnifiedPlanning(time, cond, atomDict)
            if ic.fromTime == START + 0:
                hasStart = True
            elif ic.fromTime == END - 0:
                hasEnd = True
            else:
                hasIntermediate = True
            iceAction.icond.append(ic)

        for time, eff in a.effects.items():
            ie = ActionIntermediateEffect.fromUnifiedPlanning(time, eff, atomDict)
            if ie.time == START + 0:
                hasStart = True
            elif ie.time == END - 0:
                hasEnd = True
            else:
                hasIntermediate = True
            iceAction.ieff.append(ie)

        iceAction.isSnap = not hasEnd and not hasIntermediate

        if not hasStart:
            ic = ActionIntermediateCondition.fake(START + 0, START + 0)
            iceAction.icond.append(ic)

        if not hasEnd:
            ic = ActionIntermediateCondition.fake(END - 0, END - 0)
            iceAction.icond.append(ic)

        return iceAction

    def toANML(self):
        lines = list()

        lines.append(f"action {self.getSafeName()}() {{")
        lines.append(f"\tduration := {self.duration};")
        for c in self.icond:
            for s in c.toANML():
                lines.append("\t" + s)
        lines.append("")
        for e in self.ieff:
            for s in e.toANML():
                lines.append("\t" + s)
        lines.append("};")

        return "\n".join(lines)

    def getSafeName(self):
        if "(" not in self.name:
            return self.name
        splitted = self.name.split("(")
        name = splitted[0]
        params = "_".join([x.strip().replace("-", "_") for x in splitted[1][:-1].split(",")])
        return f"{name}_{params}"
