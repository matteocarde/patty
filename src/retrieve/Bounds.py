from __future__ import annotations
import json
from typing import Tuple, Dict

from src.pddl.Atom import Atom
from src.pddl.Domain import GroundedDomain


class Bounds:

    def __init__(self):
        self.interval: Dict[Atom, Tuple[float, float]] = dict()

    @classmethod
    def fromFile(cls, file: str, domain: GroundedDomain) -> Bounds:
        b = cls()

        f = open(file, "r")
        jsonStr = f.read()
        f.close()

        boundsJson = json.loads(jsonStr)

        for atom in domain.functions:
            if atom.name in boundsJson:
                b.interval[atom] = (float(boundsJson[atom.name][0]), float(boundsJson[atom.name][1]))

        return b
