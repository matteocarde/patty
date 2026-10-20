from benchmarks.tables.ices.domains import ICES_DOMAINS

TABLE_ICES_PLANNERS = {
    "PATTY-ICES": {"type": "smt"},
    "TAMER": {"type": "search"},
    # "PATTY-T-OR-ASTAR": {"type": "smt"},
    "ANMLSMT": {"type": "smt"},
    "OPTIC": {"type": "search"},
    "ITSAT": {"type": "smt"},
    "LPG": {"type": "search"},
    "TFD": {"type": "search"},
}

ICES_ALL_SOLVED_TIME = {
    "name": "tab:results-solved-time",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Comparative analysis over all solver considering $(i)$ the number of solved instances and $(ii)$ the average time it took to "
               r"solve them. A “-” indicates that no result was obtained in our 5min time limit. The best results are in bold.",
    "columns": {
        "quantity": {
            "name": "Solved",
            "winner": +1,
            "avg": True,
            "planners": TABLE_ICES_PLANNERS.keys()
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "avg": True,
            "planners": TABLE_ICES_PLANNERS.keys()
        },
        # "bound": {
        #     "name": r"\textsc{smt} calls",
        #     "winner": -1,
        #     "avg": True,
        #     "planners": [key for (key, item) in TABLE_ICES_PLANNERS.items() if item["type"] == "smt"]
        # },
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

ICES_ALL_BOUND_MAKESPAN = {
    "name": "tab:results-bound-makespan",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Comparative analysis over all solvers and all domains considering $(i)$ for Planning as Satisfiability approaches, the average number of steps required to find a solution, and $(ii)$ the average makespan of the plans returned. "
               r"A “-” indicates that no result was obtained in our 5min time limit. The best results are in bold.",
    "columns": {
        # "quantity": {
        #     "name": "Solved",
        #     "winner": +1,
        #     "avg": True,
        #     "planners": TABLE_ICES_PLANNERS.keys()
        # },
        # "time": {
        #     "name": "Time (s)",
        #     "winner": -1,
        #     "avg": True,
        #     "planners": TABLE_ICES_PLANNERS.keys()
        # },
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "avg": True,
            "planners": [key for (key, item) in TABLE_ICES_PLANNERS.items() if item["type"] == "smt"]
        },
        "makespan": {
            "name": r"$ms(\pi)$",
            "winner": -1,
            "avg": True,
            "planners": TABLE_ICES_PLANNERS.keys()
        }
    },
    "planners": TABLE_ICES_PLANNERS,
    "domains": ICES_DOMAINS
}
