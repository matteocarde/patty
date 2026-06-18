from typing import Dict

from classes.planners.AnmlSMT import AnmlSMT
from classes.planners.ENHSP import ENHSP
from classes.planners.ENHSP_SOCS import ENHSP_SOCS
from classes.planners.ITSAT import ITSAT
from classes.planners.LPG import LPG
from classes.planners.Madagascar import Madagascar
from classes.planners.MetricFF import MetricFF
from classes.planners.NFD import NFD
from classes.planners.OMT import OMT
from classes.planners.Optic import Optic
from classes.planners.Patty import Patty
from classes.planners.Planner import Planner
from classes.planners.SpringRoll import SpringRoll
from classes.planners.TFD import TFD
from classes.planners.Tamer import Tamer

BENCHMARK_PLANNERS: Dict[str, Planner] = {
    "PATTY-T-OR": Patty("PATTY-T-OR", temporalConstraints='logical'),
    "PATTY-T-SIGMA": Patty("PATTY-T-SIGMA", temporalConstraints='numerical'),
    "PATTY-T-OR-ASTAR": Patty("PATTY-T-OR", temporalConstraints='logical', search="astar"),
    "PATTY-T-SIGMA-ASTAR": Patty("PATTY-T-SIGMA", temporalConstraints='numerical', search="astar"),
    "PATTY-O": Patty("PATTY-O", search="step", pattern="arpg"),
    "PATTY-G": Patty("PATTY-G", search="static", pattern="arpg"),
    "PATTY-H": Patty("PATTY-H", search="astar", pattern="arpg", noCompression=True),
    "PATTY-F": Patty("PATTY-F", search="astar", pattern="arpg", noCompression=False),
    "PATTY-EO": Patty("PATTY-EO", search="step", pattern="enhanced"),
    "PATTY-EG": Patty("PATTY-EG", search="static", pattern="enhanced"),
    "PATTY-EH": Patty("PATTY-EH", search="astar", pattern="enhanced", noCompression=True),
    "PATTY-EF": Patty("PATTY-EF", search="astar", pattern="enhanced", noCompression=False),
    "PATTY-CES": Patty("PATTY-CES", tcTime=40),
    "PATTY-CES-NO-TC": Patty("PATTY-CES-NO-TC", avoidClosure=True),
    "PATTY-CES-NO-C": Patty("PATTY-CES-NO-C", avoidClosureRelaxation=True),

    "PATTY-R": Patty("PATTY-R", search="step", pattern="random", quality="none"),
    "PATTY-A": Patty("PATTY-A", search="step", pattern="arpg", quality="none"),
    "PATTY-E": Patty("PATTY-E", search="step", pattern="enhanced", quality="none"),
    "PATTY-FA": Patty("PATTY-FA", search="astar", pattern="arpg", quality="none"),
    "PATTY-FE": Patty("PATTY-FE", search="astar", pattern="enhanced", quality="none"),
    "PATTY-M": Patty("PATTY-M", search="step", pattern="enhanced", quality="shortest-step"),
    "PATTY-I": Patty("PATTY-I", search="step", pattern="enhanced", quality="improve-plan"),
    "PATTY-L": Patty("PATTY-L", search="step", pattern="enhanced", quality="improve-less"),
    "PATTY-C": Patty("PATTY-C", search="step", pattern="enhanced", quality="improve-chrpa"),

    "PATTY-GD": Patty("PATTY-GD", search="gd"),
    "PATTY-BDC": Patty("PATTY-BDC", search="bdc"),

    "PATTY-B-npc": Patty("PATTY-B-npc", search="jair",
                         jairSearchStrategy="B",
                         jairGoalFunction="n",
                         jairPatternG="p",
                         jairPatternH="c"),
    "PATTY-G-nei": Patty("PATTY-G-nei", search="jair",
                         jairSearchStrategy="G",
                         jairGoalFunction="n",
                         jairPatternG="e",
                         jairPatternH="i"),
    "PATTY-B-npc-chrpa": Patty("PATTY-B-npc-chrpa", search="jair",
                               jairSearchStrategy="B",
                               jairGoalFunction="n",
                               jairPatternG="p",
                               jairPatternH="c",
                               quality="improve-chrpa"),
    "PATTY-G-nei-chrpa": Patty("PATTY-G-nei-chrpa", search="jair",
                               jairSearchStrategy="G",
                               jairGoalFunction="n",
                               jairPatternG="e",
                               jairPatternH="i",
                               quality="improve-chrpa"),

    "PATTY-Hplus": Patty("PATTY-Hplus", search="heuristic",
                               heuristic="h+"),

    "PATTY-EF-NO-ORDER": Patty("PATTY-EF-NO-ORDER", search="astar", noCompression=False, dontKeepSubgoals=True),
    "PATTY-GD-NO-ORDER": Patty("PATTY-GD-NO-ORDER", search="gd", dontKeepSubgoals=True),
    "PATTY-BDC-NO-ORDER": Patty("PATTY-BDC-NO-ORDER", search="bdc", dontKeepSubgoals=True),

    "RANTANPLAN": Patty("RANTANPLAN", search="step", pattern="enhanced", hasEffectAxioms=True, rollBound=1),
    "R2E+ROLL": Patty("R2E+ROLL", search="step", pattern="enhanced", hasEffectAxioms=True, rollBound=1000),
    "SPRINGROLL": SpringRoll(),

    "ENHSP-SOCS": ENHSP_SOCS(),
    "ENHSP-SAT-HMRP": ENHSP(False, settings="-h hmrp -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMRP"),
    "ENHSP-SAT-HMRPHJ": ENHSP(False, settings="-planner sat-hmrphj -silent -pp -pe", name="ENHSP-SAT-HMRPHJ"),
    "ENHSP-SAT-HADD": ENHSP(False, settings="-h hadd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HADD"),
    "ENHSP-SAT-HMAX": ENHSP(False, settings="-h hmax -s gbfs -silent -pp -pe", name="ENHSP-SAT-HMAX"),
    "ENHSP-SAT-AIBR": ENHSP(False, settings="-h aibr -s gbfs -silent -pp -pe", name="ENHSP-SAT-AIBR"),
    "ENHSP-SAT-HRADD": ENHSP(False, settings="-h hradd -s gbfs -silent -pp -pe", name="ENHSP-SAT-HRADD"),
    "ENHSP-SAT-BLIND": ENHSP(False, settings="-h blind -s gbfs -silent -pp -pe", name="ENHSP-SAT-BLIND"),

    "ENHSP-OPT-HMRP": ENHSP(False, settings="-h hmrp -s WAStar -silent -pp -pe", name="ENHSP-OPT-HMRP"),
    "ENHSP-OPT-HADD": ENHSP(False, settings="-h hadd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HADD"),
    "ENHSP-OPT-HMAX": ENHSP(False, settings="-h hadd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HMAX"),
    "ENHSP-OPT-AIBR": ENHSP(False, settings="-h aibr -s WAStar -silent -pp -pe", name="ENHSP-OPT-AIBR"),
    "ENHSP-OPT-HRADD": ENHSP(False, settings="-h hradd -s WAStar -silent -pp -pe", name="ENHSP-OPT-HRADD"),
    "ENHSP-OPT-BLIND": ENHSP(False, settings="-h blind -s WAStar -silent -pp -pe", name="ENHSP-OPT-BLIND"),

    "METRIC-FF": MetricFF(),
    "NFD": NFD(),
    "OMT": OMT(),
    "MADAGASCAR": Madagascar(),

    "LPG": LPG(),
    "TFD": TFD(),
    "OPTIC": Optic(),
    "ITSAT": ITSAT(),
    "ANMLSMT": AnmlSMT(),
    "TAMER": Tamer(),
    "PATTY-ICES": Patty("PATTY-ICES", ices=True),
}