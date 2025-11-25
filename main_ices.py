import traceback

from z3 import z3

from src.ices.ICEPlan import ICEPlan
from src.ices.ICETask import ICETask
from src.pddl.Domain import Domain, GroundedDomain
from src.pddl.NumericPlan import NumericPlan
from src.pddl.Plan import Plan
from src.pddl.Problem import Problem
from src.plan.Pattern import Pattern
from src.search.AStarSearchMax import AStarSearchMax
from src.search.BDCSearch import BDCSearch
from src.search.ChainSearch import ChainSearch
from src.search.ChrpaImprover import ChrpaImprover
from src.search.GDSearch import GDSearch
from src.search.ICECautiousGPCSearch import ICECautiousGPCSearch
from src.search.JairSearch import JairSearch
from src.search.PASSearch import PASSearch
from src.search.PlanImproverLess import PlanImproverLess
from src.search.PlanImproverPattern import PlanImproverPattern
from src.search.Search import Search
from src.search.StepSearch import StepSearch
from src.utils.Arguments import Arguments
from src.utils.LogPrint import LogPrint, LogPrintLevel
from src.utils.TimeStat import TimeStat


def main_ices(args):
    try:
        print(f"Using z3 version {z3.get_version_string()}")
        console: LogPrint = LogPrint(args.verboseLevel)
        ts: TimeStat = TimeStat()
        ts.start("Overall")

        task: ICETask
        if ".anml" in args.domain:
            th = ts.startHolder("Converting from ANML")
            task: ICETask = ICETask.fromANML(args.domain, args.problem)
            th.endHolder()
        else:
            th = ts.startHolder("Converting from PDDL")
            domain: Domain = Domain.fromFile(args.domain)
            problem: Problem = Problem.fromFile(args.problem)
            gDomain: GroundedDomain = domain.ground(problem)

            task: ICETask = ICETask.fromTemporalNoICEs(gDomain, problem)
            th.endHolder()


        solver = ICECautiousGPCSearch(task, args)
        plan: ICEPlan = solver.solve()

        plan.print()
        console.log("------", LogPrintLevel.STATS)
        isValid = plan.isValid()
        if isValid:
            console.log("Plan is valid", LogPrintLevel.PLAN)
        else:
            console.log("Plan is NOT valid", LogPrintLevel.PLAN)

        ts.end("Overall")
        console.log(str(ts), LogPrintLevel.TIMES)

    except:
        print("Something went wrong.")
        traceback.print_exc()
