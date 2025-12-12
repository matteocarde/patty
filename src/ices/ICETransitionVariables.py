from typing import Dict, List, Set

from src.ices.Happening import Happening, HappeningActionStart, HappeningEffect, HappeningCondition
from src.ices.ICEAction import ICEAction
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETask import ICETask
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable
from src.smt.expressions.FalseExpression import FalseExpression
from src.smt.expressions.ITEExpression import ITEExpression
from src.smt.expressions.TrueExpression import TrueExpression
from src.utils.TimeStat import TimeStat


class ICETransitionVariables:
    task: ICETask
    pattern: ICEPattern
    currentVariables: Dict[Atom, SMTVariable]
    nextVariables: Dict[Atom, SMTVariable]
    happeningVariables: Dict[Happening, SMTVariable]
    clockVariables: Dict[Happening, SMTVariable]
    sigmaExpressions: Dict[int, Dict[Atom, SMTExpression or float]]
    deltaExpressions: Dict[int, Dict[ICEAction, SMTExpression or float]]
    makespan: SMTVariable

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task = task
        self.pattern = pattern

        t = TimeStat.startHolder("Get current and next variables")
        self.currentVariables = self.__computeCurrentVariables()
        self.nextVariables = self.__computeNextVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get happening variables")
        self.happeningVariables = self.__computeHappeningVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get time variables")
        self.timeVariables = self.__computeTimeVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get time end variables")
        self.timeEndVariables = self.__computeTimeEndVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get dur variables")
        self.durVariables = self.__computeDurationVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get sigma expressions")
        self.sigmaExpressions = self.__computeSigmaExpressions()
        t.endHolder()
        t = TimeStat.startHolder("Get delta expressions")
        self.deltaExpressions = self.__computeDeltaExpressions()
        t.endHolder()

        self.makespan = SMTRealVariable(f"__makespan__")

        pass

    def __computeSigmaExpressions(self) -> Dict[int, Dict[Atom, SMTExpression or float]]:
        sigmas: Dict[int, Dict[Atom, SMTExpression or float]] = dict()

        sigmas[0] = dict()
        trueAtoms: Set[Atom] = set()
        for v in self.task.propVariables | self.task.numVariables:
            sigmas[0][v] = self.currentVariables[v]

        for j, h in enumerate(self.pattern):
            i = j + 1

            sigmas[i] = dict()

            if not isinstance(h, HappeningEffect):
                sigmas[i] = sigmas[i - 1]
                continue

            h_i = self.happeningVariables[h]
            for v in self.task.propVariables:
                if v in h.effect.atomsAdded:
                    sigmas[i][v] = sigmas[i - 1][v] | (h_i > 0)
                elif v in h.effect.atomsDeleted:
                    sigmas[i][v] = sigmas[i - 1][v] & (h_i.equal(0))
                else:
                    sigmas[i][v] = sigmas[i - 1][v]

            for v in self.task.numVariables:
                if v not in h.effect.atomToEffect:
                    sigmas[i][v] = sigmas[i - 1][v]
                    continue

                eff = h.effect.atomToEffect[v]
                psi = SMTExpression.fromPddl(eff.getNormalizedRhs(), sigmas[i - 1])
                if eff.isLinearIncrementNew():
                    sigmas[i][v] = sigmas[i - 1][v] + h_i * psi
                else:
                    sigmas[i][v] = ITEExpression.simplify(h_i > 0, psi, sigmas[i - 1][v])

        return sigmas

    def __computeDeltaExpressions(self) -> Dict[int, Dict[ICEAction, SMTExpression or float]]:
        deltas: Dict[int, Dict[ICEAction, SMTExpression or float]] = dict()

        deltas[0] = dict()
        trueAtoms: Set[Atom] = set()
        for b in self.task.actions:
            deltas[0][b] = 0

        h: Happening
        for j, h in enumerate(self.pattern):
            i = j + 1

            deltas[i] = dict()

            h_i = self.happeningVariables[h]

            for b in self.task.actions:
                if b == h.starting:
                    d_i = self.durVariables[h]
                    deltas[i][b] = ITEExpression.simplify(h_i > 0, d_i, deltas[i - 1][b])
                else:
                    deltas[i][b] = deltas[i - 1][b]

        return deltas

    def __computeCurrentVariables(self) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for v in self.task.propVariables:
            variables[v] = SMTBoolVariable(str(v))

        for x in self.task.numVariables:
            variables[x] = SMTRealVariable(str(x))

        return variables

    def __computeNextVariables(self) -> Dict[Atom, SMTVariable]:
        variables: Dict[Atom, SMTVariable] = dict()

        for v in self.task.propVariables:
            variables[v] = SMTBoolVariable(f"{str(v)}'")

        for x in self.task.numVariables:
            variables[x] = SMTRealVariable(f"{str(x)}'")

        return variables

    @staticmethod
    def __isSameAsPrevious(h: Happening, p: Happening) -> bool:
        if h.parent != p.parent:
            return False
        if isinstance(h, HappeningCondition) and isinstance(p, HappeningCondition):
            return h.condition.fromTime == p.condition.fromTime
        if isinstance(h, HappeningCondition) and isinstance(p, HappeningEffect):
            return h.condition.fromTime == p.effect.time
        if isinstance(h, HappeningEffect) and isinstance(p, HappeningCondition):
            return h.effect.time == p.condition.fromTime
        return False

    def __isSameAsPreviousEnd(h: Happening, p: Happening) -> bool:
        if h.parent != p.parent:
            return False
        if isinstance(h, HappeningCondition) and isinstance(p, HappeningCondition):
            return h.condition.toTime == p.condition.toTime
        return False

    def __computeHappeningVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        snapVariables: Dict[ICEAction, SMTVariable] = dict()

        h: Happening
        for i, h in enumerate(self.pattern):
            if isinstance(h.parent, ICEAction) and h.parent.isSnap:
                b = h.parent
                if h.starting:
                    snapVariables[b] = SMTIntVariable(str(h))
                variables[h] = snapVariables[b]
                continue

            if i > 0:
                p = self.pattern[i - 1]
                isSameAsPrevious = self.__isSameAsPrevious(h, p)
                if isSameAsPrevious:
                    variables[h] = variables[p]
                    continue

            variables[h] = SMTIntVariable(str(h))

        return variables

    def __computeTimeVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for i, h in enumerate(self.pattern):

            if i > 0:
                p = self.pattern[i - 1]
                isSameAsPrevious = ICETransitionVariables.__isSameAsPrevious(h, p)
                if isSameAsPrevious:
                    variables[h] = variables[p]
                    continue

            variables[h] = SMTRealVariable(f"t_{str(h)}")

        return variables

    def __computeTimeEndVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        snapVariables: Dict[ICEAction, SMTVariable] = dict()

        for i, h in enumerate(self.pattern):
            if isinstance(h, HappeningCondition):

                if h.condition.fromTime == h.condition.toTime:
                    variables[h] = self.timeVariables[h]
                    continue

                # if isinstance(h.parent, ICEAction) and h.parent.isSnap:
                #     b = h.parent
                #     if h.starting:
                #         snapVariables[b] = SMTRealVariable(f"t_{str(h)}_end")
                #     variables[h] = snapVariables[b]
                #     continue

                if i > 0:
                    p = self.pattern[i - 1]
                    isSameAsPrevious = ICETransitionVariables.__isSameAsPreviousEnd(h, p)
                    if isSameAsPrevious:
                        variables[h] = variables[p]
                        continue

                variables[h] = SMTRealVariable(f"t_{str(h)}_end")

        return variables

    def __computeDurationVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for h in self.pattern:
            if h.starting:
                variables[h] = SMTRealVariable(f"d_{str(h)}")

        return variables
