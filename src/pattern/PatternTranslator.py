import copy

from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate, BinaryPredicateType
from src.pddl.Constant import Constant
from src.pddl.Domain import Domain
from src.pddl.Effects import Effects
from src.pddl.Literal import Literal
from src.pddl.Preconditions import Preconditions
from src.pddl.Problem import Problem
from src.pddl.TypedPredicate import TypedPredicate
from src.plan.Pattern import Pattern


class PatternTranslator:

    def __init__(self, domain: Domain, problem: Problem):
        self.domain: Domain = domain
        self.problem: Problem = problem

        self.gDomain = self.domain.ground(self.problem)

        self.pattern = Pattern.fromARPG(self.gDomain)

        self.costLit = Literal.fromPositiveString("(cost_pattern)")
        self.costTP = TypedPredicate()
        self.costTP.name = "cost_pattern"
        self.costTP.atom = self.costLit.atom
        self.costTP.parameters = []

        self.costIncr = BinaryPredicate()
        self.costIncr.lhs = self.costLit
        self.costIncr.rhs = Constant(1)
        self.costIncr.operator = "increase"
        self.costIncr.type = BinaryPredicateType.MODIFICATION

        pass

    @staticmethod
    def getTurnLiteral(action: Action, sign: str = "+") -> Literal:
        atom = Atom.fromProperties(f"turn_{action.name}", [p.name for p in action.parameters])
        return Literal.fromAtom(atom, sign)

    @staticmethod
    def getTurnTypedPredicate(action: Action) -> TypedPredicate:
        name = f"turn_{action.name}"
        atom = Atom.fromProperties(name, [p.name for p in action.parameters])
        t = TypedPredicate()
        t.atom = atom
        t.name = name
        t.parameters = action.parameters
        return t

    @staticmethod
    def getActionToMovePattern(fAction: Action, tAction: Action) -> Action:

        fName = fAction.name.replace(" ", "_")
        tName = tAction.name.replace(" ", "_")

        name = f"movecursor_{fName}_{tName}"
        pre = Preconditions()
        pre.addPrecondition(PatternTranslator.getTurnLiteral(fAction, "+"))
        eff = Effects()
        eff.addEffect(PatternTranslator.getTurnLiteral(tAction, "+"))
        eff.addEffect(PatternTranslator.getTurnLiteral(fAction, "-"))
        a = Action.fromProperties(name, pre, eff, "notnow")

        return a

    def getTranslatedDomain(self) -> Domain:
        tDomain = copy.deepcopy(self.domain)

        tDomain.constants = copy.deepcopy(self.problem.objectsByType)

        tDomain.functions.add(self.costTP)

        for action in tDomain.actions:
            lit: Literal = PatternTranslator.getTurnLiteral(action)
            action.preconditions.addPrecondition(lit)
            action.effects.addEffect(self.costIncr)
            p: TypedPredicate = PatternTranslator.getTurnTypedPredicate(action)
            tDomain.predicates.add(p)

        couples = [(self.pattern[i], self.pattern[i + 1]) for i in range(0, len(self.pattern) - 2)]
        couples.append((self.pattern[-2], self.pattern[0]))
        for (f, t) in couples:
            action = PatternTranslator.getActionToMovePattern(f, t)
            tDomain.actions.add(action)

        return tDomain

    def getTranslatedProblem(self) -> Problem:
        tProblem = copy.deepcopy(self.problem)
        firstAction = self.pattern[0]
        tProblem.init.addPropositionalAssignment(PatternTranslator.getTurnLiteral(firstAction))
        tProblem.init.addNumericAssignment(self.costLit, 0)

        tProblem.metric = self.costLit

        return tProblem
