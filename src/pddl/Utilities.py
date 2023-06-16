import operator
import re

from antlr4 import *

from src.pddl.grammar.pddlLexer import pddlLexer
from src.pddl.grammar.pddlParser import pddlParser

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

COMPARATORS = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    "!=": operator.ne
}

INVERSE_COMPARATORS = {
    ">=": "<",
    "<=": ">",
    ">": "<=",
    "<": ">=",
    "=": "!=",
    "!=": "="
}

LATEX_OP = {
    "+": "+",
    "-": "-",
    "*": r"\times",
    ">=": r"\geq",
    "<=": r"\leq",
    ">": ">",
    "<": "<",
    "=": "=",
    "!=": r"\neq",
    "increase": r"\mathrel{+}=",
    "decrease": r"\mathrel{-}=",
    "assign": r"\mathrel{:}=",
}


class Utilities:

    @staticmethod
    def removeComments(string: str):
        return re.sub(r';.*', '', string)

    @staticmethod
    def getParseTree(string: str) -> pddlParser:
        input_stream = InputStream(string)
        lexer = pddlLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        return pddlParser(token_stream)

    @staticmethod
    def op(op: str, left, right):
        return OPERATORS[op](left, right)

    @staticmethod
    def compare(op: str, left, right):
        return COMPARATORS[op](left, right)

    @classmethod
    def inverted(cls, op: str):
        return INVERSE_COMPARATORS[op]

    @classmethod
    def latexOp(cls, op):
        return LATEX_OP[op]
