import os
import sys


def main():
    experiment = "experiments/performances/1680514712.829303"

    valid = 0
    total = 0

    for domain in os.listdir(experiment):
        if domain in {"results.csv"}:
            continue

        for problem in os.listdir(f"{experiment}/{domain}"):
            if "ERRORED" in problem:
                continue

            f = open(f"{experiment}/{domain}/{problem}", "r")
            plan = f.read()
            f.close()

            if len(plan) == 0:
                continue

            val = "/Users/carde/Bin/VAL/Validate"
            cmd = f"{val} files/{domain}/domain.pddl files/{domain}/instances/{problem} {experiment}/{domain}/{problem}"
            result = os.popen(cmd).read()
            if "Plan valid" in result:
                print(domain, problem, "Valid")
                valid += 1
            else:
                print(domain, problem, "Invalid", file=sys.stderr)
            total += 1

    print(f"{round(valid / total * 100, 2)}% valid")


if __name__ == '__main__':
    main()
