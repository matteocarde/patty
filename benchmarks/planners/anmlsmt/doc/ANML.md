ANML Input Language
===================

Tamer uses the ANML language as its default input specification
language. We use a dense interpretation of time and support a subset
of the features of the ANML language.


### (Still) Unsupported Features
* HTN features
* Interval labels (e.g. `[all] contains g1: x;`) and interval constraints (e.g. `g1 < g2`)
* Set and vector types
* Uncertainty and set operators (except for `:in` in durations to express temporal uncertainty)


#### Note:

This document is still a draft and needs more detailed explanation of
the language and its features.


Extensions
----------

We added few syntactical extensions to the language.


### Constants default values

ANML does not have a way to specify default values for function
constants. For example, consider the following declaration.

```
constant integer c(float x);
```

ANML allows to initialize a finite number of points of constant
`c`. For example:

```
c(0.1) := 3;
c(3.14) := 2;
```

but there is no way to set a default value to the constant that is
taken when a point where the constant has not been initialized is
queried. We extended the ANML syntax to allow this specification.

```
c(*) := 0; \\ Indicates that c is 0 in all the points where the c function is not explicitly initialized
```

Moreover, for constant functions having multiple arguments, we allow
for partial specification of the argument list to express default
values. For example:

```
constant integer c(float x, integer y);

c(1.0, 2) := 4;
c(1.0, *) := 0; // Sets to 0 all the values of the function having 0.1 as first parameter (except for the points set explicitly such as (1.0, 2))
c(2.0, *) := 10;
c(*) := -1;
```

This feature is useful for representing the flattening of general ANML
models. Consider the following example:

```
type T with {
  constant integer c(integer x, float y);
  ....
}
instance T a, b;
a.c(*) := 9; // Pseudo-syntax for the default value
a.c(1, 3.14) := 0;
b.c(*) := 1;
b.c(1, 6.28) := 0;
```

If we want to express the very same model without using structured
types we can produce the following model.

```
type T;
constant T_c(T object, integer x, float y);

instance T a, b;
T_c(a, *) := 9;
T_c(b, *) := 1;

T_c(a, 1, 3.14) := 0;
T_c(b, 1, 6.28) := 0;
```

This is the actual output of the Tamer flattener transformer that gets
rid of the object-oriented syntactic sugar.

#### Note

The order of assignment instruction is not relevant: more specific
assignments are always preferred to more general ones. Moreover, it is
forbidden to assign multiple times the same value of the same
constant.
