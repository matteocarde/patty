from __future__ import annotations

import copy
from itertools import chain
from typing import Dict, List, cast, Iterable, Tuple

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Literal import Literal
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.TimePredicate import TimePredicate, TimePredicateType
from src.pddl.grammar.pddlParser import pddlParser
from src.pddl.grammar.pddlParser import pddlParser as p


class Effects:
    assignments: List[Literal or BinaryPredicate]

    def __init__(self):
        self.assignments = []
        pass

    def __deepcopy__(self, m=None):
        m = {} if m is None else m
        eff = copy.deepcopy(super(), m)
        eff.__class__ = Effects
        return cast(Effects, eff)

    def __add__(self, other):
        if not isinstance(other, Effects):
            raise Exception("Cannot add if other is not Effects")
        eff = Effects()
        eff.assignments = self.assignments + other.assignments
        return eff

    @classmethod
    def fromNode(cls, node: pddlParser.EffectsContext) -> Effects:

        from src.pddl.ConditionalEffect import ConditionalEffect

        effects = cls()
        nodes: [p.EffectContext] = []

        if type(node.getChild(0)) in {p.AndEffectContext, p.AndDurativeEffectContext}:
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0).getChild(0))

        for n in nodes:
            if isinstance(n, p.BooleanLiteralContext):
                effects.assignments.append(Literal.fromNode(n.getChild(0)))
            elif type(n) in {p.AtStartEffectContext, p.OverAllEffectContext, p.AtEndEffectContext}:
                effects.assignments += TimePredicate.fromNode(n)
            elif isinstance(n, p.CeContext):
                effects.assignments.append(ConditionalEffect.fromNode(n))
            else:
                effects.assignments.append(BinaryPredicate.fromNode(n))

        return effects

    def ground(self, sub: Dict[str, str], delta=1) -> Effects:
        e = Effects()
        e.assignments = [predicate.ground(sub, delta=1) for predicate in self.assignments]
        return e

    def getFunctions(self):
        return set(chain.from_iterable([c.getFunctions() for c in self.assignments if isinstance(c, BinaryPredicate)]))

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.assignments]))

    def substitute(self, sub: Dict[Atom, float], default=None):
        e = Effects()
        e.assignments = [predicate.substitute(sub, default) for predicate in self.assignments]
        return e

    def __iter__(self) -> Iterable[Literal or BinaryPredicate]:
        return iter(self.assignments)

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self.assignments)

    def __len__(self):
        return len(self.assignments)

    def toLatex(self):
        return ",".join([a.toLatex() for a in self.assignments])
        pass

    def addEffect(self, ass: Literal or BinaryPredicate):
        self.assignments.append(ass)

    @classmethod
    def __joinFollowingBinaryPredicates(cls, lhs: BinaryPredicate, bps: List[BinaryPredicate],
                                        signs: Tuple[str, str]) -> BinaryPredicate:
        first = bps[0]
        bp = BinaryPredicate()
        bp.operator = signs[0] if first.operator == "increase" else signs[1]
        bp.lhs = lhs
        bp.rhs = Effects.__joinFollowingBinaryPredicates(first.rhs, bps[1:], signs) if len(bps) > 1 else first.rhs
        bp.type = BinaryPredicateType.OPERATION

        return bp

    # (increase x (f))
    # (decrease x (g))
    # -> (increase x (- (f g))
    @classmethod
    def joinBinaryPredicates(cls, bps: List[BinaryPredicate]) -> BinaryPredicate:
        first = bps[0]
        bp = BinaryPredicate()
        bp.operator = first.operator
        bp.lhs = first.lhs
        signs = ("+", "-") if bp.operator == "increase" else ("-", "+")
        bp.rhs = Effects.__joinFollowingBinaryPredicates(first.rhs, bps[1:], signs)
        bp.type = BinaryPredicateType.MODIFICATION

        return bp

    @classmethod
    def join(cls, effects: List[Effects]) -> Effects:
        joinedEff = cls()
        rhs: Dict[Atom, List[BinaryPredicate]] = dict()
        for e in effects:
            for c in e.assignments:
                if isinstance(c, Literal):
                    joinedEff.assignments.append(c)
                elif isinstance(c, BinaryPredicate):
                    atom = c.getAtom()
                    rhs[atom] = rhs.setdefault(atom, [])
                    rhs[atom].append(c)

        for (atom, phi) in rhs.items():
            if len(phi) == 1:
                joinedEff.assignments += phi
                continue
            joinedBp = Effects.joinBinaryPredicates(phi)
            joinedEff.assignments.append(joinedBp)
            pass

        return joinedEff

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.write(f":effect (and")
        pw.increaseTab()
        for c in self.assignments:
            c.toPDDL(pw)
        pw.decreaseTab()
        pw.write(")")

    def toTimePredicate(self, type: TimePredicateType) -> Effects:
        eff = Effects()
        eff.assignments = [a.toTimePredicate(type) for a in self.assignments]
        return eff
