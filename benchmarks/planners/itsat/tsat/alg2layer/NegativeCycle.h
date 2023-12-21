#ifndef NEGATIVECYCLE_H
#define NEGATIVECYCLE_H

#include "tsat/satlayer/SatLayer.h"
#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/parser/ParserClasses.h"
#include <vector>
using namespace std;


void PrintNegativeCycle(const vector<nsSatLayer::PlanEvent> &plan, const vector<int> &cycle, const double **weights);
bool AB_Order(const MyParser::PAction *a, const MyParser::PAction *b, nsSatLayer::ActionPart aPart, nsSatLayer::ActionPart bPart);
int PruneNegativeCycle(const vector<nsSatLayer::PlanEvent> &plan, vector<int> &cycle, const double **weights);

#endif
