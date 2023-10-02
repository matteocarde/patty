import csv
import os
import shutil
import statistics
from typing import Dict, List

from classes.Result import Result


def rString(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


DOMAINS = ["Baxter",
           "Descent",
           "HVAC",
           "Linear-Car",
           "Linear-Car-2",
           "Linear-Generator",
           "Solar-Rover"
           ]

HEURISTICS = [
    "ENHSP-SAT-HMRP",
    "ENHSP-SAT-HADD",
    # "ENHSP-SAT-HMAX",
    "ENHSP-SAT-AIBR",
    # "ENHSP-SAT-HRADD",
    "ENHSP-SAT-BLIND",
    "ENHSP-OPT-HMRP",
    "ENHSP-OPT-HADD",
    # "ENHSP-OPT-HMAX",
    "ENHSP-OPT-AIBR",
    # "ENHSP-OPT-HRADD",
    "ENHSP-OPT-BLIND"
]

DELTAS = {
    ("NODELTA", "-de 0.1 -dp 0.1 -dh 0.1"): {
        "id": "1DELTA",
        "name": r"$1\delta$",
        "type": "NODELTA",
        "config": "-de 0.1 -dp 0.1 -dh 0.1"
    },
    ("NODELTA", "-de 0.1 -dp 1 -dh 1"): {
        "id": "2DELTA",
        "name": r"$2\delta$",
        "type": "NODELTA",
        "config": "-de 0.1 -dp 1 -dh 1"
    },
    ("DELTA", "-de 0.1 -dp 0.1 -dh 0.1"): {
        "id": "KDELTA",
        "name": r"$K\delta$",
        "type": "DELTA",
        "config": "-de 0.1 -dp 0.1 -dh 0.1"
    }
}


def main():
    filename = "2023-09-30-WELLKNOWN-v4.csv"
    file = f"benchmarks/results/{filename}"

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    results: [Result] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(Result.fromCSVLine(line[0].split(",")))

    # Domain/Solver/Delta
    rDict: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()
    portfolio: Dict[str, Dict[str, Dict[str, List[Result]]]] = dict()

    TIMEOUT = 0
    for r in results:
        domain = "-".join(r.domain.split("-")[:-1])
        domainType = r.domain.split("-")[-1]
        solver = r.solver.split("[")[0]
        config = r.solver.split("[")[1][:-1]
        line = DELTAS[(domainType, config)]
        lineId = line["id"]
        rDict[domain] = rDict.setdefault(domain, {})
        rDict[domain][solver] = rDict[domain].setdefault(solver, {})
        rDict[domain][solver][lineId] = rDict[domain][solver].setdefault(lineId, [])
        rDict[domain][solver][lineId].append(r)

        if r.time > TIMEOUT:
            TIMEOUT = r.time

    table = dict()
    for domain in DOMAINS:
        table[domain] = dict()
        for heuristic in HEURISTICS:
            table[domain][heuristic] = dict()
            for delta in DELTAS.values():
                deltaId = delta["id"]
                table[domain][heuristic][deltaId] = dict()
                row = table[domain][heuristic][deltaId]
                elements = rDict[domain][heuristic][deltaId]
                time = statistics.mean([r.time if r.solved else TIMEOUT for r in elements])
                coverage = sum([1 if r.solved else 0 for r in elements]) / len(elements)
                row["coverage"] = rString(coverage * 100, 2) if coverage > 0 else "-"
                row["time"] = rString(time / 1000, 2) if coverage > 0 else "-"

    PROPERTIES = [("time", "RT (s)", -1), ("coverage", "Cov. (\%)", +1)]
    best = dict()
    for domain in DOMAINS:
        best[domain] = dict()
        for heuristic in HEURISTICS:
            best[domain][heuristic] = dict()
            for p in PROPERTIES:
                bestValue = float("-inf") if p[2] > 0 else float("+inf")
                bestItems = {}
                for delta in DELTAS.values():
                    deltaId = delta["id"]
                    value = table[domain][heuristic][deltaId][p[0]]
                    if value in {"-"}:
                        continue
                    if float(value) * p[2] > bestValue * p[2]:
                        bestItems = {deltaId}
                        bestValue = float(value)
                    elif float(value) == bestValue:
                        bestItems |= {deltaId}

                best[domain][heuristic][p[0]] = bestItems

    latex = list()
    latex.append(r"""
        \documentclass[11pt,landscape]{article}
        \usepackage{graphicx}
        \usepackage{lscape}
        \usepackage{multirow}
        \usepackage[a4paper,margin=1in,landscape]{geometry}
        
        \begin{document}
    
        \begin{table*}[tb]
        \centering
        \resizebox{\textwidth}{!}{""")

    cArray = ["cc"] + ["|ccc" for d in DOMAINS]
    latex.append(r"\begin{tabular}{" + ''.join(cArray) + "}")

    dString = [r"\multicolumn{3}{|c}{" + d + "}" for d in DOMAINS]
    latex.append(fr" & & " + "&".join(dString) + r"\\")
    lString = "&".join([l["name"] for l in DELTAS.values()] * len(DOMAINS))
    latex.append(fr"& & " + lString + r"\\")

    for h in HEURISTICS:
        latex.append(r"\hline")
        for pi, p in enumerate(PROPERTIES):
            hName = r"\multirow{2}{*}{" + h + "}" if pi == 0 else ""
            row = [hName] + [p[1]]
            for d in DOMAINS:
                for delta in DELTAS.values():
                    v = table[d][h][delta["id"]][p[0]]
                    strV = r"\textbf{" + v + "}" if delta["id"] in best[d][h][p[0]] else v
                    row.append(strV)
            latex.append("&".join(row) + r"\\")

    latex.append(r"""
        \end{tabular}} \caption{Average runtime (RT, CPU-time seconds) and coverage (Cov.) achieved by 
    informed and uninformed search approaches implemented in ENHSP (E) and UPMurphi (U) while relying on different 
    discretisation approaches on well-known benchmark domains. Average runtime (RT) considers unsolved instances as 
    cut-off time (300 seconds).} 
        \label{tab:single-static} 
        \end{table*}  
        \end{document}""")
    latexStr = "\n".join(latex)

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    with open(f"{folder}/{exp}.tex", "w") as f:
        f.write(latexStr)
    os.system(f"pdflatex -interaction=nonstopmode --output-directory='{folder}' {folder}/{exp}.tex ")

    os.remove(f"{folder}/{exp}.aux")
    os.remove(f"{folder}/{exp}.log")


if __name__ == '__main__':
    main()
