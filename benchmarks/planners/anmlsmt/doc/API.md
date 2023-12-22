API
===

Overview
--------

TAMER offers a comprehensive API that allows to interact with the
system modeling framework and to the algorithms.

From the API it is possible to parse a file or to construct a problem
through the API functions. When a problem is built, it is possible to
call a planning algorithm and to analyze the generated plan.


Usage
-----

First of all, it is necessary to create a new [environment](@ref tamer_env).

Then the planning problem can be provided by the parser or can be
built through the API functions.

* To get the planning problem from a file it is necessary to provide
the filename to the [ANML parser function](@ref tamer_parse_anml) or
to the [PDDL parser function](@ref tamer_parse_pddl).

* To build a planning problem it is needed first of all to create a
new [problem instance](@ref tamer_problem) and then to add to it all
the [actions](@ref tamer_action), the [fluents](@ref tamer_fluent),
the [constants](@ref tamer_constant), the [user types](@ref tamer_type),
the [instances](@ref tamer_instance), the initialization
[expressions](@ref tamer_expr) and the goals.

When the planning problem is built, it is possible to apply several
transformations to it.  It is possible to [ground](@ref tamer_problem_ground)
it, to [flatten](@ref tamer_problem_flatten) it, to
[compile away the temporal uncertainty](@ref tamer_problem_temporal_uncertainty_compiler)
and/or to [compile away the intermediate effects](@ref tamer_problem_intermediate_effects_compiler).

When the final planning problem is obtained, it is possible to call
one of the planning algorithms: the [tsimple](@ref tamer_do_tsimple_planning)
or the [SMT-based](@ref tamer_do_smt_planning).

The default heuristic for the tsimple algorithm is *hplus*.  To change
the heuristic used by the tsimple algorithm, it is necessary to call
the [set configuration function](@ref tamer_env_set_string_option)
with *heuristic* as key and *hplus* or *hlandmarks* as value. For the
*hplus* heuristic it can also be possible to [set](@ref tamer_env_set_float_option)
the *tsimple-weight*.  For the *SMT-based* there is the possibility to
[set](@ref tamer_env_set_integer_option) the *max-horizon*.

The result of the planning algorithms is a [time triggered plan](@ref tamer_ttplan)
or a [partial order plan](@ref tamer_potplan). It can be possible to
[set](@ref tamer_env_set_string_option) the *plan-epsilon*. The API
provides several functions to analyze the plan and to get all the
needed information from it.
