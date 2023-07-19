import argparse

from src.utils.LogPrint import LogPrintLevel


class Arguments:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Patty - The Symbolic Numeric Planner using Patterns')
        #parser.add_argument('-h', '--help', dest='help', help='Print this message', action="store_true")
        parser.add_argument('-o', '--domain', dest='domain', help='The .pddl domain file', required=True)
        parser.add_argument('-f', '--problem', dest='problem', help='The .pddl problem file', required=True)
        parser.add_argument('-n', '--bound', help='The number of steps of the SMT encoding')
        parser.add_argument('-v', '--verboseLevel', help=f'The level of verbosity: {LogPrintLevel.getLevels()} ',
                            default=LogPrintLevel.getDefault(), type=int)
        parser.add_argument('--deep', help="Iterative deepening approach to find the best plan (at the given bound)",
                            action="store_true")
        parser.add_argument('--pattern', default="arpg", help="Method too compute the pattern: arpg, random")
        parser.add_argument('--solver', default="z3", help="The solver used to compute a solution: yices, z3")
        parser.add_argument('--encoding', default="non-linear",
                            help="The way linear numeric effect are dealt with: binary, non-linear")
        parser.add_argument('-pp', help="Print pattern", action="store_true")
        parser.add_argument('--arpg', help="Prints the arpg", action="store_true")
        parser.add_argument('--binary-actions',
                            help="Number of binary actions allowed in the binary encoding (default=10)", default=10,
                            type=int)
        parser.add_argument('--save-smt', help="Where to save the smt rules")
        parser.add_argument('--save-plan', help="Where to save the plan", nargs='?', const="PROBLEM")
        parser.add_argument('--effect-axioms',
                            help="If the encoding has effect axioms for each action (quadratic, RanTanPlan's Like)",
                            action="store_true", default=False)
        parser.add_argument('--roll-bound', help="The maximum amount of time an action can be rolled at each step",
                            type=int, default=0)

        args = parser.parse_args()
        self.isHelp = "help" in args
        self.domain = args.domain
        self.problem = args.problem
        self.bound = args.bound
        self.verboseLevel = LogPrintLevel(args.verboseLevel)
        self.deep = args.deep
        self.printPattern = args.pp
        self.printARPG = args.arpg
        self.pattern = args.pattern
        self.solver = args.solver
        self.encoding = args.encoding
        self.saveSMT = args.save_smt
        self.savePlan = args.save_plan
        self.binaryActions = int(args.binary_actions)
        self.hasEffectAxioms = args.effect_axioms
        self.rollBound = args.roll_bound
