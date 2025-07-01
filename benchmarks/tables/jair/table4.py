from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

JAIR_TABLE4 = {
    "name": "tab:all-patty",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
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
        # "planLength": {
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
        "PATTY-S": {"type": "scalar"},
        "PATTY-D": {"type": "scalar"},
        "PATTY-DR": {"type": "scalar"},
        "PATTY-DI": {"type": "scalar"},
        "PATTY-DIR": {"type": "scalar"},
        "PATTY-DB": {"type": "scalar"},
        "PATTY-DBR": {"type": "scalar"},
        "PATTY-DBI": {"type": "scalar"},
        "PATTY-DBIR": {"type": "scalar"},
        "PATTY-DG": {"type": "scalar"},
        "PATTY-DGI": {"type": "scalar"},
    },
    "domains": AIJ_DOMAINS
}
