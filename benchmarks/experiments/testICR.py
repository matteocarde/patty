import sys
import time
import traceback

import boto3
from botocore.config import Config

from classes.CloudLogger import CloudLogger
from classes.Envs import Envs
from classes.ICRExp import ICRExp
from classes.ICRResult import ICRResult

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
        envs.file = "benchmarks/instances/icr.csv"

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
        expType = el[0]
        domain = el[1]
        domainFile = el[2]
        problemFile = el[3]
        traceFile = el[4]
        cProblemFile = el[5]

        try:
            if envs.isInsideAWS:
                print(f"Starting {el} ")
            exp = ICRExp()
            r: ICRResult = exp.run(expType, domain, domainFile, problemFile, traceFile, cProblemFile, envs.timeout,
                                   logger)
            print(r)
            if not r.solved:
                print(r.stdout)
            logger.log(r.toCSV())
            s3.put_object(
                Key=f"{envs.experiment}/{expType}/{r.domain}/{r.problem[:-5]}.txt",
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
