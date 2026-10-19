from benchmarks.tables.ices.domains import ICES_DOMAINS

TABLE_ABLATION_ALL_PLANNERS = {
    "PATTY-ICES": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-TIME-MIN": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-TIME-MED": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-TIME-MAX": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-ACTION-MIN": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-ACTION-MED": {"type": "smt"},
    "PATTY-ICES-PATTERN-RANDOM-ACTION-MAX": {"type": "smt"},
    "PATTY-ICES-PATTERN-GOAL-COUNTING": {"type": "smt"},
    "PATTY-ICES-NO-ROLLING": {"type": "smt"},
}

TABLE_ABLATION_ALL = {
    "name": "tab:results",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"TODO",
    "columns": {
        # "coverage": {
        #     "name": "Coverage (\%)",
        #     "winner": +1,
        #     "avg": True,
        #     "planners": TABLE_ABLATION_ALL_PLANNERS.keys()
        # },
        "quantity": {
            "name": "Solved",
            "winner": +1,
            "avg": True,
            "planners": TABLE_ABLATION_ALL_PLANNERS.keys()
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "avg": True,
            "planners": TABLE_ABLATION_ALL_PLANNERS.keys()
        },
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "avg": True,
            "planners": [key for (key, item) in TABLE_ABLATION_ALL_PLANNERS.items() if item["type"] == "smt"]
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
    "planners": TABLE_ABLATION_ALL_PLANNERS,
    "domains": ICES_DOMAINS
}
