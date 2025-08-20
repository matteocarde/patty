from benchmarks.tables.jair.domains import JAIR_DOMAINS

JAIR_CBRG = {
    "name": "tab:cbrg",
    "orientation": "landscape",
    "type": "table*",
    "width": r"\textwidth",
    "keepAll": True,
    "caption": r"Cautious, Brave, Reckless and Greedy \pattyd vs \pattyo. Planner names are abbreviated.",
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
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "avg": True
        },
        "patternLength": {
            "name": r"$|\prec|$",
            "winner": -1
        },
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
        "PATTY-EG": {"type": "scalar"},
        "PATTY-C-npc": {"type": "scalar"},
        "PATTY-B-npc": {"type": "scalar"},
        "PATTY-R-nec": {"type": "scalar"},
        "PATTY-G-nei": {"type": "scalar"},
    },
    "domains": JAIR_DOMAINS
}
