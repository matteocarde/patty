from benchmarks.classes.Result import Result


class Planner:
    name: str

    def __init__(self):
        pass

    def run(self, domain: str, problem: str) -> Result:
        raise NotImplemented()
