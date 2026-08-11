import copy
import sys
import time
import traceback

import boto3
from botocore.config import Config

from benchmarkPlanners import BENCHMARK_PLANNERS
from classes.CloudLogger import CloudLogger
from classes.Envs import Envs
from classes.Result import Result

my_config = Config(
    region_name='eu-central-1',
)


def main():
    print("Started...")
    s3 = boto3.client('s3', config=my_config)

    envs = Envs()
    if envs.isInsideAWS:
        time.sleep(envs.index / 4)
    else:
        envs.file = "benchmarks/instances/classical.csv"

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
        planner = copy.copy(BENCHMARK_PLANNERS[plName])
        planner.name = el[0]
        planner.addSettings(plSettings)
        benchmark = el[1]
        domainFile = el[2]
        problemFile = el[3]

        if hasattr(planner, "tcTime"):
            planner.tcTime = envs.tcTime

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
