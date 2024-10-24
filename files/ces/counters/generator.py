import math
import os
import shutil

MAX_BITS = 15
MAX_COUNTERS = 6
NEWLINE = "\n"


def ce(cond, eff):
    return f'''                    (when
                        (and {"".join(cond)})
                        (and {"".join(eff)})
                    )'''


def main():
    path = "domains"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    for b in range(2, MAX_BITS):

        incr = list()
        decr = list()
        lock = list()

        bits = ["{:02d}".format(i) for i in range(1, b + 1)]

        for i in bits:
            index = int(i)
            cond = [f"(not (x{i} ?a))"] + [f"(x{j} ?a)" for j in reversed(bits[:index - 1])]
            eff = [f"(x{i} ?a)"] + [f"(not (x{j} ?a))" for j in reversed(bits[:index - 1])]
            incr.append(ce(cond, eff))

            cond = [f"(x{i} ?a)"] + [f"(not (x{j} ?a))" for j in reversed(bits[:index - 1])]
            eff = [f"(not (x{i} ?a))"] + [f"(x{j} ?a)" for j in reversed(bits[:index - 1])]
            decr.append(ce(cond, eff))

        oCond = [f"(x{j} ?a)" for j in reversed(bits)]
        oEff = [f"(not (x{j} ?a))" for j in reversed(bits)]
        incr.append(ce(oCond, oEff))
        uCond = [f"(not (x{j} ?a))" for j in reversed(bits)]
        uEff = [f"(x{j} ?a)" for j in reversed(bits)]
        decr.append(ce(uCond, uEff))

        for i in bits:
            lock.append(ce([f"(x{i} ?a)", f"(x{i} ?b)"], [f"(l{i} ?a ?b)"]))
            lock.append(ce([f"(not (x{i} ?a))", f"(not (x{i} ?b))"], [f"(l{i} ?a ?b)"]))
        lock.append("(not (z ?a))")
        lock.append("(not (z ?b))")

        domain = f'''
        (define (domain counters)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (z ?a - counter)
                (next ?a - counter ?b - counter)
                {"".join([f"(l{i} ?a - counter ?b - counter)" for i in bits])}
                {"".join([f"(x{i} ?a - counter)" for i in bits])}
            )

            (:action incr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
{NEWLINE.join([e for e in incr])}
                )
            )
            
            (:action decr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
{NEWLINE.join([e for e in decr])}
                )
            )
            
            (:action lck
                :parameters (?a - counter ?b - counter)
                :precondition(and (next ?a ?b))
                :effect(and
{NEWLINE.join([e for e in lock])}
                )
            )
        )
        '''

        os.makedirs(f"{path}/{b}")
        os.makedirs(f"{path}/{b}/instances")
        with open(f"{path}/{b}/domain-{b}.pddl", "w") as f:
            f.write(domain)

        for c in range(2, MAX_COUNTERS + 1):
            rX = 0
            rY = math.ceil(2 ** (b - 1))
            rXb = format(rX, f"0{b}b")
            rYb = format(rY, f"0{b}b")
            rrXb = list(reversed(rXb))
            rrYb = list(reversed(rYb))

            counters = range(1, c + 1)

            problem = f'''(define (problem pb01)
    (:domain counters)
    (:objects {" ".join([f'c{i}' for i in counters])} - counter)
    (:init
        {"".join([f'(z c{i})' for i in range(1, c + 1)])}
        {"".join([f'(next c{i} c{i + 1})' for i in range(1, c)])}
        {"".join([f"(x{'{:02d}'.format(i + 1)} c{j})" for i in reversed(range(0, b)) if rrXb[i] == '1' for j in counters if j % 1])} ;{rX} - {rXb}
        {"".join([f"(x{'{:02d}'.format(i + 1)} c{j})" for i in reversed(range(0, b)) if rrYb[i] == '1' for j in counters if j % 2])} ;{rY} - {rYb}
    )
    (:goal
        (and  {"".join([f"(l{i} c{j} c{j + 1})" for i in bits for j in range(1, c)])})
    )
    )
            
            '''
            with open(f"{path}/{b}/instances/problem-{b}-{c}.pddl", "w") as f:
                f.write(problem)


if __name__ == '__main__':
    main()
