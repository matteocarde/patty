import os
import shutil
from typing import Tuple, Dict

RECIPES = [
    ["pressure", ["air", "air"]],
    ["energy", ["air", "fire"]],
    ["dust", ["air", "earth"]],
    ["lava", ["earth", "fire"]],
    ["rain", ["air", "water"]],
    ["mud", ["earth", "water"]],
    ["steam", ["fire", "water"]],
    ["sea", ["water", "water"]],
    ["wind", ["air", "energy"]],
    ["stone", ["air", "lava"]],
    ["atmosphere", ["air", "pressure"]],
    # ["cloud", ["air", "steam"]],
    # ["earthquake", ["earth", "energy"]],
    # ["gunpowder", ["dust", "fire"]],
    # ["salt", ["fire", "sea"]],
    # ["volcano", ["earth", "lava"]],
    # ["granite", ["lava", "pressure"]],
    # ["obsidian", ["lava", "water"]],
    # ["brick", ["fire", "mud"]],
    # ["plant", ["earth", "rain"]],
    # ["flood", ["rain", "rain"]],
    # ["ocean", ["sea", "sea"]],
    # ["geyser", ["steam", "earth"]],
    # ["sky", ["air", "cloud"]],
    # ["sand", ["air", "stone"]],
    # ["wall", ["brick", "brick"]],
    # ["fog", ["cloud", "earth"]],
    # ["mountain", ["earth", "earthquake"]],
    # ["storm", ["cloud", "energy"]],
    # ["metal", ["fire", "stone"]],
    # ["explosion", ["fire", "gunpowder"]],
    # ["swamp", ["mud", "plant"]],
    # ["tsunami", ["earthquake", "ocean"]],
    # ["algae", ["ocean", "plant"]],
    # ["isle", ["ocean", "volcano"]],
    # ["wave", ["ocean", "wind"]],
    # ["cotton", ["cloud", "plant"]],
    # ["grass", ["earth", "plant"]],
    # ["tobacco", ["fire", "plant"]],
    # ["seaweed", ["ocean", "plant"]],
    # ["garden", ["plant", "plant"]],
    # ["moss", ["plant", "stone"]],
    # ["coal", ["plant", "pressure"]],
    # ["ash", ["energy", "volcano"]],
    # ["cloud", ["air", "steam"]],
    # ["eruption", ["energy", "volcano"]],
    # ["hurricane", ["energy", "wind"]],
    # ["rust", ["air", "metal"]],
    # ["sound", ["air", "wave"]],
    # ["atomic bomb", ["energy", "explosion"]],
    # ["grenade", ["explosion", "metal"]],
    # ["fireworks", ["explosion", "sky"]],
    # ["glass", ["fire", "sand"]],
    # ["sun", ["fire", "sky"]],
    # ["dew", ["fog", "grass"]],
    # ["bullet", ["gunpowder", "metal"]],
    # ["archipelago", ["isle", "isle"]],
    # ["steel", ["coal", "metal"]],
    # ["electricity", ["energy", "metal"]],
    # ["blade", ["metal", "stone"]],
    # ["mountain range", ["mountain", "mountain"]],
    # ["river", ["mountain", "water"]],
    # ["beach", ["ocean", "sand"]],
    # ["horizon", ["ocean", "sky"]],
    # ["flower", ["garden", "plant"]],
    # ["ivy", ["plant", "wall"]],
    # ["diamond", ["coal", "pressure"]],
    # ["sandstorm", ["energy", "sand"]],
    # ["clay", ["mud", "sand"]],
    # ["cactus", ["plant", "sand"]],
    # ["desert", ["sand", "sand"]],
    # ["quicksand", ["sand", "swamp"]],
    # ["dune", ["sand", "wind"]],
    # ["moon", ["sky", "stone"]],
    # ["boiler", ["metal", "steam"]],
    # ["sandstone", ["sand", "stone"]],
    # ["life", ["energy", "swamp"]],
    # ["house", ["wall", "wall"]],
    # ["pond", ["garden", "water"]],
    # ["bird", ["air", "life"]],
    # ["scissors", ["blade", "blade"]],
    # ["blender", ["blade", "electricity"]],
    # ["scythe", ["blade", "grass"]],
    # ["sword", ["blade", "metal"]],
    # ["golem", ["clay", "life"]],
    # ["pyramid", ["desert", "stone"]],
    # ["oasis", ["desert", "water"]],
    # ["ring", ["diamond", "metal"]],
    # ["human", ["earth", "life"]],
    # ["light bulb", ["electricity", "glass"]],
    # ["wire", ["electricity", "metal"]],
    # ["pottery", ["fire", "clay"]],
    # ["water lily", ["flower", "pond"]],
    # ["sunflower", ["flower", "sun"]],
    # ["glasses", ["glass", "glass"]],
    # ["mirror", ["glass", "metal"]],
    # ["telescope", ["glass", "sky"]],
    # ["death", ["scythe", "human"]],
    # ["zombie", ["death", "human"]],
    # ["mummy", ["zombie", "pyramid"]],
    # ["pharaon", ["mummy", "god"]],
    # ["god", ["death", "life"]]
]

DOMAINS = 2


def main():
    path = "instances"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    elements = set()

    index: Dict[str, int] = {
        "earth": 1,
        "water": 1,
        "air": 1,
        "fire": 1
    }
    parents: Dict[str, Tuple[str, str]] = dict()

    for r in RECIPES:
        elements.add(r[0])
        elements.add(r[1][0])
        elements.add(r[1][1])
        parents[r[0]] = (r[1][0], r[1][1])

    def getIndex(el) -> int:
        if el in index:
            return index[el]
        index[el] = max(getIndex(parents[el][0]), getIndex(parents[el][1])) + 1
        return index[el]

    for el in elements:
        getIndex(el)

    sortedElements = sorted(elements, key=lambda a: -index[a])
    print(sortedElements)

    for i in range(1, DOMAINS + 1):
        problem = f'''(define (problem pb01)
            (:domain counters)
            (:objects {" ".join([f'{el}' for el in elements])} - element)
            (:init
                (have water)
                (have earth)
                (have fire)
                (have air)
                {" ".join([f'(combination {r[1][0]} {r[1][1]} {r[0]})' for r in RECIPES])}
            )
            (:goal
                (and  (have {sortedElements[DOMAINS - (i - 1)]}))
            )
            )

                    '''
        with open(f"{path}/problem-{i}.pddl", "w") as f:
            f.write(problem)


if __name__ == '__main__':
    main()
