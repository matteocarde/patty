#include "tsat/parser/ParserClasses.h"
#include <iostream>
#include <vector>
#include <set>
#include "tsat/utils.h"
#include "tsat/graph/ETGraph.h"
#define CheckForTimeOut() if(availableTime - (CPUTime() - startTime) < 0) throw runtime_error("Timeout during graph construction.")

using namespace std;

void ETGraph::CreateGraph(vector<int> &initState, float availableTime)
{
	float startTime = CPUTime();
	InitDataStructures(startTime, availableTime);
	UseInitialState(initState);
	LAYER layer = 0;
	while(true)
	{
		bool stop = true;

		set< pair<ID,ID> > mp;
		mp.swap(removedPropMutexes); // One stone Two birds !!
		if(!mp.empty())
			stop = false;
		for(set< pair<ID,ID> >::const_iterator itPP = mp.begin(); itPP != mp.end(); ++itPP)
		{
			CheckForTimeOut();
			RemovePropMutex(itPP->first, itPP->second, layer);
		}
		mp.clear();

		set< pair<ID,ID> > m;
		m.swap(removedActionMutexes); // One stone Two birds !!
		for(set< pair<ID,ID> >::const_iterator itAP = m.begin(); itAP != m.end(); ++itAP)
		{
			CheckForTimeOut();
			int L1 = LegalActionOnLayer(itAP->first, layer);
			int L2 = LegalActionOnLayer(itAP->second, layer);
			int t1 = (*ActionAddedOnLayer)[itAP->first];
			int t2 = (*ActionAddedOnLayer)[itAP->second];
			if(L1 == 1 && L2 == 1 && (itAP->first == itAP->second || (t1 != -1 && t2 != -1)))
			{
				RemoveActionMutex(itAP->first, itAP->second, layer);
				stop = false;
			}
			else
			{
				removedActionMutexes.insert(*itAP); // postpone
				//if(L1 == 0 || L2 == 0)
				if((L1 == 0 && t1 != -1) || (L2 == 0 && t2 != -1) || (itAP->first == itAP->second && L1 == 0))
					stop = false;
			}
		}
		m.clear();

		// INCREMENT LAYER NUMBER
		if(layer == LAYER_MAX)
			throw overflow_error("Overflow in number of layers");
		++ layer;

		if(stop)
			break;
	}
	Layers = layer;

	int nActions = actionList.size();
	for(int i=0; i<nActions; i+=2)
	{
		const ETAction &begin = actionList[i];
		const ETAction &end = actionList[i+1];
		if(end.delay == -1) // next actions are either NOOP or Overall
			break;
		int tbegin = (*ActionAddedOnLayer)[i];
		int tend = (*ActionAddedOnLayer)[i+1];
		if(tbegin != -1 && tbegin + end.delay != tend)
		{
			cout << endl << i << "\tbegin = " << tbegin << "\tend = " << tend
				<< "\tdur = " << end.delay << "\tactual = " << tend-tbegin;
		}
	}

}

int ETGraph::LegalActionOnLayer(int a, LAYER layer)
{
	const ETAction &A = actionList[a];
	if(A.delay == -1) // it is not end part of an action
		return 1; // legal
	int tbegin = (*ActionAddedOnLayer)[A.pairId];
	if(tbegin == -1) // its start is not added yet
		return -1; // illegal
	if(tbegin + A.delay > layer) // its start added already, but not enough layers has passed
		return 0; // will be legal in future layers
	return 1; // legal
}

void ETGraph::RemovePropMutex(int p, int q, LAYER layer)
{
	// p should be >=q
	if(p<q)
	{
		// swap p,q
		int pq = p;
		p = q;
		q = pq;
	}
	if((*PropMutexElimLayer)[p][q] != -1)
		return;
	(*PropMutexElimLayer)[p][q] = layer;
	if(p == q)
		(*PropAddedOnLayer)[p] = layer;

	ETProp &P = propList[p];
	ETProp &Q = propList[q];
	set<pair<ID,ID> > nodup;
	for(set<int>::const_iterator itP = P.precondList.begin(); itP != P.precondList.end(); ++itP)
	{
		for(set<int>::const_iterator itQ = Q.precondList.begin(); itQ != Q.precondList.end(); ++itQ)
		{
			// we use half below triangle of "ActionMutexCounter" matrix
			pair<ID,ID> ap;
			if(*itP >= *itQ)
			{
				ap.first = *itP;
				ap.second = *itQ;
			} else {
				ap.first = *itQ;
				ap.second = *itP;
			}
			if(nodup.find(ap) != nodup.end())
				continue;
			nodup.insert(ap);
			COUNTER &x = (*ActionMutexCounter)[ap.first][ap.second];
			if(x <= 0 || --x != 0)
				continue;
			x = -2;
			removedActionMutexes.insert(ap);
		}
	}
}

void ETGraph::RemoveActionMutex(int a, int b, LAYER layer)
{
	ETAction &A = actionList[a];
	ETAction &B = actionList[b];
	if(a == b)
		(*ActionAddedOnLayer)[a] = layer;
	for(set<int>::const_iterator itV1 = A.addList.begin(); itV1 != A.addList.end(); ++itV1)
	{
		pair<ID,ID> pp;
		for(set<int>::const_iterator itV2 = B.addList.begin(); itV2 != B.addList.end(); ++itV2)
		{
			if(*itV1 >= *itV2)
			{
				pp.first = *itV1;
				pp.second = *itV2;
			} else {
				pp.first = *itV2;
				pp.second = *itV1;
			}
			removedPropMutexes.insert(pp);
		}
	}
}

void ETGraph::InitDataStructures(float startTime, float availableTime)
{
	int nActions = actionList.size();
	int nProps = propList.size();
	PropAddedOnLayer = new vector<int> (nProps, -1); // use int instead of LAYER
	ActionAddedOnLayer = new vector<int> (nActions, -1); // use int instead of COUNTER
//	PropMutexElimLayer = new vector< vector<LAYER> > (nProps, vector<LAYER> (nProps, -1) );
//	ActionMutexCounter = new vector< vector<COUNTER> > (nActions, vector<COUNTER> (nActions, -1) );
	PropMutexElimLayer = new vector< vector<LAYER> > ();
	for(int i=0; i<nProps; i++)
	{
		PropMutexElimLayer->push_back(vector<LAYER> (i+1, -1));
	}
	ActionMutexCounter = new vector< vector<COUNTER> > ();
	for(int i=0; i<nActions; i++)
	{
		ActionMutexCounter->push_back(vector<COUNTER> (i+1, -1));
	}
	for(int i=0; i<nActions; i++)
	{
		CheckForTimeOut();
		ETAction &a = actionList[i];
		// we use half below triangle of "ActionMutexCounter" matrix
		// so we use "j<=i" instead of "j<nActions"
		for(int j=0; j<=i; j++)
		{
			ETAction &b = actionList[j];
			if(i != j)
			{
				if(ConflictCount(a.addList,b.delList) || ConflictCount(a.delList,b.addList)
					|| ConflictCount(a.delList,b.precondList) || ConflictCount(a.precondList,b.delList))
					continue; // makes them ethernal (static) mutex, since the count will remain -1
			}
			// dynamic mutex:
			int mutexCount = a.precondList.size() * b.precondList.size();
			int conf = ConflictCount(a.precondList, b.precondList);
			conf = conf*(conf-1)/2;
			mutexCount -= conf;
			if(mutexCount >= COUNTER_MAX)
				throw overflow_error("Overflow in number of mutexes between two actions");
			if(mutexCount == 0)
			{
				pair<ID,ID> ap;
				ap.first = i;
				ap.second = j;
				removedActionMutexes.insert(ap);
				mutexCount = -2;
			}
			(*ActionMutexCounter)[i][j] = mutexCount;
		}
	}
}

void ETGraph::UseInitialState(vector<int> &initState)
{
	for(vector<int>::const_iterator it1 = initState.begin(); it1 != initState.end(); ++it1)
	{
		pair<ID,ID> pp;
		for(vector<int>::const_iterator it2 = initState.begin(); it2 != it1; ++it2)
		{
			if(*it1 >= *it2)
			{
				pp.first = *it1;
				pp.second = *it2;
			} else {
				pp.first = *it2;
				pp.second = *it1;
			}
			removedPropMutexes.insert(pp);
		}
		pp.first = *it1;
		pp.second = *it1;
		removedPropMutexes.insert(pp);
	}
}

int ETGraph::GoalsLayer(vector<int> &goals)
{
	int nGoal = goals.size();
	int m = INT_MIN;
	for(int i=0; i<nGoal; ++i)
	{
		int p = goals[i];
		for(int j=0; j<nGoal; ++j)
		{
			int q = goals[j];
			int temp;
			if(p>=q)
				temp = (*PropMutexElimLayer)[p][q];
			else
				temp = (*PropMutexElimLayer)[q][p];
			if(temp == -1) // impossible if the problem is correctly defined
				return -2;
			if(temp>m)
				m = temp;
		}
	}
	return m;
}
