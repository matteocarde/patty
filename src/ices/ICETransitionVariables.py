from typing import Dict, List, Set

from src.ices.Happening import Happening, HappeningActionStart, HappeningEffect
from src.ices.ICEPattern import ICEPattern
from src.ices.ICETask import ICETask
from src.pddl.Atom import Atom
from src.pddl.BinaryPredicate import BinaryPredicate
from src.pddl.Literal import Literal
from src.smt.SMTBoolVariable import SMTBoolVariable
from src.smt.SMTExpression import SMTExpression
from src.smt.SMTNumericVariable import SMTRealVariable, SMTIntVariable
from src.smt.SMTVariable import SMTVariable


class ICETransitionVariables:
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

    def __computeSigmaExpressions(self) -> Dict[int, Dict[Atom, SMTExpression or float]]:
        sigmas: Dict[int, Dict[Atom, SMTExpression or float]] = dict()
        values = self.stateVariables

        for i, h in enumerate(self.pattern):
            sigmas[i] = dict()

            if i == 0:
                trueAtoms: Set[Atom] = set()
                for assignment in self.task.init:
                    atom = assignment.getAtom()
                    if atom not in values:
                        # print(f"Atom {atom} in initial condition doesn't concur in achieving the goal. Pruned.")
                        continue
                    if isinstance(assignment, BinaryPredicate):
                        if assignment.getAtom() not in self.task.propVariables | self.task.numVariables:
                            continue
                        v = assignment.getAtom()
                        k = float(str(assignment.rhs))
                        sigmas[i][v] = k
                    elif isinstance(assignment, Literal):
                        sigmas[i][assignment.getAtom()] = SMTExpression.TRUE()
                        trueAtoms.add(assignment.getAtom())
                    else:
                        raise NotImplemented("Shouldn't go here")

                for v in self.task.propVariables - trueAtoms:
                    sigmas[i][v] = SMTExpression.FALSE()
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
