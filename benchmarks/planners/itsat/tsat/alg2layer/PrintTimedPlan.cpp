#include "tsat/alg2layer/TimedPlan.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/parser/ParserClasses.h"
#include <vector>
#include <sstream>
#include <cmath> // for fabs
using namespace std;
using namespace MyParser;
using namespace nsSatLayer;


void PrintTimedPlan(vector<PlanEvent> &plan, const string planFileName, int &planNumber, double &makespan, float elapsedTime)
{
	const int _precision = 2;
	double newmakespan = 0;
	// calculate makespan
	for(vector<PlanEvent>::const_iterator it = plan.begin(); it != plan.end(); ++it)
	{
		if(it->part == ACTION_END) // if we ignore it we will add its duration twice
			continue;
		double m = it->doubleD;
		//if(pDomain.name == "satellite")
			//m += pProblem.pAllAction.GetActionById(it->id)->duration / (float) 100;
		//else if(pDomain.name == "pipesworld_strips")
			//m += pProblem.pAllAction.GetActionById(it->id)->duration / (float) 12;
		//else
			m += pProblem.pAllAction.GetActionById(it->id)->duration;
		if(m>newmakespan)
			newmakespan = m;
	}
	if(newmakespan > makespan || fabs(newmakespan-makespan) < 0.00001)
	{
		cout << "Omitting the plan with makespan " << newmakespan
			<< ". Best makespan found so far is " << makespan << endl;
		return;
	}
	// otherwise print the plan to screen and file, and set the best makespan
	makespan = newmakespan;
	// increment planNumber && append to end of plan file name, eg. pfile01.sol.1
	stringstream newPlanFileName;
	newPlanFileName << planFileName << "." << ++planNumber;

	int sz = plan.size();
	cout << "Writing final plan to file: " << newPlanFileName.str() << " , makespan = "
		<< makespan << " , elapsed time = " << elapsedTime << endl;
	ofstream planFile;
	if(planFileName != "*")
	{
		planFile.open(newPlanFileName.str().c_str(), ios_base::out);
		planFile << "; Metric time: " << makespan << endl; // this line is a comment in .sol file
		planFile << "; Elapsed time: " << elapsedTime << endl; // this line is a comment in .sol file
	}
	else
	{
		cout << "PLAN BEGIN:" << endl;
		cout << "; Metric time: " << makespan << endl;
		cout << "; Elapsed time: " << elapsedTime << endl;
	}
	// use d to generate real plan
	for(int i=0; i<sz; i++)
	{
		// each iteration will output a single action, eg. 0: (light_match match1) [5]
		if(plan[i].part==ACTION_END)
			continue;
		const PAction *a = pProblem.pAllAction.GetActionById(plan[i].id);
		if(planFileName != "*")
		{
			planFile.precision(_precision);
			planFile << fixed << plan[i].doubleD;
			planFile << ": (" << a->op->name;
		}
		else
		{
			cout.precision(_precision);
			cout << fixed << plan[i].doubleD;
			cout << ": (" << a->op->name;
		}
		for (int j=0; j<a->n_objects; j++)
		{
			if(planFileName != "*")
				planFile << " " << pProblem.pObjects.objects[a->objects[j]];
			else
				cout << " " << pProblem.pObjects.objects[a->objects[j]];
		}
		// FIXME: remove domain specific manual fixes:
		if(planFileName != "*")
		{
			//if(pDomain.name == "satellite")
				//planFile << ") [" << a->duration / (float) 100 << "]" << endl;
			//else if(pDomain.name == "pipesworld_strips")
				//planFile << ") [" << a->duration / (float) 12 << "]" << endl;
			//else
				planFile << ") [" << a->duration << "]" << endl;
		}
		else
		{
			//if(pDomain.name == "satellite")
				//cout << ") [" << a->duration / (float) 100 << "]" << endl;
			//else if(pDomain.name == "pipesworld_strips")
				//cout << ") [" << a->duration / (float) 12 << "]" << endl;
			//else
				cout << ") [" << a->duration << "]" << endl;
		}
	}
	if(planFileName == "*")
		cout << "PLAN END" << endl;
}
