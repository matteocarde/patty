class PDDLWriter:

    def __init__(self):
        self.__rows = []
        self.__tabs = 0

    def write(self, line: str):
        self.__rows.append("\t" * self.__tabs + line)

    def increaseTab(self):
        self.__tabs += 1

    def decreaseTab(self):
        self.__tabs -= 1

    def toString(self):
        return "\n".join(self.__rows)
