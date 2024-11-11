#include "tsat/alg1time/Alg1Time.h"
#include "tsat/sattime/SatTime.h"
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/graph/ETGraph.h"
#include "tsat/alg1time/ETGraphUsage.h"
#include <fstream>
#include <vector>
#include <sstream>
#include <cfloat> // for DBL_MAX
using namespace std;
using namespace MyParser;
using namespace nsSatTime;

#include "tsat/alg2layer/TimedPlan.h"
#include <algorithm>

bool Alg1Time(AlgCommonParams p)
{
	//if(p.satsolver=="minisat")
	//	limitMemory(3072); // 3 GB
	if(p.graphUsage == 2) // FIXME: can not handle overall variables
		p.graphUsage = 1;

	double t2, t1;
	t1 = CPUTime();
	cout << "Domain: " << pDomain.name << " Objects: " << pProblem.pObjects.size() << endl;
	cout << "Predicates: " << pDomain.predicates.size() << " Operators: " << pDomain.operators.size() << endl;
	cout << "Propositions: " << pProblem.pAllProposition.size() << " Actions: " << pProblem.pAllAction.size() << endl;
	cout << "Time taken for parsing: " << t1 << " secs" << endl << flush;

	ETGraph *g = NULL;
	vector< vector<Mutex> > *fact_mutex = NULL;
	vector<int> prop_layer;
	if(p.graphUsage != 0) // if graph usage is enabled
	{
		cout << endl << "Constructing temporal planning graph:" << endl;
		g = new ETGraph();
		cout << "  1. Initializing the graph ..." << endl;
		GraphInit(*g);
		cout << "       Done." << endl;
		cout << "  2. Constructing the graph ..." << endl;
		try
		{
			g->CreateGraph(pProblem.initialState, p.AvailableTime - CPUTime());
			if(g->Layers == -1) // construction failed
			{
				delete g;
				g = NULL;
				p.graphUsage = 0;
			}
		}
		catch(const bad_alloc &e) // out of memory
		{
			cout << endl << "Out of memory exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "Ignoring the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
			t1 = CPUTime() - t1;
		}
		catch(const overflow_error &e) // ID or COUNTER or LAYER overflow
		{
			cout << endl << "Overflow exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "But considering the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
		}
		catch(const runtime_error &e) // timeout
		{
			// NOTE: we assume that the assigned time to g->CreateGraph() is less than total available time,
			//       otherwise we should abort the planner with a "throw;"
			string ewhat = e.what();
			if(ewhat != "Timeout during graph construction.") // Unhandled exception
				throw;
			cout << endl << "Timeout exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "But considering the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
		}
		if(g != NULL) // construction was successful
		{
			cout << "       Done.\t# of Layers: " << g->Layers << endl;
			int nGoalLayer = g->GoalsLayer(pProblem.goals);
			cout << "       Goals first appear at " << nGoalLayer << "th Layer non-mutex." << endl;
			if(p.TStart < nGoalLayer)
				p.TStart = nGoalLayer;
			//GraphPrintFactMutex(*g);
			cout << "  3. Extracting mutexes between facts ...";
			int	nFactMutex = GraphExtractFactMutex(*g, fact_mutex, p.graphUsage==2);
			cout << " done." << endl;
			cout << "       # of mutexes: " << nFactMutex << endl;
			prop_layer.swap(*g->PropAddedOnLayer);
			if(p.graphUsage == 1) // mutex between facts only
				prop_layer.resize(pProblem.pAllProposition.size());
			delete g;
			g = NULL;
			t2 = CPUTime();
			cout << "Time taken for graph construction : " << t2-t1 << " secs." << endl;
			cout << "Total time so far: " << t2 << " secs." << endl;
			t1 = t2;
		}
	}

	cout << endl << "Process started:" << endl << endl << flush;
	vector<SATResults> elapsed;
	int T, Tstart=p.TStart+1, Tend=p.TStart-1, Tsuccess = -1;
	SatTime *solver;
	SATResults *res = new SATResults;
	res->outcome = INDET;
	int planNumber = 0;
	vector<PlanAction> plan;
	double bestMakeSpan = DBL_MAX;
	for(T=p.TStart; T>=p.TStart && T<=p.TEnd && p.AvailableTime - CPUTime() > 0; )
	{
		cout << endl << "Trying with T=" << T << "... " << endl << flush;
		float availableTime = p.AvailableTime - CPUTime();
		if(availableTime > p.StageTime)
			availableTime = p.StageTime;
		if(p.satsolver=="minisat")
		{
			solver = new SatTimeMinisat(
				T, res, p.detailsFileNameTemplate,
				availableTime, p.overall, p.gen_cnf, p.gen_readable_cnf, p.justgencnf);
			
		}
		else if(p.satsolver=="precosat")
		{
			solver = new SatTimePrecosat(
				T, res, p.detailsFileNameTemplate,
				availableTime, p.overall, p.gen_cnf, p.gen_readable_cnf, p.justgencnf);
		}
		else if(p.satsolver=="zchaff")
		{
			solver = new SatTimeZchaff(
				T, res, p.detailsFileNameTemplate,
				availableTime, p.overall, p.gen_cnf, p.gen_readable_cnf, p.justgencnf);
		} else return false;
		// prepare the solver
		try
		{
			if(p.graphUsage==0)
				solver->DoEncoding(); // encode without graph
			else
				solver->DoEncoding(fact_mutex, &prop_layer); // encode using graph
		}
		catch(const bad_alloc &e) // out of memory
		{
			delete solver;
			cout << endl << "Out of memory exception from solver->DoEncoding():" << e.what() << endl;
			// since the out of memory happened during the encoding,
			// if we are not using graph, then the only option is to quit
			if(p.graphUsage == 0) 
			{
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				res->outcome = UNSAT;
				break; // abort
			}
			// otherwise disable graph usage and delete any memory associated with graph:
			p.graphUsage = 0;
			prop_layer.clear();
			delete fact_mutex;
			delete g;
			fact_mutex = NULL;
			g = NULL;
			cout << "Graph usage disabled to save memory. Total time so far: " << CPUTime() << endl;
			continue; // now try again with current T, but without graph, to avoid out of memory
		}
		catch(const runtime_error &e) // probably timeout
		{
			// NOTE: we assume that the assigned time to DoEncoding() is less than total available time,
			//       otherwise we should abort the planner with a "throw;"
			delete solver;
			string ewhat = e.what();
			if(ewhat != "Timeout during encoding.") // Unhandled exception
			{
				cout << "Timeout during encoding." << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				res->outcome = UNSAT;
				break; // abort
			}
			else
				throw;
		}
		catch(const exception &e)
		{
			cout << endl << "Unhandled exception from solver->DoEncoding(): " << e.what() << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			cout << "Search for plan aborted." << endl;
			delete solver;
			res->outcome = UNSAT;
			break; // abort
		}
		// now call the ->solve()
		try
		{
			solver->Solve();
			plan.swap(solver->plan);
		}
		catch(const bad_alloc &e) // out of memory exception
		{
			delete solver;
			cout << endl << "Out of memory exception from solver->Solve():" << e.what() << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			cout << "Search for plan aborted." << endl;
			res->outcome = UNSAT;
			break; // abort
		}
		catch(const exception &e)
		{
			cout << endl << "Unhandled exception from solver->Solve():" << e.what() << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			cout << "Search for plan aborted." << endl;
			delete solver;
			res->outcome = UNSAT;
			break; // abort
		}
		delete solver;

		t2 = CPUTime();
		res->T = T;
		res->time_overall = t2 - t1;
		elapsed.push_back(*res);
		cout << "Time: " << t2 - t1 << " secs" << endl << endl << flush;
		t1 = t2;
		if(res->outcome == SAT) // a plan found
		{
			// PrintPlan(plan, p.planFileName, planNumber, CPUTime());
			
			// compress the plan and remove redundant actions
			vector<nsSatLayer::PlanEvent> LPlan;
			vector<int> negCycle;
			for(vector<PlanAction>::const_iterator it = plan.begin(); it != plan.end(); ++it)
			{
				nsSatLayer::PlanEvent e;
				e.id = it->id;
				e.part = nsSatLayer::ACTION_START;
				e.doubleD = it->t;
				LPlan.push_back(e);
				e.part = nsSatLayer::ACTION_END;
				e.doubleD = it->t + pProblem.pAllAction.GetActionById(it->id)->duration;
				LPlan.push_back(e);
			}
			sort(LPlan.begin(), LPlan.end());

			int lastT = 0; double lastD = 0;
			for(vector<nsSatLayer::PlanEvent>::iterator it = LPlan.begin(); it != LPlan.end(); ++it)
			{
				if(it->doubleD == lastD)
					it->t = lastT;
				else
				{
					it->t = ++lastT;
					lastD = it->doubleD;
				}
			}
			//if(pDomain.name != "domain-tms-2-3-light")
				FindTimedPlan(LPlan, negCycle, p.planFileName, bestMakeSpan, planNumber);
			//else
				// FIXME: return the original plan due to a "problem" in "scheduling phase"
				//PrintTimedPlan(LPlan, p.planFileName, planNumber, bestMakeSpan, CPUTime());

			int intMakespan = 0;
			for(vector<nsSatLayer::PlanEvent>::const_iterator it = LPlan.begin(); it != LPlan.end(); ++it)
			{
				if(it->part == nsSatLayer::ACTION_END) // if we ignore it we will add its duration twice
					continue;
				double m = it->doubleD;
				//if(pDomain.name == "satellite")
					//m += pProblem.pAllAction.GetActionById(it->id)->duration / (float) 100;
				//else if(pDomain.name == "pipesworld_strips")
					//m += pProblem.pAllAction.GetActionById(it->id)->duration / (float) 12;
				//else
					m += pProblem.pAllAction.GetActionById(it->id)->duration;

				double m2 = floor(m);
				//if(pDomain.name == "satellite")
					//m2 *= 100;
				//else if(pDomain.name == "pipesworld_strips")
					//m2 *= 12;
				m2 += 100 * (m - floor(m));
				if (m2 > intMakespan)
					intMakespan = roundToPrecision(m2, 0);
			}
			
			// +1 is because T must always be one unit greater than makespan:
			Tsuccess = 1 + intMakespan;
			if(Tsuccess == T) // to avoid for-ever loop
				Tend = Tsuccess-1;
			else
				Tend = Tsuccess; // to avoid non-optimal "bug" in matchlift-p1
		}
		else if(res->outcome == UNSAT) // instance unsatisfiable
		{
			if(Tsuccess == -1)
			{
				Tstart = T+1;
				T = ceil(T*p.TMultiply + p.TPlus);
				if(T>p.TEnd && (Tstart-1)<p.TEnd)
					T = p.TEnd;
				Tend = T-1;
			}
			else
				Tstart = T+1;
		}
		else // eg. timeout or memout
			break;
		if(Tsuccess != -1)
		{
			if(Tstart > Tend)
				break;
			T = (Tend + Tstart) / 2;
		}
	}
	if(g)
				delete g;
	if(Tsuccess != -1)
	{
		if(Tstart > Tend)
			cout << "Optimal makespan = ";
		else
			cout << "Epsilon-Optimal makespan = ";
		cout << bestMakeSpan << "\tTsuccess = " << Tsuccess-1 << "\t[Tstart,Tend] = [" << Tstart-1 << "," << Tend-1 << "]" << endl;
	}
	else
		cout << "No Plan found." << endl;
	cout << "Operation Total Time: " << CPUTime() << " secs" << endl;

	ofstream file3(p.resultsFileName.c_str());
	file3 << "T\toutcome\ttime_overall\ttotalClauses\ttotalMutexes\tvarTotal\tvarProp\tvarAction"
		<< "\tccInit\tccGoal\tccNotApplicable\tccCondition\tccEffect\tccAxiomDelete"
		<< "\tccAxiomAdd\tccMutexStart\tccMutexEnd\tccMutexStartEnd\tccMutexOverall" << endl;
	for(int i=0; i<elapsed.size(); i++)
	{
		SATResults *res = &elapsed[i];
		file3 << res->T << "\t" << res->outcome << "\t" << res->time_overall << "\t" << res->totalClauses
			<< "\t" << res->totalMutexes << "\t" << res->varTotal << "\t" << res->varProp << "\t" << res->varAction
			<< "\t" << res->ccInit << "\t" << res->ccGoal << "\t" << res->ccNotApplicable << "\t" << res->ccCondition
			<< "\t" << res->ccEffect << "\t" << res->ccAxiomDelete << "\t" << res->ccAxiomAdd << "\t" << res->ccMutexStart
			<< "\t" << res->ccMutexEnd << "\t" << res->ccMutexStartEnd << "\t" << res->ccMutexOverall << endl;
	}
	file3.close();
	return true;
}

void PrintPlan(vector<PlanAction> &plan, string planFileName, int &planNumber, float elapsedTime)
{
	float makespan = 0;
	// calculate makespan
	for(vector<PlanAction>::const_iterator it = plan.begin(); it != plan.end(); ++it)
	{
		const MyParser::PAction *a = MyParser::pProblem.pAllAction.GetActionById(it->id);
		float m = it->t + a->duration;
		if(m > makespan)
			makespan = m;
	}

	// increment planNumber && append to end of plan file name, eg. pfile01.sol.1
	stringstream newPlanFileName;
	newPlanFileName << planFileName << "." << ++planNumber;

	cout << "Final Plan (with makespan = " << makespan << ") is:" << endl;
	cout << "; Metric time: " << makespan << endl;
	cout << "; Elapsed time: " << elapsedTime << endl;
	ofstream planFile;
	if(planFileName != "*")
	{
		planFile.open(newPlanFileName.str().c_str(), ios_base::out);
		planFile << "; Metric time: " << makespan << endl; // this line is a comment in .sol file
		planFile << "; Elapsed time: " << elapsedTime << endl; // this line is a comment in .sol file
	}
	for(vector<PlanAction>::const_iterator it = plan.begin(); it != plan.end(); ++it)
	{
		// each iteration will output a single action, eg. 0: (light_match match1) [5]
		const MyParser::PAction *a = MyParser::pProblem.pAllAction.GetActionById(it->id);
		cout << it->t << ": (" << a->op->name;
		if(planFileName != "*")
			planFile << it->t << ": (" << a->op->name;
		for (int j=0; j<a->n_objects; j++)
		{
			cout << " " << MyParser::pProblem.pObjects.objects[a->objects[j]];
			if(planFileName != "*")
				planFile << " " << MyParser::pProblem.pObjects.objects[a->objects[j]];
		}
		cout << ") [" << a->duration << "]" << endl;
		if(planFileName != "*")
			planFile << ") [" << a->duration << "]" << endl;
	}
	cout << endl << flush;
	if(planFileName != "*")
		planFile.close();
}

