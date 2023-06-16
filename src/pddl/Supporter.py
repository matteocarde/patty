from src.pddl.Atom import Atom
from src.pddl.Preconditions import Preconditions


class SupporterEffect:

    def __init__(self, atom: Atom, value: float):
        self.atom = atom
        self.value = value
        pass

    def __str__(self):
        return f"[{self.atom}, {self.value}]"

    def __repr__(self):
        return str(self)


class Supporter:
    preconditions: Preconditions
    effect: SupporterEffect

    def __init__(self, originatingAction, preconditions: Preconditions, effect: SupporterEffect):
        self.preconditions = preconditions
        self.effect = effect
        self.originatingAction = originatingAction
        pass

    def isSatisfiedBy(self, state) -> bool:
        return state.satisfies(self.preconditions)

    def __str__(self):
        return f"<{self.preconditions}, {self.effect}>"

    def __repr__(self):
        return str(self)
