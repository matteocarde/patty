#include "tsat/alg2layer/TimedPlan.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/parser/ParserClasses.h"
#include <set>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath> // for fabs(double)
using namespace std;
using namespace MyParser;
using namespace nsSatLayer;

// FIXME: bug on tms pfile03
int PruneTimedPlan(vector<PlanEvent> &plan)
{
	int nProp=pProblem.pAllProposition.size();
	int nAction=pProblem.pAllAction.size();
	bool *curs=new bool[nProp];
	set<int>::const_iterator it1, it2, it3;
	int pruneCount = 0;
	int pruneCount2=0;
	bool *canbedel=new bool[plan.size()];
	for (int j=0; j<plan.size(); j++)
	{
		//cout << plan[j-1].t << " " << plan[j].t << " " <<  plan[j-1].id << " " <<  plan[j].id << endl;
		canbedel[j]=false;
		if (j==0)
			continue;
		if ((plan[j-1].t>plan[j].t) || ((plan[j].t==plan[j-1].t) && (plan[j-1].id>plan[j].id)))
		{
			cout << endl << "PLAN IS NOT PROPERLY ORDERED: " << plan[j-1].t << " " << plan[j].t << " " <<  plan[j-1].id << " " <<  plan[j].id << endl;
			exit(0);
		}
	}
	bool found=true;
	while (found)
	{
		//cout << endl << pruneCount << endl;
		pruneCount=0;
		found=false;
		for (int j=0; j< plan.size(); j++)
		{
			for (int k=0; k<nProp; k++)
				curs[k]=false;
			for (int k=0; k<pProblem.initialState.size(); k++)
				curs[pProblem.initialState[k]]=true;
			if (canbedel[j])
				continue;
			bool valid=true;
			for (int k=0; (k<plan.size() && valid); k++)
			{
				if (canbedel[k])
					continue;
				if ((k==j) || (k==plan[j].pair))
					continue;
				if (plan[k].part==ACTION_START)
				{
					const PAction *a = pProblem.pAllAction.GetActionById(plan[k].id);
					for (it1=a->conditionAtStart.begin(); it1!=a->conditionAtStart.end(); it1++)
						if (!curs[*it1])
							valid=false;
					for (it1=a->conditionOverAll.begin(); it1!=a->conditionOverAll.end(); it1++)
						if (!curs[*it1])
							valid=false;
					for (it1=a->addEffectAtStart.begin(); it1!=a->addEffectAtStart.end(); it1++)
						curs[*it1]=true;
					for (it1=a->delEffectAtStart.begin(); it1!=a->delEffectAtStart.end(); it1++)
						curs[*it1]=false;
				}
				if (plan[k].part==ACTION_END)
				{
					const PAction *a = pProblem.pAllAction.GetActionById(plan[k].id);
					for (it1=a->conditionAtEnd.begin(); it1!=a->conditionAtEnd.end(); it1++)
						if (!curs[*it1])
							valid=false;
					for (it1=a->addEffectAtEnd.begin(); it1!=a->addEffectAtEnd.end(); it1++)
						curs[*it1]=true;
					for (it1=a->delEffectAtEnd.begin(); it1!=a->delEffectAtEnd.end(); it1++)
						curs[*it1]=false;
				}

			}
			for (int k=0; k<pProblem.goals.size(); k++)
				if (!curs[pProblem.goals[k]])
					valid=false;
			if (valid)
			{
				
				canbedel[j]=true;
				canbedel[plan[j].pair]=true;
				found=true;
				pruneCount+=2;
				pruneCount2++;
			}
		}
	
		int nprune=0;
		int j=plan.size()-1;
		while (nprune<pruneCount)
		{
			if (canbedel[j])
			{
				plan.erase(plan.begin()+j);
				nprune++;
			}
			j--;

		}
		for (int j=0; j<plan.size(); j++)
		{
			if (plan[j].part==ACTION_START)
				for (int k=j+1; k<plan.size(); k++)
					if (plan[j].id==plan[k].id)
					{
						plan[j].pair=k;
						plan[k].pair=j;
						break;
					}
		}
	}
/*
	int nPass = plan.size()/2;
	for(int pass=0; pass<nPass; pass++)
	{
		int sz = plan.size();
		vector<int> eventStatus; // 0:unknow  1:obligatory  2:useless
		for(int i=0; i<sz; i++)
		{
			eventStatus.push_back(0); // unknown
		}
		set<int> problemGoals;
		std::copy(pProblem.goals.begin(), pProblem.goals.end(), std::insert_iterator<set<int> >(problemGoals, problemGoals.end()));
		for(int i=0; i<sz-1; i++)
		//for(int i=sz-2; i>=0; i--)
		{
			if(plan[i].part == ACTION_END && eventStatus[plan[i].pair] == 1)
				continue; // no need to further check, this action is obligatory
			set<int> effects;
			const PAction *a = pProblem.pAllAction.GetActionById(plan[i].id);
			if(plan[i].part == ACTION_START)
				std::copy(a->addEffectAtStart.begin(), a->addEffectAtStart.end(), std::insert_iterator<set<int> >(effects, effects.end()));
			else
				std::copy(a->addEffectAtEnd.begin(), a->addEffectAtEnd.end(), std::insert_iterator<set<int> >(effects, effects.end()));
			// check if any of these effects are needed
			for(int j=0; j<sz && !effects.empty(); j++)
			{
				//if(j==i || (plan[j].doubleD < plan[i].doubleD && fabs(plan[i].doubleD - plan[j].doubleD)>0.00001))
				if ((j==i) || (((plan[j].t)*pProblem.pAllAction.size()*2+plan[j].id+plan[j].part)<((plan[i].t)*pProblem.pAllAction.size()*2+plan[i].id+plan[i].part)))
					continue;
				const PAction *b = pProblem.pAllAction.GetActionById(plan[j].id);
				set<int> beffects;
				set<int> bpreconds;
				if(plan[j].part == ACTION_START)
				{
					std::copy(b->addEffectAtStart.begin(), b->addEffectAtStart.end(), std::insert_iterator<set<int> >(beffects, beffects.end()));
					std::copy(b->delEffectAtStart.begin(), b->delEffectAtStart.end(), std::insert_iterator<set<int> >(beffects, beffects.end()));
					//if(fabs(plan[i].doubleD - plan[j].doubleD)>0.00001)
						std::copy(b->conditionAtStart.begin(), b->conditionAtStart.end(), std::insert_iterator<set<int> >(bpreconds, bpreconds.end()));
					std::copy(b->conditionOverAll.begin(), b->conditionOverAll.end(), std::insert_iterator<set<int> >(bpreconds, bpreconds.end()));
				}
				else
				{
					std::copy(b->addEffectAtEnd.begin(), b->addEffectAtEnd.end(), std::insert_iterator<set<int> >(beffects, beffects.end()));
					std::copy(b->delEffectAtEnd.begin(), b->delEffectAtEnd.end(), std::insert_iterator<set<int> >(beffects, beffects.end()));
					//if(fabs(plan[i].doubleD - plan[j].doubleD)>0.00001)
					{
						std::copy(b->conditionAtEnd.begin(), b->conditionAtEnd.end(), std::insert_iterator<set<int> >(bpreconds, bpreconds.end()));
						std::copy(b->conditionOverAll.begin(), b->conditionOverAll.end(), std::insert_iterator<set<int> >(bpreconds, bpreconds.end()));
					}
				}
				//for(vector<int>::const_iterator it = b->conditionOverAll.begin(); it != b->conditionOverAll.end(); ++it)
				//{
				//	bpreconds.insert(*it);
				//}
				set<int> result;
				std::set_intersection(effects.begin(), effects.end(), bpreconds.begin(), bpreconds.end(), std::insert_iterator<set<int> >(result, result.end()));
				if(!result.empty())
				{
					eventStatus[i] = 1; // obligatory
					break;
				}
				std::set_difference(effects.begin(), effects.end(), beffects.begin(), beffects.end(), std::insert_iterator<set<int> >(result, result.end()));
				effects = result;
			}
			// still unknown? check problem goals
			if(eventStatus[i] == 0)
			{
				// check if the event provides something for problem goals, that is not deleted or provided by later events
				if(!effects.empty())
				{
					set<int> result;
					std::set_difference(problemGoals.begin(), problemGoals.end(), effects.begin(), effects.end(), std::insert_iterator<set<int> >(result, result.end()));
					if(result.size() != problemGoals.size())
					{
						eventStatus[i] = 1; // obligatory
						problemGoals = result;
					}
					else
						eventStatus[i] = 2; // useless event
				}
				else
					eventStatus[i] = 2; // useless event
			}
			if(plan[i].part == ACTION_END && eventStatus[i] == 2 && eventStatus[plan[i].pair] == 2) // useless action
			{
				int st = plan[i].pair;
				int nd = i;
				plan.erase(plan.begin() + st);
				plan.erase(plan.begin() + nd-1); // -1 because st is deleted before
				for(vector<PlanEvent>::iterator it = plan.begin(); it != plan.end(); ++it)
				{
					if(it->pair > nd) // it means that "it->pair > st" also
						it->pair -= 2;
					else if(it->pair > st)
						it->pair --;
				}
				sz -= 2;
				pruneCount++;
				// for debugging purposes:
				//cout << "[" << st << " , " << nd << endl;
				//PrintFinalPlan(plan,"*");
				//getchar();
				break;
			}
		}
	}
	*/
	return pruneCount2;
}
