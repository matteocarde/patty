import sys
import time
import traceback
from typing import Dict

import boto3
from botocore.config import Config

from classes.CloudLogger import CloudLogger
from classes.ENHSP import ENHSP
from classes.Envs import Envs
from classes.Patty import Patty
from classes.Planner import Planner
from classes.Result import Result

my_config = Config(
    region_name='eu-central-1',
)

PLANNERS: Dict[str, Planner] = {
    "PATTY": Patty("PATTY", search="step"),
    "PATTY-STATIC": Patty("PATTY-STATIC", search="static"),
    "PATTY-ASTAR": Patty("PATTY-ASTAR", search="astar-nomax"),
    "PATTY-ASTAR-MAX": Patty("PATTY-ASTAR-MAX", search="astar"),
    "PATTY-ASTAR-MAX-SCCS": Patty("PATTY-ASTAR-MAX-SCCS", search="astar", useSCCs=True),
    "PATTY-ASTAR-MAX-NO-P": Patty("PATTY-ASTAR-MAX-NO-P", search="astar", avoidP=True),
    "PATTY-ASTAR-MAX-NO-P-SCCS": Patty("PATTY-ASTAR-MAX-NO-P-SCCS", search="astar", avoidP=True, useSCCs=True),
    # "PATTY-EXPLICIT": Patty("PATTY-EXPLICIT", "arpg", solver="z3" hasEffectAxioms=True),
    # "PATTY-CONCAT": Patty("PATTY-CONCAT", "arpg", solver="z3", encoding="non-linear", concatPatterns=True),
    # "PATTY-R": Patty("PATTY-R", "random", solver="z3", encoding="non-linear"),
    # "SPRINGROLL": SpringRoll(),
    # "RANTANPLAN": Patty("RANTANPLAN", "arpg", solver="z3", encoding="non-linear", rollBound=1, hasEffectAxioms=True),
    "ENHSP-HADD": ENHSP("sat-hadd"),
    "ENHSP-HRADD": ENHSP("sat-hradd"),
    "ENHSP-HMRP": ENHSP("sat-hmrphj"),
    # "METRIC-FF": MetricFF(),
    # "NFD": NFD(),
    # "OMT": OMT(),
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
            r: Result = planner.run(benchmark, domainFile, problemFile, logger, envs.timeout)
            print(r)
            if not r.solved:
                print(r.stdout)
            logger.log(r.toCSV())
            s3.put_object(
                Key=f"{envs.experiment}/{r.solver}/{r.domain.replace('/', '_')}/{r.problem.replace('/', '_')}/{time.time_ns()}.txt",
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
