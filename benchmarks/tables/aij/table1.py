from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE1 = {
    "name": "tab:exp-random",
    "type": "table*",
    "width": r"\textwidth",
    "time-limit": 30 * 1000,
    "caption": r"Comparative analysis between  \pattyr, \pattya and \pattye. \pattyr has been run 5 times and we "
               r"report the best, worst and average performance, denoted respectively with \pattyrmin, \pattyrmax and "
               r"\pattyravg. Each domain is labeled with S (for simple) if every numeric effect of each action either "
               r"increases or decreases by a constant the assigned variable, and with L (for linear), otherwise. In "
               r"the table, names have been abbreviated to save space.  See \cite{ipc2023} for other details.",
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
        "bound": {
            "name": r"Bound $n$",
            "winner": -1,
            "stdev": True
        },
        # "length": {
        #     "name": r"$|\pi|$",
        #     "winner": -1
        # },
        "nOfVars": {
            "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
            "winner": -1,
            "stdev": True
        },
        "nOfRules": {
            "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
            "winner": -1,
            "stdev": True
        },
    },
    "planners": {
        'PATTY-R-AVG': {
            "name": r"\mathrm{P}_\mathrm{R}",
            "type": "avg",
            "stdev": 'PATTY-R-STDEV'
        },
        'PATTY-R-STDEV': {
            "name": r"\mathrm{P}_\mathrm{R}",
            "type": "stdev"
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
