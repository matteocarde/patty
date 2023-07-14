/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package runner;

import SMTPlanning.smt_encoder_decoder;
import antlr.RecognitionException;
import domain.PddlDomain;
import extraUtils.Utils;
import java.io.IOException;
//import org.antlr.runtime.RecognitionException;
import plan.SimplePlan;
import problem.EPddlProblem;
import problem.State;

/**
 *
 * @author enrico
 */
public class SMTHybridPlanner {

    private static String domainFile;
    private static String problemFile;
    private static String maxPlanLength;
    private static String minPlanLength;
    private static String stepSemantic;
    private static String sec_theory;
    private static boolean repetition_encoding;
    private static String encoding;
    private static String max_number_of_repetition;
    private static boolean must_keep_smt_file;

    /**
     * @param args the command line arguments
     */
    /**
     *
     * @param args the command line arguments
     */
    public static void parseInput(String[] args) {
        String usage = "usage:\n executable-name(java -jar...) "
                + "\n-o domain -f problem "
                + "\n-kMin min-plan-length (optional, default 0)"
                + "\n-kMax maxn-plan-length (optional, default 1000)"
                +"\n-s semantics used. From 0 to 3 with the following meaning:"
                + "\n      0: sequential semantics. Can be used for unit cost optimal planning but is slow"
                + "\n      1: sequential semantics plus rolling-up"
                + "\n      2: for each semantics"
                + "\n      3: for each semantics plus rolling-up (this is the fastest one)"
                + "\n-save_smt to keep the *last* smt file encoding the formula, i.e., smt_encoding_<problem_instance_name>";
//                + "\n-sem semantic (optional, default 1-step sequential semantic) [select 1 for sequential and n for parallel semantic]";
        if (args.length < 4) {
            System.err.println("Number of parameters is low (" + args.length + ")");
            System.err.println(usage);
            System.exit(-1);
        } else {
            domainFile = searchParameterValue(args, "-o");
            problemFile = searchParameterValue(args, "-f");
            minPlanLength = searchParameterValue(args, "-kMin");
            maxPlanLength = searchParameterValue(args, "-kMax");
            stepSemantic = searchParameterValue(args, "-sem");
            sec_theory = Utils.searchParameterValue(args, "-T");
            encoding = Utils.searchParameterValue(args, "-s");
            must_keep_smt_file =  Utils.searchParameter(args, "-save_smt");
            max_number_of_repetition = Utils.searchParameterValue(args, "-mr");

            if (minPlanLength == null) {
                minPlanLength = "0";
            }
            if (maxPlanLength == null) {
                maxPlanLength = "1000";
            }
            if (sec_theory == null) {
                sec_theory = "Real";
            }
            if (encoding == null) {
                encoding = "3";
            }
            if (domainFile == null || problemFile == null) {
                System.err.println(usage);
                System.exit(-1);
            }

        }
    }

    public static void main(String[] args) throws RecognitionException, IOException, antlr.RecognitionException, CloneNotSupportedException, Exception {
        //Controlling the input files

        parseInput(args);
        PddlDomain domain = new PddlDomain(domainFile);
        //domain.prettyPrint();
        EPddlProblem problem = new EPddlProblem(problemFile, domain.getConstants());

        domain.validate(problem);
        System.out.println("Domain and Problem Parsed");

        State InitCopy = problem.getInit().clone();

        smt_encoder_decoder smtplanner = new smt_encoder_decoder(domain, problem);
        smtplanner.must_remove_file_temp = !must_keep_smt_file;
        smtplanner.setSemantic(stepSemantic);
        smtplanner.setSec_theory(sec_theory);
        smtplanner.set_repetition_encoding(repetition_encoding);
        if (max_number_of_repetition != null) {
            smtplanner.max_number_of_repetition = Integer.parseInt(max_number_of_repetition);
        }
        // the following override the previous setting
        //4 possible option
        //0 : sem 1, 1: sem 1 -r, 2: sem N, 3: sem N -r
        parse_search_strategy(smtplanner, encoding);
        SimplePlan sp = null;

        smtplanner.search_strategy = encoding;

            if (!smtplanner.init()){
                System.out.println("Problem Unsolvable");
                return;
            }
            sp = smtplanner.solve(Integer.parseInt(minPlanLength), Integer.parseInt(maxPlanLength));
            smtplanner.printOutcome();

        if (sp != null) {
            System.out.println("Plan size: " + sp.size());
            System.out.println("Cost: " + sp.getValueObjectiveFunction(problem));
            System.out.println("Plan: " + sp);
            System.out.println("Number of different actions used:" + smtplanner.actionsFound.size());
            State end = sp.execute(InitCopy, problem.globalConstraints);
            System.out.println("(just for the pddl2.1 semantic ) Plan is valid:" + end.satisfy(problem.getGoals()));
            sp.savePlan(problem.getPddlFilRef()+".plan");
            System.out.println("Plan stored in file "+problem.getPddlFilRef()+".plan");
        }

    }

    private static String searchParameterValue(String[] args, String par) {

        for (int i = 0; i < args.length - 1; i++) {
            if (args[i].equals(par)) {
                return args[++i];
            }
        }
        return null;
    }

    private static void parse_search_strategy(smt_encoder_decoder smtplanner, String search_strategy) {

        if (search_strategy == null) {
            return;
        }
        if (search_strategy.equals("0")) {
            smtplanner.setSemantic("1");
            smtplanner.set_repetition_encoding(false);
        } else if (search_strategy.equals("1")) {
            smtplanner.setSemantic("1");
            smtplanner.set_repetition_encoding(true);
        } else if (search_strategy.equals("2")) {
            smtplanner.setSemantic("N");
            smtplanner.set_repetition_encoding(false);
        } else if (search_strategy.equals("3")) {
            smtplanner.setSemantic("N");
            smtplanner.set_repetition_encoding(true);
        }

        System.out.println("Configuration selected is: SEM:" + smtplanner.getSemantic() + " Repetition:" + smtplanner.isRepetition_encoding());

    }

}
