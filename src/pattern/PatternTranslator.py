import copy

from src.pddl.Action import Action
from src.pddl.Atom import Atom
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

        for action in tDomain.actions:
            lit: Literal = PatternTranslator.getTurnLiteral(action)
            action.preconditions.addPrecondition(lit)
            p: TypedPredicate = PatternTranslator.getTurnTypedPredicate(action)
            tDomain.predicates.add(p)

        for i in range(0, len(self.pattern) - 1):
            f = self.pattern[i]
            t = self.pattern[i + 1]
            action = PatternTranslator.getActionToMovePattern(f, t)
            tDomain.actions.add(action)

        return tDomain
