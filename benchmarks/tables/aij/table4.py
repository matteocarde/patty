from benchmarks.tables.aij.domains import AIJ_DOMAINS

AIJ_TABLE4 = {
    "name": "tab:search",
    "type": "table*",
    "orientation": "portrait",
    "width": r"\textwidth",
    "time-limit": 30 * 1000,
    "caption": r"Comparative analysis between search planners",
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
        }
    },
    "planners": {
        'ENHSP': {
            "name": r"\mathrm{EN}",
            "type": "scalar",
        },
        'NFD': {
            "name": r"\mathrm{NFD}",
            "type": "scalar",
        },
        'METRIC-FF': {
            "name": r"\mathrm{FF}",
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
