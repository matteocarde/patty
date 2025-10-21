from benchmarks import AIJ_DOMAINS
from benchmarks import AIJ_PLANNERS

JAIR_SEARCH = {
    "name": "tab:search",
    "type": "table*",
    "orientation": "portrait",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between ... and other publicly available search-based planners.",
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
        }
    },
    "planners": {
        "PATTY-C-npc": {"type": "scalar"},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-R-nec": {"type": "scalar"},
        "PATTY-G-nei": {"type": "scalar"},
        # 'PATTY-L': {
        #     "name": r"\mathrm{P}_\mathrm{I}",
        #     "type": "skip"
        # },
        'ENHSP-SOCS': {
            "type": "scalar",
        },
        'ENHSP': {
            "type": "scalar",
        },
        'NFD': {
            "type": "scalar",
        },
        'METRIC-FF': {
            "type": "scalar",
        },
    },
    "domains": AIJ_DOMAINS
}
