from benchmarks.tables.ipc.domains import IPC_DOMAINS

IPC_TABLE = {
    "name": "tab:ipc",
    "orientation": "portrait",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"\textsc{ipc}-2023 testset",
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
        "PATTY-B-npc-chrpa": {"type": "scalar"},
        "PATTY-G-nei-chrpa": {"type": "scalar"},
    },
    "domains": IPC_DOMAINS
}
