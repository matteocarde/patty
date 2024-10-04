from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE2 = {
    "name": "tab:qual-plans",
    "type": "table*",
    "orientation": "portrait",
    "width": r"\textwidth",
    "time-limit": 30 * 1000,
    "caption": r"Comparative analysis between  \pattye, \pattym and \pattyi. Each domain is labeled with S (for "
               r"simple) if every numeric effect of each action either increases or decreases by a constant the "
               r"assigned variable, and with L (for linear), otherwise. In the table, names have been abbreviated to "
               r"save space.  See \cite{ipc2023} for other details.",
    "columns": {
        "coverage": {
            "name": "Coverage (\%)",
            "winner": +1,
            "stdev": False
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "stdev": True
        },
        # "bound": {
        #     "name": r"Bound $n$",
        #     "winner": -1,
        #     "stdev": True
        # },
        "length": {
            "name": r"$|\pi|$",
            "winner": -1
        },
        # "nOfVars": {
        #     "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
        #     "winner": -1,
        #     "stdev": True
        # },
        # "nOfRules": {
        #     "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
        #     "winner": -1,
        #     "stdev": True
        # },
    },
    "planners": {
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "scalar",
        },
        'PATTY-M': {
            "name": r"\mathrm{P}_\mathrm{M}",
            "type": "scalar"
        },
        'PATTY-I': {
            "name": r"\mathrm{P}_\mathrm{I}",
            "type": "scalar"
        },
        'PATTY-L': {
            "name": r"\mathrm{P}_\leq",
            "type": "scalar"
        },
    },
    "domains": AIJ_DOMAINS
}
