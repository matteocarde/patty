SMT-Based Planning Algorithm
============================

This document describes an SMT encoding for the ANML language.

We assume a flattened problem `P` is given.

We propose a SATPlan-like encoding based on steps. We introduce a set
of variables that are replicated at each steps. We indicate variable
`v` at step `i` as `v@i` and with `H` the plan horizon.

In this encoding we disregard the self-concurrency issue by only
considering plans that do not have self-concurrency. However we can
use the very same encoding with a bounded number of self-concurrent
actions by creating multiple instances of the same action.


Types
-----

We target an SMT solver equipped with the QF_LIRA theory of numbers.
Here we present a type-mapping function for representing the TAMER
types in SMT.

`SmtType(rational)` : `Real`

`SmtType(integer)` : `Integer`

`SmtType(boolean)` : `Bool`

In addition, TAMER has 'enumeration' types that are the collection of
objects instances. We represent those in SMT as an `integer` by
assigning an id from `0` to the total number of instances `N` to each
instance. This is not the best possible translation in all the cases
as also a logarithmic Boolean encoding is possible; however, for the
time being this should be enough.


Variables
---------

* For each fluent `f` with type `T` in `P` we introduce a variable `f`
  with type `SmtType(T)`.

* For each action `a`, we introduce a Boolean variable `a` that is
  true when the action starts. Those action will be used as
  implicants, so that the SMT solver is free to assign them to true to
  signal an action start.

* For each action `a` we introduce two real variables `s_a`, `d_a` that model
  the start and the duration of action `a`.

* For each action `a`, for each formal parameter `p` (of type `T`) of
  `a` we introduce a variable `p_a` with type `SmtType(T)`.

* A real variable `t` marking the time of the steps.



Expression mapping
------------------

We divide tamer expressions in two sets, conditions and
effects. Effects are all the expression containing a `:=` operator,
conditions are the other.

Given a tamer condition `e` we convert it in SMT at step `i`
(`ToSmt(e)@i`) as follows:

* `ToSmt(f)@i = f@i` if `f` is a fluent reference
* `ToSmt(p)@i = a_p@i` if `p` is a formal parameter of action `a`
* `ToSmt(k)@i = k` if `k` is a constant (integer, Boolean, rational) or an instance reference
* `ToSmt(start(a))@i = s_a@i`
* `ToSmt(end(a))@i = s_a@i + d_a@i`
* `ToSmt(duration(a))@i = d_a@i`
* `ToSmt(start(plan))@i = 0`
* `ToSmt(end(plan))@i = t@H`
* `ToSmt(not e)@i = (not ToSmt(e)@i)`
* `ToSmt(e_1 op e_2)@i = ToSmt(e_1)@i op ToSmt(e_2)@i` with `op` being a logic or an arithmetic operator

* `ToSmt([e_1] e_2)@i =` \f[ \bigvee_{j=1}^{H} t@j \ge ToSmt(e_1)@i \wedge (\bigwedge_{j=1}^{H} (t@j-1 < ToSmt(e_1)@i \wedge t@j \ge ToSmt(e_1)@i) \rightarrow ToSmt(e_2)@j-1) \vee (ToSmt(e_1)@i = t@0 \wedge ToSmt(e_2)@0) \f]

* `ToSmt([e_1, e_2] e_3)@i =` \f[ (\bigwedge_{j=0}^{H} (t@j \ge ToSmt(e_1)@i \wedge t@j < ToSmt(e_2)@i) \rightarrow ToSmt(e_3)@j) \wedge \bigvee_{j=1}^{H} t@j \ge ToSmt(e_1)@i \wedge (\bigwedge_{j=1}^{H} (t@j-1 < ToSmt(e_1)@i \wedge t@j \ge ToSmt(e_1)@i) \rightarrow ToSmt(e_3)@j-1) \vee (ToSmt(e_1)@i = t@0 \wedge ToSmt(e_3)@0)\f]

* `ToSmt([e_1, e_2) e_3)@i =` \f[ (\bigwedge_{j=0}^{H} (t@j \ge ToSmt(e_1)@i \wedge t@j < ToSmt(e_2)@i) \rightarrow ToSmt(e_3)@j) \wedge \bigvee_{j=1}^{H} t@j \ge ToSmt(e_1)@i \wedge (\bigwedge_{j=1}^{H} (t@j-1 < ToSmt(e_1)@i \wedge t@j \ge ToSmt(e_1)@i) \rightarrow ToSmt(e_3)@j-1) \vee (ToSmt(e_1)@i = t@0 \wedge ToSmt(e_3)@0)\f]

* `ToSmt((e_1, e_2] e_3)@i =` \f[ (\bigwedge_{j=0}^{H} (t@j \ge ToSmt(e_1)@i \wedge t@j < ToSmt(e_2)@i) \rightarrow ToSmt(e_3)@j) \wedge \bigvee_{j=1}^{H} t@j \ge ToSmt(e_1)@i \wedge (\bigwedge_{j=1}^{H} (t@j-1 \le ToSmt(e_1)@i \wedge t@j > ToSmt(e_1)@i) \rightarrow ToSmt(e_3)@j-1) \vee (ToSmt(e_1)@i = t@0 \wedge ToSmt(e_3)@0)\f]

* `ToSmt((e_1, e_2) e_3)@i =` \f[ (\bigwedge_{j=0}^{H} (t@j \ge ToSmt(e_1)@i \wedge t@j < ToSmt(e_2)@i) \rightarrow ToSmt(e_3)@j) \wedge \bigvee_{j=1}^{H} t@j \ge ToSmt(e_1)@i \wedge (\bigwedge_{j=1}^{H} (t@j-1 \le ToSmt(e_1)@i \wedge t@j > ToSmt(e_1)@i) \rightarrow ToSmt(e_3)@j-1) \vee (ToSmt(e_1)@i = t@0 \wedge ToSmt(e_3)@0)\f]


Given a tamer effect `e` we convert it in SMT at step `i`
(`ToSmt(e)@i`) as follows:

* `ToSmt([e_1] f := e_2)@i =` \f[ (\bigvee_{j=0}^{H} t@j = ToSmt(e_1)@i) \wedge (\bigwedge_{j=0}^{H} t@j = ToSmt(e_1)@i \rightarrow ToSmt(f)@j = ToSmt(e_2)@j) \f]


Frame Axioms
------------

We indicate the set of effects for an action `a` as `effects^a` and the effects of the problem (TILs and Initial state) as `effects^\pi`
For each fluent `f` and each `i` in `[1, H]`

* \f[ f@i-1 \ne f@i \rightarrow  ((\bigvee_{([e_1] f := e_2) \in effects^a} \bigvee_{j=0}^{H} a@j \wedge s_a@j = t@j \wedge t@i = ToSmt(e_1)@i ) \vee (\bigvee_{([e_1] f := e_2) \in effects^\pi} t@i = ToSmt(e1)@0)) \f]



Encoding
--------

We first impose the frame axioms, then we add the following.

* for each expression `e` of the problem instance, we assert `ToSmt(e)@0`

* for each step `i` in `[0, H]` for each action `a` of the problem instance and for each expression `e` in `a`, we assert \f$ (a@i \rightarrow ToSmt(e)@i) \f$
