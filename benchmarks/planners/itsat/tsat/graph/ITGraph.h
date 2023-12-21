#ifndef ITGRAPH_H
#define ITGRAPH_H

#include <vector>
#include <set>
#include <climits> // for INT_MAX, INT_MIN
#include <stdexcept> // for overflow_error
using namespace std;

typedef pair<int,int> Mutex;

// forward declarations
class ITProp;
class ITAction;
class ITGraph;

// NOTE: "id" is defined as the index of action/proposition
//       in "actionList"/"propList" vectors of "ITGraph"
// SO: you must add every proposition you use in an ITAction
//     to the "propList" vector of "ITGraph" (beforehand or after)
//     otherwise "id" will be meaningless/wrong.

class ITProp
{
	static const int ID_MAX = 65535;
	int id;
	set<int> precondList, addList, delList;
	friend class ITGraph;

public:
	inline void AddPrecondAction(int a)	{ if(a>ID_MAX) throw overflow_error("ID overflow"); precondList.insert(a); }
	inline void AddAddAction(int a)	{ if(a>ID_MAX) throw overflow_error("ID overflow"); addList.insert(a); }
	inline void AddDelAction(int a) { if(a>ID_MAX) throw overflow_error("ID overflow"); delList.insert(a); }
	ITProp(void) {}
	~ITProp(void) {}
};

class ITAction
{
	static const int ID_MAX = 65535;
	int id;
	set<int> precondList, addList, delList;
	int origId, origPart;
	friend class ITGraph;

public:
	inline void AddPrecond(int p) { if(p>ID_MAX) throw overflow_error("ID overflow"); precondList.insert(p); }
	inline void AddAddEffect(int p) { if(p>ID_MAX) throw overflow_error("ID overflow"); addList.insert(p); }
	inline void AddDelEffect(int p) { if(p>ID_MAX) throw overflow_error("ID overflow"); delList.insert(p); }
	ITAction(int origId = -1, int origPart = -1)
		: origId(origId), origPart(origPart)
	{}
	~ITAction(void) {}
};

class ITGraph
{
	typedef unsigned short ID;
	typedef short LAYER;
	static const LAYER LAYER_MAX = SHRT_MAX;
	static const LAYER LAYER_MIN = SHRT_MIN;
	typedef char COUNTER;
	static const COUNTER COUNTER_MAX = CHAR_MAX;
	static const COUNTER COUNTER_MIN = CHAR_MIN;

	set< pair<ID,ID> > removedPropMutexes;
	set< pair<ID,ID> > removedActionMutexes;

	vector<ITAction> actionList;
	vector<ITProp> propList;

	void RemovePropMutex(int p, int q, LAYER layer);
	void RemoveActionMutex(int a, int b, LAYER layer);
	void InitDataStructures(float startTime, float availableTime);
	void UseInitialState(vector<int> &initState);

public:
	// just for readonly access to outside:
	vector< vector<COUNTER> > *ActionMutexCounter;
	vector< vector<LAYER> > *PropMutexElimLayer;
	vector<int> *ActionAddedOnLayer;
	vector<int> *PropAddedOnLayer;
	int Layers; // updated at the end of CreateGraph()
	// end

	inline void AddActionDefinition(ITAction &a) { a.id = actionList.size(); actionList.push_back(a); }
	inline void AddPropDefinition(ITProp &p) { p.id = propList.size(); propList.push_back(p); }
	void CreateGraph(vector<int> &initState, float availableTime);
	int GoalsLayer(vector<int> &goals);
	ITGraph(void)
		: ActionMutexCounter(NULL), PropMutexElimLayer(NULL)
		, ActionAddedOnLayer(NULL), PropAddedOnLayer(NULL)
		, Layers(-1)
	{}
	~ITGraph(void)
	{
		if(ActionMutexCounter) delete ActionMutexCounter;
		if(PropMutexElimLayer) delete PropMutexElimLayer;
		if(ActionAddedOnLayer) delete ActionAddedOnLayer;
		if(PropAddedOnLayer) delete PropAddedOnLayer;
	}
};

#endif
