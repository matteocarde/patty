#include "tsat/alg2layer/TimedPlan.h"
#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/alg2layer/EventPlanOrders.h"
#include "tsat/alg2layer/NegativeCycle.h"

#include "tsat/satlayer/SatLayer.h"
#include "tsat/utils.h"
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;
using namespace nsSatLayer;

bool FindTimedPlan(vector<PlanEvent> &plan, vector<int> &negcycle, const string planFileName, double &makespan, int &planNumber)
{
	// initialize orders[][] and weights[][]
	int sz = plan.size();
	int **orders = new int*[sz];
	double **weights = new double*[sz];
	for(int i=0; i<sz; i++)
	{
		orders[i] = new int[sz];
		weights[i] = new double[sz];
	}

	double epsilon = 0.01;

	// pair each start event to corresponding end event, and vise versa
	FindPairsInEventPlan(plan);
	// remove irrelevant actions w.r.t. goals, both start and end event should be irrelevant
	// PruneEventPlan_WRT_Goals(plan);
	// remove useless actions, both start and end event should be useless
	// PruneEventPlan_WRT_UselessEvents(plan);
	// find orders between events, and relax them
	FindEventPlanOrders(plan, orders);
	// show the orders in VERBOSE mode (FIXME: define a VERBOSE mode)
	PrintOrders(plan, (const int **)orders, changeExt(planFileName, "-orders.txt"));
	// assign weights to orders, usually 0 unless the orders is between two corresponding start and end event
	CalculateOrderWeights(plan, (const int **)orders, weights, epsilon);
	// orders and weights are in matrix format, convert them into adjacency list
	vector<DoubleEdge> edges;
	CreateAdjacencyOrders(plan, (const int **)orders, (const double **)weights, edges);
	double *d = new double[sz+1];
	// bellman_ford() returns false in the presence of negative cycle
	if(!bellman_ford(0, sz+1, edges, d, negcycle))
	{
		// FIXME: check entire plan for weirdness
		// HINT: we expect something like this: [A [B B] [C C] ... A]
		if(plan[negcycle[0]-1].id != plan[negcycle[negcycle.size()-1]-1].id)
		{
			cout << "Strange negative cycle detected:" << endl;
			PrintNegativeCycle(plan, negcycle, (const double **)weights);
			cout << flush;
			throw logic_error("Strange negative cycle detected");
		}
		if(bool verbose=true)
		{
			cout << "---------------" << endl;
			cout << "NEGATIVE cycle detected:" << endl;
			PrintNegativeCycle(plan, negcycle, (const double **)weights);
			cout << flush;
		}
		if(int pruneCount = PruneNegativeCycle(plan, negcycle, (const double **)weights))
		{
			if(bool verbose=true)
			{
				cout << "---------------" << endl;
				cout << pruneCount << " event(s) have been removed from negative cycle" << endl;
				cout << "New negative cycle:" << endl;
				PrintNegativeCycle(plan, negcycle, (const double **)weights);
				cout << flush;
			}
		}
		return false;
	}
	if(bool verbose=true)
	{
		cout << "Valid Timed Plan found!" << endl;
		cout << "======================" << endl;
	}
	for(int i=0; i<sz; i++)
	{
		plan[i].doubleD = (floor(-d[i+1] * 10000 + 0.5))/10000;
		//plan[i].doubleD = roundToPrecision(-d[i+1], 4);
	}
	//sort(plan.begin(), plan.end());
	//qsort((void *)&plan[0], plan.size(), sizeof(PlanEvent), compare);
	FindPairsInEventPlan(plan);
	int pruneCount = PruneTimedPlan(plan);
	sz = plan.size();
	stringstream newPlanFileName;
	if(pruneCount == 0)
		PrintTimedPlan(plan, planFileName, planNumber, makespan, CPUTime());
	else
	{
		FindPairsInEventPlan(plan);
		FindEventPlanOrders(plan, orders);
		PrintOrders(plan, (const int **)orders, changeExt(planFileName, "-orders.txt"));
		CalculateOrderWeights(plan, (const int **)orders, weights, epsilon);
		CreateAdjacencyOrders(plan, (const int **)orders, (const double **)weights, edges);
		if(!bellman_ford(0, sz+1, edges, d, negcycle))
			throw logic_error("Strange behavior of PruneTimedPlan()");
		cout << pruneCount << " redundant actions have been removed from the plan." << endl;
		for(int i=0; i<sz; i++)
		{
			plan[i].doubleD = (floor(-d[i+1] * 10000 + 0.5))/10000;
			//plan[i].doubleD = roundToPrecision(-d[i+1], 4);
		}
		sort(plan.begin(), plan.end());
		PrintTimedPlan(plan, planFileName, planNumber, makespan, CPUTime());
	}

	// clean up
	delete [] d;
	for(int i=0; i<sz; i++)
	{
		delete [] orders[i];
		delete [] weights[i];
	}
	delete [] orders;
	delete [] weights;

	return true;
}
