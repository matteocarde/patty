import os
import random
import shutil

DOMAINS = 20


def main():
    path = "instances"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    ROBOTS = ["r1", "r2", "r3"]

    for i in range(3, DOMAINS + 1):
        xs = ["x{:02d}".format(j) for j in range(1, i + 1)]
        ys = ["y{:02d}".format(j) for j in range(1, i + 1)]
        zs = ["z{:02d}".format(j) for j in range(1, i + 1)]

        init = [
            [xs[-1], ys[0], zs[0]],
            [xs[0], ys[-1], zs[0]],
            [xs[0], ys[0], zs[-1]]
        ]

        pairsX = zip(xs, xs[1:] + [xs[0]])
        pairsY = zip(ys, ys[1:] + [ys[0]])
        pairsZ = zip(zs, zs[1:] + [zs[0]])

        problem = f'''(define (problem pb{i})
            (:domain grid)
            (:objects 
                {" ".join(xs)} - x
                {" ".join(ys)} - y
                {" ".join(zs)} - z
                {" ".join(ROBOTS)} - robot
            )
            (:init
                {" ".join([f'(isNextX {a} {b})' for (a, b) in pairsX])}
                {" ".join([f'(isNextY {a} {b})' for (a, b) in pairsY])}
                {" ".join([f'(isNextZ {a} {b})' for (a, b) in pairsZ])}
                {" ".join([f'(atX {r} {init[i][0]})' for i, r in enumerate(ROBOTS)])}
                {" ".join([f'(atY {r} {init[i][1]})' for i, r in enumerate(ROBOTS)])}
                {" ".join([f'(atZ {r} {init[i][2]})' for i, r in enumerate(ROBOTS)])}
            )
            (:goal
                (and  
                    {" ".join([f'(atX {r} {xs[-1]})' for i, r in enumerate(ROBOTS)])}
                    {" ".join([f'(atY {r} {ys[-1]})' for i, r in enumerate(ROBOTS)])}
                    {" ".join([f'(atZ {r} {zs[-1]})' for i, r in enumerate(ROBOTS)])}
                )
            )
            )

                    '''
        with open(f"{path}/problem-{i}.pddl", "w") as f:
            f.write(problem)


if __name__ == '__main__':
    main()
