from typing import Dict, List

from src.ices.Happening import Happening, HappeningActionStart, HappeningEffect
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETask import ICETask
from src.pddl.Atom import Atom
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class ICETransitionVariables:
    task: ICETask
    pattern: ICEPattern
    valueVariables: Dict[Atom, SMTVariable]
    happeningVariables: Dict[Happening, SMTVariable]
    clockVariables: Dict[Happening, SMTVariable]
    sigmaExpressions: Dict[int, Dict[Atom, SMTExpression]]
    makespan: SMTVariable

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task = task
        self.pattern = pattern
        self.stateVariables = self.__computeStateVariables()
        self.nextVariables = self.__computeNextVariables()
        self.happeningVariables = self.__computeHappeningVariables()
        self.timeVariables = self.__computeTimeVariables()
        self.durVariables = self.__computeDurationVariables()
        self.sigmaExpressions = self.__computeSigmaExpressions()

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

    def __computeSigmaExpressions(self) -> Dict[int, Dict[Atom, SMTExpression]]:
        sigmas: Dict[int, Dict[Atom, SMTExpression]] = dict()

        for i, h in enumerate(self.pattern):
            sigmas[i] = dict()

            if i == 0:
                if not isinstance(h, HappeningEffect) or not h.parent == self.task.init:
                    raise Exception("The first happening in the pattern must be a PlanIntermediateEffect coming "
                                    "from the Initial Condition")

                for v in self.task.propVariables:
                    sigmas[0][v] = SMTExpression.TRUE() if v in h.effect.atomsAdded else SMTExpression.FALSE()

                for x in self.task.numVariables:
                    if not x in h.effect.atomToConstant:
                        raise Exception("The first happening in the pattern, (i.e., the plan intermediate effect in I "
                                        "happening in t=0) should define the initial value of all the variables in V_N")
                    sigmas[0][x] = SMTExpression.constant(h.effect.atomToConstant[x])

                continue

            if not isinstance(h, HappeningEffect):
                sigmas[i] = sigmas[i - 1]
                continue

            h_i = self.happeningVariables[h]
            for v in self.task.propVariables:
                if v in h.effect.atomsAdded:
                    sigmas[i][v] = sigmas[i - 1][v].OR(h_i > 0)
                elif v in h.effect.atomsDeleted:
                    sigmas[i][v] = sigmas[i - 1][v].AND(h_i == 0)
                else:
                    sigmas[i][v] = sigmas[i - 1][v]

            for v in self.task.numVariables:
                if v not in h.effect.atomToEffect:
                    sigmas[i][v] = sigmas[i - 1][v]
                    continue

                eff = h.effect.atomToEffect[v]
                psi = SMTExpression.fromPddl(eff.rhs, sigmas[i - 1])
                if eff.isLinearIncrement():
                    sigmas[i][v] = sigmas[i - 1][v] + h_i * psi
                else:
                    sigmas[i][v] = SMTExpression.ITE(h_i > 0, psi, sigmas[i - 1][v])

        return sigmas

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
