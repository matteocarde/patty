from typing import List

from pysmt.environment import get_env
from pysmt.logics import QF_NRA
from pysmt.smtlib.printers import SmtDagPrinter, SmtPrinter
from pysmt.smtlib.script import SmtLibScript, SmtLibCommand
import pysmt.smtlib.commands as smtcmd

from src.smt.SMTComment import SMTComment
from src.smt.SMTExpression import SMTExpression


class SMTSaver:

    def __init__(self):
        pass

    @staticmethod
    def save(rules: List[SMTExpression], softRules: List[SMTExpression], filename: str):
        formula = SMTExpression.andOfExpressionsList(rules).getExpression()
        with open(filename, "w") as fout:
            script = SmtLibScript()

            # script.add(name=smtcmd.SET_LOGIC,
            #            args=[QF_NRA])

            # Declare all types
            types = get_env().typeso.get_types(formula, custom_only=True)
            for type_ in types:
                script.add(name=smtcmd.DECLARE_SORT, args=[type_.decl])

            deps = formula.get_free_variables()
            # Declare all variables
            for symbol in deps:
                assert symbol.is_symbol()
                script.add(name=smtcmd.DECLARE_FUN, args=[symbol])

            for r in rules:
                # Assert formula
                if isinstance(r, SMTComment):
                    script.add_command(ExtendedSmtLibCommand(name="comment", args=[r.comment]))
                else:
                    script.add_command(ExtendedSmtLibCommand(name=smtcmd.ASSERT, args=[r.getExpression()]))

            for r in softRules:
                # Assert formula
                script.add_command(ExtendedSmtLibCommand(name="assert-soft", args=[r.getExpression()]))

            # check-sat
            script.add_command(SmtLibCommand(name=smtcmd.CHECK_SAT, args=[]))
            script.add_command(SmtLibCommand(name=smtcmd.GET_MODEL, args=[]))
            script.serialize(fout, daggify=False)


class ExtendedSmtLibCommand(SmtLibCommand):

    def serialize(self, outstream=None, printer=None, daggify=True):

        if (outstream is None) and (printer is not None):
            outstream = printer.stream
        elif (outstream is not None) and (printer is None):
            if daggify:
                printer = SmtDagPrinter(outstream)
            else:
                printer = SmtPrinter(outstream)
        else:
            assert (outstream is not None and printer is not None) or \
                   (outstream is None and printer is None), \
                "Exactly one of outstream and printer must be set."

        if self.name == "assert-soft":
            outstream.write("(%s " % self.name)
            printer.printer(self.args[0])
            outstream.write(")")
        elif self.name == "comment":
            outstream.write(f";{self.args[0]}")
        else:
            super().serialize(outstream, printer, daggify)
