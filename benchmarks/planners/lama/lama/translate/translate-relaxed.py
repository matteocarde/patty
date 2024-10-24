#! /usr/bin/env python2.5
# -*- coding: latin-1 -*-

import axiom_rules
import fact_groups
import instantiate
import pddl
import sas_tasks
import simplify

# TODO: The translator may generate trivial derived variables which are always true,
# for example if there ia a derived predicate in the input that only depends on
# (non-derived) variables which are detected as always true.
# Such a situation was encountered in the PSR-STRIPS-DerivedPredicates domain.
# Such "always-true" variables should best be compiled away, but it is
# not clear what the best place to do this should be. Similar
# simplifications might be possible elsewhere, for example if a
# derived variable is synonymous with another variable (derived or
# non-derived).

ALLOW_CONFLICTING_EFFECTS = False
USE_PARTIAL_ENCODING = True
WRITE_ALL_MUTEXES = True


def strips_to_sas_dictionary(groups):
    dictionary = {}
    for var_no, group in enumerate(groups):
        for val_no, atom in enumerate(group):
            dictionary.setdefault(atom, []).append((var_no, val_no))
    if USE_PARTIAL_ENCODING:
        assert all(len(sas_pairs) == 1
                   for sas_pairs in dictionary.values())
    return [len(group) + 1 for group in groups], dictionary


def translate_strips_conditions(conditions, dictionary, ranges):
    if not conditions:
        return {}  # Quick exit for common case.

    condition = {}
    for fact in conditions:
        atom = pddl.Atom(fact.predicate, fact.args)  # force positive
        for var, val in dictionary[atom]:
            if fact.negated:
                assert False, "neg. precondition: task not in positive normal form"
            if condition.get(var) not in (None, val):
                # Conflicting conditions on this variable: Operator invalid.
                return None
            condition[var] = val
    return condition


def translate_strips_operator(operator, dictionary, ranges):
    # NOTE: This function does not really deal with the intricacies of properly
    # encoding delete effects for grouped propositions in the presence of
    # conditional effects. It should work ok but will bail out in more
    # complicated cases even though a conflict does not necessarily exist.

    condition = translate_strips_conditions(operator.precondition, dictionary, ranges)
    if condition is None:
        return None

    effects = []

    for conditions, fact in operator.add_effects:
        eff_condition = translate_strips_conditions(conditions, dictionary, ranges)
        if eff_condition is None:  # Impossible condition for this effect.
            continue
        eff_condition = list(eff_condition.items())
        for var, val in dictionary[fact]:
            effects.append((var, val, eff_condition))

    for conditions, fact in operator.del_effects:
        eff_condition_dict = translate_strips_conditions(conditions, dictionary, ranges)
        if eff_condition_dict is None:
            continue
        eff_condition = list(eff_condition_dict.items())
        for var, val in dictionary[fact]:
            none_of_those = ranges[var] - 1

            effects.append((var, none_of_those, eff_condition))

    pre_post = []
    for var, post, eff_condition in effects:
        pre = condition.get(var, -1)
        if pre != -1:
            del condition[var]
        pre_post.append((var, pre, post, eff_condition))
    prevail = list(condition.items())

    return sas_tasks.SASOperator(operator.name, prevail, pre_post, operator.cost)


def translate_strips_axiom(axiom, dictionary, ranges):
    condition = translate_strips_conditions(axiom.condition, dictionary, ranges)
    if condition is None:
        return None
    if axiom.effect.negated:
        [(var, _)] = dictionary[axiom.effect.positive()]
        effect = (var, ranges[var] - 1)
    else:
        [effect] = dictionary[axiom.effect]
    return sas_tasks.SASAxiom(list(condition.items()), effect)


def translate_strips_operators(actions, strips_to_sas, ranges):
    result = []
    for action in actions:
        sas_op = translate_strips_operator(action, strips_to_sas, ranges)
        if sas_op:
            result.append(sas_op)
    return result


def translate_strips_axioms(axioms, strips_to_sas, ranges):
    result = []
    for axiom in axioms:
        sas_axiom = translate_strips_axiom(axiom, strips_to_sas, ranges)
        if sas_axiom:
            result.append(sas_axiom)
    return result


def translate_task(strips_to_sas, ranges, init, goals, actions, axioms):
    axioms, axiom_init, axiom_layer_dict = axiom_rules.handle_axioms(
        actions, axioms, goals)
    init = init + axiom_init
    # axioms.sort(key=lambda axiom: axiom.name)
    # for axiom in axioms:
    #  axiom.dump()

    init_values = [rang - 1 for rang in ranges]
    # Closed World Assumption: Initialize to "range - 1" == Nothing.
    for fact in init:
        pair = strips_to_sas.get(fact)
        pairs = strips_to_sas.get(fact, [])  # empty for static init facts
        for var, val in pairs:
            assert init_values[var] == ranges[var] - 1, "Inconsistent init facts!"
            init_values[var] = val
    init = sas_tasks.SASInit(init_values)

    goal_pairs = list(translate_strips_conditions(goals, strips_to_sas, ranges).items())
    goal = sas_tasks.SASGoal(goal_pairs)

    operators = translate_strips_operators(actions, strips_to_sas, ranges)
    axioms = translate_strips_axioms(axioms, strips_to_sas, ranges)

    axiom_layers = [-1] * len(ranges)
    for atom, layer in axiom_layer_dict.items():
        assert layer >= 0
        [(var, val)] = strips_to_sas[atom]
        axiom_layers[var] = layer
    variables = sas_tasks.SASVariables(ranges, axiom_layers)

    return sas_tasks.SASTask(variables, init, goal, operators, axioms)


def unsolvable_sas_task(msg):
    print("%s! Generating unsolvable task..." % msg)
    variables = sas_tasks.SASVariables([2], [-1])
    init = sas_tasks.SASInit([0])
    goal = sas_tasks.SASGoal([(0, 1)])
    operators = []
    axioms = []
    return sas_tasks.SASTask(variables, init, goal, operators, axioms)


def pddl_to_sas(task):
    print("Instantiating...")
    relaxed_reachable, atoms, actions, axioms = instantiate.explore(task)

    if not relaxed_reachable:
        return unsolvable_sas_task("No relaxed solution")

    # HACK! Goals should be treated differently (see TODO file).
    if isinstance(task.goal, pddl.Conjunction):
        goal_list = task.goal.parts
    else:
        goal_list = [task.goal]
    for item in goal_list:
        assert isinstance(item, pddl.Literal)

    #    groups, mutex_groups, translation_key = fact_groups.compute_groups(
    #        task, atoms, return_mutex_groups=WRITE_ALL_MUTEXES,
    #        partial_encoding=USE_PARTIAL_ENCODING)

    # switched off invariant syntheses -> one group for each fluent fact
    groups = [[fact] for fact in atoms]
    translation_key = [[str(fact), str(fact.negate())] for group in groups
                       for fact in group]

    print("Building STRIPS to SAS dictionary...")
    ranges, strips_to_sas = strips_to_sas_dictionary(groups)
    print("Translating task...")
    sas_task = translate_task(strips_to_sas, ranges, task.init, goal_list,
                              actions, axioms)

    try:
        simplify.filter_unreachable_propositions(
            sas_task, [], translation_key)
    except simplify.Impossible:
        return unsolvable_sas_task("Simplified to trivially false goal")

    write_translation_key(translation_key)
    return sas_task


def build_mutex_key(strips_to_sas, groups):
    group_keys = []
    for group in groups:
        group_key = []
        for fact in group:
            if strips_to_sas.get(fact):
                for var, val in strips_to_sas[fact]:
                    group_key.append((var, val, str(fact)))
            else:
                print("not in strips_to_sas, left out:", fact)
        group_keys.append(group_key)
    return group_keys


def write_translation_key(translation_key):
    groups_file = file("test.groups", "w")
    for var_no, var_key in enumerate(translation_key):
        print("var%d:" % var_no, file=groups_file)
        for value, value_name in enumerate(var_key):
            print("  %d: %s" % (value, value_name), file=groups_file)
    groups_file.close()


def write_mutex_key(mutex_key):
    invariants_file = file("all.groups", "w")
    print("begin_groups", file=invariants_file)
    print(len(mutex_key), file=invariants_file)
    for group in mutex_key:
        # print map(str, group)
        no_facts = len(group)
        print("group", file=invariants_file)
        print(no_facts, file=invariants_file)
        for var, val, fact in group:
            # print fact
            assert str(fact).startswith("Atom ")
            predicate = str(fact)[5:].split("(")[0]
            # print predicate
            rest = str(fact).split("(")[1]
            rest = rest.strip(")").strip()
            if not rest == "":
                # print "there are args" , rest
                args = rest.split(",")
            else:
                args = []
            print_line = "%d %d %s %d " % (var, val, predicate, len(args))
            for arg in args:
                print_line += str(arg).strip() + " "
            # print fact
            # print print_line
            print(print_line, file=invariants_file)
    print("end_groups", file=invariants_file)
    invariants_file.close()


if __name__ == "__main__":
    import pddl

    print("Parsing...")
    task = pddl.open()
    if task.domain_name in ["protocol", "rover"]:
        # This is, of course, a HACK HACK HACK!
        # The real issue is that ALLOW_CONFLICTING_EFFECTS = True
        # is actually the correct semantics, but then we don't get to filter
        # out operators that are impossible to apply due to mutexes between
        # different SAS+ variables. For example,
        # ALLOW_CONFLICTING_EFFECTS = True does not filter on(a,a) in
        # blocksworld/4-0.
        ALLOW_CONFLICTING_EFFECTS = True

    # EXPERIMENTAL!
    # import psyco
    # psyco.full()

    sas_task = pddl_to_sas(task)
    print("Writing output...")
    sas_task.output(file("output.sas", "w"))
    print("Done!")
    print("Creating dummy output:")
    open("all.groups", "w").write("dummy file expected by our scripts\n")
