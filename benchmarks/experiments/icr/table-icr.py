import csv
import os
import shutil
import statistics
from typing import Dict, List, Set

from classes.ICRResult import ICRResult
from classes.Result import Result


def myMean(elements):
    return statistics.mean(elements) if elements else float("-inf")


def rString(fValue, n):
    fValue = fValue if fValue > 0.1 else 0.1
    return '{:.{n}f}'.format(fValue, n=n)


EXPERIMENTS = {
    "100%": r"$\beta = 1$",
    # "75%": r"$\beta = 0.75$",
    "50%": r"$\beta = 0.5$",
    # "25%": r"$\beta = 0.25$",
    "0%": r"$\beta = 0$"
}
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
    # "UTC": {
    #     "text": r"\textsc{UTC} (L)",
    #     "kind": "Hybrid",
    # },
    "counters": {
        "text": r"\textsc{Counters} (L)",
        "kind": "Numeric",
    },
    "fo_counters": {
        "text": r"\textsc{Counters} (L)",
        "kind": "Numeric",
    },
    "delivery": {
        "text": r"\textsc{Delivery} (L)",
        "kind": "Numeric",
    },
    "drone": {
        "text": r"\textsc{Drone} (L)",
        "kind": "Numeric",
    },
    "expedition": {
        "text": r"\textsc{Expedition} (L)",
        "kind": "Numeric",
    },
    "watering": {
        "text": r"\textsc{Watering} (L)",
        "kind": "Numeric",
    },
    "farmland": {
        "text": r"\textsc{Farmland} (L)",
        "kind": "Numeric",
    },
    "fo-farmland": {
        "text": r"\textsc{Farmland} (L)",
        "kind": "Numeric",
    },
    "hydropower": {
        "text": r"\textsc{Hydropower} (L)",
        "kind": "Numeric",
    },
    "mprime": {
        "text": r"\textsc{MPrime} (L)",
        "kind": "Numeric",
    },
    "rover": {
        "text": r"\textsc{Rover} (L)",
        "kind": "Numeric",
    },
    "sailing": {
        "text": r"\textsc{Sailing} (L)",
        "kind": "Numeric",
    },
    "fo-sailing": {
        "text": r"\textsc{Sailing} (L)",
        "kind": "Numeric",
    },
    "sugar": {
        "text": r"\textsc{Sugar} (L)",
        "kind": "Numeric",
    },
    "zenotravel": {
        "text": r"\textsc{ZenoTravel} (L)",
        "kind": "Numeric",
    },

}


def main():
    DOMAINS_BY_KIND: Dict[Dict[str, List[str]]] = dict()

    for (dom, domDict) in DOMAINS.items():
        kind = domDict["kind"]
        DOMAINS_BY_KIND[kind] = DOMAINS_BY_KIND.setdefault(kind, [])
        DOMAINS_BY_KIND[kind].append(dom)

    filename = "2023-12-12-ICR-FINAL-v5.csv"
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

    commonlySolved: Dict[str, Set[str]] = dict()
    for (t, tDict) in rDict.items():
        for (d, dList) in tDict.items():
            solved = set(["-".join(r.problem.split("-")[:-1]) for r in dList])
            commonlySolved[d] = commonlySolved.setdefault(d, solved)
            commonlySolved[d] = commonlySolved[d].intersection(solved)
            pass

    DOMAIN_INFOS_COLUMNS = {
        "nOfProblems": "\#",
        "nOfAtoms": "$|V_b \cup V_n|$",
        "traceLength": "$|\mathcal{T_\delta}|$",
    }
    ICS_COLUMNS = {
        "nOfConditions": "$|\mathcal{I}(\mathcal{T_\delta}, G)|$",
        "timeICS": "ICS",
    }
    COLUMNS = {
        "timeICR": "ICR",
    }

    table: Dict[str, Dict[str, Dict[str, float or str]]] = dict()
    domainInfos: Dict[str, Dict[str, float or str]] = dict()
    for domain in DOMAINS:
        domainInfos[domain] = dict()
        for experiment in EXPERIMENTS.keys():
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
            timeICS = myMean([r.timeICS for r in elements if r.solved])
            timeICR = myMean([r.timeICR for r in elements if
                              r.solved and "-".join(r.problem.split("-")[:-1]) in commonlySolved[domain]])
            row["coverage"] = rString(coverage * 100, 1) if coverage > 0 else "-"
            row["time"] = rString(time / 1000, 1) if coverage > 0 else "-"
            row["dRW"] = rString(dRW, 1) if coverage > 0 else "-"
            row["dRC"] = rString(dCW, 1) if coverage > 0 else "-"
            row["timeICR"] = rString(timeICR / 1000, 1) + "s" if coverage > 0 else "-"
            if experiment == "100%":
                domainInfos[domain]["timeICS"] = rString(timeICS / 1000, 1) + "s" if coverage > 0 else "-"
                domainInfos[domain]["nOfAtoms"] = rString(nOfAtoms, 1) if coverage > 0 else "-"
                domainInfos[domain]["traceLength"] = rString(traceLength, 1) if coverage > 0 else "-"
                domainInfos[domain]["nOfConditions"] = rString(nOfConditions, 1) if coverage > 0 else "-"
                domainInfos[domain]["nOfProblems"] = rString(len(commonlySolved[domain]), 0)

    latex = list()
    latex.append(r"""
        \documentclass[11pt]{article}
        \usepackage{graphicx}
        \usepackage{multirow}
        \usepackage{lscape}
        \usepackage[a4paper,margin=1in]{geometry}

        \begin{document}
        \begin{table}[tb]
        \centering
        {\huge
        \resizebox{\columnwidth}{!}{""")

    nOfDomainInfos = len(DOMAIN_INFOS_COLUMNS.items())
    nOfICSInfos = len(ICS_COLUMNS.items())
    nOfColumns = len(COLUMNS.values())
    cArray = ["l|" + "c" * nOfDomainInfos + "|" + "c" * nOfICSInfos + "|"] + ["c" * nOfColumns + "|" for e in
                                                                              EXPERIMENTS.keys()]
    latex.append(r"\begin{tabular}{|" + ''.join(cArray) + "}")

    latex.append(r"\hline")
    latex.append(r" & \multicolumn{" + str(nOfDomainInfos) + "}{|c|}{Domain Stats} " +
                 r" & \multicolumn{" + str(nOfICSInfos) + "}{|c|}{ICS stats} & " +
                 "&".join(["\multicolumn{" + str(nOfColumns) + r"}{c|}{\textsc{" + e + r"}}" for e in
                           EXPERIMENTS.values()]) + r"\\")
    latex.append(fr"Domain & " +
                 "&".join(text for (key, text) in DOMAIN_INFOS_COLUMNS.items()) + "&" +
                 "&".join(text for (key, text) in ICS_COLUMNS.items()) + "&" +
                 "&".join([c for e in EXPERIMENTS.values() for c in COLUMNS.values()]) + r"\\")

    # latex.append(r"\hline")
    for (kind, domains) in DOMAINS_BY_KIND.items():
        latex.append(r"\hline")
        empty = "".join(["&" for c in COLUMNS.values() for e in EXPERIMENTS] +
                        ["&" for x in DOMAIN_INFOS_COLUMNS] +
                        ["&" for x in ICS_COLUMNS]
                        )
        latex.append(r"\textbf{" + kind + "}" + empty + r"\\")
        # latex.append(r"\hline")
        for d in domains:
            row = [DOMAINS[d]["text"]] + \
                  [domainInfos[d][key] for (key, text) in DOMAIN_INFOS_COLUMNS.items()] + \
                  [domainInfos[d][key] for (key, text) in ICS_COLUMNS.items()]
            for e in EXPERIMENTS:
                for c in COLUMNS.keys():
                    v = table[d][e][c] if d in table else "N/D"
                    row.append(f"{v}")
            latex.append("&".join(row) + r"\\")

    latex.append(r"\hline")
    latex.append(r"""\end{tabular}}} \caption{Experimental analysis on the solving times required to retrieve an 
    initial condition on well-known hybrid planning and numeric domains. The domains can be linear $(\textsc{L})$ or 
    non-linear $(\textsc{NL})$ depending on the form of the numeric effects. The percentage $\beta$ represents the 
    amount of known initial condition.} \label{tab:total} \vspace{-0.75cm} \end{table} \end{document}""")
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