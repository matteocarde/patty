from src.pddl.Type import Type


class Parameter:
    def __init__(self, name: str, t: Type):
        self.name = name
        self.type = t

    def __repr__(self):
        return f"{self.name} - {self.type.name}"
