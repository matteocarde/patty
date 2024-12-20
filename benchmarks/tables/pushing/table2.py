from benchmarks.tables.pushing.domains_table2 import PUSHING_DOMAINS_TABLE2
from benchmarks.tables.pushing.planners import PUSHING_PLANNERS

PUSHING_TABLE2 = {
    "name": "tab:exp-search",
    "type": "table*",
    "orientation": "portrait",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis of \pattyf and the search based planners \textsc{ENHSP}, \textsc{MetricFF} and "
               r"\textsc{NFD}. A ‘‘-” means that no problem in the domain was solved by the planner.",
    "columns": {
        "quantity": {
            "name": "Solved (out of $20$)",
            "winner": +1,
            "avg": False
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "avg": True
        },
    },
    "planners": {
        'PATTY-EF': {
            "name": PUSHING_PLANNERS['PATTY-F']["name"],
            "type": "scalar"
        },
        'ENHSP': {
            "name": PUSHING_PLANNERS['ENHSP']["name"],
            "type": "scalar"
        },
        'ENHSP-SOCS': {
            "name": PUSHING_PLANNERS['ENHSP-SOCS']["name"],
            "type": "scalar"
        },
        'METRIC-FF': {
            "name": PUSHING_PLANNERS['METRIC-FF']["name"],
            "type": "scalar"
        }
    },
    "domains": PUSHING_DOMAINS_TABLE2
}
