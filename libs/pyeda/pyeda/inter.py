"""
Interactive Use

To prepare a terminal for interactive use:

    >>> from libs.pyeda.pyeda.inter import *
"""


# Disable "unused-import", since that's basically all this module is for.
# pylint: disable=W0611


from libs.pyeda.pyeda.boolalg.bdd import (BDDConstant, BDDNode, BDDVariable,
                               BinaryDecisionDiagram, bdd2expr, bddvar,
                               expr2bdd, ite, upoint2bddpoint)
from libs.pyeda.pyeda.boolalg.bfarray import (bddones, bddvars, bddzeros, exprones,
                                   exprvars, exprzeros, farray, fcat, int2bdds,
                                   int2exprs, int2tts, ttones, ttvars, ttzeros,
                                   uint2bdds, uint2exprs, uint2tts)
from libs.pyeda.pyeda.boolalg.boolfunc import (Function, Variable, iter_points,
                                    iter_terms, iter_upoints, num2point,
                                    num2term, num2upoint, point2term,
                                    point2upoint, vpoint2point)
from libs.pyeda.pyeda.boolalg.expr import (ITE, AchillesHeel, And, ConjNormalForm,
                                DimacsCNF, DisjNormalForm, Equal, Exists,
                                Expression, ForAll, Implies, Majority, Mux,
                                Nand, NHot, Nor, NormalForm, Not, OneHot,
                                OneHot0, Or, Unequal, Xnor, Xor, ast2expr,
                                expr, expr2dimacscnf, expr2dimacssat, exprvar,
                                upoint2exprpoint)
from libs.pyeda.pyeda.boolalg.minimization import espresso_exprs, espresso_tts
from libs.pyeda.pyeda.boolalg.table import (TruthTable, TTConstant, TTVariable,
                                 expr2truthtable, truthtable, truthtable2expr,
                                 ttvar)
from libs.pyeda.pyeda.parsing.boolexpr import parse as parse_expr
from libs.pyeda.pyeda.parsing.dimacs import parse_cnf, parse_sat
from libs.pyeda.pyeda.util import clog2, parity
