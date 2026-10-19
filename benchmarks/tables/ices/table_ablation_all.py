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

TABLE_ABLATION_NO_ROLLING = {
    "name": "tab:ablation-no-rolling",
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
    },
    "planners": {
        "PATTY-ICES": {"type": "smt"},
        "PATTY-ICES-NO-ROLLING": {"type": "smt"},
    },
    "domains": ICES_DOMAINS
}

TABLE_ABLATION_PATTERN_RANDOM_ACTION = {
    "name": "tab:ablation-pattern-random-action",
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
    },
    "planners": {
        "PATTY-ICES": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-ACTION-MIN": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-ACTION-MED": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-ACTION-MAX": {"type": "smt"},
    },
    "domains": ICES_DOMAINS
}

TABLE_ABLATION_PATTERN_RANDOM_TIME = {
    "name": "tab:ablation-pattern-random-time",
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
    },
    "planners": {
        "PATTY-ICES": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-TIME-MIN": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-TIME-MED": {"type": "smt"},
        "PATTY-ICES-PATTERN-RANDOM-TIME-MAX": {"type": "smt"},
    },
    "domains": ICES_DOMAINS
}

TABLE_ABLATION_GOAL_COUNTING = {
    "name": "tab:ablation-goal-counting",
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
    },
    "planners": {
        "PATTY-ICES": {"type": "smt"},
        "PATTY-ICES-PATTERN-GOAL-COUNTING": {"type": "smt"}
    },
    "domains": ICES_DOMAINS
}
