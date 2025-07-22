from typing import Dict, List, Set

from src.ices.ActionIntermediateCondition import ActionIntermediateCondition
from src.ices.ActionIntermediateEffect import ActionIntermediateEffect
from src.ices.ActionRelativeTime import ActionRelativeTimeAnchor
from src.ices.Happening import Happening, HappeningActionStart, HappeningEffect, HappeningConditionStart, \
    HappeningConditionEnd, HappeningCondition, HappeningActionEnd
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


class ICETransitionVariablesInstradi:
    task: ICETask
    pattern: ICEPattern
    stateVariables: Dict[Atom, SMTVariable]
    nextVariables: Dict[Atom, SMTVariable]
    happeningVariables: Dict[Happening, SMTVariable]
    clockVariables: Dict[Happening, SMTVariable]
    sigmaExpressions: Dict[int, Dict[Atom, SMTExpression or float]]
    makespan: SMTVariable

    def __init__(self, task: ICETask, pattern: ICEPattern):
        self.task = task
        self.pattern = pattern

        t = TimeStat.startHolder("Get happening variables")
        self.happeningVariables = self.__computeHappeningVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get time variables")
        self.timeVariables = self.__computeTimeVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get dur variables")
        self.durVariables = self.__computeDurationVariables()
        t.endHolder()
        t = TimeStat.startHolder("Get sigma expressions")
        self.sigmaExpressions = self.__computeSigmaExpressions()
        t.endHolder()

        self.makespan = SMTRealVariable(f"__makespan__")

        pass

    def __computeSigmaExpressions(self) -> Dict[int, Dict[Atom, SMTExpression or float]]:
        sigmas: Dict[int, Dict[Atom, SMTExpression or float]] = dict()

        sigmas[0] = dict()
        trueAtoms: Set[Atom] = set()
        for assignment in self.task.init:
            atom = assignment.getAtom()
            if isinstance(assignment, BinaryPredicate):
                if assignment.getAtom() not in self.task.propVariables | self.task.numVariables:
                    continue
                v = assignment.getAtom()
                k = float(str(assignment.rhs))
                sigmas[0][v] = k
            elif isinstance(assignment, Literal):
                sigmas[0][assignment.getAtom()] = TrueExpression()
                trueAtoms.add(assignment.getAtom())
            else:
                raise NotImplemented("Shouldn't go here")

        for v in self.task.propVariables - trueAtoms:
            sigmas[0][v] = FalseExpression()
            continue

        for i, h in enumerate(self.pattern):
            if i == 0:
                continue

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
                psi = SMTExpression.fromPddl(eff.rhs, sigmas[i - 1])
                if eff.isLinearIncrement():
                    sigmas[i][v] = sigmas[i - 1][v] + h_i * psi
                else:
                    sigmas[i][v] = ITEExpression.simplify(h_i > 0, psi, sigmas[i - 1][v])

        return sigmas

    def __computeHappeningVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        startingHappening: Dict[ICEAction, SMTVariable] = dict()

        for h in self.pattern:
            if isinstance(h, HappeningActionStart):
                variables[h] = SMTIntVariable(str(h))
                startingHappening[h.action] = variables[h]
            elif (isinstance(h, HappeningCondition) or isinstance(h, HappeningEffect)) and isinstance(h.parent,
                                                                                                      ICEAction):
                variables[h] = startingHappening[h.parent]
            elif isinstance(h, HappeningActionEnd):
                variables[h] = startingHappening[h.action]
                # del startingHappening[h.action]
            else:
                variables[h] = SMTIntVariable(str(h))

        return variables

    def __computeTimeVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        relativeTimes: Dict[ICEAction, SMTExpression] = dict()

        for h in self.pattern:
            if isinstance(h, HappeningActionStart):
                variables[h] = SMTRealVariable(f"t_{str(h)}")
                relativeTimes[h.action] = variables[h]
            elif Happening.computeTime(h) is not None:
                variables[h] = relativeTimes[h.parent] + Happening.computeTime(h)
            else:
                variables[h] = SMTRealVariable(f"t_{str(h)}")

        return variables

    def __computeDurationVariables(self) -> Dict[Happening, SMTVariable]:
        variables: Dict[Happening, SMTVariable] = dict()

        for h in self.pattern:
            if isinstance(h, HappeningActionStart):
                variables[h] = h.action.duration  # SMTRealVariable(f"d_{str(h)}")

        return variables
