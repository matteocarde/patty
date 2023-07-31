import os
import time

from classes.LineExchange import LineExchange


def main():
    folder = f"../files/line-exchange-quantity/instances/{time.time_ns()}/"
    os.makedirs(folder)

    robots = [4]
    distance = [2]
    distribution = "all-in-first"
    maxQuantity = range(1, 41)

    for r in robots:
        for d in distance:
            for q in maxQuantity:
                l = LineExchange(
                    nOfRobots=r,
                    totalItems=q,
                    distance=d,
                    distribution=distribution,
                    max_q=q
                )
                with open(f"{folder}/{q}.pddl", "w") as f:
                    f.write(l.toPDDL())


if __name__ == '__main__':
    main()
