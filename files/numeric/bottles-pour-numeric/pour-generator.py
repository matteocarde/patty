import os
import random
import shutil


def generate_random_array(total_sum, array_size):
    # Generate array with random integers

    random_array = [random.randint(1, int(total_sum / array_size)) for _ in range(array_size - 1)]

    # Adjust the last element to ensure the total sum is N
    random_array.append(total_sum - sum(random_array))

    # Shuffle the array to ensure randomness
    random.shuffle(random_array)
    return random_array


def main():
    avgLitresPerBottle = 3
    minBottles = 2
    maxBottles = 20

    pddlFolder = "instances/"
    if os.path.exists(pddlFolder):
        shutil.rmtree(pddlFolder)
    os.mkdir(pddlFolder)
    instances = 0

    for bottles in range(minBottles, maxBottles + 1, 1):
        totalLitres = avgLitresPerBottle * bottles

        for left in range(1, bottles, 2):
            pddl = []
            anml = []
            right = bottles - left

            initLitresLeft = generate_random_array(totalLitres, left)
            goalLitresRight = generate_random_array(totalLitres, right)

            pddl.append(f"(define (problem prob_{bottles}_{left}_{right})")
            pddl.append("(:domain bottles)")
            pddl.append("\t(:objects")
            pddl.append(f"\t\t {' '.join([f'l{i}' for i in range(1, left + 1)])} - bottleleft")
            pddl.append(f"\t\t {' '.join([f'r{i}' for i in range(1, right + 1)])} - bottleright")
            pddl.append("\t)")
            pddl.append("\t(:init")
            for l in range(0, left):
                pddl.append(f"\t\t(= (litres l{l + 1}) {initLitresLeft[l]})")
            for r in range(0, right):
                pddl.append(f"\t\t(= (litres r{r + 1}) 0)")
            pddl.append("\t)")
            pddl.append("\t(:goal")
            pddl.append("\t\t(and")
            for r in range(0, right):
                pddl.append(f"\t\t\t(= (litres r{r + 1}) {goalLitresRight[r]})")
            pddl.append("\t\t)")
            pddl.append("\t)")
            pddl.append(")")

            with open(f"instances/problem_{bottles}_{left}_{right}.pddl", "w") as f:
                f.write("\n".join(pddl))
                instances += 1

    print(f"Generated {instances} problems")


if __name__ == '__main__':
    main()
