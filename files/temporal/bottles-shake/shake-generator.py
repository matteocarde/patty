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
    minBottles = 1
    maxBottles = 20
    litresPerBottle = 5

    pddlFolder = "instances/"
    anmlFolder = "anml/instances"
    if os.path.exists(pddlFolder):
        shutil.rmtree(pddlFolder)
    if os.path.exists(anmlFolder):
        shutil.rmtree(anmlFolder)
    os.mkdir(pddlFolder)
    os.mkdir(anmlFolder)
    instances = 0

    for bottles in range(minBottles, maxBottles + 1, 1):

        pddl = []
        anml = []

        pddl.append(f"(define (problem prob_{bottles})")
        pddl.append("(:domain shake)")
        pddl.append("\t(:objects")
        pddl.append(f"\t\t {' '.join([f'b{i + 1}' for i in range(0, bottles)])} - bottle")
        pddl.append("\t)")
        pddl.append("\t(:init")
        for i in range(0, bottles):
            pddl.append(f"\t\t(= (litres b{i + 1}) {litresPerBottle})")
        pddl.append("\t)")
        pddl.append("\t(:goal")
        pddl.append("\t\t(and")
        for i in range(0, bottles):
            pddl.append(f"\t\t\t(= (litres b{i + 1}) 0)")
        pddl.append("\t\t)")
        pddl.append("\t)")
        pddl.append(")")

        for i in range(0, bottles):
            anml.append(f"instance bottle b{i + 1};")

        for i in range(0, bottles):
            anml.append(f"[start] litres(b{i + 1}) := {litresPerBottle};")
        for i in range(0, bottles):
            anml.append(f"[end] litres(b{i + 1}) == 0;")

        with open(f"instances/problem_{bottles}.pddl", "w") as f:
            f.write("\n".join(pddl))
            instances += 1

        with open(f"anml/instances/problem_{bottles}.anml", "w") as f:
            f.write("\n".join(anml))

    print(f"Generated {instances} problems")


if __name__ == '__main__':
    main()
