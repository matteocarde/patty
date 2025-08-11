from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

JAIR_TABLE5 = {
    "name": "tab:table-5",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"",
    "columns": {
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
    },
    "planners": {
        "PATTY-C-npc": {"type": "scalar"},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-R-nec": {"type": "scalar"},
        "PATTY-G-nei": {"type": "scalar"},
        "PATTY-C-nps": {"type": "scalar"},
        "PATTY-B-nps": {"type": "scalar"},
        "PATTY-R-nes": {"type": "scalar"},
    },
    "domains": AIJ_DOMAINS
}
