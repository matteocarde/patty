from __future__ import annotations

import copy

import itertools
from typing import Dict, List, Set

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.OperationType import OperationType
from src.pddl.Parameter import Parameter
from src.pddl.Preconditions import Preconditions
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser as p


class Operation:
    name: str
    valName: str
    planName: str
    parameters: List[Parameter]
    preconditions: Preconditions
    effects: Effects

    def __init__(self):
        self.name: str = ""
        self.valName: str = ""
        self.parameters = list()
        self.preconditions = Preconditions()
        self.effects = Effects()
        self.functions = set()
        self.predicates = set()
        self.preB = set()
        self.addList = set()
        self.delList = set()
        self.assList = set()
        self.incrList = set()
        self.decrList = set()
        self.influencedAtoms = set()
        self.increases = dict()
        self.decreases = dict()
        self.assignments = dict()
        self.linearizationOf = self
        self.linearizationTimes = 1
        self.isFake = False

    def __deepcopy__(self, m=None) -> Operation:
        m = {} if m is None else m

        a = Operation()
        a.name = self.name
        a.valName = self.valName
        a.parameters = copy.deepcopy(self.parameters, m)
        a.preconditions = copy.deepcopy(self.preconditions, m)
        a.effects = copy.deepcopy(self.effects, m)
        a.functions = copy.deepcopy(self.functions, m)
        a.predicates = copy.deepcopy(self.predicates, m)
        a.preB = copy.deepcopy(self.preB, m)
        a.addList = copy.deepcopy(self.addList, m)
        a.delList = copy.deepcopy(self.delList, m)
        a.assList = copy.deepcopy(self.assList, m)
        a.incrList = copy.deepcopy(self.incrList, m)
        a.decrList = copy.deepcopy(self.decrList, m)
        a.influencedAtoms = copy.deepcopy(self.influencedAtoms, m)
        a.increases = copy.deepcopy(self.increases, m)
        a.decreases = copy.deepcopy(self.decreases, m)
        a.assignments = copy.deepcopy(self.assignments, m)
        a.linearizationOf = self.linearizationOf
        a.linearizationTimes = self.linearizationTimes

        return a

    @classmethod
    def fromNode(cls, node: p.ActionContext or p.EventContext or p.ProcessContext, types: Dict[str, Type]):
        operation = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                operation.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                operation.__setParameters(child.getChild(1), types)
            elif isinstance(child, p.OpPreconditionContext):
                operation.__addPreconditions(child)
            elif isinstance(child, p.OpEffectContext):
                operation.__addEffects(child)

        operation.__cacheLists()
        return operation

    @classmethod
    def fromProperties(cls, name: str, preconditions: Preconditions, effects: Effects, planName: str):
        operation = cls()
        operation.name = name
        operation.preconditions = preconditions
        operation.effects = effects
        operation.planName = planName
        operation.__cacheLists()
        return operation

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

    def __addPreconditions(self, node: p.OpPreconditionContext):
        self.preconditions = Preconditions.fromNode(node.getChild(1))

    def __addEffects(self, node: p.OpEffectContext):
        self.effects = Effects.fromNode(node.getChild(1))

    def getCombinations(self, problem: Problem) -> List[Dict[str, str]]:
        subs: List[List[str]] = list()
        for parameter in self.parameters:
            pSubs = list()
            for childType in parameter.type.getMeAndMyChildren():
                if childType.name not in problem.objectsByType:
                    continue
                pSubs += problem.objectsByType[childType.name]
            subs.append(pSubs)

        combinations: List[Dict[str, str]] = list()
        for sub in itertools.product(*subs):
            comb: Dict[str, str] = dict()
            for i, parameter in enumerate(self.parameters):
                comb[parameter.name] = sub[i]
            combinations.append(comb)

        return combinations

    def getGroundedOperations(self, problem, isPredicateStatic: Dict[str, bool]):
        combinations: List[Dict[str, str]] = self.getCombinations(problem)

        validCombinations: List[Dict[str, str]] = []

        for sub in combinations:
            if self.preconditions.canHappenLifted(sub, problem, isPredicateStatic):
                validCombinations.append(sub)

        gOperations = []
        for subs in validCombinations:
            name = self.__getGroundedName(subs)
            preconditions = self.preconditions.ground(subs)
            effects = self.effects.ground(subs)
            planName = self.__getGroundedPlanName(subs)
            operation: Operation = Operation.fromProperties(name, preconditions, effects, planName)
            gOperations.append(operation)
        return gOperations

    def __getGroundedName(self, sub: Dict[str, str]) -> str:
        parts = [self.name] + [c[1] for c in sub.items()]
        return " ".join(parts)

    def __getGroundedPlanName(self, sub: Dict[str, str]):
        parts = [self.name] + [c[1] for c in sub.items()]
        return f"({'_'.join(parts)})"

    @property
    def type(self) -> OperationType:
        raise NotImplemented()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __getFunctions(self) -> Set[Atom]:
        return self.preconditions.getFunctions() | self.effects.getFunctions()

    def __getPredicates(self) -> Set[Atom]:
        return self.preconditions.getPredicates() | self.effects.getPredicates()

    def __getModifiedPredicates(self, sign: str = None) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.effects:
            if not isinstance(c, Literal) or (sign is not None and c.sign != sign):
                continue
            atomList = atomList | c.getPredicates()
        return atomList

    def __getPreconditionAtoms(self, preconditionClass) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.preconditions:
            if not isinstance(c, preconditionClass):
                continue
            atomList = atomList | {c.getAtom()}
        return atomList

    def __getModifiedFunctions(self, operator: str = None) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.effects:
            if not isinstance(c, BinaryPredicate) or (operator is not None and c.operator != operator):
                continue
            atomList = atomList | {c.getAtom()}
        return atomList

    def __getModificationOperations(self, operator: str = None) -> Dict[Atom, Predicate]:
        modification = dict()
        for c in self.effects:
            if not isinstance(c, BinaryPredicate) or (operator is not None and c.operator != operator):
                continue
            modification[c.getAtom()] = c.rhs
        return modification

    def __getPreB(self) -> Set[Atom]:
        return self.__getPreconditionAtoms(Literal)

    def __getAddList(self) -> Set[Atom]:
        return self.__getModifiedPredicates("+")

    def __getDelList(self) -> Set[Atom]:
        return self.__getModifiedPredicates("-")

    def __getAssList(self) -> Set[Atom]:
        return self.__getModifiedFunctions("assign")

    def __getIncrList(self) -> Set[Atom]:
        return self.__getModifiedFunctions("increase")

    def __getDecrList(self) -> Set[Atom]:
        return self.__getModifiedFunctions("decrease")

    def __getInfluencedAtoms(self):
        return self.__getModifiedPredicates() | self.__getModifiedFunctions()

    def __getIncreases(self) -> Dict[Atom, Predicate]:
        return self.__getModificationOperations("increase")

    def __getDecreases(self) -> Dict[Atom, Predicate]:
        return self.__getModificationOperations("decrease")

    def __getAssignments(self) -> Dict[Atom, Predicate]:
        return self.__getModificationOperations("assign")

    def getFunctions(self) -> Set[Atom]:
        return self.functions

    def getPredicates(self) -> Set[Atom]:
        return self.predicates

    def getPreB(self) -> Set[Atom]:
        return self.preB

    def getAddList(self) -> Set[Atom]:
        return self.addList

    def getDelList(self) -> Set[Atom]:
        return self.delList

    def getAssList(self) -> Set[Atom]:
        return self.assList

    def getIncrList(self) -> Set[Atom]:
        return self.incrList

    def getDecrList(self) -> Set[Atom]:
        return self.decrList

    def getInfluencedAtoms(self):
        return self.influencedAtoms

    def getIncreases(self) -> Dict[Atom, Predicate]:
        return self.increases

    def getDecreases(self) -> Dict[Atom, Predicate]:
        return self.decreases

    def getAssignments(self) -> Dict[Atom, Predicate]:
        return self.assignments

    def couldBeRepeated(self) -> bool:
        return len(self.getIncrList() | self.getDecrList()) > 0 and \
            len(self.getPreB().intersection(self.getAddList() | self.getDelList())) == 0

    def substitute(self, sub: Dict[Atom, float], default=None) -> Operation:
        raise NotImplemented()

    def __cacheLists(self):
        self.functions = self.__getFunctions()
        self.predicates = self.__getPredicates()
        self.preB = self.__getPreB()
        self.addList = self.__getAddList()
        self.delList = self.__getDelList()
        self.assList = self.__getAssList()
        self.incrList = self.__getIncrList()
        self.decrList = self.__getDecrList()
        self.influencedAtoms = self.__getInfluencedAtoms()
        self.increases = self.__getIncreases()
        self.decreases = self.__getDecreases()
        self.assignments = self.__getAssignments()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: Operation):
        if not isinstance(other, Operation):
            return False
        return self.name == other.name

    def nameToLatex(self):
        return self.planName.replace("_", r"\_")

    def hasNonSimpleLinearIncrement(self, encoding=""):
        if encoding == "non-linear":
            return False
        for e in self.effects:
            if isinstance(e, BinaryPredicate) and e.type == BinaryPredicateType.MODIFICATION and \
                    len(e.rhs.getFunctions()) > 0:
                return True
        return False

    def getBinaryOperation(self, i: int) -> Operation:
        o_i = copy.deepcopy(self)

        replaceWith: Dict[Atom, BinaryPredicate] = dict()
        replaceWithSign: Dict[Atom, int] = dict()

        effs = Effects()

        for eff in self.effects:
            if not isinstance(eff, BinaryPredicate) or not eff.isLinearIncrement():
                effs.addEffect(copy.deepcopy(eff))
                continue
            binEff = copy.deepcopy(eff)
            binEff.rhs = 2 ** i * binEff.rhs
            preFormula = (2 ** i - 1) * copy.deepcopy(eff.rhs)
            replaceWith[eff.getAtom()] = preFormula
            replaceWithSign[eff.getAtom()] = +1 if eff.operator == "increase" else -1
            effs.addEffect(binEff)

        o_i.effects = effs

        if self.preconditions.containsOrs():
            raise Exception("""At the moment I cannot deal with ORs in preconditions when linearizing linear effects. 
                Is trivial but requires some work. Please contact us.""")

        for pre in self.preconditions:
            toChange = set(replaceWith.keys()).intersection(pre.getFunctions())
            for v in toChange:
                vl = Literal.fromAtom(v, "+")
                formula = vl + replaceWith[v] if replaceWithSign[v] > 0 else vl - replaceWith[v]
                o_i.preconditions.addClause(pre.replace(v, formula))

        o_i.name = f"{o_i.name}_{2 ** i}"
        return o_i
