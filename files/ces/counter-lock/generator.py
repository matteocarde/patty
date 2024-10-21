import os
import random
import shutil

MAX_BITS = 20
VARS = ["x", "y"]
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

        incr = dict([(v, list()) for v in VARS])
        decr = dict([(v, list()) for v in VARS])
        lock = list()

        for v in VARS:
            for i in range(1, b + 1):
                cond = [f"(not ({v}{i}))"] + [f"({v}{j})" for j in reversed(range(1, i))] + [f"(not (l{j}))" for j in
                                                                                             reversed(range(1, i + 1))]
                eff = [f"({v}{i})"] + [f"(not ({v}{j}))" for j in reversed(range(1, i))]
                incr[v].append(ce(cond, eff))

                cond = [f"({v}{i})"] + [f"(not ({v}{j}))" for j in reversed(range(1, i))] + [f"(not (l{j}))" for j in
                                                                                             reversed(range(1, i + 1))]
                eff = [f"(not ({v}{i}))"] + [f"({v}{j})" for j in reversed(range(1, i))]
                decr[v].append(ce(cond, eff))

            oCond = [f"({v}{j})" for j in reversed(range(1, b + 1))] + [f"(not (l{j}))" for j in
                                                                        reversed(range(1, b + 1))]
            oEff = [f"(not ({v}{j}))" for j in reversed(range(1, b + 1))]
            incr[v].append(ce(oCond, oEff))
            uCond = [f"(not ({v}{j}))" for j in reversed(range(1, b + 1))] + [f"(not (l{j}))" for j in
                                                                              reversed(range(1, b + 1))]
            uEff = [f"({v}{j})" for j in reversed(range(1, b + 1))]
            decr[v].append(ce(uCond, uEff))

        for i in range(1, b + 1):
            lock.append(ce([f"(x{i})", f"(y{i})"], [f"(l{i})"]))
            lock.append(ce([f"(not (x{i}))", f"(not (y{i}))"], [f"(l{i})"]))

        domain = f'''
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:predicates
                {"".join([f"(x{i})" for i in range(1, b + 1)])}
                {"".join([f"(y{i})" for i in range(1, b + 1)])}
                {"".join([f"(l{i})" for i in range(1, b + 1)])}
            )

            (:action inx
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in incr['x']])}
                )
            )
            (:action iny
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in incr['y']])}
                )
            )
            
            (:action dex
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in decr['x']])}
                )
            )
            (:action dey
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in decr['y']])}
                )
            )
            (:action lck
                :parameters ()
                :precondition()
                :effect(and
{NEWLINE.join([e for e in lock])}
                )
            )
        )
        '''

        os.makedirs(f"{path}/{b}")
        with open(f"{path}/{b}/domain-{b}.pddl", "w") as f:
            f.write(domain)

        rX = random.randint(0, (2 ** b) - 1)
        rY = random.randint(0, (2 ** b) - 1)
        rXb = format(rX, f"0{b}b")
        rYb = format(rY, f"0{b}b")
        rrXb = list(reversed(rXb))
        rrYb = list(reversed(rYb))

        problem = f'''(define (problem pb01)
  (:domain counter)

  (:init
    {"".join([f"(x{i + 1})" for i in reversed(range(0, b)) if rrXb[i] == '1'])} ;{rX} - {rXb}
    {"".join([f"(y{i + 1})" for i in reversed(range(0, b)) if rrYb[i] == '1'])} ;{rY} - {rYb}
  )
  (:goal
    (and  {"".join([f"(l{i})" for i in range(1, b + 1)])})
  )
)
        
        '''
        with open(f"{path}/{b}/problem-{b}.pddl", "w") as f:
            f.write(problem)


if __name__ == '__main__':
    main()
