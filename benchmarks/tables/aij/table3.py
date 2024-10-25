from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE3 = {
    "name": "tab:symbolic",
    "type": "table*",
    "orientation": "landscape",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between symbolic planners",
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
        },
        "bound": {
            "name": r"\textsc{smt} calls",
            "winner": -1,
            "stdev": True
        },
        "planLength": {
            "name": r"$Plan length$",
            "winner": -1
        },
        "nOfVars": {
            "name": "Variables",
            "winner": -1,
            "stdev": True,
            "avoidSlashing": True
        },
        "nOfRules": {
            "name": "Assertions",
            "winner": -1,
            "stdev": True,
            "avoidSlashing": True
        },
    },
    "planners": {
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "scalar",
            # "slashedWith": "PATTY-L"
        },
        # 'PATTY-L': {
        #     "name": r"\mathrm{P}_\mathrm{I}",
        #     "type": "skip"
        # },
        'RANTANPLAN': {
            "name": r"\mathrm{R^2\exists}",
            "type": "scalar",
        },
        'OMT': {
            "name": r"\mathrm{OMT}",
            "type": "scalar",
        },
        'SPRINGROLL': {
            "name": r"\mathrm{SR}",
            "type": "scalar",
        },
    },
    "domains": AIJ_DOMAINS
}
