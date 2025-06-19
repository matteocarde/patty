"""
Test DIMACS load/dump methods
"""


import pytest

from libs.pyeda.pyeda.parsing.dimacs import Error, parse_cnf, parse_sat


def test_cnf_errors():
    # lexical error
    with pytest.raises(Error):
        parse_cnf("#a")
    # unexpected token
    with pytest.raises(Error):
        parse_cnf("p cnf cnf 0 0\n")
    with pytest.raises(Error):
        parse_cnf("p cnf 1 1\n1 x 0")
    # formula has fewer clauses than specified
    with pytest.raises(Error):
        parse_cnf("p cnf 0 1\n")
    # formula has more clauses than specified
    with pytest.raises(Error):
        parse_cnf("p cnf 0 0\n0")
    # formula literal too large
    with pytest.raises(Error):
        parse_cnf("p cnf 0 1\n1 0")
    with pytest.raises(Error):
        parse_cnf("p cnf 0 1\n-1 0")
    # incomplete clause
    with pytest.raises(Error):
        parse_cnf("p cnf 1 1\n1")


def test_parse_cnf():
    # Empty formula corner cases
    assert parse_cnf("p cnf 0 0\n") == ("and", )
    assert parse_cnf("p cnf 1 0\n") == ("and", )

    # Empty clause corner cases
    assert parse_cnf("p cnf 0 1\n0") == ("and", ("or", ),)
    assert parse_cnf("p cnf 1 2\n0 0") == ("and", ("or", ),("or", ))

    assert parse_cnf("p cnf 2 2\n-1 2 0 1 -2 0") == ("and", ("or", ("not", ("var", ("x", ), (1, ))), ("var", ("x", ), (2, ))), ("or", ("var", ("x", ), (1, )), ("not", ("var", ("x", ), (2, )))))


#def test_sat_errors():
#    assert_raises(Error, parse_sat, "#a")
#    assert_raises(Error, parse_sat, "p sat 0\n")
#    assert_raises(Error, parse_sat, "p sat 2\n0")
#    assert_raises(Error, parse_sat, "p sat 2\n3")
#    assert_raises(Error, parse_sat, "p sat 2\n-3")
#    assert_raises(Error, parse_sat, "p sat 2\n-(0)")
#    assert_raises(Error, parse_sat, "p sat 2\n-(3)")


def test_parse_sat():
    assert parse_sat("p sat 1\n(-1)") == ("not", ("var", ("x", ), (1, )))
    assert parse_sat("p sat 2\n-(+(*(-1 2) *(1 -2)))") == ("not", ("or", ("and", ("not", ("var", ("x", ), (1, ))), ("var", ("x", ), (2, ))), ("and", ("var", ("x", ), (1, )), ("not", ("var", ("x", ), (2, ))))))
    assert parse_sat("p satx 2\nxor(-1 2)") == ("xor", ("not", ("var", ("x", ), (1, ))), ("var", ("x", ), (2, )))
    assert parse_sat("p sate 2\n=(-1 2)") == ("equal", ("not", ("var", ("x", ), (1, ))), ("var", ("x", ), (2, )))
    assert parse_sat("p satex 2\n+(xor(-1 2) =(1 -2))") == ("or", ("xor", ("not", ("var", ("x", ), (1, ))), ("var", ("x", ), (2, ))), ("equal", ("var", ("x", ), (1, )), ("not", ("var", ("x", ), (2, )))))
