from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE1 = {
    "name": "tab:exp-patty-a-patty-e",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between  \pattya and \pattye. Each domain is labeled with S (for simple) if "
               r"every numeric effect of each action either increases or decreases by a constant the assigned "
               r"variable, and with L (for linear), otherwise. In the table, names have been abbreviated to save "
               r"space.  See \cite{ipc2023} for other details.",
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
        'PATTY-R-MIN': {
            "name": r"\mathrm{P}_\mathrm{R}^{min}",
            "type": "scalar"
        },
        'PATTY-R-MED': {
            "name": r"\mathrm{P}_\mathrm{R}^{med}",
            "type": "scalar"
        },
        'PATTY-R-MAX': {
            "name": r"\mathrm{P}_\mathrm{R}^{max}",
            "type": "scalar"
        },
        'PATTY-A': {
            "name": r"\mathrm{P}_\mathrm{A}",
            "type": "scalar"
        },
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "scalar"
        },
    },
    "domains": AIJ_DOMAINS
}
