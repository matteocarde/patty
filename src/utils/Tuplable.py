from typing import Set, Tuple, List, Iterable, Iterator


class Tuplable:

    def __init__(self):
        pass

    def toTuple(self) -> Tuple:
        raise NotImplementedError()


class TuplableIterable(Iterable[Tuplable]):

    def __init__(self):
        super().__init__()

    def tuples(self) -> List[Tuple]:
        return [x.toTuple() for x in self]

    def tuplesWithSelf(self) -> List[Tuple]:
        return [(x, x.toTuple) for x in self]


class TuplableSet(Set[Tuplable], TuplableIterable):

    def __init__(self):
        super().__init__()


class TuplableList(List[Tuplable], TuplableIterable):

    def __init__(self):
        super().__init__()
