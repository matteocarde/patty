from benchmarks.tables.ices.domains import ICES_DOMAINS

TABLE_ICES_PLANNERS = {
    "PATTY-ICES": {"type": "smt"},
    "TAMER": {"type": "search"},
    "PATTY-T-OR-ASTAR": {"type": "smt"},
    "ANMLSMT": {"type": "smt"},
    "ITSAT": {"type": "smt"},
    "LPG": {"type": "search"},
    "OPTIC": {"type": "search"},
    "TFD": {"type": "search"},
}

ICES_ALL = {
    "name": "tab:results",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"TODO",
    "columns": {
        "coverage": {
            "name": "Coverage (\%)",
            "winner": +1,
            "avg": True,
            "planners": TABLE_ICES_PLANNERS.keys()
        },
        # "quantity": {
        #     "name": "Solved (out of $20$)",
        #     "winner": +1,
        #     "avg": True
        # },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "avg": True,
            "planners": TABLE_ICES_PLANNERS.keys()
        },
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "avg": True,
            "planners": [key for (key, item) in TABLE_ICES_PLANNERS.items() if item["type"] == "smt"]
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
    "planners": TABLE_ICES_PLANNERS,
    "domains": ICES_DOMAINS
}
