#include <fstream>
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/sattime/SatTime.h"

using namespace std;

namespace nsSatTime
{

void SatTimeMinisat::Solve()
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
	printf("from minisat: #variables:%12d", minisatSolver->nVars());
	printf("  #clauses:%12d\n", minisatSolver->nClauses());
	cout << flush;
	if(!minisatSolver->okay())
	{
		cout<<"Solved by preprocessing. ";
		satresults->outcome = UNSAT;
		return;
	}

	cout << "Now trying to solve..." << endl << flush;
	Minisat::vec<Minisat::Lit> dummy;
	minisatSolver->verbosity=true;
	minisatSolver->available_time = totalTime - (CPUTime() - startTime);
	outcome_minisat = minisatSolver->solveLimited(dummy);
	if(outcome_minisat==l_True)
	{
		satresults->outcome = SAT;
		cout << "Satisfied!" << endl;
		GeneratePlan();
	} else if(outcome_minisat==l_False)
	{
		satresults->outcome = UNSAT;
        cout << "Instance Unsatisfiable" << endl;
	}
	else
	{
		satresults->outcome = INDET;
        cout << "Indeterminate"<<endl;
	}
	cout << flush;

	//cout << "Time taken for SAT solving: " << SAT_GetCPUTime(zchaffSolver) << " secs" << endl;
}

void SatTimeMinisat::GeneratePlan()
{
	if(satresults->outcome!=SAT)
		return;
	int sz = minisatSolver->nVars();
	for (int i=0; i< sz; ++i)
	{
		if(minisatSolver->model[i] == l_True)
		{
			int actionIndex = var2index[i] - nvProp;
			if(actionIndex < 0) // a proposition
				continue;
			PlanAction pa;
			pa.id = actionIndex % nAction;
			pa.t = actionIndex / nAction;
			plan.push_back(pa);
		}
	}
}

}
