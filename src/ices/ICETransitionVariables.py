from typing import Dict

from src.ices.Happening import Happening, HappeningActionStart
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETask import ICETask
from src.pddl.Atom import Atom
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class ICETransitionVariables:
    task: ICETask
    pattern: ICEPattern
    valueVariables: Dict[Atom, SMTVariable]
    happeningVariables: Dict[Happening, SMTVariable]
    clockVariables: Dict[Happening, SMTVariable]
    makespan: SMTVariable

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task = task
        self.pattern = pattern
        self.stateVariables = self.__computeStateVariables()
        self.nextVariables = self.__computeNextVariables()
        self.happeningVariables = self.__computeHappeningVariables()
        self.timeVariables = self.__computeTimeVariables()
        self.durVariables = self.__computeDurationVariables()

        self.makespan = SMTRealVariable(f"__makespan__")

        pass

    def __computeStateVariables(self) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.task.numVariables:
            variables[atom] = SMTRealVariable(f"{atom}_0")
        for atom in self.task.propVariables:
            variables[atom] = SMTBoolVariable(f"{atom}_0")

        return variables

    def __computeNextVariables(self) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for atom in self.task.numVariables:
            variables[atom] = SMTRealVariable(f"{atom}_1")
        for atom in self.task.propVariables:
            variables[atom] = SMTBoolVariable(f"{atom}_1")

        return variables

    def __computeHappeningVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for h in self.pattern:
            variables[h] = SMTIntVariable(str(h))

        return variables

    def __computeTimeVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for h in self.pattern:
            variables[h] = SMTRealVariable(f"t_{str(h)}")

        return variables

    def __computeDurationVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for h in self.pattern:
            if isinstance(h, HappeningActionStart):
                variables[h] = SMTRealVariable(f"d_{str(h)}")

        return variables
