from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

AIJ_TABLE4 = {
    "name": "tab:search",
    "type": "table*",
    "orientation": "portrait",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between search planners",
    "columns": {
        "quantity": {
            "name": "Solved (out of $20$)",
            "winner": +1,
            "avg": True
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "stdev": True
        },
        "planLength": {
            "name": r"Plan Length",
            "winner": -1
        },
    },
    "planners": {
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "scalar",
            # "slashedWith": "PATTY-L"
        },
        # 'PATTY-L': {
        #     "name": r"\mathrm{P}_\mathrm{I}",
        #     "type": "skip"
        # },
        'ENHSP': {
            "name": AIJ_PLANNERS['ENHSP']["name"],
            "type": "scalar",
        },
        'NFD': {
            "name": AIJ_PLANNERS['NFD']["name"],
            "type": "scalar",
        },
        'METRIC-FF': {
            "name": AIJ_PLANNERS['METRIC-FF']["name"],
            "type": "scalar",
        },
    },
    "domains": AIJ_DOMAINS
}
