from src.ices.ICEAction import ICEAction
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect


class Happening:

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)


class HappeningAction(Happening):
    action: ICEAction

    def __init__(self, action: ICEAction):
        super().__init__()
        self.action = action


class HappeningActionStart(HappeningAction):

    def __init__(self, action: ICEAction):
        super().__init__(action)

    def __str__(self):
        return f"{self.action.name}-START"

    def __repr__(self):
        return str(self)


class HappeningActionEnd(HappeningAction):

    def __init__(self, action: ICEAction):
        super().__init__(action)

    def __str__(self):
        return f"{self.action.name}-END"


class HappeningCondition(Happening):
    condition: IntermediateCondition

    def __init__(self, condition: IntermediateCondition):
        super().__init__()
        self.condition = condition


class HappeningConditionStart(HappeningCondition):

    def __init__(self, condition: IntermediateCondition):
        super().__init__(condition)

    def __str__(self):
        return f"{self.condition}-START"


class HappeningConditionEnd(HappeningCondition):

    def __init__(self, condition: IntermediateCondition):
        super().__init__(condition)

    def __str__(self):
        return f"{self.condition}-END"


class HappeningEffect(Happening):
    effect: IntermediateEffect

    def __init__(self, effect: IntermediateEffect):
        super().__init__()
        self.effect = effect

    def __str__(self):
        return f"{self.effect}"
