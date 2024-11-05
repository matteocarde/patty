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
        'PATTY-A': {
            "name": r"\mathrm{P}_\mathrm{A}",
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
        'RANTANPLAN': {
            "name": AIJ_PLANNERS["RANTANPLAN"]["name"],
            "type": "scalar",
        },
        'OMT': {
            "name": AIJ_PLANNERS["OMT"]["name"],
            "type": "scalar",
        },
        'SPRINGROLL': {
            "name": AIJ_PLANNERS["SPRINGROLL"]["name"],
            "type": "scalar",
        },
    },
    "domains": AIJ_DOMAINS
}
