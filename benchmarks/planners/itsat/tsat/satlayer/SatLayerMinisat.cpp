#include <fstream>
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/satlayer/SatLayer.h"
#include <sstream>

using namespace std;

namespace nsSatLayer
{

void SatLayerMinisat::Solve()
{
	Minisat::lbool outcome_minisat = l_Undef;
	if(totalTime - (CPUTime() - startTime) < 0)
	{
		satresults->outcome = TIMEOUT;
		cout << "Time out whilst generating SAT formula." << endl;
		return;
	}
	if(DONT_SOLVE)
	{
		cout << "Ordered not to solve. ";
		satresults->outcome = UNSAT;
		return;
	}
	
	minisatSolver->eliminate(true);

	//SAT_SetTimeLimit(zchaffSolver, totalTime - (CPUTime() - startTime));
    if(bool verbose=false)
	{
		printf("from minisat: #variables:%12d", minisatSolver->nVars());
		printf("  #clauses:%12d\n", minisatSolver->nClauses());
		cout << flush;
	}
	if(!minisatSolver->okay())
	{
		cout<<"Solved by preprocessing. ";
		satresults->outcome = UNSAT;
		return;
	}

	if(bool verbose=false)
	{
		cout << "Now trying to solve..." << endl << flush;
	}
	Minisat::vec<Minisat::Lit> dummy;
	minisatSolver->verbosity=true;
	minisatSolver->available_time = totalTime - (CPUTime() - startTime);
	outcome_minisat = minisatSolver->solveLimited(dummy); // handle exceptions in the calling function

	if(outcome_minisat==l_True)
	{
		satresults->outcome = SAT;
		if(bool verbose=false)
			cout << "Satisfied!" << endl;
		GeneratePlan();
	}
	else if(outcome_minisat==l_False)
	{
		// outcome_minisat has type Minisat::lbool : l_True, l_False, l_Undef
		// so minisat returns l_False in case of timeout
		if(totalTime - (CPUTime() - startTime) < 0)
		{
	        cout << "Time out" << endl;
			satresults->outcome = TIMEOUT;
		}
		else
		{
	        cout << "Instance Unsatisfiable" << endl;
			satresults->outcome = UNSAT;
		}
	}
	else
	{
		satresults->outcome = INDET;
        cout << "Indeterminate"<<endl;
	}
	cout << flush;

	//cout << "Time taken for SAT solving: " << SAT_GetCPUTime(zchaffSolver) << " secs" << endl;
}

void SatLayerMinisat::GeneratePlan()
{
	if(satresults->outcome!=SAT)
		return;
	if(bool verbose=false)
		cout << "Plan is:" << endl;
	ofstream planFile;
	if(planFileName != "*")
		planFile.open(planFileName.c_str(), ios_base::out);
	plan.clear(); // is it needed really? maybe, if the solver is called more than once
	int eventCounter = 0;
	for(int t=0; t<T; t++)
	for(int id=0; id<nAction; id++)
	for(int part=0; part<2; part++) // skip part==2
	{
		int var = ActionTime2Var(id, t, part);
		if(minisatSolver->model[var-1] == l_True)
		{
			if(part==0 || part==1)
			{
				PlanEvent e;
				e.part = (ActionPart) part;
				e.id = id;
				e.t = t;
				e.var = Minisat::mkLit(var-1);
				plan.push_back(e);
				eventCounter++;
				if(bool verbose=false)
					cout << eventCounter << ", ";
				if(planFileName != "*")
					planFile << var << "\t" << id << "\t" << part << "\t" << eventCounter << "\t";
			}
			
			const MyParser::PAction *a = MyParser::pProblem.pAllAction.GetActionById(id);
			if(bool verbose=false)
			{
				cout << t << ": (" << a->op->name;
				if(part==0)
					cout << "_S";
				else if(part==1)
					cout << "_E";
				/*else if (part==2) // NEVER will happen (look at the for loop)
					cout << "_O";*/
			}
			if(planFileName != "*")
			{
				planFile << t << ": (" << a->op->name;
				if(part==0)
					planFile << "_S";
				else if(part==1)
					planFile << "_E";
				/*else if (part==2) // NEVER will happen (look at the for loop)
					cout << "_O";*/
			}
			for (int j=0; j<a->n_objects; j++)
			{
				if(bool verbose=false)
					cout << " " << MyParser::pProblem.pObjects.objects[a->objects[j]];
				if(planFileName != "*")
					planFile << " " << MyParser::pProblem.pObjects.objects[a->objects[j]];
			}
			if(bool verbose=false)
				cout << ") [" << a->duration << "]" << endl;
			if(planFileName != "*")
				planFile << ") [" << a->duration << "]" << endl;
		}
	}
	// the opposite of the above code:

	//cout << endl << "--------------------------" << endl;
	//if(planFileName != "*")
	//	planFile << endl << "--------------------------" << endl;
	//int sz = minisatSolver->nVars();
	//for (int i=0; i< sz; ++i)
	//{
	//	if(minisatSolver->model[i] == l_True)
	//	{
	//		int propIndex = var2index[i];
	//		if(propIndex > nGap) // an action
	//			continue;
	//		int id = propIndex % nProp;
	//		int t = propIndex / nProp;
	//		PProposition *p = pProblem.pAllProposition.GetPropositionById(id);
	//		cout << t << ": (" << p->prd->head;
	//		if(planFileName != "*")
	//			planFile << t << ": (" << p->prd->head;
	//		for (int j=0; j<p->objects.size(); j++)
	//		{
	//			cout << " " << pProblem.pObjects.objects[p->objects[j]];
	//			if(planFileName != "*")
	//				planFile << " " << pProblem.pObjects.objects[p->objects[j]];
	//		}
	//		cout << ")" << endl;
	//		if(planFileName != "*")
	//			planFile << ")" << endl;
	//	}
	//}
	if(planFileName != "*")
		planFile.close();
}

};
