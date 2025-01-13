from __future__ import annotations

import copy
from itertools import chain
from typing import Dict, Set, Tuple, List

from pyeda.boolalg.bdd import BDDVariable, BinaryDecisionDiagram, bdd2expr
from pyeda.boolalg.expr import OrOp, AndOp, Complement, Variable
from sympy import Expr

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Inequality import Inequality
from src.pddl.Literal import Literal
from src.pddl.PDDLWriter import PDDLWriter
from src.pddl.Predicate import Predicate
from src.pddl.TimePredicate import TimePredicate, TimePredicateType
from src.pddl.Utilities import Utilities
from src.pddl.grammar.pddlParser import pddlParser as p


class Formula:
    type: str
    conditions: [Formula or Predicate]

    def __init__(self):
        self.type = "AND"
        self.conditions: [Formula or Predicate] = list()

    def __deepcopy__(self, m=None) -> Formula:
        m = {} if m is None else m
        f = Formula()
        f.type = self.type
        f.conditions = copy.deepcopy(self.conditions, m)
        return f

    def __iter__(self):
        return iter(self.conditions)

    def __str__(self):
        return f"({self.type.lower()} {' '.join([str(c) for c in self.conditions])})"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self.conditions)

    def __add__(self, other):
        c = Formula()
        c.conditions = self.conditions + other
        return c

    def __len__(self):
        return len(self.conditions)

    @classmethod
    def fromNode(cls, node) -> Formula:
        formula = cls()

        if isinstance(node.getChild(0), p.EmptyPreconditionContext):
            return formula

        clauses = []

        formulaComponent = node.getChild(0) if type(node) in {p.PreconditionsContext,
                                                              p.DurativeConditionsContext} else node
        formula.type = "OR" if type(formulaComponent) == p.OrClauseContext else "AND"
        if type(formulaComponent) in {p.BooleanLiteralContext, p.InequalityContext,
                                      p.ComparationContext, p.NegatedComparationContext}:
            clauses.append(formulaComponent)
        elif type(formulaComponent) in {p.AndClauseContext, p.OrClauseContext, p.AndDurClauseContext}:
            clauses = formulaComponent.children
        elif type(formulaComponent) in {p.AtStartPreContext, p.OverAllPreContext, p.AtEndPreContext}:
            clauses.append(formulaComponent)
        else:
            raise Exception("Unexpected clause in precondition")

        for clause in clauses:
            if type(clause) in {p.AndClauseContext, p.OrClauseContext}:
                formula.conditions.append(Formula.fromNode(clause))
            elif isinstance(clause, p.BooleanLiteralContext):
                formula.conditions.append(Literal.fromNode(clause.getChild(0)))
            elif type(clause) in {p.ComparationContext, p.NegatedComparationContext}:
                formula.conditions.append(BinaryPredicate.fromNode(clause))
            elif type(clause) in {p.AtStartPreContext, p.OverAllPreContext, p.AtEndPreContext}:
                formula.conditions += TimePredicate.fromNode(clause)
            elif isinstance(clause, p.InequalityContext):
                formula.conditions.append(Inequality.fromNode(clause))

        return formula

    @classmethod
    def fromString(cls, string: str) -> Formula:
        return Formula.fromNode(Utilities.getParseTree(string).preconditions())

    def ground(self, subs: Dict[str, str], problem):
        gFormula = Formula()
        gFormula.type = self.type
        for condition in self.conditions:
            gFormula.addClause(condition.ground(subs, problem))
        return gFormula

    def getFunctions(self) -> Set[Atom]:
        functions = set()
        for c in self.conditions:
            if isinstance(c, Literal) or (isinstance(c, TimePredicate) and isinstance(c.subPredicate, Literal)):
                continue
            functions |= c.getFunctions()
        return functions

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.conditions]))

    def getLiterals(self):
        return set(chain.from_iterable([c.getLiterals() for c in self.conditions]))

    def substitute(self, subs: Dict[Atom, float], default=None) -> Formula:
        x = Formula()
        x.type = self.type
        x.conditions = []
        for c in self.conditions:
            if isinstance(c, Literal) and c.getAtom() in subs and subs[c.getAtom()]:
                continue
            x.conditions.append(c.substitute(subs, default))
        return x

    def canHappen(self, subs: Dict[Atom, float or bool], default=None) -> bool:
        for c in self.conditions:
            if not c.canHappen(subs, default):
                return False
        return True

    def __canHappenLiftedAnd(self, sub: Tuple, params: List[str], problem):
        for c in self.conditions:
            if not c.canHappenLifted(sub, params, problem):
                return False
        return True

    def __canHappenLiftedOr(self, sub: Tuple, params: List[str], problem):
        for c in self.conditions:
            if c.canHappenLifted(sub, params, problem):
                return True
        return False

    def canHappenLifted(self, sub: Tuple, params: List[str], problem):
        if self.type == "AND":
            return self.__canHappenLiftedAnd(sub, params, problem)
        if self.type == "OR":
            return self.__canHappenLiftedOr(sub, params, problem)

    def isValid(self, subs: Dict[Atom, float or bool], default=None) -> bool:
        for c in self.conditions:
            if not c.isValid(subs, default):
                return False
        return True

    def canHappenLiftedPartial(self, item: Tuple, params: List[str], problem):
        for c in self.conditions:
            if not c.canHappenLiftedPartial(item, params, problem):
                return False
        return True
        pass

    def isDynamicLifted(self, problem):
        for c in self.conditions:
            if not c.isDynamicLifted(problem):
                return False
        return True

    def replace(self, atom: Atom, w: BinaryPredicate) -> Formula:
        f = Formula()
        f.type = f.type
        for el in self.conditions:
            f.conditions.append(el.replace(atom, w))
        return f

    def expressify(self, symbols: Dict[Atom, Expr]) -> [Expr]:
        if self.type == "OR":
            raise Exception("Cannot expressify OR formula")
        return [c.expressify(symbols) for c in self.conditions]

    def toTimePredicate(self, type: TimePredicateType) -> Formula:
        f = Formula()
        f.type = self.type
        f.conditions = [c.toTimePredicate(type) for c in self.conditions]
        return f

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

    @classmethod
    def join(cls, formulas: List[Formula]) -> Formula:
        joinedF = cls()
        type = formulas[0].type
        joinedF.conditions = []
        for f in formulas:
            if type != f.type:
                raise Exception("Cannot join together preconditions of different types")
            joinedF.conditions += f.conditions
        joinedF.type = type
        return joinedF

    def toPDDL(self, pw: PDDLWriter = PDDLWriter()):
        pw.increaseTab()
        pw.write(f"({self.type.lower()}")
        pw.increaseTab()
        for c in self.conditions:
            c.toPDDL(pw)
        pw.decreaseTab()
        pw.write(")")
        pw.decreaseTab()

    def toBDD(self, vars: Dict[Atom, BDDVariable]):
        if self.type == "AND":
            f = 1
            for a in self.conditions:
                f &= a.toBDD(vars)
            return f
        if self.type == "OR":
            f = 0
            for a in self.conditions:
                f |= a.toBDD(vars)
            return f

    @classmethod
    def fromNary(cls, fType: str, expr, var2atom: Dict[str, Atom]):
        assert type(expr) in {OrOp, AndOp}
        f = cls()
        f.type = fType
        for subf in expr.xs:
            f.addClause(Formula.fromExpr(subf, var2atom))
        return f

    @classmethod
    def fromOrOp(cls, expr: OrOp, var2atom: Dict[str, Atom]):
        return Formula.fromNary("OR", expr, var2atom)

    @classmethod
    def fromAndOp(cls, expr: AndOp, var2atom: Dict[str, Atom]):
        return Formula.fromNary("AND", expr, var2atom)

    @classmethod
    def fromExpr(cls, expr, var2atom: Dict[str, Atom]):
        if isinstance(expr, OrOp):
            return Formula.fromOrOp(expr, var2atom)
        if isinstance(expr, AndOp):
            return Formula.fromAndOp(expr, var2atom)
        if isinstance(expr, Complement):
            return Literal.neg(var2atom[expr.top.name])
        if isinstance(expr, Variable):
            return Literal.pos(var2atom[expr.name])

    @staticmethod
    def fromBDD(bdd: BinaryDecisionDiagram, var2atom: Dict[str, Atom]):
        expr = bdd2expr(bdd)
        return Formula.fromOrOp(expr, var2atom)

    def simplify(self) -> Formula or Predicate:
        from src.pddl.FalsePredicate import FalsePredicate
        from src.pddl.TruePredicate import TruePredicate
        f = Formula()
        f.type = self.type
        f.conditions = []
        for c in self.conditions:
            if isinstance(c, Formula):
                c = c.simplify()
            if f.type == "AND":
                if isinstance(c, FalsePredicate):
                    return FalsePredicate()
                if isinstance(c, TruePredicate):
                    continue
            if f.type == "OR":
                if isinstance(c, TruePredicate):
                    return TruePredicate()
                if isinstance(c, FalsePredicate):
                    continue
            f.addClause(c)
        if not f.conditions:
            return TruePredicate() if self.type == "AND" else FalsePredicate()
        return f
