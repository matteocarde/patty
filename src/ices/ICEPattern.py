from typing import List

from src.ices.Happening import Happening
from src.ices.ICEAction import ICEAction


class ICEPattern:
    pattern: List[Happening]

    def __init__(self):
        self.pattern = list()
