Command Line Description
========================

TAMER can be used as a command-line plannner. It can be executed from
the system prompt as follows:

```
$> ./tamer (code-generate | convert-to | solve | transform | validate | trace-to-plan | repl) [options] <input-file-1> ... <input-file-n>
```

Tamer automatically combines all the given input files as a single
problem. In this way it is possible to split the "domain part" and the
"problem part" of the ANML instance in separate files and simply
invoke:

```
$> ./tamer (code-generate | convert-to | solve | transform | validate) [options] domain.anml problem.anml
```

The order of the input files is not important.

Also, Tamer is able to read PDDL2.1 specifications using the `--pddl`
flag (see examples below).

Finally, if no input file is given to Tamer, the ANML input is
expected on the command-line as standard input. This is useful to use
the Tamer executable in a pipe with other tools (e.g. a script that
outputs an ANML instance) as follows.

```
$> cat instance.anml | ./tamer (code-generate | convert-to | solve | transform | validate) [options]
```


Functions
---------

* **code-generate** - generates the C++ code of a specialized planner
    and a specialized simulator for the input problem.

* **convert-to** - converts the input ANML problem in the specified target format.

* **solve** - solves the input planning problem.

* **transform** - transforms the input problem using any pipeline of
    the internal TAMER transformers.

* **validate** - validates the provided plan for the input problem.

* **trace-to-plan** - converts the input trace in a plan.

* **repl** - starts an interactive shell. With this function, the input
    files are Python files and they are executed before starting the shell.


Options
-------

The options can be divided in the following groups.


### Generic options

* **logging level** - to set the logging level. The level is a number
    between 0 and 5 with 0 being no-log and 5 being all the log. The
    default is 0.

  `[(--logging-level | -l) <level-value>]`

* **debug** - to enable debug mode, letting exceptions to propagate to
    top-level.

  `[--debug | -D]`

* **pddl** - to indicate that PDDL is expected as input specification
    language instead of ANML.

  `[--pddl | -P]`

* **transformer** - to indicate the transformer to apply to the input
    problem. It is possible to specify multiple transformers and the
    order of specification will be the order of application.

  `[(--transformer | -t) (flattener, action-grounder, full-grounder, temporal-uncertainty-compiler, intermediate-effects-compiler, set-compiler, contains-compiler, partial-order-compiler, empty-conditions-compiler, usertype-fluents-compiler, bounder, constant-promoter, free-var-params-compiler, forall-compiler)]`

* **show problem** - prints the planning problem after transforming it.

  `[--showproblem | -p]`

* **bounding problem** - indicates the bounding problem used by the *bounder* transformer.

  `[(--bounding-problem | -b) <bounding-problem>]`

* **disable-prune-actions** - Disable actions pruning in the grounding.

  `[--disable-prune-actions | -u]`


### code-generate options

* **problem free** - enables problem-free planner code generation. By
    defaul TAMER generates problem-specific code.

  `[--problem-free | -f]`

* **output planner** - indicates the output file name where to save
    the generated planner code. The default is *gplanner.cxx*.

  `[--output-planner <output-planner-file>]`

* **output simulator** - indicates the output file name to save the
    generated simulator code. The default is *gsimulator.cxx*.

  `[--output-simulator <output-simulator-file>]`


### convert-to options

* **target** - to indicate the target format for the conversion of the ANML problem.

  `[--target (ltl | smv | uppaal | pddl)]`

* **output** - to indicate the output file name of the problem encoding in ltl or smv

  `[--output <output-file>]`

* **domain** - to indicate the output file name of the PDDL domain.

  `[--domain <output-domain-file>]`

* **problem** - to indicate the output file name of the PDDL problem.

  `[--problem <output-problem-file>]`

* **model** - to indicate the output file name of the UPPAAL model.

  `[--model <output-model-file>]`

* **query** - to indicate the output file name of the UPPAAL query.

  `[--query <output-query-file>]`


### solve options

* **algorithm** - indicates the name of the planning engine to be
    used. The options are *ftp*, *rlftp*, *ctp*, *smt* or *tsimple*. The default is *ftp*.

  `[(--algorithm | -a) (ftp | rlftp | ctp | smt | tsimple)]`

* **plan epsilon** - to set the time quantum used to separate two
    actions in a partial-order-termporal plan. The default is *0.001*.

  `[(--plan-epsilon | -e) <epsilon-value>]`

* **rational precision** - to force the plan timing to have a rational precision.

  `[--rational precision | -R]`

* **time triggered** - to force the produced plan to be a time-triggered plan.

  `[--time-triggered | -T]`

* **mission** - to force the produced plan to be a mission plan.

  `[--mission | -M]`

* **smt max horizon** - to set the maximal number of steps in SMT-based
    planning. The default is *100*.

  `[(--smt-max-horizon | -H) <number-of-steps>]`

* **smt optimization rounds** - to set the number of optimization steps in
    SMT-based planning. [Not implemented yet]

  `[(--smt-optimization-rounds | -O) <optimization-steps>]`

* **weight** - to set the weight parameter for the tsimple and ftp planners.
    The value is a number between 0 and 1. The default is *0.5*.

  `[(--weight | -w) <weight-value>]`

* **tsimple heuristic** - to indicate the heuristic to be used in the tsimple
    planner. The options are *hlandmarks* or *hplus*. The default is *hplus*.

  `[(--tsimple-heuristic | -A) (hlandmarks | hplus)]`

* **tsimple goals serialization** - to enable goals serialization.

  `[--tsimple-goals-serialization | -S]`

* **iw-disable-tuple-computation-in-initial-states** - Disables the tuple
    computation in the initial states.

  `[--iw-disable-tuple-computation-in-initial-states | -c]`

* **ftp heuristic** - to indicate the heuristic to be used in the ftp
    planner. The options are *hadd*, *hlandmarks*, *hmax*, *hsize*, *blind*,
    *rlvalue* and *rldistance*. Set multiple heuristics to use multi-gbfs.
    The default is *hadd*.

  `[(--ftp-heuristic | -B) (hadd | hlandmarks | hmax | hsize | blind)]`

* **ftp deordering** - to enable deordering in the ftp planner.

  `[--ftp-deordering | -d]`

* **weak equality** - enables weak equality in the ftp and ctp planner.

  `[--weak-equality | -k]`

* **simultaneity** - prunes simultaneous-requiring paths in the ftp and ctp planner.

  `[--simultaneity | -s]`

* **ftp-no-backtracking** - disables backtracking in ftp planner search.

  `[--ftp-no-backtracking]`

* **rlftp model** - to indicate the file name of the neural-network to
    use as heuristic.

  `[(--rlftp-model | -m) <model-file-name>]`

* **rlftp gamma** - to set the gamma value used in the
    reinforcement-learning phase. The default is *0.99*.

  `[--rlftp-gamma <gamma-value>]`

* **rlftp max plan size** - to set the max plan size. The default is *1200*.

  `[--rlftp-max-plan-size <max-plan-size-value>]`

* **rlftp disable use fluents as input** - to disable the use of
    fluents as input in the state vector.

  `[--rlftp-disable-use-fluents-as-input]`

* **rlftp disable use actions as input** - to disable the use of
    actions as input in the state vector.

  `[--rlftp-disable-use-actions-as-input]`

* **rlftp-disable-use-is-applicable-as-input** - to disable the use of
    'is applicable actions' as input in the state vector.

  `[--rlftp-disable-use-is-applicable-as-input]`

* **rlftp-disable-use-was-applied-as-input** - to disable the use of
    'was applied actions' as input in the state vector.

  `[--rlftp-disable-use-was-applied-as-input]`

* **rlftp-disable-use-will-be-applicable-as-input** - to disable the use of
    'will be applicable actions' as input in the state vector.

  `[--rlftp-disable-use-will-be-applicable-as-input]`

* **rlftp disable use constants as input** - to disable the use of
    constants as input in the state vector.

  `[--rlftp-disable-use-constants-as-input]`

* **rlftp disable use goals as input** - to disable the use of goals
    as input in the state vector.

  `[--rlftp-disable-use-goals-as-input]`

* **rlftp disable use tn as input** - to disable the use of tn as
    input in the state vector.

  `[--rlftp-disable-use-tn-as-input]`

* **rlftp use heuristic as input** - to enable the use of the
    heuristic value as input in the state vector.

  `[--rlftp-use-heuristic-as-input]`

* **rlftp use makespan as input** - to enable the use of the makespan
    value as input in the state vector.

  `[--rlftp-use-makespan-as-input]`


### transform options

* **output** - to indicate the output file name where to save the
    transformed problem.

  `[--output <output-file>]`


### validate options

* **plan** - to indicate the plan file name to validate.

  `[--plan <plan-file>]`


### trace-to-plan options

* **input-format** - to indicate the format of the input trace.
    The options are *smv* and *uppaal*.

  `[--input-format (smv | uppaal)]`

* **trace** - to indicate the trace input file name.

  `[--trace <trace-file>]`

* **output** - to indicate the output file name of the generated plan.

  `[--output <output-file>]`


### repl options

* **disable shell** - to disable the interactive shell, allowing only
    the execution of the input files.

  `[--disable-shell | -x]`


Transformers
------------

* **flattener** - to flatten the input problem, by expanding all the
    objects.

* **action-grounder** - to perform the actions grounding (as much as
    possible) on the input problem.

* **full-grounder** - to perform the actions, fluents and constants
    grounding (as much as possible) on the input problem.

* **temporal-uncertainty-compiler** - to compile away temporal
    uncertainty.

* **intermediate-effects-compiler** - to compile away intermediate
    effects.

* **set-compiler** - to compile away sets.

* **contains-compiler** - to compile away contains expressions.

* **partial-order-compiler** - to compile away actions with a partial
    order of time points.

* **empty-conditions-compiler** - to compile away empty conditions.

* **usertype-fluents-compiler** - to compile away usertype fluents.

* **bounder** - to transform the input problem adding the same
    instances of the provided bounding problem.

* **constant-promoter** - rewrites the input problem changing fluents
    that are never assigned after the initial state to constants. This
    improves planning and grounding performances when it applies.

* **free-var-params-compiler** - to compile away fluents used as actual parameters of other fluents or constants.

* **forall-compiler** - to compile away forall expressions.


Tamer REPL
----------

The supported commands are the following.

* `parse_anml(filename)` - parses the input ANML file and returns a `ProblemInstance`.

* `parse_pddl(domain_filename, problem_filename)` - parses the input PDDL files and
   returns a `ProblemInstance`.

* `parse_ttplan(problem, filename)` - parses the input time-triggered plan file and
   returns a `TTPlan` for the input `ProblemInstance`.

* `solve_with_ftp(problem)` - solves the input `ProblemInstance` using the *ftp* planning engine
   and returns a `TTPlan`.

* `solve_with_smt(problem, horizon=100)` - solves the input `ProblemInstance` using the *smt*
   planning engine and returns a `TTPlan`.

* `solve_with_tsimple(problem)` - solves the input `ProblemInstance` using the *tsimple* planning engine
   and returns a `POTPlan`.

* `validate(problem, ttplan)` - validates the input `TTPlan` for the input `ProblemInstance`.

* `flatten_problem(problem)` - flattens the input `ProblemInstance`.

* `ground_action_problem(problem, prune_actions=True)` - grounds the actions of the input `ProblemInstance`.

* `ground_full_problem(problem, prune_actions=True)` - grounds the input `ProblemInstance`.

* `bound_problem(problem, bounding_problem)` - transforms the input `ProblemInstance` adding the same
   instances of the provided bounding `ProblemInstance`.

* `compile_temporal_uncertainty(problem)` - compiles away temporal uncertainty.

* `compile_intermediate_effects(problem)` - compiles away intermediate effects.

* `compile_usertype_fluents(problem)` - compiles away usertype fluents.

* `set_boolean_option(option, value)` - sets the value of the specified option.

* `set_integer_option(option, value)` - sets the value of the specified option.

* `set_float_option(option, value)` - sets the value of the specified option.

* `set_string_option(option, value)` - sets the value of the specified option.

* `ProblemInstance.is_flat()` - returns `True` if the `ProblemInstance` is flat.

* `ProblemInstance.has_temporal_uncertainty()` - returns `True` if the `ProblemInstance`
   has temporal uncertainty.

* `ProblemInstance.to_pddl()` - returns a PDDL 2.1 encoding of the `ProblemInstance`.

* `ProblemInstance.to_ltl()` - returns a LTL encoding of the `ProblemInstance`.


Common Usage Examples
---------------------

In the following, we describe some common example usages of Tamer.


* Solve a general ANML problem with SMT-based planner.

```
$> tamer solve -a smt problem.anml
```

* Solve a general ANML problem with TSimple-based planner.
Note also that this method is unable to solve problem
that have required concurrency.

```
$> tamer solve -a tsimple problem.anml
```

* Solve a general ANML problem with FTP-based planner.

```
$> tamer solve -a ftp problem.anml
```

* Solve a general ANML problem with CTP-based planner.

```
$> tamer solve -a ctp problem.anml
```

* Reading and solving a PDDL2.1 problem.

```
$> tamer solve --pddl domain.pddl problem.pddl
```

* Since Tamer can perform a number of transformations to the planning
problem before actually solving it, it is possible to print the
problem passed to the planning engine with the `-p` flag.

```
$> tamer solve -t full-grounder -p problem.anml
```

* Convert a problem from PDDL2.1 to ANML.

```
$> tamer transform --pddl --output problem.anml domain.pddl problem.pddl
```

* Convert a problem from ANML to PDDL2.1.

```
$> tamer convert-to --target pddl --domain domain.pddl --problem problem.pddl problem.anml
```

* Convert a problem from ANML to LTL.

```
$> tamer convert-to --target ltl --output problem.smv problem.anml
```

* Convert a problem from ANML to SMV.

```
$> tamer convert-to --target smv --output problem.smv problem.anml
```

* Convert a problem from ANML to UPPAAL.

```
$> tamer convert-to --target uppaal --model model.ta --query query.q problem.anml
```

* Generate the C++ code of a specialized planner and simulator.

```
$> tamer code-generate --output-planner gplanner.cxx --output-simulator gsimulator.cxx problem.anml
```

* Generate the C++ code of a *problem free* specialized planner.

```
$> tamer code-generate --output-planner gplanner.cxx  -f problem.anml
```

* Validate a plan.

```
$> tamer validate --plan plan.txt problem.anml
```
