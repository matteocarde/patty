from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

JAIR_TABLE1 = {
    "name": "tab:exp-patty-a-patty-e",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between  \pattya and \pattye. Each domain is labeled with S (for simple) if "
               r"every numeric effect of each action either increases or decreases by a constant the assigned "
               r"variable, and with L (for linear), otherwise. In the table, names have been abbreviated to save "
               r"space.  See \cite{ipc2023} for more details. A ``-'' indicates that no problem in the domain has "
               r"been solved with the given resources. Best results are in bold",
    "columns": {
        # "coverage": {
        #     "name": "Coverage (\%)",
        #     "winner": +1,
        #     "stdev": False
        # },
        "quantity": {
            "name": "Solved (out of $20$)",
            "winner": +1,
            "avg": True
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "avg": True
        },
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "avg": True
        },
        # "length": {
        #     "name": r"$|\pi|$",
        #     "winner": -1
        # },
        # "nOfVars": {
        #     "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
        #     "winner": -1,
        #     "stdev": False
        # },
        # "nOfRules": {
        #     "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
        #     "winner": -1,
        #     "stdev": False
        # },
    },
    "planners": {
        'PATTY-E': {
            "name": AIJ_PLANNERS['PATTY-E']["name"],
            "type": "scalar"
        },
        'PATTY-A': {
            "name": AIJ_PLANNERS['PATTY-A']["name"],
            "type": "scalar"
        },
        'PATTY-R-MIN': {
            "name": AIJ_PLANNERS['PATTY-R-MIN']["name"],
            "type": "scalar"
        },
        'PATTY-R-MED': {
            "name": AIJ_PLANNERS['PATTY-R-MED']["name"],
            "type": "scalar"
        },
        'PATTY-R-MAX': {
            "name": AIJ_PLANNERS['PATTY-R-MAX']["name"],
            "type": "scalar"
        },
    },
    "domains": AIJ_DOMAINS
}
