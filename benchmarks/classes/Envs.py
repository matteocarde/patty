import os


class Envs:

    def __init__(self):
        self.experiment = os.getenv("EXPERIMENT_NAME", "local")
        self.index = int(os.getenv("AWS_BATCH_JOB_ARRAY_INDEX", 0))
        self.instances = int(os.getenv("INSTANCES_PER_MACHINE", 10))
        self.startFrom = int(os.getenv("INSTANCES_START_FROM", 0))
        self.file = os.getenv("FILE", "benchmarks/instances-smt.csv")
        self.isInsideAWS = "AWS_BATCH_JOB_ID" in os.environ
