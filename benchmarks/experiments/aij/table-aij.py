import csv
import json
import os
import shutil
import statistics
import sys
from typing import Dict, List, Set

from benchmarks.tables.aij.table1 import AIJ_TABLE1
from benchmarks.tables.aij.table2 import AIJ_TABLE2
from classes.CloudLogger import CloudLogger
from classes.Result import Result


def round(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


def rVec(v, n):
    return round(statistics.mean(v), n) if v else "-"


def main():
    # Parsing the results
    exp = "2024-09-11-IMPROVE-v1"
    file = f"benchmarks/results/csv/{exp}.csv"

    CloudLogger.saveLogs(exp, file)
    joinWith = ["2024-09-10-AIJ-v1"]
    for exp2 in joinWith:
        CloudLogger.appendLogs(exp2, file)

    tables = [("TAB1", AIJ_TABLE1), ("TAB2", AIJ_TABLE2)]

    joinWith = [file]
    # joinWith = [file]

    aResults: [Result] = []
    for fileJoin in joinWith:
        with open(fileJoin, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    # Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-sat-hadd": "ENHSP",
        "ENHSP-sat-hradd": "ENHSP",
        "ENHSP-sat-hmrphj": "ENHSP",
    })
    results = Result.splitRandom(results, "PATTY-R")

    d = dict()
    dView = dict()
    for r in results:
        d[r.domain] = d.setdefault(r.domain, dict())
        d[r.domain][r.solver] = d[r.domain].setdefault(r.solver, dict())
        d[r.domain][r.solver][r.problem] = d[r.domain][r.solver].setdefault(r.problem, list())
        d[r.domain][r.solver][r.problem].append(r)

        dView[r.solver] = dView.setdefault(r.solver, dict())
        dView[r.solver][r.domain] = dView[r.solver].setdefault(r.domain, dict())
        dView[r.solver][r.domain][r.problem] = dView[r.solver][r.domain].setdefault(r.problem, list())
        dView[r.solver][r.domain][r.problem].append(r)

    with open(f"benchmarks/results/json/{exp}.json", "w") as f:
        f.write(json.dumps(dView, indent=2))

    for tableName, table in tables:

        planners: List[str] = list(table["planners"].keys())
        domains: List[str] = list(table["domains"].keys())
        domains.sort()

        for domain in domains:
            for planner in planners:
                problems = list()
                if planner not in d[domain]:
                    continue
                for problem in d[domain][planner].keys():
                    if len(d[domain][planner][problem]) > 1:
                        print(f"There are multiple problems {problem} for {domain} with {planner}. "
                              f"Please aggregate it in some way", file=sys.stderr)
                    problems.append(d[domain][planner][problem][0])
                d[domain][planner] = problems

        t = dict()
        for domain in domains:
            t[domain] = {
                "coverage": dict(),
                "bound": dict(),
                "time": dict(),
                "length": dict(),
                "nOfVars": dict(),
                "nOfRules": dict(),
                "lastCallsToSolver": dict(),
            }

            commonlySolved = {}
            commonlyGrounded = {}
            for planner in table["planners"].keys():
                solved = {r.problem for r in d[domain][planner] if r.solved}
                grounded = {r.problem for r in d[domain][planner] if r.nOfVars > 0}
                if solved:
                    commonlySolved = solved if not commonlySolved else commonlySolved.intersection(solved)
                if grounded:
                    commonlyGrounded = solved if not commonlyGrounded else commonlyGrounded.intersection(grounded)

            for planner, plannerInfo in table["planners"].items():
                pResult = d[domain][planner]

                if plannerInfo["type"] in {"stdev"}:
                    t[domain]["coverage"][planner] = "0.0"

                    v = [abs(r.time) / 1000 for r in pResult]
                    t[domain]["time"][planner] = rVec(v, 1)

                    v = [r.bound for r in pResult if r.solved and r.problem in commonlySolved]
                    t[domain]["bound"][planner] = rVec(v, 1)

                    v = [r.planLength for r in pResult if r.solved and r.problem in commonlySolved]
                    t[domain]["length"][planner] = rVec(v, 0)

                    v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlySolved]
                    t[domain]["nOfVars"][planner] = rVec(v, 0) if v else "0"

                    v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlySolved]
                    t[domain]["nOfRules"][planner] = rVec(v, 0) if v else "0"

                    v = [r.lastCallsToSolver for r in pResult if
                         r.lastCallsToSolver > 0 and r.problem in commonlySolved]
                    t[domain]["lastCallsToSolver"][planner] = rVec(v, 2)
                    continue

                hasCoverage = sum([r.solved for r in pResult]) > 0
                t[domain]["coverage"][planner] = round(
                    sum([r.solved for r in pResult]) / table["domains"][domain]["instances"] * 100, 0)
                t[domain]["coverage"][planner] = "-" if not hasCoverage else t[domain]["coverage"][planner]

                v = [r.bound for r in pResult if r.solved and r.problem in commonlySolved]
                t[domain]["bound"][planner] = rVec(v, 1) if hasCoverage else "-"

                v = [r.time / 1000 if r.solved else table["time-limit"] / 1000 for r in pResult]
                t[domain]["time"][planner] = rVec(v, 1) if hasCoverage else "-"

                v = [r.planLength for r in pResult if r.solved and r.problem in commonlySolved]
                t[domain]["length"][planner] = rVec(v, 0) if hasCoverage else "-"

                v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlySolved]
                t[domain]["nOfVars"][planner] = rVec(v, 0) if len(v) else "-"

                v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlySolved]
                t[domain]["nOfRules"][planner] = rVec(v, 0) if len(v) else "-"

                v = [r.lastCallsToSolver for r in pResult if r.lastCallsToSolver > 0 and r.problem in commonlySolved]
                t[domain]["lastCallsToSolver"][planner] = rVec(v, 2) if len(v) else "-"

        latex = list()
        latex.append(r"""
               \documentclass[11pt,landscape]{article}
               \usepackage{graphicx}
               \usepackage{lscape}
               \usepackage{multirow}
               \usepackage[a4paper,margin=1in,landscape]{geometry}
    
               \begin{document}""")

        best: Dict[str, Dict[str, Set[str]]] = dict()
        for domain in domains:
            best[domain] = dict()
            for column, statInfo in table["columns"].items():
                winner = statInfo["winner"]
                better = set()
                betterValue = float("-inf") if winner > 0 else float("+inf")
                for planner, plannerInfo in table["planners"].items():
                    if planner not in t[domain][column]:
                        continue
                    if plannerInfo["type"] in {"stdev"}:
                        continue
                    value = t[domain][column][planner]
                    if value in {"-", "G", "-1.00"}:
                        continue
                    if float(value) * winner > betterValue * winner:
                        betterValue = float(value)
                        better = {planner}
                    elif float(value) == betterValue:
                        better |= {planner}
                best[domain][column] = better

        latex.append(r"""
            \begin{""" + table["type"] + r"""}[tb]
            \centering
            \resizebox{""" + table["width"] + r"""}{!}{""")

        plannersHeader = []
        mString = []
        cString = ""
        for (column, columnInfos) in table["columns"].items():
            nCells = 0
            clString = []
            for (planner, plannerInfo) in table["planners"].items():
                if plannerInfo["type"] not in {"stdev"}:
                    plannersHeader.append(f"${plannerInfo['name']}$")
                    nCells += 1
                    clString.append("c")

            cString += f"|{''.join(clString)}|"
            mString.append(r"\multicolumn{" + str(nCells) + "}{c||}{" + columnInfos["name"] + "}")

        columns = f"|l|{cString}" + "|"

        latex.append(r"\begin{tabular}{" + columns + "}")
        latex.append(r"\hline")
        latex.append(fr" & " + "&".join(mString) + r"\\")
        latex.append(fr"Domain & " + "&".join(plannersHeader) + r"\\")
        latex.append(fr"\hline")

        rows = list()
        for domain, domainInfo in table["domains"].items():
            row = [domainInfo["name"]]
            for (column, columnInfo) in table["columns"].items():
                for (planner, plannerInfo) in table["planners"].items():
                    if plannerInfo["type"] in {"stdev"}:
                        continue
                    if planner not in t[domain][column]:
                        row.append("-")
                        continue
                    value = t[domain][column][planner]
                    subvalue = ""
                    if plannerInfo["type"] in {"avg"} and columnInfo["stdev"]:
                        stdev = t[domain][column][plannerInfo["stdev"]]
                        subvalue = rf"$\pm {stdev}$"
                    if planner in best[domain][column]:
                        row.append(r"\textbf{" + value + "}" + subvalue)
                        continue
                    row.append(value + subvalue)
            rows.append("&".join(row))

        latex.append("\\\\\n".join(rows))
        latex.append(fr"\\\hline")
        row = [r"\textit{Total}"]

        for column, columnInfo in table["columns"].items():
            for planner, plannerInfo in table["planners"].items():
                if plannerInfo["type"] in {"stdev"}:
                    continue
                nOfBest = 0
                for domain, domainInfo in table["domains"].items():
                    if planner in best[domain][column]:
                        nOfBest += 1
                row.append(r"\textbf{" + str(nOfBest) + "}")
        latex.append("&".join(row) + r"\\\hline")

        latex.append(r"""
        \end{tabular}}
        \caption{""" + table["caption"] + """}
        \label{""" + table["name"] + """}
        \end{""" + table["type"] + """}
        """)

        pass

        latex.append("\end{document}")

        latexStr = "\n".join(latex)
        folder = f'benchmarks/latex/{exp}'
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
        file = f"{exp}-{tableName}"
        with open(f"{folder}/{file}.tex", "w") as f:
            f.write(latexStr)
        os.system(f"pdflatex -interaction=nonstopmode --output-directory='{folder}' {folder}/{file}.tex ")

        os.remove(f"{folder}/{file}.aux")
        os.remove(f"{folder}/{file}.log")

    for table, tableName in tables:
        os.system(f"open {folder}/{exp}-{tableName}.pdf")


if __name__ == '__main__':
    main()
