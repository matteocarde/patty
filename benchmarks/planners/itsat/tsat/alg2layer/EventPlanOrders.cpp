#include "tsat/alg2layer/EventPlanOrders.h"
#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include <vector>
#include <fstream>
using namespace std;
using namespace nsSatLayer;
using namespace MyParser;

void FindPairsInEventPlan(vector<PlanEvent> &plan)
{
	int sz = plan.size();
	for(int i=0; i<sz; i++)
	{
		plan[i].pair = -1;
	}
	for(int i=0; i<sz; i++)
	{
		if(plan[i].part==ACTION_END) // or plan[i].pair!=-1
			continue;
		for(int j=i+1; j<sz; j++)
		{
			// if i,j are start and end of a single ground action:
			//    i=([A)  ...  j=(A])
			if(plan[i].id == plan[j].id && plan[i].part==ACTION_START && plan[j].part==ACTION_END)
			{
				// check if i,j are match : [A i=([A) ...no other A... j=(A]) A]
				//    or: [A i=([A) [A [A ...no other A... A] A] j=(A]) A]
				int openParenthesis = 0;
				for(int k=i+1; k<j-1; k++)
				{
					if(plan[k].id==plan[i].id && plan[k].part!=ACTION_OVERALL)
					{
						if(plan[k].part==ACTION_START)
							openParenthesis++;
						else
							openParenthesis--;
					}
				}
				if(openParenthesis==0)
				{
					plan[i].pair = j;
					plan[j].pair = i;
					break;
				}
				// otherwise i,j are not match: i=([A) [A ...no other A... j=(A]) A]
				//   so continue the search
			}
		}
	}
}

void FindEventPlanOrders(const vector<PlanEvent> &plan, int **orders)
{
	// be sure to call FindPairsInEventPlan(plan, orders); first
	int sz = plan.size();
	for(int i=0; i<sz; i++)
	{
		for(int j=0; j<sz; j++)
		{
			orders[i][j] = 0;
		}
	}

	for(int i=0; i<sz; i++)
	{
		for(int j=0; j<sz; j++)
		{
			if(i==j)
				continue;
			if(plan[i].t > plan[j].t)
				continue;
			if ((plan[i].t == plan[j].t) && (i >= j))
				continue;
			// make sure that no instance of a single ground action
			//   runs concurrent with another instance of that action
			if(plan[i].id == plan[j].id) 
			{
				// [A pair with  A]
				// [A ==duration==> A]
				if(plan[i].part==ACTION_START && plan[j].part==ACTION_END)
				{
					if(plan[i].pair==j) // && plan[j].pair==i)
						orders[i][j] = 2; // order with distance=duration
					else
						orders[i][j] = 0; // no need to make an order
					continue;
				}
				// A] ...no [A or A] between...  [A
				// A] ==0==> [A
				if(plan[i].part==ACTION_END && plan[j].part==ACTION_START)
				{
					bool interrupted = false;
					for(int k=i+1; k<j; k++)
					{
						if(plan[k].id==plan[i].id && plan[k].part!=ACTION_OVERALL)
						{
							interrupted = true;
							break;
						}
					}
					if(!interrupted)
					{
						// FIXME: remove domain specific code
						//if(pDomain.name != "domain-tms-2-3-light")
							orders[i][j] = 1; // orders with distance=0 (without epsilon seperation)         CHANGED 3 TO 1
					}
					else
						orders[i][j] = 0; // no need to make an orders
					continue;
				}
			}

			const PAction *a = pProblem.pAllAction.GetActionById(plan[i].id);
			const PAction *b = pProblem.pAllAction.GetActionById(plan[j].id);
			const set<int> *aPre, *aAdd, *aDel;
			const set<int> *bPre, *bAdd, *bDel;
			if(plan[i].part==ACTION_START)
			{
				aPre = &a->conditionAtStart;
				aAdd = &a->addEffectAtStart;
				aDel = &a->delEffectAtStart;
			}
			else // if(plan[i].part==1)
			{
				aPre = &a->conditionAtEnd;
				aAdd = &a->addEffectAtEnd;
				aDel = &a->delEffectAtEnd;
			}
			if(plan[j].part==ACTION_START)
			{
				bPre = &b->conditionAtStart;
				bAdd = &b->addEffectAtStart;
				bDel = &b->delEffectAtStart;
			}
			else // if(plan[j].part==1)
			{
				bPre = &b->conditionAtEnd;
				bAdd = &b->addEffectAtEnd;
				bDel = &b->delEffectAtEnd;
			}

			//if(plan[i].t <= plan[j].t)
			//{
			orders[i][j] = 0; // default is no order
			if( Conflict(*aAdd, b->conditionOverAll)
				|| (plan[i].part==ACTION_END && Conflict(*bDel, a->conditionOverAll)) )
			{
				if ((plan[i].id==5) && (plan[j].id)==90)
					cout << endl << "*******************************";
				orders[i][j] = 1; // order without epsilon seperation    CHANGED 3 TO 1
			}
			if( Conflict(*aAdd, *bPre) || Conflict(*aAdd, *bDel)
				|| Conflict(*aDel, *bAdd) || Conflict(*bDel, *aPre)
				|| (plan[j].part==ACTION_START && Conflict(*aDel, b->conditionOverAll)))
			{
				orders[i][j] = 1; // order with epsilon seperation
			}
			//}
			//if(plan[i].t == plan[j].t)
			//{
			//	// consider that t is equal for both of events:
			//	// drive-truck] [load-truck : b is starting && a provides b's overall
			//	// [light-match [mend-fuse : a can be starting or ending
			//	if(plan[j].part==0 && Conflict(*aAdd, b->conditionOverAll))
			//		orders[i][j] = 1;
			//	// load-truck] [drive-truck : a is ending && b deletes a's overall
			//	// mend-fuse] light-match] : b can be starting or ending
			//	if(plan[i].part==1 && Conflict(*bDel, a->conditionOverAll))
			//		orders[i][j] = 1;
			//}
		}
	}
}

void PrintOrders(const vector<PlanEvent> &plan, const int **orders, const string ordersFileName)
{
	int sz = plan.size();
	ofstream orderFile(ordersFileName.c_str());
	orderFile << "     ";
	for(int i=0; i<sz; i++)
	{
		orderFile.width(3);
		orderFile << i+1;
	}
	orderFile << endl;
	for(int i=0; i<sz; i++)
	{
		orderFile.width(3);
		orderFile << i+1 << ": ";
		for(int j=0; j<sz; j++)
		{
			if(orders[i][j])
			{
				orderFile.width(3);
				orderFile << orders[i][j];
			}
			else
				orderFile << "---";
		}

		const PAction *a = pProblem.pAllAction.GetActionById(plan[i].id);
		orderFile << "  " << plan[i].t << ": (" << a->op->name;
		if(plan[i].part==ACTION_START)
			orderFile << "_S";
		else // if(plan[i].part==1)
			orderFile << "_E";
		for (int j=0; j<a->n_objects; j++)
		{
			orderFile << " " << pProblem.pObjects.objects[a->objects[j]];
		}
		orderFile << ")";

		orderFile << endl;
	}
}

void CreateAdjacencyOrders(const vector<PlanEvent> &plan, const int **orders, const double **weights, vector<DoubleEdge> &edges)
{
	int sz = plan.size();
	edges.clear();
	DoubleEdge e;
	// add edges for special start node
	for(int i=0; i<sz; i++)
	{
		e.u = 0;
		e.v = i+1;
		e.weight = 0;
		edges.push_back(e);
	}
	// add edges for other nodes
	for(int i=0; i<sz; i++)
	{
		for(int j=0; j<sz; j++)
		{
			if(orders[i][j] == 2)
			{
				e.u = i+1;
				e.v = j+1;
				e.weight = weights[i][j];
				edges.push_back(e);
				e.u = j+1;
				e.v = i+1;
				e.weight = weights[j][i];
				edges.push_back(e);
			}
			else if(orders[i][j] == 1)
			{
				e.u = i+1;
				e.v = j+1;
				e.weight = weights[i][j];
				edges.push_back(e);
			}
			else if(orders[i][j] != 0)
			{
				e.u = i+1;
				e.v = j+1;
				e.weight = 0;
				edges.push_back(e);
			}
		}
	}
}

void CalculateOrderWeights(const vector<PlanEvent> &plan, const int **orders, double **weights, double epsilon)
{
	int sz = plan.size();
	for(int i=0; i<sz; i++)
		for(int j=0; j<sz; j++)
			weights[i][j] = 0;
	for(int i=0; i<sz; i++)
	{
		for(int j=0; j<sz; j++)
		{
			if(orders[i][j]==2)
			{
				// FIXME: remove domain specific manual fixes:
				//if(pDomain.name == "satellite")
					//weights[j][i] = pProblem.pAllAction.GetActionById(plan[i].id)->duration / (float)100;
				//else if(pDomain.name == "pipesworld_strips")
					//weights[j][i] = pProblem.pAllAction.GetActionById(plan[i].id)->duration / (float)12;
				//else
					weights[j][i] = pProblem.pAllAction.GetActionById(plan[i].id)->duration;
				weights[i][j] = -weights[j][i];
			}
			else if(orders[i][j]==1) // epsilon seperation is necessary
			{
				weights[i][j] = -epsilon;
			}
		}
	}
}
