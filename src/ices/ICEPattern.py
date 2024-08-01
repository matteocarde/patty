from typing import List

from src.ices.ICEAction import ICEAction


class ICEPattern:
    pattern: List[ICEAction]

    def __init__(self):
        self.pattern = list()
