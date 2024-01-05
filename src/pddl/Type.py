from __future__ import annotations

from typing import List

from src.pddl.PDDLWriter import PDDLWriter


class Type:

    def __init__(self, name: str, parent: Type = None):
        self.name: str = name.lower()
        self.parent: Type = parent
        self.children: List[Type] = list()

    def addChild(self, c: Type):
        self.children.append(c)

    def __repr__(self):
        return f"{self.name} - {self.parent}"

    def getMeAndMyChildren(self):
        children = [self]
        for c in self.children:
            children += c.getMeAndMyChildren()
        return children

    def __eq__(self, other):
        if not isinstance(other, Type):
            return False
        return self.name == other.name and self.parent == other.parent

    def toPDDL(self, pw=PDDLWriter()):
        if self.parent:
            pw.write(f"{self.name} - {self.parent.name}")
        else:
            pw.write(f"{self.name}")
        return pw
