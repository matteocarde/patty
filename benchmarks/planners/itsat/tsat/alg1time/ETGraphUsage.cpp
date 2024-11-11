#include "tsat/alg1time/ETGraphUsage.h"
#include "tsat/graph/ETGraph.h"
#include "tsat/parser/ParserClasses.h"

using namespace MyParser;

void GraphInit(ETGraph &g)
{
	int nProps = pProblem.pAllProposition.size();
	int nActions = pProblem.pAllAction.size();

	// ADD PROPOSETIONS TO GRAPH
	for(vector<PProposition>::const_iterator it = pProblem.pAllProposition.all.begin();
		it != pProblem.pAllProposition.all.end(); ++it)
	{
		ETProp p;
		set<int>::const_iterator itA;
		// AtStart Event
		for(itA = it->conditionAtStart.begin(); itA != it->conditionAtStart.end(); ++itA)
		{
			p.AddPrecondAction((*itA) * 2);
		}
		for(itA = it->addEffectAtStart.begin(); itA != it->addEffectAtStart.end(); ++itA)
		{
			p.AddAddAction((*itA) * 2);
		}
		for(itA = it->delEffectAtStart.begin(); itA != it->delEffectAtStart.end(); ++itA)
		{
			p.AddDelAction((*itA) * 2);
		}
		// AtEnd Event
		for(itA = it->conditionAtEnd.begin(); itA != it->conditionAtEnd.end(); ++itA)
		{
			p.AddPrecondAction((*itA) * 2 + 1);
		}
		for(itA = it->addEffectAtEnd.begin(); itA != it->addEffectAtEnd.end(); ++itA)
		{
			p.AddAddAction((*itA) * 2 + 1);
		}
		for(itA = it->delEffectAtEnd.begin(); itA != it->delEffectAtEnd.end(); ++itA)
		{
			p.AddDelAction((*itA) * 2 + 1);
		}
		// NOOP
		int noop = nActions*2 + it->id;
		p.AddPrecondAction(noop);
		p.AddAddAction(noop);
		// OVERALL NOOP
		for(itA = it->conditionOverAll.begin(); itA != it->conditionOverAll.end(); ++itA)
		{
			noop = (*itA) + nActions*2 + nProps;
			p.AddPrecondAction(noop);
			p.AddAddAction(noop);
		}
		g.AddPropDefinition(p);
	}

	// ADD EVENTS(START,END) TO GRAPH
	for(vector<PAction>::const_iterator it = pProblem.pAllAction.all.begin();
		it != pProblem.pAllAction.all.end(); ++it)
	{
		int startEvent = it->id * 2;
		int endEvent = 1 + startEvent;
		int overallEvent = it->id + nActions*2 + nProps;
		int connector = nProps + it->id;

		ETAction as(endEvent), ae(startEvent, it->duration);
		set<int>::const_iterator itP;
		// AtStart Event
		for(itP = it->conditionAtStart.begin(); itP != it->conditionAtStart.end(); ++itP)
		{
			as.AddPrecond(*itP);
		}
		for(itP = it->addEffectAtStart.begin(); itP != it->addEffectAtStart.end(); ++itP)
		{
			as.AddAddEffect(*itP);
		}
		for(itP = it->delEffectAtStart.begin(); itP != it->delEffectAtStart.end(); ++itP)
		{
			as.AddDelEffect(*itP);
		}
		// AtEnd Event
		for(itP = it->conditionAtEnd.begin(); itP != it->conditionAtEnd.end(); ++itP)
		{
			ae.AddPrecond(*itP);
		}
		for(itP = it->addEffectAtEnd.begin(); itP != it->addEffectAtEnd.end(); ++itP)
		{
			ae.AddAddEffect(*itP);
		}
		for(itP = it->delEffectAtEnd.begin(); itP != it->delEffectAtEnd.end(); ++itP)
		{
			ae.AddDelEffect(*itP);
		}
		as.AddAddEffect(connector);
		ae.AddPrecond(connector);
		ae.AddDelEffect(connector);
		// Add AtStart and AtEnd Events to Graph
		g.AddActionDefinition(as);
		g.AddActionDefinition(ae);
		// "Connector" proposition:
		ETProp p;
		p.AddAddAction(startEvent); // start event
		p.AddPrecondAction(endEvent); // end event
		p.AddDelAction(endEvent); // end event
		p.AddAddAction(overallEvent); // overall event
		p.AddPrecondAction(overallEvent); // overall event
		g.AddPropDefinition(p);
	}

	// ADD NOOP ACTIONS TO GRAPH (FOR EACH PROPOSETION)
	// note that there is no need to iterate over pProblem.pAllPropositions.all
	// since we just need their "id"s which is [0,nProps-1]
	for(int i=0; i<nProps; ++i)
	{
		ETAction nop;
		nop.AddPrecond(i);
		nop.AddAddEffect(i);
		g.AddActionDefinition(nop);
	}

	// ADD OVERALL ACTIONS TO GRAPH (FOR EACH ACTION)
	for(vector<PAction>::const_iterator it = pProblem.pAllAction.all.begin();
		it != pProblem.pAllAction.all.end(); ++it)
	{
		ETAction o;
		int connector = nProps + it->id;
		o.AddPrecond(connector);
		o.AddAddEffect(connector);
		for(set<int>::const_iterator itP = it->conditionOverAll.begin(); itP != it->conditionOverAll.end(); ++itP)
		{
			o.AddPrecond(*itP);
		}
		g.AddActionDefinition(o);
	}
}

// just for debugging
void GraphPrintFactMutex(ETGraph &g)
{
	int nProps = pProblem.pAllProposition.size();

	cout << "PROPOSITION MUTEX" << endl;
	cout << "-----------------" << endl;
	for(int i=0; i<nProps; i++)
	{
		if((*g.PropAddedOnLayer)[i] == -1)
			continue;
		PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		for(int j=0; j<i; j++)
		{
			if((*g.PropAddedOnLayer)[j] == -1)
				continue;
			if((*g.PropMutexElimLayer)[i][j] <= -1)
			{
				PProposition *q = pProblem.pAllProposition.GetPropositionById(j);
				cout << "[" << (*g.PropMutexElimLayer)[i][j] << "]   " << i << "," << j << " : " << (*g.PropAddedOnLayer)[i] << " , " << p->ToFullString() << " -- " << (*g.PropAddedOnLayer)[j] << " , " << q->ToFullString() << endl;
			}
		}
	}
}

int GraphExtractFactMutex(ETGraph &g, vector< vector<Mutex> > *&fm, bool includeOveralls)
{
	int total = 0;

	int nProp = pProblem.pAllProposition.size();
	int nAction = pProblem.pAllAction.size();

	fm = new vector< vector<Mutex> > (g.Layers + 1);

	int EndRange = nProp;
	if(includeOveralls)
		EndRange += nAction;

	for(int i=0; i<EndRange; i++)
	{
		Mutex m;
		if((*g.PropAddedOnLayer)[i] == -1)
			continue;
		m.first = i;
		for(int j=0; j<i; j++)
		{
			if((*g.PropAddedOnLayer)[j] == -1)
				continue;
			int l = (*g.PropMutexElimLayer)[i][j];
			if(l==-1)
			{
				m.second = j;
				(*fm)[g.Layers].push_back(m);
				++ total;
			}
			else if (l>0)
			{
				m.second = j;
				(*fm)[l-1].push_back(m);
				++ total;
			}
		}
	}
	return total;
}
