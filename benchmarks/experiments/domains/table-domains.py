import json
import os
import shutil
import statistics
from typing import Dict


def r(fValue, n):
    return '{:.{n}f}'.format(fValue, n=n)


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
    # "numeric/ipc-2023/markettrader": r"\textsc{MarketTrader}",
    "numeric/ipc-2023/mprime": r"\textsc{MPrime} (S)",
    "numeric/ipc-2023/pathwaysmetric": r"\textsc{PathwaysMetric} (S)",
    "numeric/ipc-2023/rover": r"\textsc{Rover} (S)",
    "numeric/ipc-2023/sailing": r"\textsc{Sailing} (S)",
    "numeric/ipc-2023/satellite": r"\textsc{Satellite} (S)",
    "numeric/ipc-2023/settlers": r"\textsc{Settlers} (S)",
    "numeric/ipc-2023/sugar": r"\textsc{Sugar} (S)",
    "numeric/ipc-2023/tpp": r"\textsc{TPP} (L)",
    "numeric/ipc-2023/zenotravel": r"\textsc{ZenoTravel} (S)",
    # "line-exchange": r"\textsc{LineExchange} (L)",
    # "line-exchange-quantity": r"\textsc{LineExchange-QTY} (L)"
}

CLUSTERS = {
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
        "numeric/ipc-2023/fo-sailing"
    ],
    r"\textit{Lowly Numeric}": [
        "numeric/ipc-2023/delivery",
        "numeric/ipc-2023/expedition",
        # "ipc-2023/markettrader",
        "numeric/ipc-2023/mprime",
        "numeric/ipc-2023/pathwaysmetric",
        "numeric/ipc-2023/rover",
        "numeric/ipc-2023/satellite",
        # "ipc-2023/settlers",
        "numeric/ipc-2023/sugar",
        "numeric/ipc-2023/tpp",
        "numeric/ipc-2023/zenotravel"
    ]
}


def main():
    folder = "benchmarks/stats/numeric/"
    filename = f"{folder}/numeric.json"
    stats: Dict[str, Dict[str, Dict[str, str]]]
    with open(filename, "r") as f:
        stats = json.load(f)

    t: Dict[str, Dict[str, str]] = dict()

    for domain, d in stats.items():
        t[domain] = dict()
        nOfFunctions = statistics.mean([int(p["nOfFunctions"]) for p in d.values()])
        nOfPredicates = statistics.mean([int(p["nOfPredicates"]) for p in d.values()])
        t[domain]["nOfFunctions"] = r(nOfFunctions, 1)
        t[domain]["nOfPredicates"] = r(nOfPredicates, 1)
        t[domain]["nOfSnapActions"] = r(statistics.mean([int(p["nOfSnapActions"]) for p in d.values()]), 1)
        t[domain]["ratio"] = r(nOfPredicates / nOfFunctions, 1) if nOfFunctions else "-"

    tables = [{
        "name": "tab:domains",
        "type": "table",
        "width": r"\textwidth",
        "columns": {
            "nOfPredicates": "$|V_B|$",
            "nOfFunctions": "$|V_N|$",
            "nOfSnapActions": "$|A|$",
            "ratio": "$|V_B|/|V_N|$"
        },
        "caption": r"Statistic on domains of the 2023 IPC."
    }]

    latex = []
    latex.append(r"""
                \documentclass[11pt]{article}
                \usepackage{graphicx}
                \usepackage{multirow}
                \usepackage[a4paper,margin=1in]{geometry}

                \begin{document}""")

    for table in tables:
        keys = table["columns"].keys()
        keysLatex = table["columns"].values()

        latex.append(r"""
                \begin{""" + table["type"] + r"""}[tb]
                \centering
                \resizebox{""" + table["width"] + r"""}{!}{""")

        columns = f"|l|{''.join(['c' for k in keys])}" + "|"

        latex.append(r"\begin{tabular}{" + columns + "}")
        latex.append(r"\hline")
        latex.append(fr"Domain & " + "&".join(keysLatex) + r"\\")
        latex.append(fr"\hline")

        for (cluster, clusterDomains) in CLUSTERS.items():
            rows = []
            row = [cluster] + ['' for k in keys]
            latex.append("&".join(row) + r"\\\hline")

            for domain in clusterDomains:
                row = [DOMAINS[domain]] + [t[domain][key] for key in keys]
                rows.append("&".join(row))
            latex.append("\\\\\n".join(rows))
            latex.append(fr"\\\hline")

        latex.append(r"""
            \end{tabular}}
            \caption{""" + table["caption"] + """}
            \label{""" + table["name"] + """}
            \end{""" + table["type"] + """}
            """)

    latex.append(r"""\end{document}""")

    latexStr = "\n".join(latex)

    file = filename.replace(".json", "")

    with open(f"{file}.tex", "w") as f:
        f.write(latexStr)
    os.system(f"pdflatex -interaction=nonstopmode --output-directory='{folder}' {file}.tex ")

    os.remove(f"{file}.aux")
    os.remove(f"{file}.log")


if __name__ == '__main__':
    main()
