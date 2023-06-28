package planners;


import com.hstairs.ppmajal.domain.PDDLDomain;
import com.hstairs.ppmajal.extraUtils.Utils;
import com.hstairs.ppmajal.pddl.heuristics.PDDLHeuristic;
import com.hstairs.ppmajal.problem.PDDLProblem;
import com.hstairs.ppmajal.problem.PDDLSearchEngine;
import com.hstairs.ppmajal.problem.PDDLState;
import com.hstairs.ppmajal.search.SearchEngine;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.lang3.tuple.Pair;
import com.hstairs.ppmajal.search.SearchHeuristic;
import com.hstairs.ppmajal.transition.TransitionGround;
import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/*
 * Copyright (C) 2016-2017 Enrico Scala. Email enricos83@gmail.com.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301  USA
 */
/**
 *
 * @author enrico
 *
 *
 *
 */
public class ENHSP {

    private String domainFile;
    private String problemFile;
    private String searchEngineString;
    private String hw;
    private String heuristic = "aibr";
    private String gw;
    private boolean saving_json = false;
    private String deltaExecution;
    private float depthLimit;
    private String savePlan;
    private boolean printTrace;
    private String tieBreaking;
    private String planner;
    private String deltaHeuristic;
    private String deltaPlanning;
    private String deltaValidation;
    private boolean helpfulActionsPruning;
    private Integer numSubdomains;
    private PDDLProblem problem;
    private boolean pddlPlus;
    private PDDLDomain domain;
    private PDDLDomain domainHeuristic;
    private PDDLProblem heuristicProblem;
    private long overallStart;
    private boolean copyOfTheProblem;
    private boolean anyTime;
    private long timeOut;
    private boolean aibrPreprocessing;
    private SearchHeuristic h;
    private long overallPlanningTime;
    private float endGValue;
    private boolean helpfulTransitions;
    private boolean internalValidation = false;
    private int planLength;
    private String redundantConstraints;
    private String groundingType;
    private boolean naiveGrounding;
    private boolean stopAfterGrounding;
    private boolean printEvents;

    private boolean sdac;
    private boolean onlyPlan;
    private boolean ignoreMetric;
    private boolean printActions;
    private String inputPlan;
    private PrintStream out;

    public ENHSP(boolean copyProblem) {
        copyOfTheProblem = copyProblem;
    }

    public int getPlanLength() {
        return planLength;
    }

    public Pair<PDDLDomain, PDDLProblem> parseDomainProblem(String domainFile, String problemFile, String delta, PrintStream out) {
        try {
            final PDDLDomain localDomain = new PDDLDomain(domainFile);
            //domain.substituteEqualityConditions();
            pddlPlus = !localDomain.getProcessesSchema().isEmpty() || !localDomain.getEventsSchema().isEmpty();
            out.println("Domain parsed");
            final PDDLProblem localProblem = new PDDLProblem(problemFile, localDomain.getConstants(),
                    localDomain.getTypes(), localDomain, out, groundingType, sdac, ignoreMetric,new BigDecimal(deltaPlanning),new BigDecimal(deltaExecution));
            if (!localDomain.getProcessesSchema().isEmpty()) {
                localProblem.setDeltaTimeVariable(delta);
            }
            //this second model is the one used in the heuristic. This can potentially be different from the one used in the execution model. Decoupling it
            //allows us to a have a finer control on the machine
            //the third one is the validation model, where, also in this case we test our plan against a potentially more accurate description
            out.println("Problem parsed");
            out.println("Grounding..");

            localProblem.prepareForSearch(aibrPreprocessing, stopAfterGrounding);
            
            if (printActions){
                System.out.println(localProblem.getTransitions());
            }
            if (stopAfterGrounding) {
                System.exit(1);
            }
            return Pair.of(localDomain, localProblem);
        } catch (Exception ex) {
            Logger.getLogger(ENHSP.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public void parsingDomainAndProblem(String[] args) {
        try {
            overallStart = System.currentTimeMillis();
            Pair<PDDLDomain, PDDLProblem> res = parseDomainProblem(domainFile, problemFile, deltaExecution, System.out);
            domain = res.getKey();
            problem = res.getRight();
            if (pddlPlus) {
                res = parseDomainProblem(domainFile, problemFile, deltaHeuristic, new PrintStream(new OutputStream() {
                    public void write(int b) {}}));
                domainHeuristic = res.getKey();
                heuristicProblem = res.getRight();
                copyOfTheProblem = true;
            } else {
                heuristicProblem = problem;
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void configurePlanner() {
        if (planner != null) {
            setPlanner();
        }
    }

    public void planning() {

        try {
            printStats();
            setHeuristic();
            do {
                LinkedList sp = search();
                if (sp == null) {
                    return;
                }
                depthLimit = endGValue;
                if (anyTime) {
                    System.out.println("NEW COST ==================================================================================>" + depthLimit);
                }
                sp = null;
                System.gc();
            } while (anyTime);
        } catch (Exception ex) {
            Logger.getLogger(ENHSP.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    public void parseInput(String[] args) {
        Options options = new Options();
        options.addRequiredOption("o", "domain", true, "PDDL domain file");
        options.addRequiredOption("f", "problem", true, "PDDL problem file");
        options.addOption("planner", true, "Fast Preconfgured Planner. For available options look into the code. This overrides all other parameters but domain and problem specs.");
        options.addOption("h", true, "heuristic: options (default is AIBR):\n"
                + "aibr, Additive Interval Based relaxation heuristic\n"
                + "hadd, Additive version of subgoaling heuristic\n"
                + "hradd, Additive version of subgoaling heuristic plus redundant constraints\n"
                + "hmax, Hmax for Numeric Planning\n"
                + "hrmax, Hmax for Numeric Planning with redundant constraints\n"
                + "hmrp, heuristic based on MRP extraction\n"
                + "blcost, goal sensitive heuristic (1 to non goal-states, 0 to goal-states)"
                + "blind, full blind heuristic (0 to all states)");
        options.addOption("s", true, "allows to select search strategy (default is WAStar):\n"
                + "gbfs, Greedy Best First Search (f(n) = h(n))\n"
                + "WAStar, WA* (f(n) = g(n) + h_w*h(n))\n"
                + "wa_star_4, WA* (f(n) = g(n) + 4*h(n))\n");
        options.addOption("ties", true, "tie-breaking (default is arbitrary): larger_g, smaller_g, arbitrary");
        options.addOption("dp", "delta_planning", true, "planning decision executionDelta: float");
        options.addOption("de", "delta_execuction", true, "planning execution executionDelta: float");
        options.addOption("dh", "delta_heuristic", true, "planning heuristic executionDelta: float");
        options.addOption("dv", "delta_validation", true, "validation executionDelta: float");
        options.addOption("d", "delta", true, "Override other delta_<planning,execuction,validation,heuristic> configurations: float");
        options.addOption("epsilon", true, "epsilon separation: float");
        options.addOption("wh", true, "h-values weight: float");
        options.addOption("sjr", false, "save state space explored in json file");
        options.addOption("ha", "helpful-actions", true, "activate helpful actions pruning");
        options.addOption("pe", "print-events-plan", false, "activate printing of events");

        options.addOption("ht", "helpful-transitions", true, "activate up-to-macro actions");
        options.addOption("sp", true, "Save plan. Argument is filename");
        options.addOption("pt", false, "print state trajectory (Experimental)");
//        options.addOption("im", false, "Ignore Metric in the heuristic");
        options.addOption("dap", false, "Disable Aibr Preprocessing");
        options.addOption("red", "redundant_constraints", true, "Choose mechanism for redundant constraints generation among, "
                + "no, brute and smart. No redundant constraints generation is the default");
        options.addOption("gro", "grounding", true, "Activate grounding via internal mechanism, fd or metricff or internal or naive (default is internal)");

        options.addOption("dl", true, "bound on plan-cost: float (Experimental)");
        options.addOption("k", true, "maximal number of subdomains. This works in combination with haddabs: integer");
        options.addOption("anytime", false, "Run in anytime modality. Incrementally tries to find a lower bound. Does not stop until the user decides so");
        options.addOption("timeout", true, "Timeout for anytime modality");
        options.addOption("stopgro", false, "Stop After Grounding");
        options.addOption("ival", false, "Internal Validation");
        options.addOption("sdac", false, "Activate State Dependent Action Cost (Very Experimental!)");
        options.addOption("onlyplan",false,"Print only the plan without waiting");
        options.addOption("print_actions",false,"Print all actions after grounding");
        options.addOption("tolerance",true,"Numeric tolerance in evaluating numeric conditions. Default is 0.00001");
        options.addOption("inputplan",true,"Insert the name of the file containing the plan to validate. This is to be used with ival activated");
        options.addOption("silent",false,"Activate silent modality");
 

        CommandLineParser parser = new DefaultParser();
        try {
            CommandLine cmd = parser.parse(options, args);
            domainFile = cmd.getOptionValue("o");
            problemFile = cmd.getOptionValue("f");
            planner = cmd.getOptionValue("planner");
            heuristic = cmd.getOptionValue("h");
            String optionValue = cmd.getOptionValue("tolerance");
            if (optionValue != null){
                System.out.println(optionValue);
                Utils.tolerance = Double.parseDouble(optionValue);
            }
            
            if (heuristic == null) {
                heuristic = "hadd";
            }
            searchEngineString = cmd.getOptionValue("s");
            if (searchEngineString == null) {
                searchEngineString = "gbfs";
            }
            tieBreaking = cmd.getOptionValue("ties");
            deltaPlanning = cmd.getOptionValue("dp");
            if (deltaPlanning == null) {
                deltaPlanning = "1.0";
            }
            optionValue = cmd.getOptionValue("red");
            if (optionValue == null) {
                redundantConstraints = "no";
            } else {
                redundantConstraints = optionValue;
            }
            optionValue = cmd.getOptionValue("gro");
            if (optionValue != null) {
                groundingType = optionValue;
            } else {
                groundingType = "internal";
            }
            
            internalValidation = cmd.hasOption("ival");

            deltaExecution = cmd.getOptionValue("de");
            if (deltaExecution == null) {
                deltaExecution = "1.0";
            }
            deltaHeuristic = cmd.getOptionValue("dh");
            if (deltaHeuristic == null) {
                deltaHeuristic = "1.0";
            }
            deltaValidation = cmd.getOptionValue("dv");
            if (deltaValidation == null) {
                deltaValidation = "1";
            }
            String temp = cmd.getOptionValue("dl");
            if (temp != null) {
                depthLimit = Float.parseFloat(temp);
            } else {
                depthLimit = Float.NaN;
            }

            String timeOutString = cmd.getOptionValue("timeout");
            if (timeOutString != null) {
                timeOut = Long.parseLong(timeOutString) * 1000;
            } else {
                timeOut = Long.MAX_VALUE;
            }

            String delta = cmd.getOptionValue("delta");
            if (delta != null) {
                deltaHeuristic = delta;
                deltaValidation = delta;
                deltaPlanning = delta;
                deltaExecution = delta;
            }
            
            inputPlan = cmd.getOptionValue("inputplan");
            inputPlan = cmd.getOptionValue("inputplan");

            String k = cmd.getOptionValue("k");
            if (k != null) {
                numSubdomains = Integer.parseInt(k);
            } else {
                numSubdomains = 2;
            }

            gw = cmd.getOptionValue("wg");
            hw = cmd.getOptionValue("wh");
            saving_json = cmd.hasOption("sjr");
            if (cmd.hasOption("silent")){
                out = new PrintStream(new OutputStream() {
                    @Override
                    public void write(int b) throws IOException {
                    }
                });
            }else{
                out = System.out;
            }

            sdac = cmd.hasOption("sdac");
            helpfulActionsPruning = cmd.getOptionValue("ha") != null && "true".equals(cmd.getOptionValue("ha"));
            printEvents = cmd.hasOption("pe");

            printTrace = cmd.hasOption("pt");
            savePlan = cmd.getOptionValue("sp");
            onlyPlan = cmd.hasOption("onlyplan");
            anyTime = cmd.hasOption("anytime");
            aibrPreprocessing = !cmd.hasOption("dap");
            stopAfterGrounding = cmd.hasOption("stopgro");
            helpfulTransitions = cmd.getOptionValue("ht") != null && "true".equals(cmd.getOptionValue("ht"));
            ignoreMetric = cmd.hasOption("im");
            printActions = cmd.hasOption("print_actions");
        } catch (ParseException exp) {
//            Logger.getLogger(ENHSP.class.getName()).log(Level.SEVERE, null, ex);
            System.err.println("Parsing failed.  Reason: " + exp.getMessage());
            HelpFormatter formatter = new HelpFormatter();
            formatter.printHelp("enhsp", options);
            System.exit(-1);
        }

    }

    /**
     * @return the problem
     */
    public PDDLProblem getProblem() {
        return problem;
    }

    public void printStats() {
//        System.out.println("Grounding and Simplification finished");
        System.out.println("|A|:" + getProblem().getActions().size());
        System.out.println("|P|:" + getProblem().getProcessesSet().size());
        System.out.println("|E|:" + getProblem().getEventsSet().size());
        if (pddlPlus) {
            System.out.println("Delta time heuristic model:" + deltaHeuristic);
            System.out.println("Delta time planning model:" + deltaPlanning);
            System.out.println("Delta time search-execution model:" + deltaExecution);
            System.out.println("Delta time validation model:" + deltaValidation);
        }
    }

    private void setPlanner() {
        helpfulTransitions = false;
        helpfulActionsPruning = false;
        tieBreaking = "arbitrary";
        switch (planner) {
            case "sat-hmrp":
                heuristic = "hmrp";
                searchEngineString = "gbfs";
                tieBreaking = "arbitrary";
                break;
            case "sat-hmrph":
                heuristic = "hmrp";
                helpfulActionsPruning = true;
                searchEngineString = "gbfs";
                tieBreaking = "arbitrary";
                break;
            case "sat-hmrphj":
                heuristic = "hmrp";
                helpfulActionsPruning = true;
                helpfulTransitions = true;
                searchEngineString = "gbfs";
                tieBreaking = "arbitrary";
                break;
            case "sat-hmrpff":
                heuristic = "hmrp";
                helpfulActionsPruning = false;
                redundantConstraints = "brute";
                helpfulTransitions = false;
                searchEngineString = "gbfs";
                tieBreaking = "arbitrary";
                break;
            case "sat-hadd":
                heuristic = "hadd";
                searchEngineString = "gbfs";
                tieBreaking = "smaller_g";
                break;
            case "sat-aibr":
                heuristic = "aibr";
                searchEngineString = "WAStar";
                tieBreaking = "arbitrary";
                break;
            case "sat-hradd":
                heuristic = "hradd";
                searchEngineString = "gbfs";
                tieBreaking = "smaller_g";
                break;
            case "opt-hmax":
                heuristic = "hmax";
                searchEngineString = "WAStar";
                tieBreaking = "larger_g";
                break;
            case "opt-hlm":
                heuristic = "hlm-lp";
                searchEngineString = "WAStar";
                tieBreaking = "larger_g";
                break;
            case "opt-hlmrd":
                heuristic = "hlm-lp";
                redundantConstraints = "brute";
                searchEngineString = "WAStar";
                tieBreaking = "larger_g";
                break;
            case "opt-hrmax":
                heuristic = "hrmax";
                searchEngineString = "WAStar";
                tieBreaking = "larger_g";
                break;
            case "opt-blind":
                heuristic = "blind";
                searchEngineString = "WAStar";
                tieBreaking = "larger_g";
                aibrPreprocessing = false;
                break;
            default:
                System.out.println("! ====== ! Warning: Unknown planner configuration. Going with default: gbfs with hadd ! ====== !");
                heuristic = "hadd";
                searchEngineString = "gbfs";
                tieBreaking = "smaller_g";
                break;
        }

    }

    private void setHeuristic() {
//        System.out.println("ha:" + helpfulActionsPruning + " ht" + helpfulTransitions);
        h = PDDLHeuristic.getHeuristic(heuristic, heuristicProblem, redundantConstraints, helpfulActionsPruning, helpfulTransitions);
    }

   

    private LinkedList<Pair<BigDecimal, Object>> search() throws Exception {

        LinkedList<Pair<BigDecimal, Object>> rawPlan = null;//raw list of actions returned by the search strategies

        final PDDLSearchEngine searchEngine = new PDDLSearchEngine(out,problem, h); //manager of the search strategies
        Runtime.getRuntime().addShutdownHook(new Thread() {//this is to save json also when the planner is interrupted
            @Override
            public void run() {
                if (saving_json) {
                    searchEngine.searchSpaceHandle.print_json(getProblem().getPddlFileReference() + ".sp_log");
                }
            }
        });

        searchEngine.saveSearchTreeAsJson = saving_json;

        if (tieBreaking != null) {
            switch (tieBreaking) {
                case "smaller_g":
                    searchEngine.tbRule = SearchEngine.TieBreaking.LOWERG;
                    break;
                case "larger_g":
                    searchEngine.tbRule = SearchEngine.TieBreaking.HIGHERG;
                    break;
                default:
                    System.out.println("Wrong setting for break-ties. Arbitrary tie breaking");
                    break;
            }
        } else {//the following is the arbitrary setting
            tieBreaking = "arbitrary";
            searchEngine.tbRule = SearchEngine.TieBreaking.ARBITRARY;

        }

        if (hw != null) {
            searchEngine.setWH(Float.parseFloat(hw));
            System.out.println("w_h set to be " + hw);
        } else {
            searchEngine.setWH(1);
        }


        if (depthLimit != Float.NaN) {
            searchEngine.depthLimit = depthLimit;
            System.out.println("Setting horizon to:" + depthLimit);
        } else {
            searchEngine.depthLimit = Float.POSITIVE_INFINITY;
        }
        
        if (helpfulActionsPruning)
            System.out.println("Helpful Action Pruning Activated");
        
        if (inputPlan == null){
        searchEngine.helpfulActionsPruning = helpfulActionsPruning;
        if ("WAStar".equals(searchEngineString)) {
            System.out.println("Running WA-STAR");
            rawPlan = searchEngine.WAStar(getProblem(), timeOut);
        } else if ("wa_star_4".equals(searchEngineString)) {
            System.out.println("Running greedy WA-STAR with hw = 4");
            searchEngine.setWH(4);
            rawPlan = searchEngine.WAStar();
        } else if ("gbfs".equals(searchEngineString)) {
            System.out.println("Running Greedy Best First Search");
            rawPlan = searchEngine.gbfs(getProblem(), timeOut);
        } else if ("gbfs_ha".equals(searchEngineString)) {
            System.out.println("Running Greedy Best First Search with Helpful Actions");
            rawPlan = searchEngine.gbfs(getProblem(), timeOut);
        } else if ("ida".equals(searchEngineString)) {
            System.out.println("Running IDAStar");
            rawPlan = searchEngine.idastar(getProblem(), true);
        } else if ("ucs".equals(searchEngineString)) {
            System.out.println("Running Pure Uniform Cost Search");
            rawPlan = searchEngine.UCS(getProblem());
        } else if ("brfs".equals(searchEngineString)) {
            System.out.println("Running Pure Breath First Search");
            rawPlan = searchEngine.breathFirstSearch(getProblem());
        } else if ("ehc".equals(searchEngineString)) {
            System.out.println("Running Enforced Hill Climbing");
            rawPlan = searchEngine.enforceHillClimbing(getProblem());
        } else if ("dfsbnb".equals(searchEngineString)) {
            System.out.println("Running dfsbnb");
            rawPlan = searchEngine.dfsbnb(getProblem(),true);
        }else {
            throw new RuntimeException("Search strategy is not correct");
        }
        endGValue = searchEngine.currentG;
        }
        overallPlanningTime = (System.currentTimeMillis() - overallStart);

        boolean valid = true;
        if (printTrace) {
            String fileName = getProblem().getPddlFileReference() + "_search_" + searchEngineString + "_h_" + heuristic + "_break_ties_" + tieBreaking + ".npt";
            valid = problem.validate(rawPlan,new BigDecimal(this.deltaExecution), new BigDecimal(deltaExecution), fileName);
            System.out.println("Numeric Plan Trace saved to " + fileName);
        } else if (internalValidation) {
            Pair<PDDLDomain, PDDLProblem> res = parseDomainProblem(domainFile, problemFile, deltaValidation, new PrintStream(new OutputStream() {
                    public void write(int b) {}}));
            PDDLSearchEngine validator = new PDDLSearchEngine(res.getRight(), h);
            
            if (inputPlan == null)
                valid = res.getRight().validate(rawPlan,new BigDecimal(this.deltaExecution), new BigDecimal(deltaValidation),"/tmp/temp_trace.pddl");
            else{
                List<PDDLState> simulate = res.getRight().simulate(getPlan(problem, inputPlan), deltaValidation, (PDDLState) problem.getInit(), problem, true);
                valid = simulate.get(simulate.size()-1).satisfy(problem.getGoals());
                for (var v: simulate){
                    System.out.println(v);
                }
            }
            if (valid) {
                System.out.println("Plan is valid");
            }else{
                System.out.println("Plan is not valid");
            }
        }
        printInfo(rawPlan, searchEngine);
        return rawPlan;
    }

//    private SimplePlan validate(PDDLSearchEngine searchEngine, LinkedList raw_plan) throws CloneNotSupportedException, Exception {
//        SimplePlan sp = new SimplePlan(domain, getProblem(), false, pddlPlus);  //placeholder for the plan to be found
//        PDDLState lastState = null;
//        System.out.println("Starting Validation");
//        if (raw_plan != null) {// Print some useful information on the outcome of the planning process
//            sp.print_trace = print_trace;
//            if (!pddlPlus) {
//                sp.addAll(raw_plan);
//                lastState = sp.execute((PDDLState) getProblem().getInit(), getProblem().globalConstraints);
//                System.out.println("(Pddl2.1 semantics) Plan is valid:" + lastState.satisfy(getProblem().getGoals()));
//            } else { //This is when you have also autonomous processes going on
//                PDDLDomain validationDomain = new PDDLDomain(domainFile);
//                PDDLProblem validationProblem = new PDDLProblem(problemFile, validationDomain.getConstants(), validationDomain.getTypes(),validationDomain);
//                //this is when you have processes
//                validationProblem.groundingActionProcessesConstraints();
////                validationProblem.syncAllVariablesAndUpdateCollections(getProblem());
//                validationProblem.setDeltaTimeVariable(delta_val);
//                validationProblem.simplifyAndSetupInit(true);
//                Float time = sp.build_pddl_plus_plan(raw_plan, epsilon);
//                lastState = sp.execute((PDDLState) validationProblem.getInit(), validationProblem.globalConstraints, validationProblem.getProcessesSet(), validationProblem.getEventsSet(), searchEngine.planningDelta, Float.parseFloat(delta_val), time);
////                System.out.println("Last PDDLState:"+last_state.pddlPrint());
//                boolean goal_reached = lastState.satisfy(getProblem().getGoals());
//                System.out.println("(Pddl+ semantics) Plan is valid:" + goal_reached);
//            }
//        }else{
//            return null;
//        }
//        if (lastState != null) {
//            if (!pddlPlus) {
//                sp.setDuration(sp.size());
//            } else {
//                sp.setDuration(lastState.time);//                System.out.println("Duration Via Simulation:"+String.format("%.7f",last_state.getTime().getNumber()));
//            }
//        }
//        return sp;
//    }
    private void printInfo(LinkedList<Pair<BigDecimal, Object>> sp, PDDLSearchEngine searchEngine) throws CloneNotSupportedException {

        PDDLState s = (PDDLState) searchEngine.getLastState();
        if (pddlPlus && sp != null){
        }
        if (sp != null) {
            System.out.println("Problem Solved\n");
            System.out.println("Found Plan:");
            printPlan(sp, pddlPlus, s,savePlan);
            System.out.println("\nPlan-Length:" + sp.size());
            planLength = sp.size();
        } else {
            System.out.println("Problem unsolvable");
        }
        if (pddlPlus && sp != null) {
            System.out.println("Elapsed Time: " + s.time);
        }
        System.out.println("Metric (Search):" + searchEngine.currentG);
        System.out.println("Planning Time (msec): " + overallPlanningTime);
        System.out.println("Heuristic Time (msec): " + searchEngine.getHeuristicCpuTime());
        System.out.println("Search Time (msec): " + searchEngine.getOverallSearchTime());
        System.out.println("Expanded Nodes:" + searchEngine.getNodesExpanded());
        System.out.println("States Evaluated:" + searchEngine.getNumberOfEvaluatedStates());
        System.out.println("Fixed constraint violations during search (zero-crossing):" + searchEngine.constraintsViolations);
        System.out.println("Number of Dead-Ends detected:" + searchEngine.deadEndsDetected);
        System.out.println("Number of Duplicates detected:" + searchEngine.duplicatesNumber);
//        if (searchEngine.getHeuristic() instanceof quasi_hm) {
//            System.out.println("Number of LP invocations:" + ((quasi_hm) searchEngine.getHeuristic()).n_lp_invocations);
//        }
        if (saving_json) {
            searchEngine.searchSpaceHandle.print_json(getProblem().getPddlFileReference() + ".sp_log");
        }
    }

    private void printPlan(LinkedList<Pair<BigDecimal, Object>> plan, boolean temporal, PDDLState par, String fileName) {
        float i = 0f;
        Pair<BigDecimal, Object> previous = null;
        List<String> fileContent = new ArrayList();
        boolean startProcess = false;
        int size = plan.size();
        int  j = 0;
        for (Pair<BigDecimal, Object> ele : plan) {
            j++;
            if (!temporal) {
                System.out.print(i + ": " + ele.getRight() + "\n");
                if (fileName != null){
                    TransitionGround t = (TransitionGround) ele.getRight();
                    fileContent.add(t.toString());
                }
                i++;
            } else {
                TransitionGround t = (TransitionGround) ele.getRight();
                if (t.getSemantics() == TransitionGround.Semantics.PROCESS) {
                    if (!startProcess) {
                        previous = ele;
                        startProcess = true;
                    }
                    if (j == size) {
                        if (!onlyPlan){
                            System.out.println(previous.getLeft() + ": -----waiting---- " + "[" + par.time + "]");
                        }
                    }
                } else {
                    if (t.getSemantics() != TransitionGround.Semantics.EVENT || printEvents) {
                        if (startProcess) {
                            startProcess = false;
                            if (!onlyPlan){
                                System.out.println(previous.getLeft() + ": -----waiting---- " + "[" + ele.getLeft() + "]");
                            }
                        }
                        System.out.print(ele.getLeft() + ": " + ele.getRight() + "\n");
                        if (fileName != null) {
                            fileContent.add(ele.getLeft() + ": "+ t.toString());
                        }
                    } else {
                        if (j == size) {
                            if (!onlyPlan){
                                System.out.println(previous.getLeft() + ": -----waiting---- " + "[" + ele.getLeft() + "]");
                            }
                        }
                    }
                }
            }
        }
        
        if (fileName != null) {
            try {
                if (temporal){
                    fileContent.add(par.time+": @PlanEND ");
                }
                Files.write(Path.of(fileName), fileContent);
                
            } catch (IOException ex) {
                Logger.getLogger(ENHSP.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
    private static LinkedList<Pair<BigDecimal,TransitionGround>> getPlan(PDDLProblem problem, String plan) throws IOException {
        Path path = Paths.get(plan);
        final LinkedList<Pair<BigDecimal,TransitionGround>> pddlPlan = new LinkedList();
            final List<String> readAllLines = Files.readAllLines(path,StandardCharsets.UTF_8);
            for (var v: readAllLines){
                String actionName = v.split(":")[1];
                actionName = actionName.trim();
                final BigDecimal time = new BigDecimal(v.split(":")[0]);
                TransitionGround pddlAction = problem.getActionsByName(actionName);
                if (pddlAction == null && !actionName.equals("@PlanEND")){
                    throw new RuntimeException("Action "+actionName+" is either not present in the domain or not applicable at time "+time);
                }
//                if (!actionName.equals("@PlanEND")){
                    pddlPlan.add(Pair.of(time,pddlAction));
//                }
            }
        return pddlPlan;
    }
}
