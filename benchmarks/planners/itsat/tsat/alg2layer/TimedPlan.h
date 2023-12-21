#ifndef TIMEDPLAN_H
#define TIMEDPLAN_H

#include "tsat/satlayer/SatLayer.h"
#include <vector>
using namespace std;

int PruneTimedPlan(vector<nsSatLayer::PlanEvent> &plan);
void PrintTimedPlan(vector<nsSatLayer::PlanEvent> &plan, const string planFileName, int &planNumber, double &makespan, float elapsedTime);
bool FindTimedPlan(vector<nsSatLayer::PlanEvent> &plan, vector<int> &negcycle, const string planFileName, double &makespan, int &planNumber);

#endif
