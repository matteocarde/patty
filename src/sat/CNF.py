from typing import List

from src.sat.CNFVariable import CNFVariable


class CNF:
    clauses: List[List[int]]

    def __init__(self):
        self.clauses = []

    def addClause(self, clause: List[int or CNFVariable]):
        self.clauses += [[int(l) for l in clause]]
