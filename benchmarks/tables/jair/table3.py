from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

JAIR_TABLE3 = {
    "name": "tab:table-3",
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
        }
    },
    "planners": {
        "PATTY-C-npc": {"type": "scalar"},
        "PATTY-C-nrc": {"type": "scalar"},
        "PATTY-C-noc": {"type": "scalar"},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-B-nrc": {"type": "scalar"},
        "PATTY-B-noc": {"type": "scalar"},
    },
    "domains": AIJ_DOMAINS
}
