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
    "PATTY": Patty(pattern="arpg", solver="yices", encoding="binary"),
    "PATTY-Z3": Patty("random", solver="z3", encoding="binary"),
    "PATTY-NL": Patty("random", solver="z3", encoding="non-linear"),
    "PATTY-R-YICES": Patty("random", solver="yices", encoding="binary"),
    "PATTY-R-Z3-NL": Patty("random", solver="z3", encoding="non-linear"),
    "SPRINGROLL": SpringRoll(),
    "ENHSP": ENHSP("WAStar", "aibr"),
    "METRIC-FF": MetricFF(),
}


def main():
    print("Started...")
    s3 = boto3.client('s3', config=my_config)

    envs = Envs()
    logger = CloudLogger(envs.experiment)

    f = open("benchmarks/instances.csv", "r")
    csv = f.read()
    f.close()
    instances = [[v for v in line.split(",")] for line in csv.split("\n")]

    a = min(envs.startFrom + (envs.index * envs.instances), len(instances))
    b = min(envs.startFrom + ((envs.index + 1) * envs.instances), len(instances))

    for el in instances[a:b]:
        planner = PLANNERS[el[0]]
        benchmark = el[1]
        domainFile = el[2]
        problemFile = el[3]

        try:
            r: Result = planner.run(benchmark, domainFile, problemFile, logger)
            print(r)
            print(r.stdout)
            logger.log(r.toCSV())

            s3.put_object(
                Key=f"{envs.experiment}/{r.solver}-{r.domain}-{r.problem}-{time.time_ns()}.txt",
                Bucket="patty-benchmarks",
                Body=bytes(r.stdout, 'utf-8')
            )

        except:
            logger.error(traceback.format_exc())
            print(traceback.format_exc(), file=sys.stderr)


if __name__ == '__main__':
    main()
