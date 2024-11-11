#ifndef FSM_GENERAL_H
#define FSM_GENERAL_H

#include "tsat/satlayer/SatLayer.h"
#include <set>
#include <iterator>
using namespace std;

// was used in ITSAT that was submitted to JELIA 2012
void AddNegCycleAutomaton_General(const vector<nsSatLayer::PlanEvent> &negCycle, int T, nsSatLayer::SatLayer *solver, bool **mutextable, bool *compress);
//void Fill_SimilarA(const vector<nsSatLayer::PlanEvent> &negCycle, std::back_insert_iterator< vector< set<int> > > it, std::back_insert_iterator< vector<int> > itpos, bool **mutextable);
//void Fill_SimilarA_Frame(const vector<nsSatLayer::PlanEvent> &negCycle, std::back_insert_iterator< vector< set<int> > > it);

#endif
