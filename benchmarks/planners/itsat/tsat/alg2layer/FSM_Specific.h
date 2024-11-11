#ifndef FSM_SPECIFIC_H
#define FSM_SPECIFIC_H

#include "tsat/satlayer/SatLayer.h"

// was used in ITSAT that was submitted to ECAI 2012
void AddNegCycleAutomaton(const vector<nsSatLayer::PlanEvent> &negCycle, int T, nsSatLayer::SatLayer *solver);

#endif
