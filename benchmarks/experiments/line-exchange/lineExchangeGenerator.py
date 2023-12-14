import os
import time

from experiments.classes.LineExchange import LineExchange


def main():
    folder = f"./instances/{time.time_ns()}/"
    os.makedirs(folder)

    robots = range(2, 6)
    itemsPerRobot = [5, 10, 15]
    distance = [10, 50, 100]
    distribution = [25, 50, 90]

    for r in robots:
        for i in itemsPerRobot:
            for d in distance:
                for p in distribution:
                    l = LineExchange(
                        nOfRobots=r,
                        itemsPerRobot=i,
                        distance=d,
                        distribution=p,
                    )
                    with open(f"{folder}/{r}_{i}_{p}_{d}.pddl", "w") as f:
                        f.write(l.toPDDL())


if __name__ == '__main__':
    main()
