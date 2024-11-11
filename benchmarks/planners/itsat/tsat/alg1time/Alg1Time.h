#ifndef ALG1TIME_H
#define ALG1TIME_H

#include "tsat/AlgCommonParams.h"
#include "tsat/sattime/SatTime.h"
#include <string>
using namespace std;
using namespace nsSatTime;

/// Main part of the planner. It uses the ground problem to generate SAT encoding,
/// and calls the chosen SAT solver to solve it. If it succeeds, a plan is generated,
/// otherwise the makespan is increased and the search is continued.
bool Alg1Time(AlgCommonParams p);

/// Expects a timed plan in which the actions are sorted in ascending order
/// and Prints it to both the console and plan file
/// planFileName can be "*" so no plan file will be generated
void PrintPlan(vector<PlanAction> &plan, string planFileName, int &planNumber, float elapsedTime);

#endif
