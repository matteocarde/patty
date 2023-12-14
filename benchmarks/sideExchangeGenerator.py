import os

from benchmarks.classes.SideExchange import SideExchange


def main():
    folder = f"../files/side-exchange/instances"
    # os.makedirs(folder)

    robots = 3
    quantities = range(1, 40)

    for q in quantities:
        print(f"Creating {q}")
        problem = SideExchange(
            nOfRobots=robots,
            itemsPerBin=q
        )
        with open(f"{folder}/{q}.pddl", "w") as f:
            f.write(problem.toPDDL())


if __name__ == '__main__':
    main()
