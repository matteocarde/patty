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


def main():
    f = open("translate-list.csv", "r")
    csv = f.read()
    f.close()
    instances = [[v for v in line.split(",")] for line in csv.split("\n")]

    if type == "TRANSLATED":

        folder = domainFile.replace("domain.pddl", "")
        if not os.path.exists(folder):
            os.mkdir(folder + "instances-translated")
        domain = Domain.fromFile(domainFile)
        problem = Problem.fromFile(problemFile)

        domainFile = folder + "domain-translated.pddl"
        problemFile = problemFile.replace("/instances/", "/instances-translated/")

        pt = PatternTranslator(domain, problem)
        tDomain = pt.getTranslatedDomain()
        tProblem = pt.getTranslatedProblem()

        with open(domainFile, "w") as f:
            f.write(tDomain.toPDDL().toString())
        with open(domainFile, "w") as f:
            f.write(tDomain.toPDDL().toString())

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
