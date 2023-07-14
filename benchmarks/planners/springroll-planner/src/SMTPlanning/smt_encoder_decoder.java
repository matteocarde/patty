/**
 * *******************************************************************
 *
 * This program is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation; either version 2 of the License, or (at your option) any later
 * version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc., 59 Temple
 * Place - Suite 330, Boston, MA 02111-1307, USA.
 *
 ********************************************************************
 */
/**
 * *******************************************************************
 * Description: SpringRoller Planner.
 *
 * Author: Enrico Scala 2016 Contact: enricos83@gmail.com
 *
 ********************************************************************
 */
package SMTPlanning;

import conditions.AndCond;
import conditions.Comparison;
import conditions.Conditions;
import conditions.NotCond;
import conditions.NumFluentAssigner;
import conditions.OrCond;
import conditions.PDDLObjectsEquality;
import conditions.Predicate;
import domain.PddlDomain;
import expressions.NumEffect;
import expressions.NumFluent;
import extraUtils.Utils;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Objects;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.jgrapht.experimental.dag.DirectedAcyclicGraph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.traverse.TopologicalOrderIterator;
import plan.SimplePlan;
import problem.GlobalConstraint;
import problem.GroundAction;
import problem.EPddlProblem;
import problem.RelState;
import heuristics.Aibr;

/**
 *
 * @author enrico
 */
public class smt_encoder_decoder {

    private boolean repetition_encoding = false;
    private boolean not_homogenous = false;
    private PddlDomain domain;
    private EPddlProblem problem;
    private ArrayList smt2String;
    HashSet SC;
    //private RelState possibleState;
    Collection<Predicate> reacheable_predicates = null;
    private LinkedHashSet<GroundAction> actions;
    private HashMap<Predicate, HashSet> predDeleters;
    private HashMap<Predicate, HashSet> predAchievers;
    public SimplePlan extractedPlan;
    private String semantic;
    private HashMap<NumFluent, HashSet> numModifiers;
    private Set interferences;
    private long overallTime;
    private long overallEcondingTime;
    boolean sat;

    private HashMap<GroundAction, Boolean> num_rel_actions;

    private int debugInfo;

    private boolean implicit_goal;
    private String name_file_temp;
    private HashSet<NumFluent> contVars;

    private String sec_theory;
    public boolean must_remove_file_temp = true;
    private Set<NumFluent> numeric_variables;
    private HashMap<String, Integer> repetitions;
    public HashSet actionsFound;
    public int last_horizon;
    public int max_number_of_repetition = -1;
    public String search_strategy;
    private HashMap<GroundAction, Boolean> eligible;
    private boolean z3solver = true;
    private HashMap<NumFluent,Boolean> derived_fluents;

    public smt_encoder_decoder(PddlDomain dm, EPddlProblem p) {
        super();
        this.domain = dm;
        this.problem = p;
        extractedPlan = null;
        semantic = "1";
        overallTime = 0;
        overallEcondingTime = 0;
        sat = false;
        debugInfo = 0;
        implicit_goal = false;
        repetitions = new HashMap();
        last_horizon = 0;
    }


    public SimplePlan solve(int minI, int maxI) throws Exception {
        SimplePlan sp = null;

        //implicit goal captures free variables in the goal
        if (isImplicit_goal() || (this.getProblem().getInit().getNumericFluents() != null)) {
            int i = Math.max(0, minI);

            while (i <= maxI) {//until a given horizon is reached. This ensures termination
                if (sat(i)) {
                    this.last_horizon = i;
                    sp = this.extractedPlan;
                    break;
                } else {
                    i = i + 1;
                }
            }
            if (i > maxI) {
                if (this.debugInfo > 0) {
                    System.out.println("Goal not reacheable in " + maxI + " steps");
                }
            }
        } else {
            System.out.println("Goal not reacheable (Graphplan Analysis)");
        }

        return sp;
    }

    public boolean init() throws Exception {

        grounding();
        

        setActions(new LinkedHashSet(problem.getActions()));

        if (!compute_relevance_analysis(problem.getActions())) {
            return false;
        }
        //Build action interferences
        compute_action_interferencies();
        return true;
    }

    public ArrayList<String> encode(int k) throws Exception {

        //the smt2string encodes a list of strings to be provided as a SMTLIB a file. That file can be used by any SMT solver to detect if there is a solution
        //of length k
        smt2String = new ArrayList();
        smt2String.add("\n(set-option :produce-models true)\n");
        long start = System.currentTimeMillis();
        smt2String.add("; Discrete Variables\n");
        smt2String.addAll(build_prop_variables_plus_init_state_axiom(k));

        smt2String.add("; Continuous Variables\n");
        smt2String.addAll(build_numeric_variables_plus_init_global_axiom(k));

        smt2String.add("; Goal\n");
        smt2String.add("(assert " + this.problem.getGoals().toSmtVariableString(k) + ")\n");
        smt2String.add(";Time for Propositions: " + (System.currentTimeMillis() - start));

        start = System.currentTimeMillis();
        smt2String.add(";Number of Actions" + getActions().size());

        smt2String.add("; Actions Variable plus Preconditions and Effects\n");
        smt2String.addAll(build_action_variables(k));
        smt2String.add(";Time for Actions: " + (System.currentTimeMillis() - start));

        smt2String.add("; Frame Axiom\n");
        smt2String.addAll(build_frame_axiom(k));

        if (this.isRepetition_encoding()) {
            smt2String.add("\n(check-sat-using  (then simplify solve-eqs (or-else smt qfnra-nlsat  )))\n(get-model)");
        } else {
            smt2String.add("\n(check-sat)\n(get-info :all-statistics)\n(get-model)");
        }
        return smt2String;
    }

    /**
     * @return the domain
     */
    public PddlDomain getDomain() {
        return domain;
    }

    /**
     * @param domain the domain to set
     */
    public void setDomain(PddlDomain domain) {
        this.domain = domain;
    }

    /**
     * @return the problem
     */
    public EPddlProblem getProblem() {
        return problem;
    }

    /**
     * @param problem the problem to set
     */
    public void setProblem(EPddlProblem problem) {
        this.problem = problem;
    }

    //return interferences according to for each semantics
    private HashSet for_each_semantics_mutexes(Set actions) {
        HashSet ret = new HashSet();
        for (Object o : actions) {
            for (Object o1 : actions) {
                if (!o.equals(o1)) {
                    GroundAction a = (GroundAction) o;
                    GroundAction b = (GroundAction) o1;
                    if (for_each_semantic_interferences(a, b) || interference(a, b, SC)) {
                        GroundAction[] temp = new GroundAction[2];
                        temp[0] = a;
                        temp[1] = b;
                        ret.add(temp);
                    }
                }
            }
        }
        return ret;
    }
    //1-step semantics mutexes
    private HashSet one_step_semantics_mutexes(Set actions) {
        HashSet ret = new HashSet();
        for (Object o : actions) {
            for (Object o1 : actions) {
                if (!o.equals(o1)) {
                    GroundAction a = (GroundAction) o;
                    GroundAction b = (GroundAction) o1;
                    GroundAction[] temp = new GroundAction[2];
                    temp[0] = a;
                    temp[1] = b;
                    ret.add(temp);
                }
            }
        }
        return ret;
    }

    //interferences_for_foreach_semantics
    private boolean for_each_semantic_interferences(GroundAction a, GroundAction b) {


        //remove an action that threats the precondition of the other
        if (a.threat((AndCond) b.getPreconditions()) || (b.threat((AndCond) a.getPreconditions()))) {
            return true;
        }

        Set intersection;
        if (a.getPreconditions() != null && b.getNumericFluentAffected() != null) {
            if (a.getPreconditions().getInvolvedFluents() != null) {
                intersection = new HashSet(a.getPreconditions().getInvolvedFluents());
                intersection.retainAll(b.getNumericFluentAffected().keySet());
                if (intersection.size() > 0) {
                    return true;
                }
            }
        }
        if (b.getPreconditions() != null && a.getNumericFluentAffected() != null && b.getPreconditions().getInvolvedFluents() != null) {
            intersection = new HashSet(b.getPreconditions().getInvolvedFluents());
            intersection.retainAll(a.getNumericFluentAffected().keySet());
            if (intersection.size() > 0) {
                return true;
            }
        }


        if (a.getNumericFluentAffected() != null && b.getNumericFluentAffected() != null) {

            for (NumEffect ef1 : a.getNumericEffectsAsCollection()) {
                for (NumEffect ef2 : b.getNumericEffectsAsCollection()) {
                    if (ef2.getRight().involve(ef1.getFluentAffected()) || (ef1.getRight().involve(ef2.getFluentAffected()))) {
                        return true;
                    }
                }
            }

        }

        return false;
    }

   
    private String predicateModifiers(Predicate p, HashMap<Predicate, HashSet> predAchievers, int i) {
        HashSet achievers = predAchievers.get(p);
        String ret = "(or";
        for (Object o : achievers) {
            GroundAction gr = (GroundAction) o;

                ret += " (> " + gr.toSmtVariableString(i) + " 0)";
        }
        ret += ")";
        if (ret.equals("(or)")) {
            return "false";
        }

        return ret;
    }

    private String compute_numeric_modifiers(NumFluent nf, HashMap<NumFluent, HashSet> numAchievers, int i) {
        HashSet achievers = numAchievers.get(nf);
        if (achievers == null) {
            return "false";
        }
        String ret = "(or";
        for (Object o : achievers) {
            GroundAction gr = (GroundAction) o;
                ret += " (> " + gr.toSmtVariableString(i) + " 0)";

        }
        ret += ")";
        if (ret.equals("(or)")) {
            return "false";
        }

        return ret;
    }


    private String pddlActionString(String line) {

        line = line.substring(line.lastIndexOf("ACTION") + 6, line.indexOf(" ()"));

        String[] ret = line.split("@");

        String parameters = "";
        for (int i = 1; i < ret.length - 1; i++) {
            parameters += " " + ret[i];
        }

        //System.out.println(ret[ret.length - 1].split("-")[1] + ": (" + ret[0] + parameters + ")");
        return ret[ret.length - 1].split("-")[1] + ": (" + ret[0] + parameters + ")";
    }

    /**
     * @return the semantic
     */
    public String getSemantic() {
        return semantic;
    }

    /**
     * @param semantic the semantic to set
     */
    public void setSemantic(String semantic) {
        this.semantic = semantic;
    }

    private void setEdgesViaOrders(DirectedAcyclicGraph po) {

        for (Object o : po.vertexSet()) {
            for (Object o1 : po.vertexSet()) {
                if (!o.equals(o1)) {
                    String a = (String) o;
                    String b = (String) o1;
                    if (Integer.parseInt(a.split(":")[0]) < Integer.parseInt(b.split(":")[0])) {
                        po.addEdge(a, b);
                    }
                }
            }
        }

    }

    public boolean writeSmt2File(ArrayList<String> smtString, int index) {
        long start = System.currentTimeMillis();

        try {
            name_file_temp = "smt_encoding_" + this.problem.getPddlFilRef().replace("/", "").replace(".pddl", "") + "-" + String.valueOf(index) + ".smt";
            BufferedWriter w = new BufferedWriter(new FileWriter(name_file_temp));
            for (int k = 0; k < smtString.size(); k++) {
                w.write(smtString.get(k).replaceAll("(\\d*?),(\\d\\d)", "$1.$2"), 0, smtString.get(k).length());
            }
            w.close();
        } catch (IOException ex) {
            System.err.println("What the hell!" + ex);
            return false;
        }
        this.overallTime += (System.currentTimeMillis() - start);
        return true;
    }

    public void printOutcome() {
        if (this.sat) {
            System.out.println("Solved: True");
        } else {
            System.out.println("Solved: False");
        }
        System.out.println("Encoding time: " + this.overallEcondingTime);
        System.out.println("Planning time: " + this.overallTime);
        System.out.println("Plan Steps: " + this.last_horizon);

    }

    /**
     * @return the implicit_goal
     */
    public boolean isImplicit_goal() {
        return implicit_goal;
    }

    /**
     * @param implicit_goal the implicit_goal to set
     */
    public void setImplicit_goal(boolean implicit_goal) {
        this.implicit_goal = implicit_goal;
    }


    /**
     * @return the sec_theory
     */
    public String getSec_theory() {
        return sec_theory;
    }

    /**
     * @param sec_theory the sec_theory to set
     */
    public void setSec_theory(String sec_theory) {
        this.sec_theory = sec_theory;
    }

    private String add_constraint_for_repetition(GroundAction gr, int i) throws CloneNotSupportedException {
        String ret = "(and ";
        String var = "(- " + gr.toSmtVariableString(i) + " 1)";

        if (gr.getPreconditions() != null) {
            for (Conditions c : (Collection<Conditions>) gr.getPreconditions().sons) {
                ret += " " + c.toSmtVariableString(i, gr, var) + " ";
            }
        }
        for (Object o : SC) {
            if (o instanceof GlobalConstraint) {
                GlobalConstraint gc = (GlobalConstraint) o;
                Conditions temp = generate_m_times_regressed_conditions(gc.condition, gr);
                ret += " " + temp.toSmtVariableString(i) + " ";
                //TO-DO This following should be better clearer and homogenous with previous encodings; for some reason doesn't work/ Needs to be checked thouroughly
                //ret += generate_string_m_times_regressed_conditions(gc.condition, gr, i);
            }
        }

        return ret += " true)";

    }

    public String generate_string_m_times_regressed_conditions(Conditions c, GroundAction gr, int i) {
        String var = gr.toSmtVariableString(i);
        if (c instanceof OrCond) {
            String middle = "";
            for (Conditions c1 : (Collection<Conditions>) c.sons) {
                if (c1 instanceof Predicate) {
                    continue;
                }
                if (c1 instanceof NotCond) {
                    NotCond nc = (NotCond) c1;
                    
                    if (nc.son != null && !nc.son.isEmpty()) {
                        Object next = nc.son.iterator().next();
                        if (next instanceof Comparison) {
                            throw new UnsupportedOperationException("For action repetition, numeric global constraint have to be represented in positive CNF:"+c1);
                        }else{
                            continue;
                        }
                    }
                }
                if (c1 instanceof Comparison) {
                    Comparison comp = (Comparison) c1;
                    if (comp.involve(gr.getNumericFluentAffected()))
                        middle += "(and " + comp.toSmtVariableString(i) + " " + comp.toSmtVariableString(i, gr, var) + " )";
                } else if (c1 instanceof AndCond) {
                    throw new UnsupportedOperationException("For action repetition, numeric global constraint have to be represented in positive CNF:"+c1);
                }
            }
            if ("".equals(middle)) {
                return "";
            }
            return "(or " + middle + " )";
        } else if (c instanceof AndCond) {
            String middle = "";
            for (Conditions c1 : (Collection<Conditions>) c.sons) {
                if (c1 instanceof Predicate) {
                    continue;
                }
                if (c1 instanceof NotCond) {
                    NotCond nc = (NotCond) c1;
                    if (nc.son != null && !nc.son.isEmpty()) {
                        if (!(nc.son.iterator().next() instanceof Predicate)) {
                            throw new UnsupportedOperationException("For action repetition, numeric global constraint have to be represented in positive CNF:"+c1);
                        }
                    }
                }
                if (c1 instanceof Comparison) {
                    Comparison comp = (Comparison) c1;
                    if (comp.involve(gr.getNumericFluentAffected()))
                        middle += "(and " + comp.toSmtVariableString(i) + " " + comp.toSmtVariableString(i, gr, var) + " )";
                } else {
                    System.out.println(c1.getClass());
                    throw new UnsupportedOperationException("For action repetition, numeric global constraint have to be represented in positive CNF:"+c1);
                }

            }
            if ("".equals(middle)) {
                return "";
            }
            return "(and " + middle + " )";
        } else if (c instanceof Comparison) {
            Comparison comp = (Comparison) c;
            if (comp.involve(gr.getNumericFluentAffected()))

                return "(and " + comp.toSmtVariableString(i) + " " + comp.toSmtVariableString(i, gr, var) + " )";
            else
                return "";
        } else if (c instanceof Predicate) {
        } else if (c instanceof NotCond) {
            NotCond nc = (NotCond) c;
            if (nc.son != null && !nc.son.isEmpty()) {
                if (!(nc.son.iterator().next() instanceof Predicate)) {
                    throw new UnsupportedOperationException("For action repetition, numeric global constraint have to be represented in positive CNF:"+c);
                }
            }
        } else {
            throw new UnsupportedOperationException("Numeric global Constraint have to be represented in positive CNF:"+c);
        }
        return null;

    }


    private String add_prop_constraint_for_repetition(GroundAction gr, int i) {
        String var = gr.toSmtVariableString(i);
        AndCond and = new AndCond();

        boolean atLeast_one = false;
        if (gr.getPreconditions() != null) {
            for (Conditions c : (Collection<Conditions>) gr.getPreconditions().sons) {
                if (c instanceof Predicate) {
                    and.addConditions(c);
                    atLeast_one = true;
                }
            }
        }
        if (gr.getAddList() != null) {
            for (Conditions c : (Collection<Conditions>) gr.getAddList().sons) {
                if (c instanceof Predicate) {
                    //and.addConditions(c);
                    atLeast_one = true;
                }
            }
        }
        if (gr.getDelList() != null) {
            for (Conditions c : (Collection<Conditions>) gr.getDelList().sons) {
                if (c instanceof NotCond) {
                    and.addConditions(c);
                    atLeast_one = true;
                }
            }
        }

        if (!atLeast_one || and.sons.isEmpty()) {
//            System.out.println("return null");
            return null;
        }

//        return or.to_smtlib_with_repetition(i);
        return "(=> (>= " + var + " 2) " + and.toSmtVariableString(i) + " )";
    }

    /**
     * @return the repetition_encoding
     */
    public boolean isRepetition_encoding() {
        return repetition_encoding;
    }

    /**
     * @param repetition_encoding the repetition_encoding to set
     */
    public void set_repetition_encoding(boolean repetition_encoding) {
        this.repetition_encoding = repetition_encoding;
    }



    private void init_ach_mod() {
        predAchievers = new HashMap();
        predDeleters = new HashMap();
        numModifiers = new HashMap();

        for (Object o : reacheable_predicates) {

            HashSet achievers = new HashSet();
            HashSet deleters = new HashSet();
            for (Object o1 : getActions()) {
                GroundAction gr = (GroundAction) o1;

                if (gr.achieve((Predicate) o)) {
                    achievers.add(gr);
                }
                if (gr.delete((Predicate) o)) {
                    deleters.add(gr);
                }

            }
            predAchievers.put((Predicate) o, achievers);
            predDeleters.put((Predicate) o, deleters);
        }
        for (Object o : getProblem().getInit().getNumericFluents()) {
            NumFluentAssigner temp = (NumFluentAssigner) o;
            NumFluent nf = temp.getNFluent();
            HashSet modifiers = new HashSet();
            for (Object o1 : getActions()) {
                GroundAction gr = (GroundAction) o1;
                if (gr.getNumericFluentAffected().get(nf) != null) {
                    modifiers.add(gr);
                }
                numModifiers.put(nf, modifiers);
            }
        }

    }

    private Collection build_prop_variables_plus_init_state_axiom(int k) {
        ArrayList<String> ret = new ArrayList();
        for (int i = 0; i <= k; i++) {
            for (Object o : reacheable_predicates) {
                Predicate p = (Predicate) o;
                ret.add("(declare-const " + p.toSmtVariableString(i) + " Bool)\n");
                if (i == 0) {
                    if (problem.getInit().containProposition(p)) {
                        ret.add("(assert " + p.toSmtVariableString(i) + ")\n");
                    } else {
                        ret.add("(assert (not " + p.toSmtVariableString(i) + "))\n");
                    }
                }
            }
        }
        return ret;
    }

    private Collection build_numeric_variables_plus_init_global_axiom(int k) {
        HashMap<String, Boolean> declared = new HashMap();
        ArrayList<String> ret = new ArrayList();

        for (int i = 0; i <= k; i++) {

            for (Object o : SC) {

                GlobalConstraint gc;
                gc = (GlobalConstraint) o;
                for (Object o1 : (Set) gc.condition.getInvolvedFluents()) {
                    NumFluent nf = (NumFluent) o1;
                    if (declared.get(nf.toSmtVariableString(i)) == null || !declared.get(nf.toSmtVariableString(i))) {
                        declared.put(nf.toSmtVariableString(i), Boolean.TRUE);

                        ret.add("(declare-const " + nf.toSmtVariableString(i) + " " + this.getSec_theory() + ")\n");
                    }
                }
                ret.add(";;Global Constraint: " + gc.name + "\n");
                ret.add("(assert " + gc.condition.toSmtVariableString(i) + ")\n");
            }
            
            for (NumFluent nf : this.numeric_variables) {

                if (declared.get(nf.toSmtVariableString(i)) == null || !declared.get(nf.toSmtVariableString(i))) {
                    declared.put(nf.toSmtVariableString(i), Boolean.TRUE);
                    ret.add("(declare-const " + nf.toSmtVariableString(i) + " " + this.getSec_theory() + ")\n");
                }
                if (i == 0) {//this is init state
                    if (this.domain.generateAbstractInvariantFluents().get(nf) == null && this.derived_fluents.get(nf)==null) {

                        ret.add("(assert (= " + nf.toSmtVariableString(i) + " " + problem.getInit().functionValue(nf).toString().replace(",", ".") + "))\n");
                    }
                }
            }

//            System.out.println("Numeric Variables:"+numeric_variables);
//            for (Object o : this.numeric_variables) {
//                NumFluent nf = (NumFluent) o;
//                if (declared.get(nf.toSmtVariableString(i)) == null || !declared.get(nf.toSmtVariableString(i))) {
//                    declared.put(nf.toSmtVariableString(i), Boolean.TRUE);
//                    ret.add("(declare-const " + nf.toSmtVariableString(i) + " " + this.getSec_theory() + ")\n");
//
//                }
//                if (i == 0) {
//                    
//                    if (this.domain.generateAbstractInvariantFluents().get(nf) == null && this.derived_fluents.get(o)==null) {
//                        if (this.problem.getInit().functionValue(nf) == null) {
//                            System.out.println(" Undefined values not supported yet");
//                            System.exit(-1);
//                        }
//                    }
//                }
//            }

        }
        return ret;

    }

    private Collection build_action_variables(int k) throws CloneNotSupportedException {
        ArrayList<String> ret = new ArrayList();

        for (int i = 0; i < k; i++) {
            Set actionInTheLevel = getActions();

            for (Object o : actionInTheLevel) {
                GroundAction gr = (GroundAction) o;
                if (!this.isRepetition_encoding() || !eligible.get(gr)) {//differentiate regular actions from rolling-up-able ones
                    
                    
                    ret.add("(declare-const " + gr.toSmtVariableString(i) + " Int)\n");
                    ret.add("(assert (or (= " + gr.toSmtVariableString(i) + " 0) (= " + gr.toSmtVariableString(i) + " 1) ))\n");
                    //precondition implications
                    if (gr.getPreconditions() != null && !gr.getPreconditions().sons.isEmpty()) {
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getPreconditions().toSmtVariableString(i) + " ))\n");
                    }

                    AndCond add = (AndCond) gr.getAddList();
                    if (add != null && !add.sons.isEmpty()) {
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getAddList().toSmtVariableString(i + 1) + " ))\n");
                    }
                    if (gr.getDelList() != null && !gr.getDelList().sons.isEmpty()) {
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getDelList().toSmtVariableString(i + 1) + " ))\n");
                    }
                    if (gr.getNumericEffects() != null && !gr.getNumericEffects().sons.isEmpty()) {
                        //System.out.println(gr.getNumericEffects().to_smtlib_with_repetition(i));
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getNumericEffects().toSmtVariableString(i) + " ))\n");
                    }
                } else {

                    ret.add("(declare-const " + gr.toSmtVariableString(i) + "  Int)\n");

                    ret.add("(assert (>= " + gr.toSmtVariableString(i) + " 0))\n");
                    if (Objects.equals(num_rel_actions.get(gr), Boolean.FALSE)) {
                        ret.add("(assert (<= " + gr.toSmtVariableString(i) + " 1))\n");
                        if (gr.getNumericEffects() != null && !gr.getNumericEffects().sons.isEmpty()) {
                            ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getNumericEffects().toSmtVariableString(i) + " ))\n");
                        }
                    } else {//action repetition constraints
                        ret.add(";repetition constraint\n");
//                        System.out.println("GroundAction under analysis:"+gr   );
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 1) " + add_constraint_for_repetition(gr, i) + " ))\n");

                        String s = add_prop_constraint_for_repetition(gr, i);
                        if (s != null) {
                            ret.add(";prop_constraint\n(assert " + s + ")\n");
                        }
                        if (max_number_of_repetition != -1) {
                            ret.add("(assert (<= " + gr.toSmtVariableString(i) + " " + max_number_of_repetition + "))\n");
                        }
                        if (gr.getNumericEffects() != null && !gr.getNumericEffects().sons.isEmpty()) {
                            for (NumEffect ne : (Collection<NumEffect>) gr.getNumericEffects().sons) {
                                ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + ne.to_smtlib_with_repetition(i, gr.toSmtVariableString(i)) + " ))\n");
                            }

                        }
                    }
                    if (gr.getPreconditions() != null && !gr.getPreconditions().sons.isEmpty()) {
                        ret.add(";precondition\n(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getPreconditions().toSmtVariableString(i) + " ))\n");
                    }

                    AndCond add = (AndCond) gr.getAddList();
                    if (add != null && !add.sons.isEmpty()) {
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getAddList().toSmtVariableString(i + 1) + " ))\n");
                    }
                    if (gr.getDelList() != null && !gr.getDelList().sons.isEmpty()) {
                        ret.add("(assert (=> (> " + gr.toSmtVariableString(i) + " 0) " + gr.getDelList().toSmtVariableString(i + 1) + " ))\n");
                    }

                }
            }

            ret.add("(assert (or ");

            for (Object o : actionInTheLevel) {
                GroundAction gr = (GroundAction) o;
                ret.add(" (>  " + gr.toSmtVariableString(i) + "  0)");
            }

            ret.add(" true ))\n");
            for (Object o : interferences) {
                GroundAction[] interferring = (GroundAction[]) o;
               
                if (actionInTheLevel.contains(interferring[0]) && actionInTheLevel.contains(interferring[1])) {

                    String a = "";
                    String b = "";
                    if (num_rel_actions.get(interferring[0]) == Boolean.TRUE || !not_homogenous) {
                        a = "(> " + interferring[0].toSmtVariableString(i) + " 0)";
                    } else {
                        a = interferring[0].toSmtVariableString(i);
                    }
                    if (num_rel_actions.get(interferring[1]) == Boolean.TRUE || !not_homogenous) {
                        b = "(> " + interferring[1].toSmtVariableString(i) + " 0)";
                    } else {
                        b = interferring[1].toSmtVariableString(i);
                    }
                    ret.add("(assert (not (and " + a + " " + b + " )))\n");
//                    }
                }
                //}
            }
        }
        return ret;

    }

    private Collection build_frame_axiom(int k) {
        ArrayList<String> ret = new ArrayList();

        for (int i = 0; i < k; i++) {
            //frame axiom
            //Propositional Part
            for (Object o : reacheable_predicates) {
                Predicate p = (Predicate) o;
                ret.add("(assert (=> (and " + p.toSmtVariableString(i) + " (not " + p.toSmtVariableString(i + 1) + ")) " + predicateModifiers(p, predDeleters, i) + " ))\n");
                ret.add("(assert (=> (and " + p.toSmtVariableString(i + 1) + " (not " + p.toSmtVariableString(i) + ")) " + predicateModifiers(p, predAchievers, i) + " ))\n");
            }
            //Numeric one
            for (NumFluent o : this.numeric_variables) {
                ret.add("(assert (=> (not " + this.compute_numeric_modifiers(o, numModifiers, i) + ") (= " + o.toSmtVariableString(i) + " " + o.toSmtVariableString(i + 1) + ")))\n");

            }
        }
        return ret;
    }

    AndCond build_frame_for_global_constraint(GroundAction gr, Comparison t1, Conditions t) throws CloneNotSupportedException {

        Comparison t2 = (Comparison) t1;
        Comparison nc = gr.regressComparisonMtimes((Comparison) t2.clone());

        AndCond t4 = new AndCond();
        t4.addConditions(t);
        if (t instanceof NotCond) {
            NotCond t3 = new NotCond();
            t3.addConditions(nc);
            if (!nc.equals(t2)) {
                t4.addConditions(t3);
            }
        } else {
            t4.addConditions(nc);
        }

        return t4;

    }

    private Conditions generate_m_times_regressed_conditions(Conditions c, GroundAction gr) throws CloneNotSupportedException {
        if (c instanceof OrCond) {
            OrCond ret = new OrCond();
            for (Conditions c1 : (Collection<Conditions>) c.sons) {
                if (c1 instanceof NotCond) {
                    NotCond t = (NotCond) c1;
                    Object t1 = t.son.iterator().next();
                    if (t1 != null && t1 instanceof Comparison) {
                        ret.addConditions((AndCond) build_frame_for_global_constraint(gr, (Comparison) t1, t));
                    } else {
                        throw new UnsupportedOperationException("Global Constraints have to contain numeric constraint");
                    }
                } else if (c1 instanceof Comparison) {
                    ret.addConditions((AndCond) build_frame_for_global_constraint(gr, (Comparison) c1, c1));
                } else if (c1 instanceof PDDLObjectsEquality) {
                    ret.addConditions(c1);
                } else {
                    throw new UnsupportedOperationException("Global Constraints have to be represented in CNF");
                }
            }
            return ret;
        } else if (c instanceof NotCond) {
            NotCond t = (NotCond) c;
            Object t1 = t.son.iterator().next();
            if (t1 != null && t1 instanceof Comparison) {
                return build_frame_for_global_constraint(gr, (Comparison) t1, t);
            } else {
                throw new UnsupportedOperationException("Global Constraints have to contain numeric constraint when repetition is activated");
            }
        } else if (c instanceof AndCond) {
            AndCond ret = new AndCond();
            for (Conditions c1 : (Collection<Conditions>) c.sons) {
                if (c1 instanceof NotCond) {
                    NotCond t = (NotCond) c1;
                    Object t1 = t.son.iterator().next();
                    if (t1 != null && t1 instanceof Comparison) {
                        ret.addConditions((AndCond) build_frame_for_global_constraint(gr, (Comparison) t1, t));
                    } else {
                        throw new UnsupportedOperationException("Global Constraints have to contain numeric constraint");
                    }
                } else if (c1 instanceof Comparison) {
                    ret.addConditions((AndCond) build_frame_for_global_constraint(gr, (Comparison) c1, c1));
                } else if (c1 instanceof PDDLObjectsEquality) {
                    ret.addConditions(c1);
                } else {
                    System.out.println(c1.getClass());
                    throw new UnsupportedOperationException("Global Constraints have to be represented in CNF");
                }
            }
            return ret;
        } else if (c instanceof Comparison) {
            return build_frame_for_global_constraint(gr, (Comparison) c, c);
        } else {
            throw new UnsupportedOperationException("Global Constraints have to be represented in CNF");
        }
    }

    public void compute_action_interferencies() {
        interferences = null;
        if (this.semantic == null || this.semantic.equalsIgnoreCase("1")) {
            System.out.println("1-step semantics");
            interferences = this.one_step_semantics_mutexes(getActions());
        } else if (this.semantic.equalsIgnoreCase("n")) {
            System.out.println("foreach-step semantics");

            interferences = this.for_each_semantics_mutexes(getActions());
        }else {
            System.err.println("No semantic defined");
            System.exit(-1);
        }
    }

    /**
     * @return the actions
     */
    public LinkedHashSet getActions() {
        return actions;
    }

    /**
     * @param actions the actions to set
     */
    public void setActions(LinkedHashSet actions) {
        this.actions = actions;
    }

    public boolean compute_relevance_analysis(Set a) throws Exception {

        Aibr reachability = new Aibr(problem.getGoals(), a);
        Float ret = reachability.setup(getProblem().getInit());
        if (ret == Float.MAX_VALUE && domain.get_derived_variables().isEmpty()) {
            return false;
        }

        setActions(new LinkedHashSet(reachability.reachable));

        num_rel_actions = new HashMap();
        numeric_variables = new LinkedHashSet();
        eligible = new HashMap();

        
        //find derived variables and actions involving derived variables; if it is the case       
        derived_fluents = new HashMap();
        if (!domain.get_derived_variables().isEmpty()){
            for (GroundAction gr: (Collection<GroundAction>)problem.getActions()){
                boolean action_to_add = false;
                if (gr.getPreconditions() != null && !gr.getPreconditions().sons.isEmpty()){             
                    for (NumFluent nf: gr.getPreconditions().getInvolvedFluents()){

                    }
                }
                Collection<NumFluent> collection = new LinkedHashSet();
                collection.addAll(gr.getPreconditions().getInvolvedFluents());
                collection.addAll(gr.getNumericEffects().getInvolvedFluents());
    //            System.out.println("Collection of fluents:"+ collection);
                for (NumFluent nf: collection){
                    for (NumFluent derived: domain.get_derived_variables()){
                        if (nf.getName() == null ? derived.getName() == null : nf.getName().equals(derived.getName())){
                            //here we are very conservative
                            derived_fluents.put(nf,Boolean.TRUE);
                            action_to_add = true;
                            numeric_variables.add(nf);
                        }

                    }
                }
                if (action_to_add){
                    actions.add(gr);
                }
            }
//            System.out.println("Derived Variables:"+ derived_fluents);

        }

        for (GroundAction gr : actions) {
            num_rel_actions.put(gr, true);

            if (gr.getNumericFluentAffected() != null && !gr.getNumericFluentAffected().isEmpty()) {
                numeric_variables.addAll(gr.getNumericFluentAffected().keySet());
            }
            //third is due to lack of support for complex exponential functions in smt theories
            if ((gr.internal_dependencies_length() > 0) || gr.has_complex_preconditions() || gr.has_exponential_or_nl_effects_asymptotic_effects() || !gr.has_additive_effects() || gr.delete_own_preconditions()) {
                eligible.put(gr, false);
            } else {
                eligible.put(gr, true);
            }
        }

        reacheable_predicates = reachability.reacheable_state.poss_propositions.keySet();
        System.out.println("|P|" + reacheable_predicates.size());
        System.out.println("|X|" + numeric_variables.size());
        RelState reacheableState = reachability.reacheable_state;
        Iterator it = SC.iterator();
        while (it.hasNext()) {
            GlobalConstraint c = (GlobalConstraint) it.next();
            if (c.isTautology(reacheableState)) {
                it.remove();
            }

        }
        
        //preprocess achievers and modifiers
        init_ach_mod();

        System.out.println("|A|:" + getActions().size());
        return true;
    }

    public void grounding() {
        getProblem().grounding();
        

        SC = getProblem().globalConstraintSet;
    }

    //interference with global constraint
    private boolean interference(GroundAction a, GroundAction b, HashSet SC) {
        HashSet<GlobalConstraint> gc_coll = (HashSet<GlobalConstraint>) SC;

        if ((a.getNumericFluentAffected() == null) || b.getNumericFluentAffected() == null) {
            return false;
        }

        boolean a_interacts = false;
        for (GlobalConstraint gc : gc_coll) {
            for (NumFluent nf : gc.condition.getInvolvedFluents()) {
                if ((a.getNumericFluentAffected().get(nf) != null)) {
                    if (a.getNumericFluentAffected().get(nf)) {
                        a_interacts = true;
                    }
                }
            }
        }
        if (!a_interacts) {
            return false;
        }
        for (GlobalConstraint gc : gc_coll) {
            for (NumFluent nf : gc.condition.getInvolvedFluents()) {
                if ((b.getNumericFluentAffected().get(nf) != null)) {
                    if (b.getNumericFluentAffected().get(nf)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    //sat via z3 or cvc4 plus extraction plan from valid model (if any)
    private boolean sat(int i) throws Exception {

        System.out.print("Current Horizon:" + i);
        long start = System.currentTimeMillis();
        ArrayList<String> smtString = null;
        smtString = this.encode(i);

        writeSmt2File(smtString, i);
        this.overallTime += (System.currentTimeMillis() - start);
        this.overallEcondingTime += (System.currentTimeMillis() - start);

        //invoking the solver
        start = System.currentTimeMillis();

        Process process = null;
        if (z3solver){
            process = new ProcessBuilder("z3", "-smt2", name_file_temp).start();
        }else{
           process = new ProcessBuilder("cvc4-1.4-x86_64-linux-opt", "-L","smtlib", name_file_temp).start();
        }
        InputStream is = process.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader br = new BufferedReader(isr);
        String line;

        int j = 0;
        sat = false;

        extractedPlan = new SimplePlan(this.domain);

        //Pop encodes the plan resulting from the sat test, if any
        DirectedAcyclicGraph pop = new DirectedAcyclicGraph(DefaultEdge.class);

        //parsing the outcome. Can be optimized and written in a more elegant way. Statistics should be collected and then provided as output
        while ((line = br.readLine()) != null) {
            if (j == 0) {
                if (line.contains("unsat") || line.contains("unknown")) {
                    sat = false;
                    if (debugInfo > 0) {
                        System.out.println("unsat with " + i);
                    }
                    System.out.print(":Solving-TIME:" + (System.currentTimeMillis() - start));

                    //break;
                } else if (!line.contains("error")) {
                    if (debugInfo > 0) {
                        System.out.println("sat with" + i);
                    }
                    System.out.print(":Solving-TIME:" + (System.currentTimeMillis() - start));
                    sat = true;
                    //break;
                } else if (line.contains("error")) {
                    System.out.println("Error in the encoding");
                    System.exit(-1);
                }
            } else {
                if (line.contains("ACTION") && (sat)) {
                    String nextLine = null;
                    if (z3solver)
                        nextLine = br.readLine();
                    else
                        nextLine = line; //line = br.readLine();
                    if (nextLine != null) {
                            Pattern p = null;
                            if (z3solver)
                                p = Pattern.compile(".*([0-9]+)\\)||.*true.*");
                            else
                                p = Pattern.compile(".*Int ([0-9]+)\\)");

                            Matcher m = p.matcher(nextLine);
                            if (!m.matches()) {
                                continue;
                            }
                            float frep = 1.0f;
                            if (!nextLine.contains("true") && z3solver) {
                                frep = Float.parseFloat(nextLine.replace(")", "").replace(" ", ""));

                            }else{
                                frep = Float.parseFloat(m.group(1));
                            }
                            int repetition = (int) frep;//could map directly to integer in the first place. Done for experiment, not sure whether removing comprimise functioning
                            if (repetition > 0) {
                                //mapping a given action with the number of times such an action has to be repeated
                                repetitions.put(pddlActionString(new String(line)), repetition);
                                pop.addVertex(pddlActionString(new String(line)));
                            }
                    }
                } else if (line.contains(":time")) {
                    if (debugInfo > 1) {
                        System.out.println(line);
                    }
                }
            }
            j++;

        }

        System.out.println("");

        int nOfVars = 0;
        int nOfRules = 0;
        for (int k = 0; k < smtString.size(); k++) {
            String smtLine = smtString.get(k);
            if(smtLine.contains("(assert")){
                nOfRules = nOfRules + 1;
            }
            if(smtLine.contains("(declare-const")){
                nOfVars = nOfRules + 1;
            }
        }
        System.out.println("Vars at Horizon " + i + ": " + nOfVars);
        System.out.println("Rules at Horizon " + i + ": " + nOfRules);

        this.overallTime += (System.currentTimeMillis() - start);
        if (sat) {
            if (debugInfo > 0) {
                System.out.println("Encoding time:" + this.overallEcondingTime);
            }
            if (debugInfo > 0) {
                System.out.println("Planning time:" + this.overallTime);
            }
        }
        //The next finds a topological order ot the pop, and store it in a simple plan representation
        //This is useful when we adopt a parallel semantic

        setEdgesViaOrders(pop);

        TopologicalOrderIterator toi = new TopologicalOrderIterator(pop);

        while (toi.hasNext()) {
            //System.out.println(toi.next());
            String action = (String) toi.next();
            if (action != null) {
                Integer r = repetitions.get(action);
                if (r == null) {
                    r = 1;
                }
                for (int k = 0; k < r; k++) {
                    extractedPlan.addActionsFromString(action);
                }
            }
        }

        actionsFound = new HashSet();
        for (Object o : extractedPlan) {
            actionsFound.add(o);
        }
        if (debugInfo > 1) {
            System.out.println(extractedPlan);
        }
        if (must_remove_file_temp) {
            Utils.remove_file(name_file_temp);
        }
        return sat;

    }


}
