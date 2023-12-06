import csv
import os
import shutil
import statistics
from typing import Dict, List

from classes.ICRResult import ICRResult
from classes.Result import Result


def myMean(elements):
    return statistics.mean(elements) if elements else float("-inf")


def rString(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


EXPERIMENTS = ["TOTAL", "PARTIAL"]
DOMAINS = {
    "Baxter": {
        "text": r"\textsc{Baxter} (L)",
        "kind": "Hybrid",
    },
    "Descent": {
        "text": r"\textsc{Descent} (NL)",
        "kind": "Hybrid",
    },
    "HVAC": {
        "text": r"\textsc{HVAC} (NL)",
        "kind": "Hybrid",
    },
    "Linear-Car": {
        "text": r"\textsc{LinearCar} (L)",
        "kind": "Hybrid",
    },
    "Solar-Rover": {
        "text": r"\textsc{SolarRover} (L)",
        "kind": "Hybrid",
    },
    "UTC": {
        "text": r"\textsc{UTC} (L)",
        "kind": "Hybrid",
    },
    "counters": {
        "text": r"\textsc{Counters} (S)",
        "kind": "Numeric",
    },
    "fo_counters": {
        "text": r"\textsc{Counters} (L)",
        "kind": "Numeric",
    },
    "delivery": {
        "text": r"\textsc{Delivery} (S)",
        "kind": "Numeric",
    },
    "drone": {
        "text": r"\textsc{Drone} (S)",
        "kind": "Numeric",
    },
    "expedition": {
        "text": r"\textsc{Expedition} (S)",
        "kind": "Numeric",
    },
    "watering": {
        "text": r"\textsc{PlantWatering} (S)",
        "kind": "Numeric",
    },
    "farmland": {
        "text": r"\textsc{Farmland} (S)",
        "kind": "Numeric",
    },
    "fo-farmland": {
        "text": r"\textsc{Farmland} (L)",
        "kind": "Numeric",
    },
    "hydropower": {
        "text": r"\textsc{Hydropower} (S)",
        "kind": "Numeric",
    },
    "mprime": {
        "text": r"\textsc{MPrime} (S)",
        "kind": "Numeric",
    },
    "rover": {
        "text": r"\textsc{Rover} (S)",
        "kind": "Numeric",
    },
    "sailing": {
        "text": r"\textsc{Sailing} (S)",
        "kind": "Numeric",
    },
    "fo-sailing": {
        "text": r"\textsc{Sailing} (L)",
        "kind": "Numeric",
    },
    "sugar": {
        "text": r"\textsc{Sugar} (S)",
        "kind": "Numeric",
    },
    "zenotravel": {
        "text": r"\textsc{ZenoTravel} (S)",
        "kind": "Numeric",
    },

}


def main():
    DOMAINS_BY_KIND: Dict[Dict[str, List[str]]] = dict()

    for (dom, domDict) in DOMAINS.items():
        kind = domDict["kind"]
        DOMAINS_BY_KIND[kind] = DOMAINS_BY_KIND.setdefault(kind, [])
        DOMAINS_BY_KIND[kind].append(dom)

    filename = "2023-12-05-ICR-ALL-v2.csv"
    file = f"benchmarks/results/{filename}"

    exp = filename.replace(".csv", "")
    folder = f'benchmarks/latex/{exp}'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    results: [ICRResult] = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            results.append(ICRResult.fromCSVLine(line[0].split(",")))

    # Domain/Solver/Delta
    rDict: Dict[str, Dict[str, List[ICRResult]]] = dict()

    TIMEOUT = 0
    for r in results:
        type = r.expType
        domain = r.domain

        rDict[type] = rDict.setdefault(type, {})
        rDict[type][domain] = rDict[type].setdefault(domain, [])
        rDict[type][domain].append(r)

        if r.time > TIMEOUT:
            TIMEOUT = r.time

    pass

    DOMAIN_INFOS_COLUMNS = {
        # "nOfProblems": "\#",
        "nOfAtoms": "$|V_b \cup V_n|$",
        "traceLength": "$|\mathcal{T}|$",
        "nOfConditions": "$|\mathcal{I}(\mathcal{T}, G)|$",
    }
    COLUMNS = {
        # "nOfAtoms": "$|V_b \cup V_n|$",
        # "traceLength": "$|\mathcal{T}|$",
        # "nOfConditions": "$|\mathcal{I}(\mathcal{T}, G)|$",
        # "coverage": "Cov. (\%)",
        "time": "Time (s)",
        # "dRC": r"$||I - I_\star||^2$",
        # "dRW": r"$||I - \tilde{I}||^2$",
    }

    table: Dict[str, Dict[str, Dict[str, float or str]]] = dict()
    domainInfos: Dict[str, Dict[str, float or str]] = dict()
    for domain in DOMAINS:
        domainInfos[domain] = dict()
        for experiment in EXPERIMENTS:
            if domain not in rDict[experiment]:
                continue
            table[domain] = table.setdefault(domain, dict())
            table[domain][experiment] = dict()
            row = table[domain][experiment]
            elements = rDict[experiment][domain]
            time = statistics.mean([r.time if r.solved else TIMEOUT for r in elements])
            coverage = sum([1 if r.solved else 0 for r in elements]) / len(elements)
            dRW = myMean([r.dRW for r in elements if r.solved])
            dCW = myMean([r.dRC for r in elements if r.solved])
            nOfAtoms = myMean([r.nOfAtoms for r in elements if r.solved])
            traceLength = myMean([r.traceLength for r in elements if r.solved])
            nOfConditions = myMean([r.nOfConditions for r in elements if r.solved])
            row["coverage"] = rString(coverage * 100, 2) if coverage > 0 else "-"
            row["time"] = rString(time / 1000, 2) if coverage > 0 else "-"
            row["dRW"] = rString(dRW, 2) if coverage > 0 else "-"
            row["dRC"] = rString(dCW, 2) if coverage > 0 else "-"
            if experiment == "TOTAL":
                domainInfos[domain]["nOfAtoms"] = rString(nOfAtoms, 2) if coverage > 0 else "-"
                domainInfos[domain]["traceLength"] = rString(traceLength, 2) if coverage > 0 else "-"
                domainInfos[domain]["nOfConditions"] = rString(nOfConditions, 2) if coverage > 0 else "-"
                domainInfos[domain]["nOfProblems"] = rString(len(elements), 0)

    latex = list()
    latex.append(r"""
        \documentclass[11pt]{article}
        \usepackage{graphicx}
        \usepackage{multirow}
        \usepackage{lscape}
        \usepackage[a4paper,margin=1in]{geometry}

        \begin{document}

        \begin{table*}[tb]
        \centering
        \resizebox{\textwidth}{!}{""")

    nOfDomainInfos = len(DOMAIN_INFOS_COLUMNS.items())
    nOfColumns = len(COLUMNS.values())
    cArray = ["l|" + "c" * nOfDomainInfos + "|"] + ["c" * nOfColumns + "|" for e in EXPERIMENTS]
    latex.append(r"\begin{tabular}{|" + ''.join(cArray) + "}")

    latex.append(r"\hline")
    latex.append(r" & \multicolumn{" + str(nOfDomainInfos) + "}{|c|}{Domain Infos} & " + "&".join(
        ["\multicolumn{" + str(nOfColumns) + r"}{c|}{\textsc{" + e + r"}}" for e in EXPERIMENTS]) + r"\\")
    latex.append(fr"Domain & " + "&".join(text for (key, text) in DOMAIN_INFOS_COLUMNS.items()) + "&" + "&".join(
        [c for e in EXPERIMENTS for c in COLUMNS.values()]) + r"\\")

    # latex.append(r"\hline")
    for (kind, domains) in DOMAINS_BY_KIND.items():
        latex.append(r"\hline")
        empty = "".join(["&" for c in COLUMNS.values() for e in EXPERIMENTS] + ["&" for x in DOMAIN_INFOS_COLUMNS])
        latex.append(r"\textbf{" + kind + "}" + empty + r"\\")
        # latex.append(r"\hline")
        for d in domains:
            row = [DOMAINS[d]["text"]] + [domainInfos[d][key] for (key, text) in DOMAIN_INFOS_COLUMNS.items()]
            for e in EXPERIMENTS:
                for c in COLUMNS.keys():
                    v = table[d][e][c] if d in table else "N/D"
                    row.append(str(v))
            latex.append("&".join(row) + r"\\")

    latex.append(r"\hline")
    latex.append(r"""
        \end{tabular}} \caption{Something goes here}
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
