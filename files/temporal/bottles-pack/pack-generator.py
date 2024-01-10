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
    minBottles = 2
    maxBottles = 40
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

    for bottles in range(minBottles, maxBottles + 1, 2):

        pddl = []
        anml = []

        pddl.append(f"(define (problem prob_{bottles})")
        pddl.append("(:domain shake)")
        pddl.append("\t(:objects")
        pddl.append(f"\t\t {' '.join([f'b{i + 1}' for i in range(0, bottles)])} - bottle")
        pddl.append("\t)")
        pddl.append("\t(:init")
        pddl.append(f"\t\t(= (on-platform) 0)")
        pddl.append("\t)")
        pddl.append("\t(:goal")
        pddl.append("\t\t(and")
        for i in range(0, bottles):
            pddl.append(f"\t\t\t(packed b{i + 1})")
        pddl.append("\t\t)")
        pddl.append("\t)")
        pddl.append(")")

        for i in range(0, bottles):
            anml.append(f"instance bottle b{i + 1};")

        anml.append(f"[start] on_platform := 0;")
        for i in range(0, bottles):
            anml.append(f"[start] packed(b{i + 1}) == false;")
        for i in range(0, bottles):
            anml.append(f"[end] packed(b{i + 1}) == true;")

        with open(f"instances/problem_{bottles}.pddl", "w") as f:
            f.write("\n".join(pddl))
            instances += 1

        with open(f"anml/instances/problem_{bottles}.anml", "w") as f:
            f.write("\n".join(anml))

    print(f"Generated {instances} problems")


if __name__ == '__main__':
    main()
