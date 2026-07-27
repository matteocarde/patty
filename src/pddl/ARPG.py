import copy
import itertools
from typing import Set, List, Dict

from src.pattern.BooleanPatternActionGraph import BooleanPatternActionGraph
from src.pattern.NumericPatternActionGraph import NumericPatternActionGraph
from src.pattern.PatternActionGraph import PatternActionGraph
from src.pddl.Action import Action
from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Formula import Formula
from src.pddl.Goal import Goal
from src.pddl.PDDLException import PDDLException
from src.pddl.RelaxedIntervalState import RelaxedIntervalState
from src.pddl.SnapAction import SnapAction
from src.pddl.State import State
from src.pddl.Supporter import Supporter
from src.pddl.TimePredicate import TimePredicateType
from src.utils.TimeStat import TimeStat

SEED = 0


class ARPG:
    supporterLevels: List[Set[Supporter]]
    stateLevels: List[RelaxedIntervalState]
    actionLevels: List[Set[Action]]
    layers: List[Set[Action]]

    def __init__(self, domain: GroundedDomain, state: State, goal: Goal, avoidRaising=False):
        self.goalNotReachable = False
        self.supporterLevels = list()
        self.stateLevels = list()
        self.actionLevels = list()
        self.actions: List[Action] = list(domain.actions)
        # self.affectedGraph: AffectedGraph = domain.affectedGraph

        self.originalOrder = dict([(action, i) for (i, action) in enumerate(self.actions)])

        supporters: Set[Supporter] = set()
        for a in self.actions:
            supporters |= a.getSupporters()

        usedActions = set()
        state: RelaxedIntervalState = RelaxedIntervalState.fromState(state, domain.predicates)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state) and s.respectsTemporal(usedActions)}
        usedActions = usedActions | {s.originatingAction for s in activeSupporters}
        self.supporterLevels.append(activeSupporters)
        self.actionLevels.append({s.originatingAction for s in activeSupporters})
        self.stateLevels.append(state)

        fullBooleanGoal = len(goal.getFunctions()) == 0

        isFixpoint = False
        while activeSupporters or not isFixpoint:
            supporters = supporters - activeSupporters
            newState = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if
                                s.isSatisfiedBy(newState) and s.respectsTemporal(usedActions)}
            usedActions = usedActions | {s.originatingAction for s in activeSupporters}

            self.supporterLevels.append(activeSupporters)
            self.stateLevels.append(newState)
            self.actionLevels.append({s.originatingAction for s in activeSupporters})

            isFixpoint = state.coincide(newState)
            state = newState

        if not fullBooleanGoal and not state.satisfies(goal):
            self.goalNotReachable = True
            if not avoidRaising:
                raise PDDLException.GoalNotReachable()

        self.layers: List[Set[Action]] = list()
        self.usedActions = set()

        for supporters in self.supporterLevels:
            partialOrder = set()
            for supporter in supporters:
                if supporter.originatingAction not in self.usedActions:
                    partialOrder.add(supporter.originatingAction)
                self.usedActions.add(supporter.originatingAction)
            self.layers.append(partialOrder)

    def __getPurelyBoolean(self) -> List[Action]:
        order: List[Action] = list()
        for action in self.actions:
            if not action.getFunctions():
                order.append(action)
        return order

    def getUsefulActions(self) -> Set[Action]:
        usefulActions: Set[Action] = set()
        for supporters in self.supporterLevels:
            for supporter in supporters:
                usefulActions.add(supporter.originatingAction)
        return usefulActions

    def getActionsOrder(self, enhanced=False, boolean=False) -> List[Action] or bool:

        t = TimeStat.startHolder("Initializing Layers")
        layers = copy.copy(self.layers)
        leftActions = set(self.actions) - self.usedActions
        layerInstant = {a for a in leftActions if not isinstance(a, SnapAction)}
        layerSnap = {a for a in leftActions if isinstance(a, SnapAction) and a.timeType != TimePredicateType.OVER_ALL}
        layers.append(layerInstant)
        layers.append(layerSnap)
        t.endHolderMilliseconds()

        # print("Left actions", {a.name for a in leftActions})

        order = list()
        for i, layer in enumerate(layers):
            if enhanced:
                pag = NumericPatternActionGraph(layer) if not boolean else BooleanPatternActionGraph(layer)
                sortedLayer = pag.getSorted()
                order += sortedLayer
            else:
                order += sorted(layer)

        return order

    def getActionsOrderAndLeft(self, enhanced):
        layers = copy.copy(self.layers)
        leftActions = set(self.actions) - self.usedActions

        order = list()
        for i, layer in enumerate(layers):
            if enhanced:
                sortedLayer = PatternActionGraph(layer).getSorted()
                order += sortedLayer
            else:
                order += sorted(layer)

        return order, leftActions

    def getActionsOrderWithoutUnused(self, enhanced):
        layers = copy.copy(self.layers)

        order = list()
        for i, layer in enumerate(layers):
            if enhanced:
                sortedLayer = PatternActionGraph(layer).getSorted()
                order += sortedLayer
            else:
                order += sorted(layer)

        return order

    def getUnusedActions(self):
        return set(self.actions) - self.usedActions

    def getConstantAtoms(self) -> Dict[Atom, float or bool]:
        if len(self.stateLevels) < 2:
            return dict()
        lastLevel: RelaxedIntervalState = self.stateLevels[-1]
        subs: Dict[Atom, float] = dict()
        for (atom, interval) in lastLevel.intervals.items():
            if interval.lb == interval.ub:
                subs[atom] = interval.lb
        return subs

    def __str__(self):
        string = ""
        n = len(self.supporterLevels)
        prevActions = set()
        for layer in range(0, n):
            string += f"S_{layer} = {self.stateLevels[layer]}\n"
            actionLayer = {s.originatingAction for s in self.supporterLevels[layer]} - prevActions
            string += f"A_{layer} = {actionLayer}\n"

        return string

    def getConeOfInfluence(self, goal: Goal) -> List[Action]:

        level = None
        for i, l in enumerate(self.stateLevels):
            if l.satisfies(goal):
                level = i
                break

        actionLayers: List[List[Action]] = []
        atoms = goal.getFunctions() | goal.getPredicates()
        usedActions = set()
        orState = copy.deepcopy(goal)
        orState.type = "OR"

        while level > 0:
            level -= 1
            prevAtoms = set()
            actions = set()
            state = self.stateLevels[level]
            newOrState = Formula.disjunction()
            for s in self.supporterLevels[level]:
                if s.effect.atom not in atoms:
                    continue
                if not state.applySupporters({s}).satisfies(orState):
                    continue
                prevAtoms |= s.preconditions.getPredicates() | s.preconditions.getFunctions()
                action = s.originatingAction
                for f in action.preconditions:
                    newOrState.addClause(f)
                actions.add(s.originatingAction)
            atoms |= prevAtoms
            actions = actions - usedActions
            usedActions |= actions
            actionLayers = [list(actions)] + actionLayers
            orState = newOrState

        order = []
        for layer in actionLayers:
            order += layer
        return order

    def printLayers(self, columns: int):
        cs = f"|{'|'.join('c' for i in range(columns))}|"
        print(r"\begin{tabular}{" + cs + "}")

        layers = 0
        rows = []
        while layers < len(self.layers):
            headers = []
            cells = []

            i = 0
            while i < columns:
                if layers < len(self.layers) and self.layers[layers]:
                    filtered = {l for l in self.layers[layers] if "time_flow_patty" not in l.name}
                    if not filtered:
                        layers += 1
                        continue
                    sortedLayers = PatternActionGraph(filtered).getSorted()
                    headers.append(rf"$\ttt{{time}} = {str(layers)}$")
                    string = "\makecell{" + " \\\\ ".join([str(h) for h in sortedLayers]) + "}"
                    cells.append(string.replace("blue", "b")
                                 .replace("red", "r")
                                 .replace(" ", "")
                                 .replace("0.002", "$2\epsilon$")
                                 .replace("+0.000", "")
                                 .replace("-0.000", "")
                                 .replace("ZE", "E"))
                else:
                    headers.append("")
                    cells.append("")
                i += 1
                layers += 1
            print(r"\hline")
            print("&".join(headers) + r"\\")
            print("&".join(cells) + r"\\\hline")
            print(r"\multicolumn{" + str(columns) + r"}{l}{} \\")

        print(r"\end{tabular}")
