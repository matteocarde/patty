import copy
import sys
import time
import traceback
from typing import Dict

import boto3
from botocore.config import Config

from classes.CloudLogger import CloudLogger
from classes.planners.AnmlSMT import AnmlSMT
from classes.planners.ENHSP import ENHSP
from classes.Envs import Envs
from classes.planners.ITSAT import ITSAT
from classes.planners.LPG import LPG
from classes.planners.MetricFF import MetricFF
from classes.planners.NFD import NFD
from classes.planners.OMT import OMT
from classes.planners.Optic import Optic
from classes.planners.Patty import Patty
from classes.planners.Planner import Planner
from classes.Result import Result
from classes.planners.SpringRoll import SpringRoll
from classes.planners.TFD import TFD

my_config = Config(
    region_name='eu-central-1',
)

PLANNERS: Dict[str, Planner] = {
    "PATTY-T-OR": Patty("PATTY-T-OR", temporalConstraints='logical'),
    "PATTY-T-SIGMA": Patty("PATTY-T-SIGMA", temporalConstraints='numerical'),
    "PATTY-T-OR-ASTAR": Patty("PATTY-T-OR", temporalConstraints='logical', search="astar"),
    "PATTY-T-SIGMA-ASTAR": Patty("PATTY-T-SIGMA", temporalConstraints='numerical', search="astar"),
    "PATTY-O": Patty("PATTY-O", search="step", pattern="arpg"),
    "PATTY-G": Patty("PATTY-G", search="static", pattern="arpg"),
    "PATTY-H": Patty("PATTY-H", search="astar", pattern="arpg", noCompression=True),
    "PATTY-F": Patty("PATTY-F", search="astar", pattern="arpg", noCompression=False),

    "PATTY-R": Patty("PATTY-R", search="step", pattern="random", quality="none"),
    "PATTY-A": Patty("PATTY-A", search="step", pattern="arpg", quality="none"),
    "PATTY-E": Patty("PATTY-E", search="step", pattern="enhanced", quality="none"),
    "PATTY-FA": Patty("PATTY-FA", search="astar", pattern="arpg", quality="none"),
    "PATTY-FE": Patty("PATTY-FE", search="astar", pattern="enhanced", quality="none"),
    "PATTY-M": Patty("PATTY-M", search="step", pattern="enhanced", quality="shortest-step"),
    "PATTY-I": Patty("PATTY-I", search="step", pattern="enhanced", quality="improve-plan"),
    "PATTY-L": Patty("PATTY-L", search="step", pattern="enhanced", quality="improve-less"),
    "RANTANPLAN": Patty("RANTANPLAN", search="static", pattern="arpg", hasEffectAxioms=True, rollBound=1),
    "SPRINGROLL": SpringRoll(),

    "ENHSP-SAT-HMRP": ENHSP(False, settings="-h hmrp -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMRP"),
    "ENHSP-SAT-HMRPHJ": ENHSP(False, settings="-planner sat-hmrphj -silent -pp -pe", name="ENHSP-SAT-HMRPHJ"),
    "ENHSP-SAT-HADD": ENHSP(False, settings="-h hadd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HADD"),
    "ENHSP-SAT-HMAX": ENHSP(False, settings="-h hmax -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMAX"),
    "ENHSP-SAT-AIBR": ENHSP(False, settings="-h aibr -s gbfs -silent -pp -pe", name="ENHSP-SAT-AIBR"),
    "ENHSP-SAT-HRADD": ENHSP(False, settings="-h hradd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HRADD"),
    "ENHSP-SAT-BLIND": ENHSP(False, settings="-h blind -s gbfs -silent -pp -pe", name="ENHSP-SAT-BLIND"),

    "ENHSP-OPT-HMRP": ENHSP(False, settings="-h hmrp -s WAStar -silent -pp -pe", name="ENHSP-OPT-HMRP"),
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
    "OPTIC": Optic(),
    "ITSAT": ITSAT(),
    "ANMLSMT": AnmlSMT(),
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
            print(r.stdout)
            if not r.solved:
                print(r.stdout)

            logger.log(r.toCSV())
            s3.put_object(
                Key=f"{envs.experiment}/{r.solver}/{r.domain}/plans/{r.problem}{'-unsolved' if not r.solved else ''}.txt",
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
