from benchmarks.tables.ices.domains import ICES_DOMAINS

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
            "avg": True
        },
        # "quantity": {
        #     "name": "Solved (out of $20$)",
        #     "winner": +1,
        #     "avg": True
        # },
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
        # "PATTY-FE": {},
        "PATTY-ICES": {"type": "scalar"},
        "PATTY-T-OR-ASTAR": {"type": "scalar"},
        "TAMER": {"type": "scalar"}
    },
    "domains": ICES_DOMAINS
}
