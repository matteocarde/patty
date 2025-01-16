import os
import random
import shutil

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

    BITS = range(3, 10)
    TAPES = range(2, 10)
    LENGTH = range(3, 10)

    with open(f"domain-template.pddl", "r") as f:
        domainTemplate = f.read()

    problemIndex = 0
    for b in BITS:

        incrCEs = list()

        bits = ["{:02d}".format(i) for i in range(1, b + 1)]

        for i in bits:
            index = int(i)
            cond = [f"(not (x{i} ?a))"] + [f"(x{j} ?a)" for j in reversed(bits[:index - 1])]
            eff = [f"(x{i} ?a)"] + [f"(not (x{j} ?a))" for j in reversed(bits[:index - 1])]
            incrCEs.append(ce(cond, eff))

        oCond = [f"(x{j} ?a)" for j in reversed(bits)]
        oEff = [f"(not (x{j} ?a))" for j in reversed(bits)]
        incrCEs.append(ce(oCond, oEff))

        incr = f'''
            (:action incr
		        :parameters (?r - robot ?a - counter)
		        :precondition(and
			        (connected ?r ?a)
		        )
                :effect(and
                    {NEWLINE.join([e for e in incrCEs])}
                )
            )
        '''

        domain = domainTemplate.replace(";#INCR#", incr)

        for t in TAPES:
            for l in LENGTH:
                problemIndex = problemIndex + 1

                tapes = ["t{:02d}".format(j) for j in range(1, t + 1)]
                counters = ["a{:02d}".format(j) for j in range(1, t + 1)]
                cells = ["c{:02d}".format(j) for j in range(1, l + 1)]
                bits = ["x{:02d}".format(j) for j in range(1, b + 1)]
                counterCell = cells[len(cells) // 2]

                countersInit = []
                for c in counters:
                    r = random.randint(1, (2 ** b) - 1)
                    rb = list(reversed(format(r, f"0{b}b")))
                    bitsInit = [i + 1 for i in reversed(range(b)) if rb[i] == '1']
                    countersInit += [f"(x{'{:02d}'.format(i)} {c})" for i in bitsInit]

                goal = [(f"({b} {c1})", f"({b} {c2})") for b in bits for c1, c2 in zip(counters[:-1], counters[1:])]

                goalPDDL = [f"(or (and {b1} {b2})(and (not {b1}) (not {b2})))" for (b1, b2) in goal]

                problem = f'''
(define (problem pb{problemIndex})
    (:domain tapes)
    (:objects 
        r - robot
        {" ".join(tapes)} - tape
        {" ".join(counters)} - counter
        {" ".join(cells)} - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        {" ".join([f"(onCellCounter {c} {t} {counterCell})" for c, t in zip(counters, tapes)])}
        (startCell c01)
        {" ".join([f'(isNextCell {a} {b})' for (a, b) in zip(cells, cells[1:] + [cells[0]])])}
        {" ".join([f'(isNextTape {a} {b})' for (a, b) in zip(tapes, tapes[1:] + [tapes[0]])])}
        {" ".join(countersInit)}
    )
    (:goal
        (and  
            {" ".join(goalPDDL)}
        )
    )
    )
 '''
                name = f"{b}-{t}-{l}"
                domainFolder = f"{path}/{name}"
                os.makedirs(domainFolder)
                with open(f"{domainFolder}/domain-{name}.pddl", "w") as f:
                    f.write(domain)
                with open(f"{domainFolder}/problem-{name}.pddl", "w") as f:
                    f.write(problem)


if __name__ == '__main__':
    main()
