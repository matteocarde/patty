#include <fstream>
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/satlayer/SatLayer.h"
#include <sstream>

using namespace std;

namespace nsSatLayer
{

void SatLayerPrecosat::Solve()
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

void SatLayerPrecosat::GeneratePlan()
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
		if(precosatSolver->val (2*var) >= 0)
		{
			if(part==0 || part==1)
			{
				PlanEvent e;
				e.part = (ActionPart) part;
				e.id = id;
				e.t = t;
				//e.var = Minisat::mkLit(var-1);
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
	if(planFileName != "*")
		planFile.close();
}

};
