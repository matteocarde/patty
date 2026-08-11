import re
import subprocess
from typing import List, Tuple, Dict, Set

from pyeda_linux.boolalg.expr import Atom
from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.utils.TimeStat import TimeStat


class Invariants:
    __invariants: List[Tuple[Literal, Literal]]
    __invariantsByAtom: Dict[Atom, Set[Tuple[Literal, Literal]]]

    def __init__(self, domain: GroundedDomain, problem: Problem):
        t = TimeStat.startHolder("Computing Invariants with Madagascar")
        invariantsText = Invariants.__run_madagascar(domain.path, problem.path)
        t.endHolderMilliseconds()

        name2Var = {v.getFunctionName(): v for v in domain.predicates}

        pattern = re.compile(r"^(~?)(.*?) OR (~?)(.*?)$")
        self.__invariants = []
        self.__invariantsByAtom = dict()

        for line in invariantsText.splitlines():
            match = pattern.fullmatch(line.strip())

            if match:
                posLeft = match.group(1) != "~"
                leftAtom = name2Var[match.group(2)]
                posRight = match.group(3) != "~"
                rightAtom = name2Var[match.group(4)]

                left: Literal = Literal.pos(leftAtom) if posLeft else Literal.neg(leftAtom)
                right: Literal = Literal.pos(rightAtom) if posRight else Literal.neg(rightAtom)

                inv: Tuple[Literal, Literal] = (left, right)

                self.__invariantsByAtom.setdefault(left.atom, set())
                self.__invariantsByAtom[left.atom].add(inv)
                self.__invariantsByAtom.setdefault(right.atom, set())
                self.__invariantsByAtom[right.atom].add(inv)

                self.__invariants.append(inv)

    def __iter__(self):
        return iter(self.__invariants)

    def getInvariantsConcerningAtom(self, v: Atom) -> Set[Tuple[Literal, Literal]]:
        return self.__invariantsByAtom.get(v, set())

    @staticmethod
    def __run_madagascar(domain_file, instance_file) -> str:
        result = subprocess.run(
            [
                "/Users/carde/Bin/madagascar/madagascar",
                domain_file,
                instance_file,
                "-I",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout
