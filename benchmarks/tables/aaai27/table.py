from benchmarks.tables.aaai27.domains import AAAI27_DOMAINS

AAAI27_TABLE = {
    "name": "tab:ipc",
    "orientation": "portrait",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Classic \textsc{ipc}-2014 testset",
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
        # "PATTY-FE": {},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-G-nei": {"type": "scalar"},
        "PATTY-Hplus": {"type": "scalar"},
    },
    "domains": AAAI27_DOMAINS
}
