from benchmarks.tables.aij.domains import AIJ_DOMAINS
from benchmarks.tables.aij.planners import AIJ_PLANNERS

AIJ_TABLE3 = {
    "name": "tab:symbolic",
    "type": "table*",
    "orientation": "landscape",
    "width": r"\textwidth",
    "time-limit": 300 * 1000,
    "caption": r"Comparative analysis between \pattye and other symbolic planners. In the table, names have been "
               r"abbreviated to save space. See \cite{ipc2023} for more details. A ``-'' indicates that no problem in "
               r"the domain has been solved with the given resources.  Best results are in bold.",
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
            "name": r"Plan length",
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
            "name": AIJ_PLANNERS["RANTANPLAN"]["name"],
            "type": "scalar",
        },
        'R2E+ROLL': {
            "name": AIJ_PLANNERS["R2E+ROLL"]["name"],
            "type": "scalar",
        },
        'OMT': {
            "name": AIJ_PLANNERS["OMT"]["name"],
            "type": "scalar",
        },
        'SPRINGROLL': {
            "name": AIJ_PLANNERS["SPRINGROLL"]["name"],
            "type": "scalar",
        },
    },
    "domains": AIJ_DOMAINS
}
