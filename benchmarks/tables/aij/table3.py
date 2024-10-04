from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE3 = {
    "name": "tab:symbolic",
    "type": "table*",
    "orientation": "landscape",
    "width": r"\textwidth",
    "time-limit": 30 * 1000,
    "caption": r"Comparative analysis between symbolic planners",
    "columns": {
        "coverage": {
            "name": "Coverage (\%)",
            "winner": +1,
            "stdev": False
        },
        "time": {
            "name": "Time (s)",
            "winner": -1,
            "stdev": True
        },
        "bound": {
            "name": r"Bound $n$",
            "winner": -1,
            "stdev": True
        },
        "length": {
            "name": r"$|\pi|$",
            "winner": -1
        },
        "nOfVars": {
            "name": "$|\mathcal{X} \cup \mathcal{A}^\prec \cup \mathcal{X}'|$",
            "winner": -1,
            "stdev": True
        },
        "nOfRules": {
            "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
            "winner": -1,
            "stdev": True
        },
    },
    "planners": {
        'RANTANPLAN': {
            "name": r"\mathrm{R^2\exists}",
            "type": "scalar",
        },
        'OMT': {
            "name": r"\mathrm{OMT}",
            "type": "scalar",
        },
        'Springroll': {
            "name": r"\mathrm{SR}",
            "type": "scalar",
        },
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "scalar",
        },
        'PATTY-I': {
            "name": r"\mathrm{P}_\mathrm{I}",
            "type": "scalar"
        },
    },
    "domains": AIJ_DOMAINS
}