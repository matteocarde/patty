import sys

import traceback

import os

import boto3
import time
from botocore.config import Config
from typing import Dict

from classes.CloudLogger import CloudLogger
from classes.ENHSP import ENHSP
from classes.Envs import Envs
from classes.MetricFF import MetricFF
from classes.Patty import Patty
from classes.Planner import Planner
from classes.Result import Result
from classes.SpringRoll import SpringRoll

my_config = Config(
    region_name='eu-central-1',
)

PLANNERS: Dict[str, Planner] = {
    "PATTY": Patty("PATTY", "arpg", solver="z3", encoding="non-linear"),
    "PATTY-R": Patty("PATTY-R", "random", solver="z3", encoding="non-linear"),
    "SPRINGROLL": SpringRoll(),
    "RANTANPLAN": Patty("RANTANPLAN", "arpg", solver="z3", encoding="non-linear", rollBound=1, hasEffectAxioms=True),
    "ENHSP-HADD": ENHSP("sat-hadd"),
    "ENHSP-HRADD": ENHSP("sat-hradd"),
    "ENHSP-HMRP": ENHSP("sat-hmrphj"),
    "METRIC-FF": MetricFF(),
}


def main():
    print("Started...")
    s3 = boto3.client('s3', config=my_config)

    envs = Envs()
    if envs.isInsideAWS:
        time.sleep(envs.index / 4)

    logger = CloudLogger(envs.experiment)

    f = open(envs.file, "r")
    csv = f.read()
    f.close()
    instances = [[v for v in line.split(",")] for line in csv.split("\n")]

    if envs.isInsideAWS:
        a = min(envs.startFrom + (envs.index * envs.instances), len(instances))
        b = min(envs.startFrom + ((envs.index + 1) * envs.instances), len(instances))
        instances = instances[a:b]

    for el in instances:
        planner = PLANNERS[el[0]]
        benchmark = el[1]
        domainFile = el[2]
        problemFile = el[3]

        try:
            if envs.isInsideAWS:
                print(f"Starting {planner} {benchmark} {domainFile} {problemFile}")
            r: Result = planner.run(benchmark, domainFile, problemFile, logger)
            print(r)
            if not r.solved:
                print(r.stdout)
            logger.log(r.toCSV())
            s3.put_object(
                Key=f"{envs.experiment}/{r.solver}-{r.domain}-{r.problem}-{time.time_ns()}.txt",
                Bucket="patty-benchmarks",
                Body=bytes(r.stdout, 'utf-8')
            )

        except Exception as error:
            if isinstance(error, KeyboardInterrupt):
                print("Interrupted by user...")
                break
            logger.error(traceback.format_exc())
            print(traceback.format_exc(), file=sys.stderr)


if __name__ == '__main__':
    main()
