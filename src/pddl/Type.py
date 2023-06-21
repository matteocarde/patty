from __future__ import annotations

from typing import List


class Type:

    def __init__(self, name: str, parent: Type = None):
        self.name: str = name
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
