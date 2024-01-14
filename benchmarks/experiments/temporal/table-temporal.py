import csv
import os
import shutil
import statistics

from classes.Result import Result

SMT_SOLVERS = {'PATTY-T-OR', 'PATTY-T-SIGMA', 'PATTY-T-OR-ASTAR', 'PATTY-T-SIGMA-ASTAR', 'ANMLSMT', 'ITSAT'}

SOLVERS = {
    "PATTY-T-OR": r"\textsc{Patty}_{\vee}",
    "PATTY-T-SIGMA": r"\textsc{Patty}_{\Sigma}",
    "PATTY-T-OR-ASTAR": r"\textsc{Patty}_{\vee}^*",
    "PATTY-T-SIGMA-ASTAR": r"\textsc{Patty}_{\Sigma}^*",
    "ANMLSMT": r"\textsc{AnmlSMT}",
    "ITSAT": r"\textsc{ITSat}",
    "LPG": r"\textsc{LPG}",
    "OPTIC": r"\textsc{Optic}",
    "TFD": r"\textsc{TFD}",
}

DOMAINS = {
    "temporal/cushing": r"\textsc{Cushing} (B)",
    "temporal/bottles-pour": r"\textsc{Pour} (N)",
    "temporal/bottles-shake": r"\textsc{Shake} (N)",
    "temporal/bottles-pack": r"\textsc{Pack} (N)",
    "temporal/bottles-all": r"\textsc{Bottles} (N)",
    "temporal/majsp": r"\textsc{Majsp} (N)",
    "temporal/match-ac": r"\textsc{MatchAC} (B)",
    "temporal/match-ms": r"\textsc{MatchMS} (B)",
    "temporal/oversub": r"\textsc{Oversub} (B)",
    "temporal/painter": r"\textsc{Painter} (B)",
}

TIMEOUT = 30 * 1000


def main():
    filename = "2024-01-13-ASTAR-v1.csv"
    files = [f"benchmarks/results/{filename}", f"benchmarks/results/2024-01-12-FINAL-v7.csv"]

    results: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                results.append(Result.fromCSVLine(line[0].split(",")))

    solvers = set()
    domains = set()
    d = dict()
    for r in results:
        if r.domain not in DOMAINS:
            continue
        d[r.domain] = d.setdefault(r.domain, dict())
        solvers.add(r.solver)
        domains.add(r.domain)
        d[r.domain][r.solver] = d[r.domain].setdefault(r.solver, [])
        d[r.domain][r.solver].append(r)

    solvers = list(solvers)
    solvers.sort()
    domains = list(domains)
    domains.sort()

    DOMAINS_STATS = dict()

    for domain in domains:
        DOMAINS_STATS[domain] = 0
        for solver in solvers:
            if domain not in d or solver not in d[domain]:
                continue
            DOMAINS_STATS[domain] = max(DOMAINS_STATS[domain], len(d[domain][solver]))

    def r(fValue, n):
        return '{:.{n}f}'.format(fValue, n=n)

    t = dict()
    stats = set()
    for (domain, domainDict) in d.items():
        t[domain] = {
            "coverage": dict(),
            "bound": dict(),
            "time": dict(),
            "length": dict(),
            "nOfVars": dict(),
            "nOfRules": dict(),
        }

        commonlySolved = {}
        commonlyGrounded = {}
        for solver in SMT_SOLVERS:
            if solver not in domainDict:
                continue
            solved = {r.problem[:-5] for r in domainDict[solver] if r.solved}
            grounded = {r.problem[:-5] for r in domainDict[solver] if r.nOfVars > 0}
            if solved:
                commonlySolved = solved if not commonlySolved else commonlySolved.intersection(solved)
            if grounded:
                commonlyGrounded = solved if not commonlyGrounded else commonlyGrounded.intersection(grounded)

        for solver in solvers:
            if solver not in domainDict:
                continue
            pResult = domainDict[solver]
            t[domain]["coverage"][solver] = r(sum([r.solved for r in pResult]) / DOMAINS_STATS[domain] * 100, 1)
            t[domain]["coverage"][solver] = "-" if t[domain]["coverage"][solver] == "0.0" else t[domain]["coverage"][
                solver]
            bounds = [r.bound for r in pResult if r.solved if
                      r.problem[:-5] in commonlySolved or r.domain == "temporal/oversub"]
            t[domain]["bound"][solver] = r(statistics.mean(bounds), 2) if t[domain]["coverage"][
                                                                              solver] != "-" and bounds else "-"
            t[domain]["time"][solver] = r(statistics.mean([r.time if r.solved else TIMEOUT for r in pResult]) / 1000,
                                          2) if \
                t[domain]["coverage"][solver] != "-" else "-"
            t[domain]["length"][solver] = r(statistics.mean([r.planLength for r in pResult if r.solved]), 0) if \
                t[domain]["coverage"][solver] != "-" else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 0) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 0) if len(v) else "-"

    domainsClusters = {
        r"\textit{Temporal}": [
            "temporal/cushing",
            "temporal/bottles-pour",
            "temporal/bottles-shake",
            "temporal/bottles-pack",
            "temporal/bottles-all",
            "temporal/majsp",
            "temporal/match-ac",
            "temporal/match-ms",
            "temporal/oversub",
            "temporal/painter"
        ],
        # r"\textit{Temporal Numeric}": [
        #     "temporal/paper-example",
        #     "temporal/majsp",
        #     "temporal/rovers",
        #     "temporal/satellite",
        #     "temporal/zenotravel",
        # ]
    }

    winners = {
        "coverage": +1,
        "bound": -1,
        "time": -1,
        "nOfVars": -1,
        "nOfRules": -1,
    }

    tables = [{
        "name": "tab:experiments",
        "type": "table*",
        "width": r"\textwidth",
        "columns": {
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}),
            "time": ("Time (s)", {"SMT", "SEARCH"}),
            "bound": ("Bound (Common)", {"SMT"}),
            # "nOfVars": ("$|\mathcal{X} \cup \mathcal{A} \cup \mathcal{X}'|$", {"SMT"}),
            # "nOfRules": ("$|\mathcal{T}(\mathcal{X},\mathcal{A},\mathcal{X}')|$", {"SMT"}),
        },
        "solvers": {
            # "PATTY-T-OR": r"SMT",
            # "PATTY-T-SIGMA": r"SMT",
            "PATTY-T-OR-ASTAR": r"SMT",
            "PATTY-T-SIGMA-ASTAR": r"SMT",
            "ANMLSMT": r"SMT",
            "ITSAT": r"SMT",
            "LPG": r"SEARCH",
            "OPTIC": r"SEARCH",
            "TFD": r"SEARCH",
        },
        "caption": r"Comparative analysis between ..."
    },
        #     {
        #     "name": "tab:exp-search",
        #     "type": "table",
        #     "width": r"\columnwidth",
        #     "columns": {
        #         "coverage": "Coverage (\%)",
        #         "time": "Time (s)",
        #         # "length": "Plan Length"
        #     },
        #     "solvers": [
        #         # 'PATTY-arpg-yices-binary',
        #         'PATTY',
        #         # 'RANTANPLAN',
        #         # 'SpringRoll',
        #         'ENHSP',
        #         'METRIC-FF',
        #         "NFD"
        #     ],
        #     "caption": r"Comparative analysis between \textsc{Patty} and the search-based solvers \textsc{ENHSP} (E), "
        #                r"\textsc{MetricFF} (FF) and \textsc{NumericFastDownward} (NFD)."
        # }
    ]

    latex = []
    latex.append(r"""
            \documentclass[11pt,landscape]{article}
            \usepackage{graphicx}
            \usepackage{lscape}
            \usepackage{multirow}
            \usepackage[a4paper,margin=1in,landscape]{geometry}

            \begin{document}""")
    for table in tables:
        stats = table["columns"].keys()
        solvers = table["solvers"].keys()

        best = dict()
        for (domain, domainDict) in d.items():
            best[domain] = dict()
            for stat in table["columns"].keys():
                better = {}
                betterValue = float("-inf") if winners[stat] > 0 else float("+inf")
                for solver in solvers:
                    if solver not in t[domain][stat]:
                        continue
                    value = t[domain][stat][solver]
                    if value in {"-", "G", "-1.00"}:
                        continue
                    if float(value) * winners[stat] > betterValue * winners[stat]:
                        betterValue = float(value)
                        better = {solver}
                    elif float(value) == betterValue:
                        better |= {solver}
                best[domain][stat] = better

        latex.append(r"""
            \begin{""" + table["type"] + r"""}[tb]
            \centering
            \resizebox{""" + table["width"] + r"""}{!}{""")

        solversHeader = []
        mString = []
        cString = ""
        for (stat, (name, statTypes)) in table["columns"].items():
            nCells = 0
            for (solver, type) in table["solvers"].items():
                if type not in statTypes:
                    continue
                solversHeader.append(f"${SOLVERS[solver]}$")
                nCells += 1
            mString.append(r"\multicolumn{" + str(nCells) + "}{c||}{" + name + "}")
            cString += f"|{nCells * 'c'}|"

        columns = f"|l|{cString}" + "|"
        latex.append("\Huge{")
        latex.append(r"\begin{tabular}{" + columns + "}")
        latex.append(r"\hline")
        latex.append(fr" & " + "&".join(mString) + r"\\")
        latex.append(fr"Domain & " + "&".join(solversHeader) + r"\\")
        latex.append(fr"\hline")

        for (cluster, clusterDomains) in domainsClusters.items():
            rows = []
            row = [cluster]
            for (stat, (name, statTypes)) in table["columns"].items():
                for (solver, type) in table["solvers"].items():
                    if type not in statTypes:
                        continue
                    nOfBest = 0
                    for domain in clusterDomains:
                        if domain in best and solver in best[domain][stat]:
                            nOfBest += 1
                    row.append(r"\textbf{" + str(nOfBest) + "}")
            latex.append("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                if domain not in DOMAINS:
                    continue
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes)) in table["columns"].items():
                    for (solver, type) in table["solvers"].items():
                        if type not in statTypes:
                            continue
                        if domain not in t or solver not in t[domain][stat]:
                            row.append("-")
                            continue
                        if solver in best[domain][stat]:
                            row.append(r"\textbf{" + t[domain][stat][solver] + "}")
                        else:
                            row.append(t[domain][stat][solver])
                rows.append("&".join(row))
            latex.append("\\\\\n".join(rows))
            latex.append(fr"\\\hline")

        latex.append(r"""
        \end{tabular}}}
        \caption{""" + table["caption"] + """}
        \label{""" + table["name"] + """}
        \end{""" + table["type"] + """}
        """)

    latex.append(r"""\end{document}""")

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

    pass


if __name__ == '__main__':
    main()
