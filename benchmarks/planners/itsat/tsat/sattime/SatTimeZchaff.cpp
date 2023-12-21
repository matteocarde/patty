#include <fstream>
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/sattime/SatTime.h"

using namespace std;

namespace nsSatTime
{

void SatTimeZchaff::Solve()
{
	SAT_StatusT outcome_zchaff = UNDETERMINED;
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
	SAT_SetTimeLimit(zchaffSolver, totalTime - (CPUTime() - startTime));
	outcome_zchaff = (SAT_StatusT) SAT_Solve(zchaffSolver);
	switch (outcome_zchaff) {
	case SATISFIABLE:
		satresults->outcome = SAT;
		cout << "Satisfied!" << endl;
		GeneratePlan();
		break;
	case UNSATISFIABLE:
		satresults->outcome = UNSAT;
        cout << "Instance Unsatisfiable" << endl;
		break;
	case TIME_OUT:
		satresults->outcome = TIMEOUT;
        cout << "Time out"<<endl;
		break;
	case MEM_OUT:
		satresults->outcome = MEMOUT;
        cout << "Memory out"<<endl;
	default:
		satresults->outcome = INDET;
        cout << "Unknown outcome" << endl;
	}
	cout << flush;

	//cout << "Time taken for SAT solving: " << SAT_GetCPUTime(zchaffSolver) << " secs" << endl;
}

void SatTimeZchaff::GeneratePlan()
{
	if(satresults->outcome!=SAT)
		return;
	int sz = SAT_NumVariables(zchaffSolver);
	for (int i=1; i <= sz; ++i)
	{
		if(SAT_GetVarAsgnment(zchaffSolver, i) == 1) // ==1 for happening , ==0 for not happending
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
