from benchmarks.tables.pushing.domains_table1 import PUSHING_DOMAINS_TABLE1
from benchmarks.tables.pushing.planners import PUSHING_PLANNERS

PUSHING_TABLE1 = {
    "name": "tab:experiments",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis of \pattyo, \pattyg, \pattyh and \pattyf. The labels (S) and (L) indicate if the "
               r"domain is Simple or Linear, according to the \ipc definition. The table with all the 19 domains is in "
               r"the supplementary material.",
    "columns": {
        "quantity": {
            "name": "Solved (out of $20$)",
            "winner": +1
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
        "nOfVars": {
            "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
            "winner": -1,
            "avg": True
        },
        "nOfRules": {
            "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
            "winner": -1,
            "avg": True
        },
    },
    "planners": {
        'PATTY-EF': {
            "name": PUSHING_PLANNERS['PATTY-EF']["name"],
            "type": "scalar"
        },
        'PATTY-EH': {
            "name": PUSHING_PLANNERS['PATTY-EH']["name"],
            "type": "scalar"
        },
        'PATTY-EG': {
            "name": PUSHING_PLANNERS['PATTY-EG']["name"],
            "type": "scalar"
        },
        'PATTY-EO': {
            "name": PUSHING_PLANNERS['PATTY-EO']["name"],
            "type": "scalar"
        },
    },
    "domains": PUSHING_DOMAINS_TABLE1

}
