from benchmarks import AIJ_DOMAINS
from benchmarks import AIJ_PLANNERS

JAIR_ABL_PATTERNG = {
    "name": "tab:abl-patterng",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Impact of the $\pattern_g$ refinement on Cautious and Brave \pattyd. Planner names are abbreviated.",
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
