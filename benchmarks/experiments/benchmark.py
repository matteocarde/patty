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
from classes.ITSAT import ITSAT
from classes.LPG import LPG
from classes.MetricFF import MetricFF
from classes.NFD import NFD
from classes.OMT import OMT
from classes.Optic import Optic
from classes.Patty import Patty
from classes.Planner import Planner
from classes.Result import Result
from classes.SpringRoll import SpringRoll
from classes.TFD import TFD

my_config = Config(
    region_name='eu-central-1',
)

PLANNERS: Dict[str, Planner] = {
    "PATTY-O": Patty("PATTY-O", search="step"),
    "PATTY-G": Patty("PATTY-G", search="static"),
    "PATTY-H": Patty("PATTY-H", search="astar", noCompression=True),
    "PATTY-F": Patty("PATTY-F", search="astar", noCompression=False),

    "PATTY-R": Patty("PATTY-R", search="step", pattern="random", quality="none"),
    "PATTY-A": Patty("PATTY-A", search="step", pattern="arpg", quality="none"),
    "PATTY-E": Patty("PATTY-E", search="step", pattern="enhanced", quality="none"),
    "PATTY-FA": Patty("PATTY-FA", search="astar", pattern="arpg", quality="none"),
    "PATTY-FE": Patty("PATTY-FE", search="astar", pattern="enhanced", quality="none"),
    "PATTY-M": Patty("PATTY-M", search="step", pattern="enhanced", quality="shortest-step"),
    "SPRINGROLL": SpringRoll(),

    "ENHSP-SAT-HMRP": ENHSP(False, settings="-h hmrp -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMRP"),
    "ENHSP-SAT-HADD": ENHSP(False, settings="-h hadd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HADD"),
    "ENHSP-SAT-HMAX": ENHSP(False, settings="-h hmax -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMAX"),
    "ENHSP-SAT-AIBR": ENHSP(False, settings="-h aibr -s gbfs -silent -pp -pe", name="ENHSP-SAT-AIBR"),
    "ENHSP-SAT-HRADD": ENHSP(False, settings="-h hradd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HRADD"),
    "ENHSP-SAT-BLIND": ENHSP(False, settings="-h blind -s gbfs -silent -pp -pe", name="ENHSP-SAT-BLIND"),

    "ENHSP-OPT-HMRP": ENHSP(False, settings="-h hmrp -s WAStar -silent -pp -pe", name="ENHSP-OPT-HMRP"),
    "ENHSP-OPT-HMRPHJ": ENHSP(False, settings="-planner sat-hmrphj -silent -pp -pe", name="ENHSP-OPT-HMRPHJ"),
    "ENHSP-OPT-HADD": ENHSP(False, settings="-h hadd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HADD"),
    "ENHSP-OPT-HMAX": ENHSP(False, settings="-h hadd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HMAX"),
    "ENHSP-OPT-AIBR": ENHSP(False, settings="-h aibr -s WAStar -silent -pp -pe", name="ENHSP-OPT-AIBR"),
    "ENHSP-OPT-HRADD": ENHSP(False, settings="-h hradd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HRADD"),
    "ENHSP-OPT-BLIND": ENHSP(False, settings="-h blind -s WAStar -silent -pp -pe", name="ENHSP-OPT-BLIND"),

    "METRIC-FF": MetricFF(),
    "NFD": NFD(),
    "OMT": OMT(),

    "LPG": LPG(),
    "TFD": TFD(),
    "Optic": Optic(),
    "ITSAT": ITSAT(),
}


def main():
    print("Started...")
    s3 = boto3.client('s3', config=my_config)

    envs = Envs()
    if envs.isInsideAWS:
        time.sleep(envs.index / 4)
    else:
        envs.file = "benchmarks/instances/aij.csv"

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
            if r.solved:
                logger.log(r.toCSV())
                s3.put_object(
                    Key=f"{envs.experiment}/{r.solver}/{r.domain}/plans/{r.problem}.txt",
                    Bucket="patty-benchmarks",
                    Body=bytes(r.stdout, 'utf-8'),
                    ContentType='text/plain'
                )

        except Exception as error:
            if isinstance(error, KeyboardInterrupt):
                print("Interrupted by user...")
                break
            r: Result = Result(domainFile, problemFile)
            r.solver = benchmark
            print(r)
            logger.log(r.toCSV())
            logger.error(traceback.format_exc())
            print(traceback.format_exc(), file=sys.stderr)


if __name__ == '__main__':
    main()
