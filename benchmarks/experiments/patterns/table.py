import csv
import os
import shutil
import statistics

from classes.Result import Result

SMT_SOLVERS = {'SPRINGROLL', 'PATTY', 'RANTANPLAN', "OMT"}

SOLVERS = {
    'SPRINGROLL': "SR",
    'PATTY': "P",
    'PATTY-R': "P_r",
    'RANTANPLAN': "\mathrm{R^2\exists}",
    'METRIC-FF': "\mathrm{FF}",
    'ENHSP': r"\mathrm{ENHSP}",
    'NFD': "\mathrm{NFD}",
    'SMTPLAN+': "\mathrm{SMTP}^+",
    'OMT': "\mathrm{OMT}",
}

DOMAINS = {
    "numeric/ipc-2023/block-grouping": r"\textsc{BlockGrouping} (S)",
    "numeric/ipc-2023/counters": r"\textsc{Counters} (S)",
    "numeric/ipc-2023/delivery": r"\textsc{Delivery} (S)",
    "numeric/ipc-2023/drone": r"\textsc{Drone} (S)",
    "numeric/ipc-2023/expedition": r"\textsc{Expedition} (S)",
    "numeric/ipc-2023/ext-plant-watering": r"\textsc{PlantWatering} (S)",
    "numeric/ipc-2023/farmland": r"\textsc{Farmland} (S)",
    "numeric/ipc-2023/fo-farmland": r"\textsc{Farmland} (L)",
    "numeric/ipc-2023/fo-sailing": r"\textsc{Sailing} (L)",
    "numeric/ipc-2023/fo_counters": r"\textsc{Counters} (L)",
    "numeric/ipc-2023/hydropower": r"\textsc{HydroPower} (S)",
    # "ipc-2023/markettrader": r"\textsc{MarketTrader}",
    "numeric/ipc-2023/mprime": r"\textsc{MPrime} (S)",
    "numeric/ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
    "numeric/ipc-2023/rover": r"\textsc{Rover} (S)",
    "numeric/ipc-2023/sailing": r"\textsc{Sailing} (S)",
    "numeric/ipc-2023/satellite": r"\textsc{Satellite} (S)",
    "numeric/ipc-2023/settlers": r"\textsc{Settlers} (S)",
    "numeric/ipc-2023/sugar": r"\textsc{Sugar} (S)",
    "numeric/ipc-2023/tpp": r"\textsc{TPP} (L)",
    "numeric/ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
    "numeric/line-exchange": r"\textsc{LineExchange} (L)",
    "numeric/line-exchange-quantity": r"\textsc{LineExchange-QTY} (L)"
}

TOTALS = {
    "numeric/ipc-2023/block-grouping": 20,
    "numeric/ipc-2023/counters": 20,
    "numeric/ipc-2023/delivery": 20,
    "numeric/ipc-2023/drone": 20,
    "numeric/ipc-2023/expedition": 20,
    "numeric/ipc-2023/ext-plant-watering": 20,
    "numeric/ipc-2023/farmland": 20,
    "numeric/ipc-2023/fo-farmland": 20,
    "numeric/ipc-2023/fo-sailing": 20,
    "numeric/ipc-2023/fo_counters": 20,
    "numeric/ipc-2023/hydropower": 20,
    "numeric/ipc-2023/markettrader": 20,
    "numeric/ipc-2023/mprime": 20,
    "numeric/ipc-2023/pathwaysmetric": 20,
    "numeric/ipc-2023/rover": 20,
    "numeric/ipc-2023/sailing": 20,
    "numeric/ipc-2023/satellite": 20,
    "numeric/ipc-2023/settlers": 20,
    "numeric/ipc-2023/sugar": 20,
    "numeric/ipc-2023/tpp": 20,
    "numeric/ipc-2023/zenotravel": 20,
    "numeric/line-exchange": 108,
    "numeric/line-exchange-quantity": 20
}


def main():
    ## Parsing the results
    exp = "2024-03-13-AIJ-ALL-V1"
    files = [
        f"benchmarks/results/{exp}.csv"
    ]

    aResults: [Result] = []
    for file in files:
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                aResults.append(Result.fromCSVLine(line[0].split(",")))

    ## Joining together portfolios
    results = Result.joinPorfolios(aResults, {
        "ENHSP-SAT-HADD": "ENHSP",
        "ENHSP-SAT-AIBR": "ENHSP",
        "ENHSP-SAT-HMRP": "ENHSP",
    })

    solvers = set()
    domains = set()
    d = dict()
    for r in results:
        d[r.domain] = d.setdefault(r.domain, dict())
        solvers.add(r.solver)
        domains.add(r.domain)
        d[r.domain][r.solver] = d[r.domain].setdefault(r.solver, dict())
        d[r.domain][r.solver][r.problem] = d[r.domain][r.solver].setdefault(r.problem, list())
        d[r.domain][r.solver][r.problem].append(r)

    solvers = list(solvers)
    solvers.sort()
    domains = list(domains)
    domains.sort()

    for domain in domains:
        for solver in solvers:
            problems = list()
            if solver not in d[domain]:
                continue
            for problem in d[domain][solver].keys():
                problems.append(Result.average(d[domain][solver][problem]))
            d[domain][solver] = problems

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
            solved = {r.problem for r in domainDict[solver] if r.solved}
            grounded = {r.problem for r in domainDict[solver] if r.nOfVars > 0}
            if solved:
                commonlySolved = solved if not commonlySolved else commonlySolved.intersection(solved)
            if grounded:
                commonlyGrounded = solved if not commonlyGrounded else commonlyGrounded.intersection(grounded)

        a = 1 + 1

        for solver in solvers:
            if solver not in domainDict:
                continue
            pResult = domainDict[solver]
            coverage = r(sum([r.solved for r in pResult]) / TOTALS[domain] * 100, 1)
            t[domain]["coverage"][solver] = "-" if coverage == "0.0" else coverage

            bounds = [r.bound for r in pResult if r.solved and r.problem in commonlySolved]
            t[domain]["bound"][solver] = r(statistics.mean(bounds), 1) if coverage != "-" and bounds else "-"
            v = [r.time if r.solved else 300000 for r in pResult]
            t[domain]["time"][solver] = r(statistics.mean(v) / 1000, 1) if coverage != "-" else "-"

            v = [r.planLength for r in pResult if r.solved and r.problem in commonlySolved]
            t[domain]["length"][solver] = r(statistics.mean(v), 1) if coverage != "-" and v else "-"

            v = [r.nOfVars for r in pResult if r.nOfVars > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfVars"][solver] = r(statistics.mean(v), 1) if len(v) else "-"
            v = [r.nOfRules for r in pResult if r.nOfRules > 0 and r.problem in commonlyGrounded]
            t[domain]["nOfRules"][solver] = r(statistics.mean(v), 1) if len(v) else "-"

    domainsClusters = {
        r"\textit{Highly Numeric}": [
            "numeric/ipc-2023/block-grouping",
            "numeric/ipc-2023/counters",
            "numeric/ipc-2023/fo_counters",
            "numeric/ipc-2023/drone",
            "numeric/ipc-2023/ext-plant-watering",
            "numeric/ipc-2023/farmland",
            "numeric/ipc-2023/fo-farmland",
            "numeric/ipc-2023/hydropower",
            "numeric/ipc-2023/sailing",
            "numeric/ipc-2023/fo-sailing",
            # "line-exchange",
            # "line-exchange-quantity"
        ],
        r"\textit{Lowly Numeric}": [
            "numeric/ipc-2023/delivery",
            "numeric/ipc-2023/expedition",
            # "numeric/ipc-2023/markettrader",
            "numeric/ipc-2023/mprime",
            "numeric/ipc-2023/pathwaysmetric",
            "numeric/ipc-2023/rover",
            "numeric/ipc-2023/satellite",
            # "numeric/ipc-2023/settlers",
            "numeric/ipc-2023/sugar",
            "numeric/ipc-2023/tpp",
            "numeric/ipc-2023/zenotravel"
        ]
    }

    winners = {
        "coverage": +1,
        "bound": -1,
        "time": -1,
        "length": -1,
        "nOfVars": -1,
        "nOfRules": -1,
    }

    tables = [{
        "name": "tab:experiments-all",
        "type": "table*",
        "width": r"\textwidth",
        "columns": {
            "coverage": ("Coverage (\%)", {"SMT", "SEARCH"}),
            "time": ("Time (s)", {"SMT", "SEARCH"}),
            "length": ("Plan Length", {"SMT", "SEARCH"}),
        },
        "solvers": {
            'PATTY': "SMT",
            'PATTY-R': "SMT",
            'RANTANPLAN': "SMT",
            'SPRINGROLL': "SMT",
            "OMT": "SMT",
            'ENHSP': "SEARCH",
            'METRIC-FF': "SEARCH",
            "NFD": "SEARCH"
        },
        "caption": r""
    },
        {
            "name": "tab:experiments-smt",
            "type": "table*",
            "width": r"\textwidth",
            "columns": {
                "bound": ("Bound (Common)", {"SMT"}),
                "nOfVars": ("$|\mathcal{X} \cup \mathcal{A} \cup \mathcal{X}'|$", {"SMT"}),
                "nOfRules": ("$|\mathcal{T}(\mathcal{X},\mathcal{A},\mathcal{X}')|$", {"SMT"}),
            },
            "solvers": {
                'PATTY': "SMT",
                'PATTY-R': "SMT",
                'RANTANPLAN': "SMT",
                'SPRINGROLL': "SMT",
                "OMT": "SMT"
            },
            "caption": r""
        }
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
                        if solver in best[domain][stat]:
                            nOfBest += 1
                    row.append(r"\textbf{" + str(nOfBest) + "}")
            latex.append("&".join(row) + r"\\\hline")
            for domain in clusterDomains:
                row = [DOMAINS[domain]]
                for (stat, (name, statTypes)) in table["columns"].items():
                    for (solver, type) in table["solvers"].items():
                        if type not in statTypes:
                            continue
                        if solver not in t[domain][stat]:
                            row.append("TBD")
                            continue
                        if solver in best[domain][stat]:
                            row.append(r"\textbf{" + t[domain][stat][solver] + "}")
                        else:
                            row.append(t[domain][stat][solver])
                rows.append("&".join(row))
            latex.append("\\\\\n".join(rows))
            latex.append(fr"\\\hline")

        row = ["$\emph{Total}$"]
        for (stat, (name, statTypes)) in table["columns"].items():
            for (solver, type) in table["solvers"].items():
                if type not in statTypes:
                    continue
                nOfBest = 0
                for (cluster, clusterDomains) in domainsClusters.items():
                    for domain in clusterDomains:
                        if solver in best[domain][stat]:
                            nOfBest += 1
                row.append(r"\textbf{" + str(nOfBest) + "}")
        latex.append("&".join(row) + r"\\\hline")

        latex.append(r"""
        \end{tabular}}
        \caption{""" + table["caption"] + """}
        \label{""" + table["name"] + """}
        \end{""" + table["type"] + """}
        """)

    latex.append(r"""\end{document}""")

    latexStr = "\n".join(latex)

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
