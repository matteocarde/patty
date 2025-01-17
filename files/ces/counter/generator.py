import math
import os
import shutil

MAX_BITS = 15
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

        bits = ["{:02d}".format(i) for i in range(1, b + 1)]

        for i in bits:
            index = int(i)
            cond = [f"(not (x{i}))"] + [f"(x{j})" for j in reversed(bits[:index - 1])]
            eff = [f"(x{i})"] + [f"(not (x{j}))" for j in reversed(bits[:index - 1])]
            incr.append(ce(cond, eff))

        oCond = [f"(x{j})" for j in reversed(bits)]
        oEff = [f"(not (x{j}))" for j in reversed(bits)]
        incr.append(ce(oCond, oEff))

        domain = f'''
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                {"".join([f"(x{i})" for i in bits])}
            )

            (:action incr
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in incr])}
                )
            )
        )
        '''

        os.makedirs(f"{path}/{b}")
        with open(f"{path}/{b}/domain-{b}.pddl", "w") as f:
            f.write(domain)

        problem = f'''(define (problem pb01)
(:domain counters)
(:init

)
(:goal
    (and  (x{bits[-1]}))
)
)
        
        '''
        with open(f"{path}/{b}/problem-{b}.pddl", "w") as f:
            f.write(problem)


if __name__ == '__main__':
    main()
