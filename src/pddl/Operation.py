from __future__ import annotations

import copy
import itertools
from typing import Dict, List, Set, Tuple

from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.ConditionalEffect import ConditionalEffect
from src.pddl.Constant import Constant
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.OperationType import OperationType
from src.pddl.Parameter import Parameter
from src.pddl.Parameters import Parameters
from src.pddl.Preconditions import Preconditions
from src.pddl.Predicate import Predicate
from src.pddl.Problem import Problem
from src.pddl.Type import Type
from src.pddl.grammar.pddlParser import pddlParser as p


class Operation:
    name: str
    valName: str
    planName: str
    parameters: Parameters
    duration: Predicate
    preconditions: Preconditions
    effects: Effects
    __hash: int
    lifted: Operation or None

    def __init__(self):
        self.name: str = ""
        self.valName: str = ""
        self.parameters = Parameters()
        self.duration: Predicate = Constant(0)
        self.preconditions = Preconditions()
        self.effects = Effects()
        self.functions = set()
        self.predicates = set()
        self.preB = set()
        self.preN = set()
        self.addList = set()
        self.delList = set()
        self.assList = set()
        self.incrList = set()
        self.decrList = set()
        self.numEffList = set()
        self.influencedAtoms = set()
        self.increases = dict()
        self.decreases = dict()
        self.assignments = dict()
        self.linearizationOf = self
        self.originalName: str = ""
        self.linearizationTimes = 1
        self.__couldBeRepeated = False
        self.isFake = False
        self.lifted = None
        self.addedAtoms: Set[Atom] = set()
        self.deletedAtoms: Set[Atom] = set()
        self.deltaPlus: Dict[Atom, List[ConditionalEffect]] = dict()
        self.deltaMinus: Dict[Atom, List[ConditionalEffect]] = dict()

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
        a.preN = copy.deepcopy(self.preN, m)
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
        a.originalName = self.originalName
        a.linearizationTimes = self.linearizationTimes
        a.originalName = self.originalName
        a.duration = copy.deepcopy(self.duration)
        a.lifted = self.lifted

        a.cacheLists()

        return a

    @classmethod
    def fromNode(cls, node: p.ActionContext or p.EventContext or p.ProcessContext, types: Dict[str, Type]):
        operation = cls()
        for child in node.children:
            if isinstance(child, p.OpNameContext):
                operation.name = child.getText()
            elif isinstance(child, p.OpParametersContext):
                operation.parameters = Parameters.fromNode(child.getChild(1), types)
            elif isinstance(child, p.OpPreconditionContext):
                operation.addPreconditions(child)
            elif isinstance(child, p.OpEffectContext):
                operation.addEffects(child, types)
        operation.duration = Constant(0)

        operation.cacheLists()
        return operation

    @classmethod
    def fromProperties(cls, name: str, parameters: List[Parameter], preconditions: Preconditions, effects: Effects,
                       planName: str, duration=Predicate or None):
        operation = cls()
        operation.name = name
        operation.parameters = parameters
        operation.preconditions = preconditions
        operation.effects = effects
        operation.planName = planName
        operation.duration = duration
        operation.originalName = name
        operation.cacheLists()
        return operation

    def addPreconditions(self, node: p.OpPreconditionContext or p.OpDurativeConditionContext):
        self.preconditions = Preconditions.fromNode(node.getChild(1))

    def addEffects(self, node: p.OpEffectContext or p.OpDurativeEffectContext, types):
        self.effects = Effects.fromNode(node.getChild(1), types)

    def getSignature(self):
        params = [p.name for p in self.parameters]
        return f"{self.name}({','.join(params)})"

    def eliminateQuantifiers(self, problem: Problem) -> Operation:
        qeOperation = copy.deepcopy(self)
        qeOperation.effects = qeOperation.effects.eliminateQuantifiers(problem)

        return qeOperation

    def hasQuantifiers(self):
        return self.effects.hasQuantifiers()

    def getDynamicAtoms(self):
        return self.effects.getDynamicAtoms()

    def __getValidCombinationsSub(self, problem: Problem, item: Tuple, itemParams: List[str],
                                  downLevels: List[List[str]], paramsLeft: List[str]) -> List[Tuple]:

        if item and not self.preconditions.canHappenLiftedPartial(item, itemParams, problem):
            return []

        if not downLevels:
            return [item]

        paths: List[Tuple] = list()
        for itemDown in downLevels[0]:
            paths += self.__getValidCombinationsSub(problem,
                                                    item + tuple([itemDown]),
                                                    itemParams + [paramsLeft[0]],
                                                    downLevels[1:],
                                                    paramsLeft[1:])
        return paths

    def __getValidCombinations(self, problem, levels: List[List[str]], params: List[str]) -> List[Tuple]:
        paths: List[Tuple] = self.__getValidCombinationsSub(problem, tuple(), [], levels, params)
        return paths

    def getGroundedOperations(self, problem):
        levels: List[List[str]] = self.parameters.getCombinations(problem)

        combinations: List[Tuple]

        if self.preconditions.isDynamicLifted(problem):
            combinations = list(itertools.product(*levels))
        else:
            opParams = [p.name for p in self.parameters]
            combinations = self.__getValidCombinations(problem, levels, opParams)

        validCombinations: List[Dict[str, str]] = []
        for sub in combinations:
            validCombinations.append(dict([(p.name, sub[i]) for i, p in enumerate(self.parameters)]))

        gOperations = []
        for sub in validCombinations:
            name = self.__getGroundedName(sub)
            planName = self.__getGroundedPlanName(sub)
            preconditions = self.preconditions.ground(sub, problem)
            effects = self.effects.ground(sub, problem)
            duration = None
            if self.duration:
                duration = self.duration.ground(sub, problem)
            operation: Operation = Operation.fromProperties(name, [], preconditions, effects, planName,
                                                            duration=duration)
            operation.lifted = self
            gOperations.append(operation)
        return gOperations

    def __getGroundedName(self, sub: Dict[str, str]) -> str:
        parts = [self.name] + [str(c) for c in sub.values()]
        return " ".join(parts)

    def __getGroundedPlanName(self, sub: Dict[str, str]):
        parts = [self.name] + [str(c) for c in sub.values()]
        return f"({'_'.join(parts)})"

    @property
    def type(self) -> OperationType:
        raise NotImplemented()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __getFunctions(self) -> Set[Atom]:
        functions = self.preconditions.getFunctions() | self.effects.getFunctions()
        if self.duration and isinstance(self.duration, Predicate):
            functions |= self.duration.getFunctions()
        return functions

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

    def __getEffectFunctions(self) -> Set[Atom]:
        atomList: Set[Atom] = set()
        for c in self.effects:
            if not isinstance(c, BinaryPredicate):
                continue
            atomList |= c.getFunctions()
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

    def __getPreN(self) -> Set[Atom]:
        return self.preconditions.getFunctions()

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
        return self.__couldBeRepeated

    def substitute(self, sub: Dict[Atom, float], default=None) -> Operation:
        raise NotImplemented()

    def cacheLists(self):
        self.__hash = hash(self.name)
        self.functions = self.__getFunctions()
        self.predicates = self.__getPredicates()
        self.preB = self.__getPreB()
        self.preN = self.__getPreN()
        self.effN = self.__getEffectFunctions()
        self.addList = self.__getAddList()
        self.delList = self.__getDelList()
        self.assList = self.__getAssList()
        self.incrList = self.__getIncrList()
        self.decrList = self.__getDecrList()
        self.numEffList = self.assList | self.incrList | self.decrList
        self.effRhs = self.effN - self.numEffList
        self.influencedAtoms = self.__getInfluencedAtoms()
        self.increases = self.__getIncreases()
        self.decreases = self.__getDecreases()
        self.assignments = self.__getAssignments()
        self.__couldBeRepeated = self.__checkIfCanBeRepeated()

        self.deltaPlus: Dict[Atom, List[ConditionalEffect]] = dict()
        self.deltaMinus: Dict[Atom, List[ConditionalEffect]] = dict()
        self.addedAtoms: Set[Atom] = set()
        self.deletedAtoms: Set[Atom] = set()
        for v in self.predicates:
            self.deltaPlus.setdefault(v, list())
            self.deltaMinus.setdefault(v, list())

        if not self.hasConditionalEffects():
            for e in self.effects:
                if not isinstance(e, Literal):
                    continue
                noCondition = ConditionalEffect()
                noCondition.effects.addEffect(e)
                v = e.getAtom()
                if e.sign == "+":
                    self.deltaPlus[v].append(noCondition)
                    self.addedAtoms.add(v)
                if e.sign == "-":
                    self.deltaMinus[v].append(noCondition)
                    self.deletedAtoms.add(v)
            return

        # noCondition = ConditionalEffect()
        # newEffects = Effects()
        # for e in self.effects:
        #     if isinstance(e, ConditionalEffect):
        #         newEffects.addEffect(e)
        #         continue
        #     noCondition.effects.addEffect(e)
        # newEffects.addEffect(noCondition)
        # self.effects = newEffects

        for ce in self.effects:
            assert isinstance(ce, ConditionalEffect)
            for l in ce.effects:
                assert isinstance(l, Literal)
                v = l.getAtom()
                if l.sign == "+":
                    self.addedAtoms.add(v)
                    self.deltaPlus[v].append(ce)
                if l.sign == "-":
                    self.deletedAtoms.add(v)
                    self.deltaMinus[v].append(ce)

    def __hash__(self):
        return self.__hash

    def __checkIfCanBeRepeated(self):
        if not self.getIncrList() and not self.getDecrList():
            return False
        if self.getPreB().intersection(self.getAddList() | self.getDelList()):
            return False

        lhs = set()
        rhs = set()
        for e in self.effects:
            if not isinstance(e, BinaryPredicate):
                continue
            lhs |= {e.getAtom()}
            rhs |= e.rhs.getFunctions()

        if lhs.intersection(rhs):
            return False

        return True

    def __eq__(self, other: Operation):
        if not isinstance(other, Operation):
            return False
        return self.name == other.name

    def nameToLatex(self):
        return self.planName.replace("_", r"\_")

    def hasConditionalEffects(self):
        for eff in self.effects:
            if isinstance(eff, ConditionalEffect):
                return True
        return False

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

    def interferes(self, other: Operation) -> bool:
        return bool(self.influencedAtoms.intersection(other.preB | other.preN))

    @staticmethod
    def __isMutex(a_i: Operation, a_j: Operation) -> bool:
        # Condition 1 - Paper Temporal
        if a_i.addList.intersection(a_j.preB) or \
                a_i.delList.intersection(a_j.preB) or \
                a_i.numEffList.intersection(a_j.preN):
            # print(f"{a_i} and {a_j} are in mutex due to C1")
            return True
        # Condition 2 - Paper Temporal
        if a_i.addList.intersection(a_j.delList) or a_i.delList.intersection(a_j.addList):
            # print(f"{a_i} and {a_j} are in mutex due to C2")
            return True
        # Condition 3 - Paper Temporal
        if a_i.assList.intersection(a_j.assList) or a_i.effRhs.intersection(a_j.numEffList):
            # print(f"{a_i} and {a_j} are in mutex due to C3")
            return True

        # print(f"{a_i} and {a_j} are NOT in mutex")
        return False

    def isMutex(self, other: Operation) -> bool:
        return Operation.__isMutex(self, other) or Operation.__isMutex(other, self)

    def isSame(self, end: Operation):
        return self.originalName == end.originalName
