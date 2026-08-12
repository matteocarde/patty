from benchmarks.tables.aaai27.domains import AAAI27_DOMAINS
from benchmarks.tables.jair_classical.domains import JAIR_CLASSICAL_DOMAINS

JAIR_CLASSICAL_TABLE = {
    "name": "tab:CLASSICAL",
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
        "MADAGASCAR": {"type": "scalar"},
    },
    "domains": JAIR_CLASSICAL_DOMAINS
}
