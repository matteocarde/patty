"""
Lexical Analysis Utilities

Exceptions:
    Error
    CompileError
    RunError

Interface Classes:
    RegexLexer
"""

import collections
import re

from libs.pyeda.pyeda.parsing.token import EndToken


class Error(Exception):
    """
    Base class for all lexical analysis errors
    """


class CompileError(Error):
    """
    Errors raised during compilation of lexical analysis rules.
    """


class RunError(Error):
    """
    Errors raised during lexical analysis of the source text.
    """
    def __init__(self, msg, lineno, offset, text):
        self.lineno = lineno
        self.offset = offset
        self.text = text
        super().__init__(msg, lineno, offset, text)


class RegexLexer:
    """
    Lexer based on regular expressions.
    """
    RULES = {
        "root": []
    }

    def __init__(self, string):
        self.string = string

        self.pos = None
        self.lineno = None
        self.offset = None

        self.states = []
        self.tokens = collections.deque()

        self.gtoks = None

        self._rules = {}
        self._compile_rules()

    def __iter__(self):
        self.pos = 0
        self.lineno = 1
        self.offset = 1

        self.states = ["root"]
        self.tokens.clear()

        self.gtoks = self._iter_tokens()

        return self

    def __next__(self):
        if self.tokens:
            return self.tokens.pop()
        else:
            return next(self.gtoks)

    def _compile_rules(self):
        """Compile the rules into the internal lexer state."""
        for state, table in self.RULES.items():
            patterns = []
            actions = []
            nextstates = []
            for i, row in enumerate(table):
                if len(row) == 2:
                    pattern, action_ = row
                    nextstate = None
                elif len(row) == 3:
                    pattern, action_, nextstate = row
                else:
                    fstr = "invalid RULES: state {}, row {}"
                    raise CompileError(fstr.format(state, i))
                patterns.append(pattern)
                actions.append(action_)
                nextstates.append(nextstate)
            reobj = re.compile("|".join("(" + p + ")" for p in patterns))
            self._rules[state] = (reobj, actions, nextstates)

    def _iter_tokens(self):
        """Iterate through all tokens in the input string."""
        reobj, actions, nextstates = self._rules[self.states[-1]]
        mobj = reobj.match(self.string, self.pos)
        while mobj is not None:
            text = mobj.group(0)
            idx = mobj.lastindex - 1
            nextstate = nextstates[idx]

            # Take action
            actions[idx](self, text)
            while self.tokens:
                yield self.pop_token()
            if nextstate and nextstate != self.states[-1]:
                self.states[-1] = nextstate

            # Update position variables
            self.pos = mobj.end()
            lines = text.split("\n")
            nlines = len(lines) - 1
            if nlines == 0:
                self.offset = self.offset + len(lines[0])
            else:
                self.lineno = self.lineno + nlines
                self.offset = 1 + len(lines[-1])

            reobj, actions, nextstates = self._rules[self.states[-1]]
            mobj = reobj.match(self.string, self.pos)

        if self.pos != len(self.string):
            msg = "unexpected character"
            text = self.string[self.pos]
            raise RunError(msg, self.lineno, self.offset, text)

        yield EndToken("", self.lineno, self.offset)

    def push_token(self, tok):
        """Push a token into the token queue.

                 +--+--+--+--+
        token => |  |  |  |  |
                 +--+--+--+--+
        """
        self.tokens.appendleft(tok)

    def pop_token(self):
        """Pop a token from the token queue.

        +--+--+--+--+
        |  |  |  |  | => token
        +--+--+--+--+
        """
        return self.tokens.pop()

    def unpop_token(self, tok):
        """Return a popped token to top of the token queue.

        +--+--+--+--+
        |  |  |  |  | <= token
        +--+--+--+--+
        """
        self.tokens.append(tok)

    def peek_token(self):
        """Peek at the next token from the token queue."""
        tok = next(self)
        self.unpop_token(tok)
        return tok


def action(toktype):
    """Return a parser action property."""
    def outer(func):
        """Return a function that pushes a token onto the token queue."""
        def inner(lexer, text):
            """Push a token onto the token queue."""
            value = func(lexer, text)
            lexer.tokens.append(toktype(value, lexer.lineno, lexer.offset))
        return inner
    return outer
