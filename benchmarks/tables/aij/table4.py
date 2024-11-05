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
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
        },
        "planLength": {
            "name": r"Plan Length",
            "winner": -1
        },
        "bound": {
            "name": r"Bound $n$",
            "winner": -1
        },
    },
    "planners": {
        'PATTY-G': {
            "name": r"\mathrm{P}_\mathrm{G}",
            "type": "scalar",
            # "slashedWith": "PATTY-L"
        },
        'PATTY-H': {
            "name": r"\mathrm{P}_\mathrm{H}",
            "type": "scalar",
            # "slashedWith": "PATTY-L"
        },
        'PATTY-F': {
            "name": r"\mathrm{P}_\mathrm{F}",
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
