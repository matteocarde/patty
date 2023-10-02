import copy
import sys
import time
import traceback
from typing import Dict

import boto3
from botocore.config import Config

from classes.CloudLogger import CloudLogger
from classes.ENHSP import ENHSP
from classes.Envs import Envs
from classes.MetricFF import MetricFF
from classes.NFD import NFD
from classes.OMT import OMT
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

    "ENHSP-SAT-HMRP": ENHSP(False, settings="-h hmrp -s gbfs -silent", name="ENHSP-SAT-HMRP"),
    "ENHSP-SAT-HADD": ENHSP(False, settings="-h hadd -s gbfs -silent", name="ENHSP-SAT-HADD"),
    "ENHSP-SAT-HMAX": ENHSP(False, settings="-h hmax -s gbfs -silent", name="ENHSP-SAT-HMAX"),
    "ENHSP-SAT-AIBR": ENHSP(False, settings="-h aibr -s gbfs -silent", name="ENHSP-SAT-AIBR"),
    "ENHSP-SAT-HRADD": ENHSP(False, settings="-h hradd -s gbfs -silent", name="ENHSP-SAT-HRADD"),
    "ENHSP-SAT-BLIND": ENHSP(False, settings="-h blind -s gbfs -silent", name="ENHSP-SAT-BLIND"),

    "ENHSP-OPT-HMRP": ENHSP(False, settings="-h hmrp -s WAStar -silent", name="ENHSP-OPT-HMRP"),
    "ENHSP-OPT-HADD": ENHSP(False, settings="-h hadd -s WAStar -silent", name="ENHSP-OPT-HADD"),
    "ENHSP-OPT-HMAX": ENHSP(False, settings="-h hadd -s WAStar -silent", name="ENHSP-OPT-HMAX"),
    "ENHSP-OPT-AIBR": ENHSP(False, settings="-h aibr -s WAStar -silent", name="ENHSP-OPT-AIBR"),
    "ENHSP-OPT-HRADD": ENHSP(False, settings="-h hradd -s WAStar -silent", name="ENHSP-OPT-HRADD"),
    "ENHSP-OPT-BLIND": ENHSP(False, settings="-h blind -s WAStar -silent", name="ENHSP-OPT-BLIND"),

    "METRIC-FF": MetricFF(),
    "NFD": NFD(),
    "OMT": OMT(),
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
        plName = el[0]
        plSettings = ""
        if "[" in el[0]:
            plName = el[0].split("[")[0]
            plSettings = el[0].split("[")[1][:-1]
        planner = copy.copy(PLANNERS[plName])
        planner.name = el[0]
        planner.addSettings(plSettings)
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
                Key=f"{envs.experiment}/{r.solver}/{r.domain}/{r.problem}/{time.time_ns()}.txt",
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
