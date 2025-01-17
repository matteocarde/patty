"""
Test logic functions for addition
"""


import random

import pytest

from libs.pyeda.pyeda.boolalg.bfarray import exprvars, fcat, int2exprs, uint2exprs
from libs.pyeda.pyeda.logic.addition import brent_kung_add as bka
from libs.pyeda.pyeda.logic.addition import kogge_stone_add as ksa
from libs.pyeda.pyeda.logic.addition import ripple_carry_add as rca

NVECS = 100


def uadd(S, A, B, aval, bval):
    N = len(A)
    R = S.vrestrict({A: uint2exprs(aval, N), B: uint2exprs(bval, N)})
    return R.to_uint()


def sadd(S, A, B, aval, bval):
    N = len(A)
    R = S.vrestrict({A: int2exprs(aval, N), B: int2exprs(bval, N)})
    return R.to_int()


def test_errors():
    A = exprvars('A', 7)
    B = exprvars('B', 9)

    for adder in (rca, ksa, bka):
        with pytest.raises(ValueError):
            adder(A, B)


def test_unsigned_add():
    N = 9

    A = exprvars('A', N)
    B = exprvars('B', N)

    for adder in (rca, ksa, bka):
        S, C = adder(A, B)
        S = fcat(S, C[-1])

        # 0 + 0 = 0
        assert uadd(S, A, B, 0, 0) == 0
        # 255 + 255 = 510
        assert uadd(S, A, B, 2**N-1, 2**N-1) == (2**(N+1)-2)
        # 255 + 1 = 256
        assert uadd(S, A, B, 2**N-1, 1) == 2**N

        # unsigned random vectors
        for _ in range(NVECS):
            ra = random.randint(0, 2**N-1)
            rb = random.randint(0, 2**N-1)
            assert uadd(S, A, B, ra, rb) == ra + rb


def test_signed_add():
    A = exprvars('A', 8)
    B = exprvars('B', 8)

    for adder in (rca, ksa, bka):
        S, C = adder(A, B)

        # 0 + 0 = 0
        assert sadd(S, A, B, 0, 0) == 0
        # -64 + -64 = -128
        assert sadd(S, A, B, -64, -64) == -128
        # -1 + 1 = 0
        assert sadd(S, A, B, -1, 1) == 0
        # -64 + 64 = 0
        assert sadd(S, A, B, -64, 64) == 0

        # signed random vectors
        for _ in range(NVECS):
            ra = random.randint(-2**6, 2**6-1) # -64..63
            rb = random.randint(-2**6, 2**6)   # -64..64
            assert sadd(S, A, B, ra, rb) == ra + rb

        # 64 + 64, overflow
        R = C.vrestrict({A: int2exprs(64, 8), B: int2exprs(64, 8)})
        assert R[7] != R[6]
        # -65 + -64, overflow
        R = C.vrestrict({A: int2exprs(-65, 8), B: int2exprs(-64, 8)})
        assert R[7] != R[6]
