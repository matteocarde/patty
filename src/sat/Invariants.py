import re
import subprocess
from typing import List

from src.pddl.Domain import GroundedDomain
from src.pddl.Literal import Literal
from src.pddl.Problem import Problem
from src.utils.TimeStat import TimeStat


class Invariants:
    __invariants: List[List[Literal]]

    def __init__(self, domain: GroundedDomain, problem: Problem):
        t = TimeStat.startHolder("Computing Invariants with Madagascar")
        invariantsText = Invariants.__run_madagascar(domain.path, problem.path)
        t.endHolderMilliseconds()

        name2Var = {v.getFunctionName(): v for v in domain.predicates}

        pattern = re.compile(r"^(~?)(.*?) OR (~?)(.*?)$")
        self.__invariants = []

        for line in invariantsText.splitlines():
            match = pattern.fullmatch(line.strip())

            if match:
                posLeft = match.group(1) != "~"
                leftAtom = name2Var[match.group(2)]
                posRight = match.group(3) != "~"
                rightAtom = name2Var[match.group(4)]

                left = Literal.pos(leftAtom) if posLeft else Literal.neg(leftAtom)
                right = Literal.pos(rightAtom) if posRight else Literal.neg(rightAtom)

                self.__invariants.append([left, right])

    def __iter__(self):
        return iter(self.__invariants)

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
