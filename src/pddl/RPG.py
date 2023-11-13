from typing import List, Set

from src.pddl.Action import Action
from src.pddl.GroundedDomain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem


class RPG:
    __literalsLayers: List[Set[Literal]]
    __actionLayers: List[Set[Action]]

    def __init__(self, domain: GroundedDomain, problem: Problem):

        self.__literalsLayers = list()
        self.__actionLayers = list()

        self.actions = domain.actions

        literals = {lit for lit in problem.init.assignments if isinstance(lit, Literal)}
        for atom in domain.predicates:
            posLit = Literal.fromAtom(atom, "+")
            negLit = Literal.fromAtom(atom, "-")
            if posLit not in literals:
                literals.add(negLit)
        prevActions = {}
        actions = self.__getApplicableActions(literals)
        self.__literalsLayers.append(literals)
        self.__actionLayers.append(actions)

        while prevActions != actions:
            prevActions = actions
            literals = self.__applyActions(actions) | literals
            actions = self.__getApplicableActions(literals)
            self.__literalsLayers.append(literals)
            self.__actionLayers.append(actions)

        pass

    @staticmethod
    def __applyActions(actions: Set[Action]):
        newLiterals = set()
        for action in actions:
            for eff in action.effects:
                if not isinstance(eff, Literal):
                    continue
                newLiterals.add(eff)

        return newLiterals

    def __getApplicableActions(self, literals: Set[Literal]) -> Set[Action]:
        actions = set()
        for a in self.actions:
            applicable = True
            for p in a.preconditions:
                if not isinstance(p, Literal):
                    continue
                if p not in literals:
                    applicable = False
                    break
            if applicable:
                actions.add(a)

        return actions

    def getActionsOrder(self) -> List[Action]:
        usedActions = set()
        orderedActions = list()
        for layer in self.__actionLayers:
            newActions = layer - usedActions
            orderedActions += list(newActions)
            usedActions |= layer

        return orderedActions

    def getPartialOrder(self) -> List[Set[Action]]:

        usedActions = set()
        partialOrder = list()

        for layer in self.__actionLayers:
            partialOrder.append(layer - usedActions)
            usedActions |= layer

        return partialOrder
