from benchmarks import AIJ_DOMAINS
from benchmarks import AIJ_PLANNERS

JAIR_ABL_GF = {
    "name": "tab:abl-gf",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Impact of the goal function on Cautious, Brave, Reckless and Greedy \pattyd. Planner names are abbreviated.",
    "columns": {
        # "coverage": {
        #     "name": "Coverage (\%)",
        #     "winner": +1,
        #     "stdev": False
        # },
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
        # "bound": {
        #     "name": r"\textsc{smt} calls",
        #     "winner": -1,
        #     "avg": True
        # },
        # "length": {
        #     "name": r"$|\pi|$",
        #     "winner": -1
        # },
        # "nOfVars": {
        #     "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
        #     "winner": -1,
        #     "stdev": False
        # },
        # "nOfRules": {
        #     "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
        #     "winner": -1,
        #     "stdev": False
        # },
    },
    "planners": {
        # "PATTY-FE": {},
        "PATTY-C-npc": {"type": "scalar"},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-R-nec": {"type": "scalar"},
        "PATTY-G-nei": {"type": "scalar"},
        "PATTY-C-gpc": {"type": "scalar"},
        "PATTY-B-gpc": {"type": "scalar"},
        "PATTY-R-gec": {"type": "scalar"},
        "PATTY-G-gei": {"type": "scalar"},
        "PATTY-C-aes": {"type": "scalar"},
    },
    "domains": AIJ_DOMAINS
}
