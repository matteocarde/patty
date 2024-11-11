#ifndef ALG2LAYER_H
#define ALG2LAYER_H

#include "tsat/AlgCommonParams.h"

/// Main part of the planner. It uses the ground problem to generate SAT encoding,
/// and calls the chosen SAT solver to solve it. If it succeeds, a "leveled" plan is generated,
/// otherwise the makespan is increased and the search is continued.
/// Then the leveled plan is used to create a timed plan using a Simple Temporal Network
/// For more info refer to the ITSAT paper.
bool Alg2Layer(AlgCommonParams p);

#endif
