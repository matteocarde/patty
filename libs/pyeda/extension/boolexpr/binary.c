/*
** Filename: binary.c
**
** Convert all N-ary operators to binary operators
*/


#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>

#include "boolexpr.h"
#include "memcheck.h"
#include "share.h"
#include "util.h"


static struct BoolExpr *
_commutative_binify(struct BoolExpr *op)
{
    if (op->data.xs->length == 2)
        return BX_IncRef(op);

    size_t mid = op->data.xs->length / 2;
    size_t n0 = mid;
    size_t n1 = op->data.xs->length - mid;
    struct BoolExpr **left = op->data.xs->items;
    struct BoolExpr **right = op->data.xs->items + mid;
    struct BoolExpr *xs[2];
    struct BoolExpr *temp;
    struct BoolExpr *y;

    if (n0 == 1) {
        xs[0] = BX_IncRef(left[0]);
    }
    else {
        CHECK_NULL(temp, _bx_op_new(op->kind, n0, left));
        CHECK_NULL_1(xs[0], _commutative_binify(temp), temp);
        BX_DecRef(temp);
    }

    CHECK_NULL_1(temp, _bx_op_new(op->kind, n1, right), xs[0]);
    CHECK_NULL_2(xs[1], _commutative_binify(temp), xs[0], temp);
    BX_DecRef(temp);

    CHECK_NULL_2(y, _bx_op_new(op->kind, 2, xs), xs[0], xs[1]);
    BX_DecRef(xs[0]);
    BX_DecRef(xs[1]);

    return y;
}


static struct BoolExpr *
_eq_binify(struct BoolExpr *op)
{
    if (op->data.xs->length == 2)
        return BX_IncRef(op);

    size_t length;
    struct BoolExpr **xs;
    struct BoolExpr *temp;
    struct BoolExpr *y;

    length = (op->data.xs->length * (op->data.xs->length - 1)) >> 1;
    xs = malloc(length * sizeof(struct BoolExpr *));

    for (size_t i = 0, index = 0; i < (op->data.xs->length - 1); ++i) {
        for (size_t j = i + 1; j < op->data.xs->length; ++j, ++index) {
            CHECK_NULL_N(xs[index], BX_EqualN(2, op->data.xs->items[i],
                                                 op->data.xs->items[j]), index, xs);
        }
    }

    CHECK_NULL_N(temp, BX_And(length, xs), length, xs);

    _bx_free_exprs(length, xs);

    CHECK_NULL_1(y, _commutative_binify(temp), temp);
    BX_DecRef(temp);

    return y;
}


static struct BoolExpr *
_fixed_binify(struct BoolExpr *op)
{
    return BX_IncRef(op);
}


static struct BoolExpr *
(*_op_binify[16])(struct BoolExpr *ex) = {
    NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL,

    _commutative_binify,
    _commutative_binify,
    _commutative_binify,
    _eq_binify,

    _fixed_binify,
    _fixed_binify,
    _fixed_binify,
    NULL,
};


struct BoolExpr *
BX_ToBinary(struct BoolExpr *ex)
{
    if (BX_IS_ATOM(ex))
        return BX_IncRef(ex);

    struct BoolExpr *temp;
    struct BoolExpr *y;

    CHECK_NULL(temp, _bx_op_transform(ex, BX_ToBinary));
    CHECK_NULL_1(y, _op_binify[temp->kind](temp), temp);
    BX_DecRef(temp);

    return y;
}

