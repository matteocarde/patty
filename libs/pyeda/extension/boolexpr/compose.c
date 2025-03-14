/*
** Filename: compose.c
**
** Function Composition
*/


#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>

#include "boolexpr.h"
#include "memcheck.h"
#include "share.h"
#include "util.h"


static struct BoolExpr *
_const_compose(struct BoolExpr *c, struct BX_Dict *var2ex)
{
    return BX_IncRef(c);
}


static struct BoolExpr *
_var_compose(struct BoolExpr *var, struct BX_Dict *var2ex)
{
    struct BoolExpr *ex;

    ex = BX_Dict_Search(var2ex, var);

    if (ex == (struct BoolExpr *) NULL)
        return BX_IncRef(var);

    return BX_IncRef(ex);
}


static struct BoolExpr *
_comp_compose(struct BoolExpr *comp, struct BX_Dict *var2ex)
{
    struct BoolExpr *var;
    struct BoolExpr *temp;
    struct BoolExpr *y;

    CHECK_NULL(var, BX_Not(comp));

    CHECK_NULL_1(temp, _var_compose(var, var2ex), var);
    BX_DecRef(var);

    CHECK_NULL_1(y, BX_Not(temp), temp);
    BX_DecRef(temp);

    return y;
}


static struct BoolExpr *
_op_compose(struct BoolExpr *op, struct BX_Dict *var2ex)
{
    size_t n = op->data.xs->length;
    struct BoolExpr **xs;
    unsigned int mod_count = 0;
    struct BoolExpr *y;

    xs = malloc(n * sizeof(struct BoolExpr *));
    if (xs == NULL)
        return NULL; // LCOV_EXCL_LINE

    for (size_t i = 0; i < n; ++i) {
        CHECK_NULL_N(xs[i], BX_Compose(op->data.xs->items[i], var2ex), i, xs);
        mod_count += (xs[i] != op->data.xs->items[i]);
    }

    if (mod_count)
        y = _bx_op_new(op->kind, n, xs);
    else
        y = BX_IncRef(op);

    _bx_free_exprs(n, xs);

    return y;
}


static struct BoolExpr *
(*_compose[16])(struct BoolExpr *ex, struct BX_Dict *var2ex) = {
    _const_compose,
    _const_compose,
    _const_compose,
    _const_compose,

    _comp_compose,
    _var_compose,
    NULL,
    NULL,

    _op_compose,
    _op_compose,
    _op_compose,
    _op_compose,

    _op_compose,
    _op_compose,
    _op_compose,
    NULL,
};


struct BoolExpr *
BX_Compose(struct BoolExpr *ex, struct BX_Dict *var2ex)
{
    return _compose[ex->kind](ex, var2ex);
}


struct BoolExpr *
BX_Restrict(struct BoolExpr *ex, struct BX_Dict *var2const)
{
    struct BoolExpr *temp;
    struct BoolExpr *y;

    CHECK_NULL(temp, BX_Compose(ex, var2const));
    CHECK_NULL_1(y, BX_Simplify(temp), temp);
    BX_DecRef(temp);

    return y;
}

