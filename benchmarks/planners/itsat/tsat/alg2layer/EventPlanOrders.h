#ifndef EVENTPLANORDERS_H
#define EVENTPLANORDERS_H

#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/utils.h" // for DoubleEdge
#include <vector>
using namespace std;


void FindPairsInEventPlan(vector<nsSatLayer::PlanEvent> &plan);
void FindEventPlanOrders(const vector<nsSatLayer::PlanEvent> &plan, int **orders);
void PrintOrders(const vector<nsSatLayer::PlanEvent> &plan, const int **orders, const string ordersFileName);
void CreateAdjacencyOrders(const vector<nsSatLayer::PlanEvent> &plan, const int **orders, const double **weights, vector<DoubleEdge> &edges);
void CalculateOrderWeights(const vector<nsSatLayer::PlanEvent> &plan, const int **orders, double **weights, double epsilon = 0.01);

#endif
