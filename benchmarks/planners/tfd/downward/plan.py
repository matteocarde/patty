#! /usr/bin/env python

from __future__ import print_function

import subprocess
import sys


def main():
    def run(*args, **kwargs):
        input = kwargs.pop("input", None)
        output = kwargs.pop("output", None)
        assert not kwargs
        redirections = {}
        if input:
            redirections["stdin"] = open(input)
        if output:
            redirections["stdout"] = open(output, "w")
        print(args, redirections)
        subprocess.check_call(sum([arg.split("+") for arg in args], []), **redirections)

    config, domain, problem, result_name = sys.argv[1:]

    # run translator
    run("/var/tfd/downward/translate/translate.py", domain, problem)

    # run preprocessing
    run("/var/tfd/downward/preprocess/preprocess", input="output.sas")

    # run search
    run("/var/tfd/downward/search/search", config, "p", result_name, input="output")


if __name__ == "__main__":
    main()