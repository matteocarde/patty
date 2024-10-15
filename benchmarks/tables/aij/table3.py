from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE3 = {
    "name": "tab:symbolic",
    "type": "table*",
    "orientation": "landscape",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
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
            "stdev": True,
            "avoidSlashing": True
        },
        "nOfRules": {
            "name": "$|\mathcal{T}^\prec(\mathcal{X},\mathcal{A}^\prec,\mathcal{X}')|$",
            "winner": -1,
            "stdev": True,
            "avoidSlashing": True
        },
    },
    "planners": {
        'PATTY-E': {
            "name": r"\mathrm{P}_\mathrm{E}",
            "type": "slashed",
            "slashedWith": "PATTY-L"
        },
        'PATTY-L': {
            "name": r"\mathrm{P}_\mathrm{I}",
            "type": "skip"
        },
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
