from __future__ import annotations

from typing import List, Set, Dict

from classes.utils.Constants import EPSILON
from src.ices.Happening import HappeningActionStart
from src.ices.ICEAction import BEGIN
from src.ices.ICEEncoding import ICEEncoding
from src.ices.ICETask import ICETask
from src.ices.IntermediateCondition import IntermediateCondition
from src.ices.IntermediateEffect import IntermediateEffect
from src.ices.ParallelIntermediateEffects import ParallelIntermediateEffects
from src.ices.TimedICEAction import TimedICEAction, TimedICEActionList
from src.pddl.State import State
from src.pddl.TimedState import TimedState
from src.smt.SMTSolution import SMTSolution
from src.utils.ValAssert import ValAssert, ValidationError


class ICEPlan:
    timedActions: TimedICEActionList
    encoding: ICEEncoding
    task: ICETask
    iconds: Set[IntermediateCondition]
    ieffs: Set[IntermediateEffect]

    def __init__(self):
        self.timedActions = TimedICEActionList()

    @classmethod
    def fromSMTSolution(cls, encoding: ICEEncoding, solution: SMTSolution) -> ICEPlan:
        plan = cls()
        plan.encoding = encoding
        tVars = encoding.transVars.timeVariables
        hVars = encoding.transVars.happeningVariables
        dVars = encoding.transVars.durVariables

        for h_i in encoding.pattern:
            if not isinstance(h_i, HappeningActionStart):
                continue
            mu_h_i: int = solution.getVariable(hVars[h_i])
            mu_t_i: float = solution.getVariable(tVars[h_i])
            mu_d_i: float = solution.getVariable(dVars[h_i])
            if mu_h_i > 0:
                th = TimedICEAction(mu_t_i, h_i.action, mu_d_i)
                plan.timedActions.append(th)

        plan.task: ICETask = encoding.task
        plan.iconds = set()
        plan.ieffs = set()
        ms: float = plan.getMakeSpan()

        for (t, b, d) in plan.timedActions.tuples():
            for icond in b.icond:
                plan.iconds.add(icond.toAbsolute(t, t + d))
            for ieff in b.ieff:
                plan.ieffs.add(ieff.toAbsolute(t, t + d))

        for ieff in plan.task.effects:
            if ieff.time == BEGIN + 0:
                continue
            plan.ieffs.add(ieff.toAbsolute(0, ms))
        for icond in plan.task.conditions:
            plan.iconds.add(icond.toAbsolute(0, ms))

        return plan

    def print(self):
        sortedPlan = sorted(self.timedActions)
        print("Found Plan:")
        for ta in sortedPlan:
            print(f"{ta.time}: {ta.action} [{ta.duration}]")

    def getMakeSpan(self) -> float:
        ms = 0
        for (t, b, d) in self.timedActions.tuples():
            ms = max(ms, t + d)

        return ms

    def getTimedStates(self) -> List[TimedState]:

        task = self.encoding.task
        pieffDict: Dict[float, ParallelIntermediateEffects] = dict()

        for ieff in self.ieffs:
            t = ieff.time
            pieffDict.setdefault(t, ParallelIntermediateEffects())
            pieffDict[t].add(ieff)

        pieffs: List[ParallelIntermediateEffects] = [par for (t, par) in sorted(pieffDict.items())]

        initState: State = State.fromInitialCondition(task.init)
        states: List[TimedState] = [TimedState(0, initState)]

        s = initState
        for pieff in pieffs:
            s = s.applyParallelIntermediateEffects(pieff)
            states.append(TimedState(pieff.time, s))

        return states

    def __checkGoal(self) -> bool:
        states: List[TimedState] = self.getTimedStates()
        finalState: State = states[-1].state

        try:
            ValAssert(finalState.satisfies(self.task.goal),
                      "Goal is not valid.\n"
                      f"Final state: {finalState}\n"
                      f"Goal: {self.task.goal}")
        except ValidationError:
            return False

        return True

    def __checkIntermediateConditions(self) -> bool:
        states: List[TimedState] = self.getTimedStates()
        m = len(states) - 1

        try:
            for icond in self.iconds:
                t_s = icond.fromTime
                t_e = icond.toTime
                cond = icond.conditions

                checked = False
                for i in range(0, len(states)):
                    t = states[i].time
                    s = states[i].state
                    t_ = states[i + 1].time if i < m else None


                    # 2.a
                    if i == 0 and t_s == t:
                        ValAssert(s.satisfies(cond), f"Rule 2.a - \n{s} \nshould satisfy \n{cond} in [{t_s}, {t_e}]")
                        checked = True

                    # 2.b
                    if i < m and (t < t_s <= t_ or t < t_e <= t_):
                        ValAssert(s.satisfies(cond), f"Rule 2.b - \n{s} \nshould satisfy \n{cond} in [{t_s}, {t_e}]")
                        checked = True

                    # 1.c
                    if t_s < t < t_e:
                        ValAssert(s.satisfies(cond), f"Rule 1.c - \n{s} \nshould satisfy \n{cond} in [{t_s}, {t_e}]")
                        checked = True

                    # # 1.d
                    # if i == m and t_e == t:
                    #     ValAssert(s.satisfies(cond), f"Rule 1.d - \n{s} \nshould satisfy \n{cond}")
                    #     checked = True

                assert checked

        except AssertionError:
            return False

        return True

    def __checkSelfOverlapping(self) -> bool:
        # TODO
        return True

    def __checkEpsilonSeparation(self) -> bool:

        try:
            # for c in self.iconds:
            #     for e in self.ieffs:
            #         if c.inMutexWith(e):
            #             fromAssertion = abs(c.fromTime - e.time) >= EPSILON / 2
            #             toAssertion = abs(c.toTime - e.time) >= EPSILON / 2
            #             self.__assert(fromAssertion, f"c={c} and e={e} are in mutex and not epsilon separated: "
            #                                          f"{abs(c.fromTime - e.time)} < {EPSILON}")
            #             self.__assert(toAssertion, f"c={c} and e={e} are in mutex and not epsilon separated:"
            #                                        f"{abs(c.toTime - e.time)} < {EPSILON}")

            for e1 in self.ieffs:
                for e2 in self.ieffs:
                    if e1 == e2:
                        continue
                    if e1.inMutexWith(e2):
                        assertion = abs(e1.time - e2.time) >= EPSILON / 2
                        ValAssert(assertion,
                                  f"e_1={e1.effects} is in mutex with e_2={e2.effects} but are not "
                                  f"epsilon separated. t_1 = {e1.time} and t_2 = {e2.time}")

        except AssertionError:
            return False

        return True

    def isValid(self) -> bool:

        return self.__checkIntermediateConditions() \
            and self.__checkSelfOverlapping() \
            and self.__checkEpsilonSeparation()
