import os

from Domain import Domain
from Problem import Problem

domains = {
    "block-grouping": {
        "folder": "block-grouping",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "fn-counters": {
        "folder": "counters/fn-counters",
        "domain": "domain.pddl",
        "problems-folder": "problems/"
    },
    "fn-counters-inv": {
        "folder": "counters/fn-counters-inv",
        "domain": "domain.pddl",
        "problems-folder": "problems/"
    },
    "fn-counters-rnd": {
        "folder": "counters/fn-counters-rnd",
        "domain": "domain.pddl",
        "problems-folder": "problems/"
    },
    "farmland": {
        "folder": "farmland",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "plant-watering": {
        "folder": "plant-watering",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    },
    "sailing": {
        "folder": "sailing",
        "domain": "domain.pddl",
        "problems-folder": "instances/"
    }
}

for (domainName, domainObj) in domains.items():
    folder = f"files/{domainObj['folder']}"
    domainFile = f"{folder}/{domainObj['domain']}"
    problemFolder = f"{folder}/{domainObj['problems-folder']}"
    try:
        domain: Domain = Domain.fromFile(f"files/{domainObj['folder']}/{domainObj['domain']}")
    except Exception as e:
        print("Error in parsing domain: ", e)

    for problemFile in os.listdir(problemFolder):

        print(folder, problemFile)
        try:
            problem: Problem = Problem.fromFile(f"{problemFolder}/{problemFile}")
        except:
            print("Error in parsing problem:")
