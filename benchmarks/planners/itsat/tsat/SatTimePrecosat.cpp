#include <fstream>
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/sattime/SatTime.h"

using namespace std;

namespace nsSatTime
{

void SatTimePrecosat::Solve()
{
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
	
	cout << "Now trying to solve..." << endl << flush;
	precosatSolver->available_time = totalTime - (CPUTime() - startTime);
	int res = precosatSolver->solve();

	if(res > 0)
	{
		if (!precosatSolver->satisfied ())
			throw runtime_error("Critical error in Precosat solver.");
		satresults->outcome = SAT;
		cout << "Satisfied!" << endl << flush;
		GeneratePlan();
	}
	else if(res == -2)
	{
		satresults->outcome = UNSAT;
        cout << "Timeout, Assuming: Instance Unsatisfiable" << endl << flush;
	}
	else if(res < 0)
	{
		satresults->outcome = UNSAT;
        cout << "Instance Unsatisfiable" << endl << flush;
	}
	else
	{
		satresults->outcome = INDET;
        cout << "Indeterminate" << endl << flush;
	}
}

void SatTimePrecosat::GeneratePlan()
{
	if(satresults->outcome!=SAT)
		return;
	int sz = precosatSolver->getMaxVar();
	for (int i=1; i <= sz; ++i)
	{
		if(precosatSolver->val (2*i) >= 0)
		{
			int actionIndex = var2index[i-1] - nvProp;
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
