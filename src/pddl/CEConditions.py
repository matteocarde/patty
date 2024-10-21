from src.pddl.Formula import Formula
from src.pddl.Literal import Literal


class CEConditions(Formula):

    def __init__(self):
        super().__init__()

    def getPositive(self):
        return {e for e in self.conditions if isinstance(e, Literal) and e.sign == "+"}

    def getNegative(self):
        return {e for e in self.conditions if isinstance(e, Literal) and e.sign == "-"}
