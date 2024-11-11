#include "tsat/alg2layer/NegativeCycle.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include <vector>
#include <iostream>
using namespace std;
using namespace nsSatLayer;
using namespace MyParser;

bool AB_Order(const PAction *a, const PAction *b, ActionPart aPart, ActionPart bPart)
{
	const set<int> *aPre, *aAdd, *aDel;
	const set<int> *bPre, *bAdd, *bDel;
	if(aPart==ACTION_START)
	{
		aPre = &a->conditionAtStart;
		aAdd = &a->addEffectAtStart;
		aDel = &a->delEffectAtStart;
	}
	else // if(plan[bef].part==1)
	{
		aPre = &a->conditionAtEnd;
		aAdd = &a->addEffectAtEnd;
		aDel = &a->delEffectAtEnd;
	}
	if(bPart==ACTION_START)
	{
		bPre = &b->conditionAtStart;
		bAdd = &b->addEffectAtStart;
		bDel = &b->delEffectAtStart;
	}
	else // if(plan[aft].part==1)
	{
		bPre = &b->conditionAtEnd;
		bAdd = &b->addEffectAtEnd;
		bDel = &b->delEffectAtEnd;
	}

	return Conflict(*aAdd, b->conditionOverAll)
		|| Conflict(*aAdd, *bPre) || Conflict(*aAdd, *bDel)
		|| Conflict(*aDel, *bAdd) || Conflict(*bDel, *aPre)
		|| (bPart==ACTION_END && Conflict(*bDel, a->conditionOverAll))
		|| (aPart==ACTION_START && Conflict(*aDel, b->conditionOverAll));
}

// FIXME: Mr. Feyzbakhsh's idea
int PruneNegativeCycle(const vector<PlanEvent> &plan, vector<int> &cycle, const double **weights)
{
	PlanEvent e;
	vector<int> newCycle;
	vector<bool> coupled;
	int pruneCount = 0;
	int sz = cycle.size();
	// remove lonely events:
	newCycle.push_back(cycle[0]);
	coupled.push_back(true);
	for(int i=1; i<sz-1; i++) // skip [FrameS && FrameE]
	{
		// we decrease cycle[i] by 1 because we added an special node to plan
		//    before we run bellman_ford()
		e = plan[cycle[i]-1];
		bool lonely = true;
		for(int j=0; j<sz; j++)
		{
			if(cycle[j]-1 == e.pair)
			{
				lonely = false;
				break;
			}
		}
		if(!lonely)
		{
			coupled.push_back(true);
			newCycle.push_back(cycle[i]);
		}
		else
		{
			int bef = cycle[i-1]-1;
			int aft = cycle[i+1]-1;
			const PAction *a = pProblem.pAllAction.GetActionById(plan[bef].id);
			const PAction *b = pProblem.pAllAction.GetActionById(plan[aft].id);
			// check that the cycle will not be broken
			if(!AB_Order(a, b, plan[bef].part, plan[aft].part))
			{
				coupled.push_back(false);
				newCycle.push_back(cycle[i]); // broken, so do not delete
			}
			else
				pruneCount++; // safe to delete
		}
	}
	coupled.push_back(true);
	newCycle.push_back(cycle[sz-1]);
	cycle.swap(newCycle);

	sz = cycle.size();
	// [FrameS Alone1 [AS AE] [BS BE] Alone2 [CS CE] Alone3 FrameE]
	//   0      1      2   3   4   5   6      7   8    9      10
	//
	for(int i=sz-2; i>=2; i -= coupled[i] ? 2 : 1)
	{
		if(!coupled[i])
			continue;
		int bef = cycle[i-2]-1;
		int st = cycle[i-1]-1; // was "= plan[nd].pair"
		int nd = cycle[i]-1;
		int aft = cycle[i+1]-1;

		// check that the cycle will not be broken
		const PAction *a = pProblem.pAllAction.GetActionById(plan[bef].id);
		const PAction *b = pProblem.pAllAction.GetActionById(plan[aft].id);
		if(!AB_Order(a, b, plan[bef].part, plan[aft].part))
			continue;

		// check that the cycle will remain negative
		double value = 0;
		for(int j=0; j<sz-1; j++)
		{
			if(cycle[j]-1 == nd || cycle[j]-1 == st)
				continue;
			value += weights[cycle[j]-1][cycle[j+1]-1];
		}
		value += weights[cycle[sz-1]-1][cycle[0]-1];
		if(value >= 0) // don't delete the pair
			continue;

		// so delete the pair
		newCycle.clear();
		for(int j=0; j<sz; j++)
		{
			if(cycle[j]-1 == nd || cycle[j]-1 == st)
				continue;
			newCycle.push_back(cycle[j]);
		}
		cycle.swap(newCycle);
		sz = cycle.size();
		pruneCount += 2;
	}
	return pruneCount;
}

void PrintNegativeCycle(const vector<PlanEvent> &plan, const vector<int> &cycle, const double **weights)
{
	int sz = cycle.size();
	for(int i=0; i<sz; i++)
	{
		// we decrease cycle[i] by 1 because we added an special node to plan
		//    before we run bellman_ford()
		int node, nodeNext;
		node = cycle[i]-1;
		if(i<sz-1)
			nodeNext = cycle[i+1]-1;
		else
			nodeNext = cycle[0]-1;
		const PAction *a = pProblem.pAllAction.GetActionById(plan[node].id);
		cout << plan[node].t << ": (" << a->op->name;
		if(plan[node].part==ACTION_START)
			cout << "_S";
		else // if(plan[i].part==1)
			cout << "_E";
		for (int j=0; j<a->n_objects; j++)
		{
			cout << " " << pProblem.pObjects.objects[a->objects[j]];
		}
		cout << ") :" << weights[node][nodeNext] << endl;
	}
}
