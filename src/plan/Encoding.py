from typing import List, Pattern, Set

import pysmt

from src.pddl.Domain import GroundedDomain
from src.pddl.Problem import Problem
from src.smt.SMTExpression import SMTExpression

import pysmt.smtlib.commands as smtcmd
import pysmt.smtlib.script
from pysmt.environment import get_env
from pysmt.logics import QF_NRA

from src.smt.SMTSolution import SMTSolution
from src.smt.SMTVariable import SMTVariable


class Encoding:
    domain: GroundedDomain
    problem: Problem
    rules: List[SMTExpression]
    softRules: List[SMTExpression]
    minimize: SMTExpression or None
    actionVariables: Set[SMTVariable]

    def __init__(self, domain: GroundedDomain, problem: Problem, pattern: Pattern, bound: int):
        self.domain = domain
        self.problem = problem
        self.pattern = pattern
        self.bound = bound
        self.minimize = None
        self.rules = []
        self.softRules = []
        self.actionVariables = set()
        pass

    def __str__(self):
        string = ""
        for rule in self.rules:
            string += str(rule) + "\n"
        return string

    def printRules(self):
        for rule in self.rules:
            print(rule)

    def writeSMTLIB(self, filename: str):
        formula = SMTExpression.andOfExpressionsList(self.rules).expression
        with open(filename, "w") as fout:
            script = pysmt.smtlib.script.SmtLibScript()

            script.add(name=smtcmd.SET_LOGIC,
                       args=[QF_NRA])

            # Declare all types
            types = get_env().typeso.get_types(formula, custom_only=True)
            for type_ in types:
                script.add(name=smtcmd.DECLARE_SORT, args=[type_.decl])

            deps = formula.get_free_variables()
            # Declare all variables
            for symbol in deps:
                assert symbol.is_symbol()
                script.add(name=smtcmd.DECLARE_FUN, args=[symbol])

            for r in self.rules:
                # Assert formula
                script.add_command(pysmt.smtlib.script.SmtLibCommand(name=smtcmd.ASSERT,
                                                                     args=[r.expression]))

            # check-sat
            script.add_command(pysmt.smtlib.script.SmtLibCommand(name=smtcmd.CHECK_SAT,
                                                                 args=[]))
            script.serialize(fout, daggify=False)

    def getPlanFromSolution(self, solution: SMTSolution):
        raise NotImplemented

    def getNVars(self):
        variables = set()
        for i, rule in enumerate(self.rules):
            variables |= rule.variables
        # print(variables)
        return len(variables)

    def getNRules(self):
        return len(self.rules)
