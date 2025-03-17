from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

JAIR_TABLE1 = {
    "name": "tab:all-patty",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "time-limit": 30 * 1000,
    "caption": r"",
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
        # "PATTY-FE": {},
        # "PATTY-HE": {},
        "PATTY-GAMMA-MAX": {"type": "scalar"},
        "PATTY-GAMMA-GC": {"type": "scalar"},
        "PATTY-GAMMA-PLUS": {"type": "scalar"},
        "PATTY-GAMMA-XOR": {"type": "scalar"},
        "PATTY-DELTA-MAX": {"type": "scalar"},
        "PATTY-DELTA-PLUS": {"type": "scalar"},
        "PATTY-DELTA-XOR": {"type": "scalar"},
    },
    "domains": AIJ_DOMAINS
}
