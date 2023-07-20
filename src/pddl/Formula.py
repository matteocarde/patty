from __future__ import annotations

import copy

from itertools import chain
from typing import Dict, Set

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.pddl.Predicate import Predicate
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Formula:
    type: str
    conditions: [Formula or Predicate]

    def __init__(self):
        self.type = "AND"
        self.conditions = list()

    def __deepcopy__(self, m=None) -> Formula:
        m = {} if m is None else m
        f = Formula()
        f.type = self.type
        f.conditions = copy.deepcopy(self.conditions, m)
        return f

    @classmethod
    def fromNode(cls, node) -> Formula:
        formula = cls()

        if isinstance(node.getChild(0), p.EmptyPreconditionContext):
            return formula

        clauses = []

        formulaComponent = node.getChild(0) if type(node) == p.PreconditionsContext else node
        formula.type = "OR" if type(formulaComponent) == p.OrClauseContext else "AND"
        if isinstance(formulaComponent, p.BooleanLiteralContext):
            clauses.append(formulaComponent)
        elif type(formulaComponent) in {p.ComparationContext, p.NegatedComparationContext}:
            clauses.append(formulaComponent)
        elif type(formulaComponent) in {p.AndClauseContext, p.OrClauseContext}:
            clauses = formulaComponent.children
        else:
            raise Exception("Unexpected clause in precondition")

        for clause in clauses:
            if type(clause) in {p.AndClauseContext, p.OrClauseContext}:
                formula.conditions.append(Formula.fromNode(clause))
            elif isinstance(clause, p.BooleanLiteralContext):
                formula.conditions.append(Literal.fromNode(clause.getChild(0)))
            elif type(clause) in {p.ComparationContext, p.NegatedComparationContext}:
                formula.conditions.append(BinaryPredicate.fromNode(clause))

        return formula

    @classmethod
    def fromString(cls, string: str) -> Formula:
        return Formula.fromNode(Utilities.getParseTree(string).preconditions())

    def ground(self, subs: Dict[str, str]):
        gFormula = Formula()
        gFormula.type = self.type
        for condition in self.conditions:
            gFormula.conditions.append(condition.ground(subs))
        return gFormula

    def getFunctions(self) -> Set[Atom]:
        functions = set()
        for c in self.conditions:
            if isinstance(c, Literal):
                continue
            functions |= c.getFunctions()
        return functions

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.conditions]))

    def substitute(self, subs: Dict[Atom, float], default=None) -> Formula:
        x = Formula()
        x.type = self.type
        x.conditions = [c.substitute(subs, default) for c in self.conditions]
        return x

    def canHappen(self, subs: Dict[Atom, float], default=None) -> bool:
        canHappen = [c.canHappen(subs, default) for c in self.conditions]
        return all(canHappen)

    def replace(self, atom: Atom, w: BinaryPredicate) -> Formula:
        f = Formula()
        f.type = f.type
        for el in self.conditions:
            f.conditions.append(el.replace(atom, w))
        return f

    def __iter__(self):
        return iter(self.conditions)

    def __str__(self):
        return f"({self.type.lower()} {' '.join([str(c) for c in self.conditions])})"

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return str(self.conditions)

    def __add__(self, other):
        c = Formula()
        c.conditions = self.conditions + other
        return c

    def __len__(self):
        return len(self.conditions)

    def toLatex(self):
        if not self.conditions:
            return r"\emptyset"
        symbol = r"\wedge" if self.type == "AND" else r"\vee"
        return "(" + symbol.join([c.toLatex() for c in self.conditions]) + ")"
        pass

    def containsOrs(self):
        if self.type == "OR":
            return True
        for c in self.conditions:
            if isinstance(c, Formula) and c.containsOrs():
                return True
        return False

    def addClause(self, clause: Formula or Predicate):
        self.conditions.append(clause)
