#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/graph/ITGraph.h"
#include "tsat/alg2layer/ITGraphUsage.h"
#include "tsat/alg2layer/FSM_General.h"
#include "tsat/alg2layer/TimedPlan.h"

#include "tsat/parser/ParserClasses.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/utils.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cfloat> // for DBL_MAX
using namespace std;
using namespace MyParser;
using namespace nsSatLayer;

bool Alg2Layer(AlgCommonParams p)
{
	//if(p.satsolver=="minisat")
	//	limitMemory(2*1024); // 2 GB
	if(p.satsolver!="minisat" && p.satsolver!="precosat")
		return false;

	ITGraph *g = NULL;
	vector< vector<Mutex> > *fact_mutex = NULL;
	vector<int> prop_layer;

	bool solutionFound = false;
	int solfoundStep = 1; // 1 => -2 => 3 => -4 => 5 ...
	int maxLookingAround = 30; // FIXME: move this to the program switches
	double bestMakeSpan = DBL_MAX;
	vector<SATResults *> elapsed;
	SatLayer *solver = NULL;
	SATResults *res = new SATResults;
	res->outcome = INDET;
	vector<vector<PlanEvent> > negcyclePool;
	int T = 0, planNumber = 0, restarts = 0;
	set<int> checkedT;
	double t2, t1;

	t1 = CPUTime();
	cout << "Domain: " << pDomain.name << " Objects: " << pProblem.pObjects.size() << endl;
	cout << "Predicates: " << pDomain.predicates.size() << " Operators: " << pDomain.operators.size() << endl;
	cout << "Propositions: " << pProblem.pAllProposition.size() << " Actions: " << pProblem.pAllAction.size() << endl;
	cout << "Time taken : " << t1 << " secs" << endl;

	if(p.graphUsage != 0) // if graph usage is enabled
	{
		cout << endl << "Constructing temporal planning graph:" << endl;
		g = new ITGraph();
		cout << "  1. Converting temporal to classical setting ..." << endl;
		GraphInit(*g);
		cout << "       Done." << endl;
		cout << "  2. Constructing the graph ..." << endl;
		try
		{
			g->CreateGraph(pProblem.initialState, p.AvailableTime - CPUTime());
			if(g->Layers == -1) // construction failed
			{
				delete g;
				g = NULL;
				p.graphUsage = 0;
			}
		}
		catch(const bad_alloc &e) // out of memory
		{
			cout << endl << "Out of memory exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "Ignoring the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
			t1 = CPUTime() - t1;
		}
		catch(const overflow_error &e) // ID or COUNTER or LAYER overflow
		{
			cout << endl << "Overflow exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "But considering the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
		}
		catch(const runtime_error &e) // timeout
		{
			// NOTE: we assume that the assigned time to g->CreateGraph() is less than total available time,
			//       otherwise we should abort the planner with a "throw;"
			string ewhat = e.what();
			if(ewhat != "Timeout during graph construction.") // Unhandled exception
				throw;
			cout << endl << "Timeout exception from g->CreateGraph(): " << e.what() << endl;
			cout << "Running the planner without planning graph analysis." << endl;
			cout << "But considering the time wasted on planning graph construction." << endl << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			delete g;
			g = NULL;
			p.graphUsage = 0;
		}
		if(g!=NULL) // construction was successful
		{
			cout << "       Done.\t# of Layers: " << g->Layers << endl;
			int nGoalLayer = g->GoalsLayer(pProblem.goals);
			cout << "       Goals first appear at " << nGoalLayer << "th Layer non-mutex." << endl;
			//if(p.TStart < nGoalLayer)

				//p.TStart = nGoalLayer;
			//GraphPrintFactMutex(*g);
			cout << "  3. Extracting mutexes between facts ...";
			int nFactMutex = GraphExtractFactMutex(*g, fact_mutex, p.graphUsage==2);
			cout << " done." << endl;
			cout << "       # of mutexes: " << nFactMutex << endl;
			prop_layer.swap(*g->PropAddedOnLayer);
			if(p.graphUsage == 1) // mutex between facts only
				prop_layer.resize(pProblem.pAllProposition.size());
			delete g;
			g = NULL;
			t2 = CPUTime();
			cout << "Time taken : " << t2-t1 << " secs.";
			cout << "Total time so far: " << t2 << " secs." << endl;
			t1 = t2;
		}
	}

	cout << endl << "Process started:" << endl << endl << flush;
	///////////////////////////////////////////////// New: Relevant Actions (Start)/////////////////////////////////////////////////////////////
	

	set<int>::const_iterator it1, it2, it3;
	
	int nProp = pProblem.pAllProposition.size();
	int nAction = pProblem.pAllAction.size();
	
	bool *relac= new bool[nAction];
	for (int j=0; j<nAction; j++)
		relac[j]=false;
	bool *relprop= new bool[nProp];
	for (int j=0; j<nProp; j++)
		relprop[j]=false;
	int *newp= new int [nProp];
	int nnewp=0;
	for (int j=0; j<pProblem.goals.size(); j++)
	{
		newp[nnewp]=pProblem.goals[j];
		nnewp++;
		relprop[pProblem.goals[j]]=true;
	}
	//cout << endl << "TAMAM   " << pProblem.goals[0] << endl;
	//exit(0);
	while (nnewp>0)
	{

		int p1=newp[nnewp-1];
		//cout << endl << p1 << endl;
		nnewp--;
		const PProposition *prop1 = pProblem.pAllProposition.GetPropositionById(p1);
		for (it1=prop1->addEffectAtStart.begin(); it1!=prop1->addEffectAtStart.end(); it1++)
		{
			if (!relac[*it1])
			{
				relac[*it1]=true;
				const PAction *a1=pProblem.pAllAction.GetActionById(*it1);
				for (it2=a1->conditionAtStart.begin(); it2!=a1->conditionAtStart.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
				for (it2=a1->conditionOverAll.begin(); it2!=a1->conditionOverAll.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
				for (it2=a1->conditionAtEnd.begin(); it2!=a1->conditionAtEnd.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
			}
		}
		for (it1=prop1->addEffectAtEnd.begin(); it1!=prop1->addEffectAtEnd.end(); it1++)
		{
			if (!relac[*it1])
			{
				relac[*it1]=true;
				const PAction *a1=pProblem.pAllAction.GetActionById(*it1);
				for (it2=a1->conditionAtStart.begin(); it2!=a1->conditionAtStart.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
				for (it2=a1->conditionOverAll.begin(); it2!=a1->conditionOverAll.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
				for (it2=a1->conditionAtEnd.begin(); it2!=a1->conditionAtEnd.end(); it2++)
				if (!relprop[*it2])
				{
					relprop[*it2]=true;
					newp[nnewp]=*it2;
					nnewp++;

				}
			}
		}
	}
	//cout << endl << "*" << endl;
	bool canbedel;
	for (int j=0; j<pProblem.initialState.size(); j++)
	if (relprop[pProblem.initialState[j]])
	{
		canbedel=false;
		const PProposition *prop1= pProblem.pAllProposition.GetPropositionById(pProblem.initialState[j]);
		for (it1=prop1->delEffectAtStart.begin(); ((it1!=prop1->delEffectAtStart.end()) && (!canbedel)); it1++)
			if (relac[*it1])
				canbedel=true;
		for (it1=prop1->delEffectAtEnd.begin(); ((it1!=prop1->delEffectAtEnd.end()) && (!canbedel)); it1++)
			if (relac[*it1])
				canbedel=true;
		if (!canbedel)
			relprop[pProblem.initialState[j]]=false;
	}
	int totalrel=0;
	for (int j=0; j<nAction; j++)
		if (relac[j])
			totalrel++;
	cout << endl << "Ration of Relevant Actions: " << double(totalrel)/nAction << endl;
	//exit(0);
	int *newacid= new int[nAction];
	int thisid=0;
	for (int j=0; j<nAction; j++)
	{
		if (!relac[j])
			continue;
		newacid[j]=thisid;
		thisid++;
	}
	int *newpropid= new int[nProp];
	thisid=0;
	for (int j=0; j<nProp; j++)
	{
		if (!relprop[j])
			continue;
		newpropid[j]=thisid;
		thisid++;
	}

	int *newvalac= new int[nAction];
	int nnewvalac=0;
	int *newvalprop= new int[nProp];
	int nnewvalprop=0;
	vector<MyParser::PAction>::iterator it=pProblem.pAllAction.all.begin();
	vector<MyParser::PAction> *newactions= new vector<MyParser::PAction>;
	//cout << endl << "**" << endl;
	while (it!=pProblem.pAllAction.all.end())
	{
		//cout << endl << (*it).id << endl;
		if (!relac[(*it).id])
		{
			it++;
			
			//it=pProblem.pAllAction.all.erase(it);
			continue;
			
		}
		
		//it++;
		//continue;
		nnewvalprop=0;
		set<int>::iterator it1=it->addEffectAtStart.begin();
		while (it1!=it->addEffectAtStart.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->addEffectAtStart.erase(it1);
			it1=it->addEffectAtStart.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->addEffectAtStart.insert(newvalprop[j]);

		nnewvalprop=0;
		it1=it->addEffectAtEnd.begin();
		while (it1!=it->addEffectAtEnd.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->addEffectAtEnd.erase(it1);
			it1=it->addEffectAtEnd.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->addEffectAtEnd.insert(newvalprop[j]);

		nnewvalprop=0;
		it1=it->delEffectAtStart.begin();
		while (it1!=it->delEffectAtStart.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->delEffectAtStart.erase(it1);
			it1=it->delEffectAtStart.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->delEffectAtStart.insert(newvalprop[j]);


		nnewvalprop=0;
		it1=it->delEffectAtEnd.begin();
		while (it1!=it->delEffectAtEnd.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->delEffectAtEnd.erase(it1);
			it1=it->delEffectAtEnd.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->delEffectAtEnd.insert(newvalprop[j]);

		nnewvalprop=0;
		it1=it->conditionAtStart.begin();
		while (it1!=it->conditionAtStart.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->conditionAtStart.erase(it1);
			it1=it->conditionAtStart.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->conditionAtStart.insert(newvalprop[j]);

		nnewvalprop=0;
		it1=it->conditionAtEnd.begin();
		while (it1!=it->conditionAtEnd.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}
			it->conditionAtEnd.erase(it1);
			it1=it->conditionAtEnd.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->conditionAtEnd.insert(newvalprop[j]);

		nnewvalprop=0;
		it1=it->conditionOverAll.begin();
		while (it1!=it->conditionOverAll.end())
		{
			
			if (relprop[*it1])
			{
				newvalprop[nnewvalprop]=newpropid[*it1];
				nnewvalprop++;
			}

			it->conditionOverAll.erase(it1);
			it1=it->conditionOverAll.begin();
		}
		for (int j=0; j<nnewvalprop; j++)
			it->conditionOverAll.insert(newvalprop[j]);
		newactions->push_back(*(pProblem.pAllAction.GetActionById((*it).id)));
		it++;
	}
	//cout << endl << "***" << endl;
	pProblem.pAllAction.all.clear();
	vector<MyParser::PAction>::iterator ittt=newactions->begin();
	int acid=0;
	while (ittt!=newactions->end())
	{
		(*ittt).id=acid;
		pProblem.pAllAction.all.push_back(*ittt);
		ittt++;
		acid++;
	}
	//exit(0);
	//cout << endl << "***" << endl;
	newactions->clear();
	vector<MyParser::PProposition> *newpropositions= new vector<MyParser::PProposition>;
	vector<MyParser::PProposition>::iterator itt=pProblem.pAllProposition.all.begin();
	while (itt!=pProblem.pAllProposition.all.end())
	{
		
		if (!relprop[(*itt).id])
		{
			itt++;
			//itt=pProblem.pAllProposition.all.erase(itt);
			continue;
		}

		//continue;
		nnewvalac=0;
		set<int>::iterator it1=itt->addEffectAtStart.begin();
		while (it1!=itt->addEffectAtStart.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->addEffectAtStart.erase(it1);
			it1=itt->addEffectAtStart.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->addEffectAtStart.insert(newvalac[j]);

		nnewvalac=0;
		it1=itt->addEffectAtEnd.begin();
		while (it1!=itt->addEffectAtEnd.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->addEffectAtEnd.erase(it1);
			it1=itt->addEffectAtEnd.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->addEffectAtEnd.insert(newvalac[j]);

		nnewvalac=0;
		it1=itt->delEffectAtStart.begin();
		while (it1!=itt->delEffectAtStart.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->delEffectAtStart.erase(it1);
			it1=itt->delEffectAtStart.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->delEffectAtStart.insert(newvalac[j]);


		nnewvalac=0;
		it1=itt->delEffectAtEnd.begin();
		while (it1!=itt->delEffectAtEnd.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->delEffectAtEnd.erase(it1);
			it1=itt->delEffectAtEnd.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->delEffectAtEnd.insert(newvalac[j]);

		nnewvalac=0;
		it1=itt->conditionAtStart.begin();
		while (it1!=itt->conditionAtStart.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->conditionAtStart.erase(it1);
			it1=itt->conditionAtStart.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->conditionAtStart.insert(newvalac[j]);

		nnewvalac=0;
		it1=itt->conditionAtEnd.begin();
		while (it1!=itt->conditionAtEnd.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->conditionAtEnd.erase(it1);
			it1=itt->conditionAtEnd.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->conditionAtEnd.insert(newvalac[j]);

		nnewvalac=0;
		it1=itt->conditionOverAll.begin();
		while (it1!=itt->conditionOverAll.end())
		{
			
			if (relac[*it1])
			{
				newvalac[nnewvalac]=newacid[*it1];
				nnewvalac++;
			}
			itt->conditionOverAll.erase(it1);
			it1=itt->conditionOverAll.begin();
		}
		for (int j=0; j<nnewvalac; j++)
			itt->conditionOverAll.insert(newvalac[j]);
		newpropositions->push_back(*(pProblem.pAllProposition.GetPropositionById((*itt).id)));
		itt++;
	}
	pProblem.pAllProposition.all.clear();
	vector<MyParser::PProposition>::iterator itttt=newpropositions->begin();
	int propid=0;
	while (itttt!=newpropositions->end())
	{
		(*itttt).id=propid;
		pProblem.pAllProposition.all.push_back(*itttt);
		itttt++;
		propid++;
	}
	//exit(0);
	//cout << endl << "***" << endl;
	newpropositions->clear();
		nnewvalprop=0;
		int atleastone=0;
		int *newinit= new int[nProp];
		int nnewinit=0;
		//for (int j=0; j<pProblem.initialState.size(); j++)
		//{
			
			//if (relprop[pProblem.initialState[j]])
			//{
				////pProblem.initialState[j]=newpropid[pProblem.initialState[j]];
				//atleastone=pProblem.initialState[j];
			//}
		//}
		for (int j=0; j<pProblem.initialState.size(); j++)
		{
			
			if (relprop[pProblem.initialState[j]])
			{
				newinit[nnewinit]=newpropid[pProblem.initialState[j]];
				nnewinit++;
				//pProblem.initialState[j]=newpropid[pProblem.initialState[j]];
				//atleastone=pProblem.initialState[j];
			}
			//else
				//pProblem.initialState[j]=newpropid[atleastone];
		}
		pProblem.initialState.clear();
		for (int j=0; j<nnewinit; j++)
			pProblem.initialState.push_back(newinit[j]);
		delete newinit;
		for (int j=0; j<pProblem.goals.size(); j++)
		{
			
			if (relprop[pProblem.goals[j]])
			{
				pProblem.goals[j]=newpropid[pProblem.goals[j]];
				//atleastone=pProblem.initialState[j];
			}
			else
			{
				cout << endl << "ERROR: Goals Deleted" << endl;
				exit(0);
			}
		}
	delete relac;
	delete relprop;
	delete newp;
	delete newacid;
	delete newpropid;
	delete newvalac;
	delete newvalprop;
	//cout << endl << double(totalrel)/nAction << endl;
	cout << endl << "Number of Actons: " << nAction<< "    Number of Propositions: " << nProp<< endl;
	//exit(0);	
	//pProblem.pAllAction.all.erase(
		//PProblem.pAllAction
	//exit(0);
	//cout << endl << pProblem.pAllAction.GetActionById(186)->conditionOverAll.size() << endl;
	//exit(0);
	//for (int j=0; j<pProblem.pAllAction.all.size(); j++)
		//cout << endl << pProblem.pAllAction.GetActionById(j)->ToFullString() << " ***** " << j << endl;
	//exit(0);
	///////////////////////////////////////////////// New: Relevant Actions (End)/////////////////////////////////////////////////////////////

	///////////////////////////////////////////////// New: New Graph/////////////////////////////////////////////////////////////
	nProp = pProblem.pAllProposition.size();
	nAction = pProblem.pAllAction.size();	
	cout << endl << "Number of Relevant Actons: " << nAction<< "    Number of Relevant Propositions: " << nProp<< endl;
	bool **mutextable = new bool*[nProp];
	short **nps=new short*[nProp];

	for (int j=0; j<nProp; j++)
	{
		
		nps[j]=new short[nAction];

		for (int k=0; k<nAction; k++)
		{
			const PAction *a1 = pProblem.pAllAction.GetActionById(k);
			nps[j][k]=(short)(a1->conditionAtStart.size());
		}

		const PProposition *p1 = pProblem.pAllProposition.GetPropositionById(j);
		//cout << endl << j << "    " << p1->delEffectAtStart.size() << endl;
		//if (j==176)
		//{
		//	cout << endl << j << "    " << p1->delEffectAtStart.size() << endl;
		//	exit(0);
		//}
		for (it1=p1->delEffectAtStart.begin(); it1!=p1->delEffectAtStart.end(); it1++)
			nps[j][*it1]++;

	}
	//cout << endl << nAction<< "    " << nProp<< endl;
	//exit(0);
	short **npd=new short*[nProp];
	for (int j=0; j<nProp; j++)
	{
		npd[j]=new short[nAction];

		for (int k=0; k<nAction; k++)
		{
			const PAction *a1 = pProblem.pAllAction.GetActionById(k);
			npd[j][k]=(short)(1+(a1->conditionOverAll.size()));
		}
	}
	short **npe=new short*[nProp];
	for (int j=0; j<nProp; j++)
	{
		npe[j]=new short[nAction];

		for (int k=0; k<nAction; k++)
		{
			const PAction *a1 = pProblem.pAllAction.GetActionById(k);
			npe[j][k]=(short)(1+(a1->conditionAtEnd.size()));
		}
		const PProposition *p1 = pProblem.pAllProposition.GetPropositionById(j);
		for (it1=p1->delEffectAtEnd.begin(); it1!=p1->delEffectAtEnd.end(); it1++)
			npe[j][*it1]++;	
	}

	short *npp=new short[nProp];
	for (int j=0; j<nProp; j++)
	{
		npp[j]=1;
	}
	short *nss=new short[nAction];
	for (int j=0; j<nAction; j++)
	{
		const PAction *a1 = pProblem.pAllAction.GetActionById(j);
		nss[j]=(short)(a1->conditionAtStart.size()*a1->conditionAtStart.size());
	}
	short *ndd=new short[nAction];
	for (int j=0; j<nAction; j++)
	{
		const PAction *a1 = pProblem.pAllAction.GetActionById(j);
		ndd[j]=(short)(2*a1->conditionOverAll.size()+a1->conditionOverAll.size()*a1->conditionOverAll.size());
	}
	short *nee=new short[nAction];
	for (int j=0; j<nAction; j++)
	{
		const PAction *a1 = pProblem.pAllAction.GetActionById(j);
		nee[j]=(short)(2*a1->conditionAtEnd.size()+a1->conditionAtEnd.size()*a1->conditionAtEnd.size());
	}
	for (int j=0; j<nProp; j++)
	{
		mutextable[j]=new bool[nProp+nAction+nAction];
		for (int k=0; k<nProp+nAction+nAction; k++)
			mutextable[j][k]=true;
			//mutextable[j][k]=false;
	}

	//int **newmux= new int*[nProp*nProp];
	//for (int j=0; j<nProp*nProp; j++)
	int **newmux= new int*[10000000];
	for (int j=0; j<10000000; j++)
	{
		newmux[j]=new int[2];
	}
	int nnewmux=0;

	//cout << endl;
	//cout << endl << nAction<< "    " << nProp<< endl;
	//exit(0);
	for (int j=0; j<pProblem.initialState.size(); ++j)
	{
		for (int k=j; k<pProblem.initialState.size(); ++k)
		{
			//cout << endl << pProblem.pAllProposition.GetPropositionById(pProblem.initialState[j])->ToFullString() << "    " << pProblem.pAllProposition.GetPropositionById(pProblem.initialState[k])->ToFullString() << endl;
			if (mutextable[pProblem.initialState[j]][pProblem.initialState[k]])
			{
			mutextable[pProblem.initialState[j]][pProblem.initialState[k]]=false;
			mutextable[pProblem.initialState[k]][pProblem.initialState[j]]=false;
			newmux[nnewmux][0]=pProblem.initialState[j];
			//cout << newmux[nnewmux][0] << "   ";
			newmux[nnewmux][1]=pProblem.initialState[k];
			//cout << newmux[nnewmux][1] << endl;
			nnewmux++;
			}
		}
	}
	//cout << endl << "TAMAM" << endl;
	//exit(0);
	bool muxflag;
	bool finished=true;
	for (int j=0; j<nAction; j++)
	{
					const PAction *a1 = pProblem.pAllAction.GetActionById(j);
					if (nss[j]==0)
					{
						for (it2=a1->addEffectAtStart.begin(); it2!=a1->addEffectAtStart.end(); it2++)
							for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
						{
							if (!mutextable[*it3][nProp+j])
								continue;
							mutextable[*it3][nProp+j]=false;
							newmux[nnewmux][0]=*it3;
							newmux[nnewmux][1]=nProp+j;
							nnewmux++;
						}
					}
					//delete a1;

	}
	for (int j=0; j<nAction; j++)
	{
					const PAction *a1 = pProblem.pAllAction.GetActionById(j);
					if (nee[j]==0)
					{
						for (it2=a1->addEffectAtEnd.begin(); it2!=a1->addEffectAtEnd.end(); it2++)
							for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}


					}
					//delete a1;
	}
	while (nnewmux>0)
	{
	while (nnewmux>0)
	{
		//cout << endl << npp[9] << "   " << nps[9][0] << "    " << npd[9][0]  <<"    " << npe[9][0] << endl;
		//cout << endl << nnewmux;
		//if (nnewmux>nProp*nProp)
		//{
			//cout << endl << "Too Many Mutexes";
			//exit(0);
		//}
		//cout << newmux[nnewmux-1][0] << "  " << newmux[nnewmux-1][1] << endl;
		finished=true;
		int p1=newmux[nnewmux-1][0];
		int p2=newmux[nnewmux-1][1];
		const PProposition *prop1 = pProblem.pAllProposition.GetPropositionById(p1);
		nnewmux--;
		if (p2<nProp)
		{
			//cout << endl << pProblem.pAllProposition.GetPropositionById(p1)->ToFullString() << "   " << p1 << "    " << pProblem.pAllProposition.GetPropositionById(p2)->ToFullString() << "    " << p2 << endl;
			if (p1==p2)
			{
				
				npp[p1]=0;
				for (int j=0; j<nAction; j++)
					if ((nss[j]==0) && (nps[p1][j]==0))
					{
						//cout << endl << "ERROR";
						//exit(0);
						const PAction *a1 = pProblem.pAllAction.GetActionById(j);
						for (it1=a1->addEffectAtStart.begin(); it1!=a1->addEffectAtStart.end(); ++it1)
						{
							if (!mutextable[p1][*it1])
								continue;
							mutextable[p1][*it1]=false;
							mutextable[*it1][p1]=false;
							newmux[nnewmux][0]=p1;
							newmux[nnewmux][1]=*it1;
							nnewmux++;
						}
						if (!mutextable[p1][nProp+j])
							continue;
						mutextable[p1][nProp+j]=false;
						newmux[nnewmux][0]=p1;
						newmux[nnewmux][1]=nProp+j;
						nnewmux++;
						//delete a1;
					}
				for (int j=0; j<nAction; j++)
					if ((ndd[j]==0) && (npd[p1][j]==0))
					{
						//cout << endl << "ERROR";
						//exit(0);

						if (!mutextable[p1][nProp+nAction+j])
							continue;
						mutextable[p1][nProp+nAction+j]=false;
						newmux[nnewmux][0]=p1;
						newmux[nnewmux][1]=nProp+nAction+j;
						nnewmux++;
					}
				for (int j=0; j<nAction; j++)
					if ((nee[j]==0) && (npe[p1][j]==0))
					{
						//cout << endl << "ERROR";
						//exit(0);
						const PAction *a1 = pProblem.pAllAction.GetActionById(j);
						for (it1=a1->addEffectAtEnd.begin(); it1!=a1->addEffectAtEnd.end(); ++it1)
						{
							if (!mutextable[p1][*it1])
								continue;
							mutextable[p1][*it1]=false;
							mutextable[*it1][p1]=false;
							newmux[nnewmux][0]=p1;
							newmux[nnewmux][1]=*it1;
							nnewmux++;
						}
						//delete a1;
					}
				for (it1=prop1->conditionAtStart.begin();it1!=prop1->conditionAtStart.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nss[*it1]--;
					if (nss[*it1]==0)
					{
						for (it2=a1->addEffectAtStart.begin(); it2!=a1->addEffectAtStart.end(); it2++)
							for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
						{
							if (!mutextable[*it3][nProp+*it1])
								continue;
							mutextable[*it3][nProp+*it1]=false;
							newmux[nnewmux][0]=*it3;
							newmux[nnewmux][1]=nProp+*it1;
							nnewmux++;
						}
						for (int j=0; j<nProp; j++)
							if ((npp[j]==0) && (nps[j][*it1]==0))
							{
								for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
								{
									if (!mutextable[j][*it3])
										continue;
									mutextable[*it3][j]=false;
									mutextable[j][*it3]=false;
									newmux[nnewmux][0]=j;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
								if (!mutextable[j][*it1+nProp])
									continue;
								mutextable[j][*it1+nProp]=false;
								newmux[nnewmux][0]=j;
								newmux[nnewmux][1]=*it1+nProp;
								nnewmux++;
							}

					}
					//delete a1;
				}


				for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
				{

					ndd[*it1]--;
					if (ndd[*it1]==0)
					{
						for (int j=0; j<nProp; j++)
							if ((npp[j]==0) && (npd[j][*it1]==0))
							{
								if (!mutextable[j][*it1+nProp+nAction])
									continue;
								mutextable[j][*it1+nProp+nAction]=false;
								newmux[nnewmux][0]=j;
								newmux[nnewmux][1]=*it1+nProp+nAction;
								nnewmux++;
							}

					}
				}


				for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nee[*it1]--;
					if (nee[*it1]==0)
					{
						for (it2=a1->addEffectAtEnd.begin(); it2!=a1->addEffectAtEnd.end(); it2++)
							for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (int j=0; j<nProp; j++)
							if ((npp[j]==0) && (npe[j][*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[j][*it3])
										continue;
									mutextable[*it3][j]=false;
									mutextable[j][*it3]=false;
									newmux[nnewmux][0]=j;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
							}

					}
					//delete a1;
				}

				for (it1=prop1->conditionAtStart.begin();it1!=prop1->conditionAtStart.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nps[p1][*it1]--;
					if (nps[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (nss[*it1]==0))
							{
								for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
								{
									if (!mutextable[p1][*it3])
										continue;
									mutextable[*it3][p1]=false;
									mutextable[p1][*it3]=false;
									newmux[nnewmux][0]=p1;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
								if (!mutextable[p1][nProp+*it1])
									continue;
								mutextable[p1][nProp+*it1]=false;
								newmux[nnewmux][0]=p1;
								newmux[nnewmux][1]=*it1+nProp;
								nnewmux++;
							}

					}
					//delete a1;
				}
				for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npd[p1][*it1]--;
					if (npd[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (ndd[*it1]==0))
							{

								if (!mutextable[p1][nAction+nProp+*it1])
									continue;
								mutextable[p1][nAction+nProp+*it1]=false;
								newmux[nnewmux][0]=p1;
								newmux[nnewmux][1]=*it1+nProp+nAction;
								nnewmux++;
							}

					}
					//delete a1;
				}
				for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npe[p1][*it1]--;
					if (npe[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (nee[*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[p1][*it3])
										continue;
									mutextable[*it3][p1]=false;
									mutextable[p1][*it3]=false;
									newmux[nnewmux][0]=p1;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}

							}

					}
					//delete a1;
				}				

				
			}
			else //p1!=p2
			{
				const PProposition *prop1 = pProblem.pAllProposition.GetPropositionById(p1);
				const PProposition *prop2 = pProblem.pAllProposition.GetPropositionById(p2);
				int *aclist= new int[nAction];
				int naclist=0;
				for (it1=prop1->conditionAtStart.begin();it1!=prop1->conditionAtStart.end(); it1++)
					for (it2=prop2->conditionAtStart.begin();it2!=prop2->conditionAtStart.end(); it2++)
						if (*it1==*it2)
						{
							aclist[naclist]=*it1;
							naclist++;
						}


				for (int j=0; j<naclist; j++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(aclist[j]);
					nss[aclist[j]]--;
					nss[aclist[j]]--;
					if (nss[aclist[j]]==0)
					{
						for (it2=a1->addEffectAtStart.begin(); it2!=a1->addEffectAtStart.end(); it2++)
							for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
						{
							if (!mutextable[*it3][nProp+aclist[j]])
								continue;
							mutextable[*it3][nProp+aclist[j]]=false;
							newmux[nnewmux][0]=*it3;
							newmux[nnewmux][1]=nProp+aclist[j];
							nnewmux++;
						}
						for (int k=0; k<nProp; k++)
							if ((npp[k]==0) && (nps[k][aclist[j]]==0))
							{
								for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
								{
									if (!mutextable[k][*it3])
										continue;
									mutextable[*it3][k]=false;
									mutextable[k][*it3]=false;
									newmux[nnewmux][0]=k;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
								if (!mutextable[k][aclist[j]+nProp])
									continue;
								mutextable[k][aclist[j]+nProp]=false;
								newmux[nnewmux][0]=k;
								newmux[nnewmux][1]=aclist[j]+nProp;
								nnewmux++;
							}

					}
					//delete a1;
				}

				naclist=0;
				for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
					for (it2=prop2->conditionOverAll.begin();it2!=prop2->conditionOverAll.end(); it2++)
						if (*it1==*it2)
						{
							aclist[naclist]=*it1;
							naclist++;
						}

				for (int j=0; j<naclist; j++)
				{

					ndd[aclist[j]]--;
					ndd[aclist[j]]--;
					if (ndd[aclist[j]]==0)
					{
						for (int k=0; k<nProp; k++)
							if ((npp[k]==0) && (npd[k][aclist[j]]==0))
							{
								if (!mutextable[k][aclist[j]+nProp+nAction])
									continue;
								mutextable[k][aclist[j]+nProp+nAction]=false;
								newmux[nnewmux][0]=k;
								newmux[nnewmux][1]=aclist[j]+nProp+nAction;
								nnewmux++;
							}

					}
				}

				naclist=0;
				for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
					for (it2=prop2->conditionAtEnd.begin();it2!=prop2->conditionAtEnd.end(); it2++)
						if (*it1==*it2)
						{
							aclist[naclist]=*it1;
							naclist++;
						}
				for (int j=0; j<naclist; j++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(aclist[j]);
					nee[aclist[j]]--;
					nee[aclist[j]]--;
					if (nee[aclist[j]]==0)
					{
						for (it2=a1->addEffectAtEnd.begin(); it2!=a1->addEffectAtEnd.end(); it2++)
							for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (int k=0; k<nProp; j++)
							if ((npp[k]==0) && (npe[k][*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[k][*it3])
										continue;
									mutextable[*it3][k]=false;
									mutextable[k][*it3]=false;
									newmux[nnewmux][0]=k;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
							}

					}
					//delete a1;
				}

				for (it1=prop2->conditionAtStart.begin();it1!=prop2->conditionAtStart.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nps[p1][*it1]--;
					if (nps[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (nss[*it1]==0))
							{
								for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
								{
									if (!mutextable[p1][*it3])
										continue;
									mutextable[*it3][p1]=false;
									mutextable[p1][*it3]=false;
									newmux[nnewmux][0]=p1;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
								if (!mutextable[p1][nProp+*it1])
									continue;
								mutextable[p1][nProp+*it1]=false;
								newmux[nnewmux][0]=p1;
								newmux[nnewmux][1]=*it1+nProp;
								nnewmux++;
							}

					}
					//delete a1;
				}

				for (it1=prop1->conditionAtStart.begin();it1!=prop1->conditionAtStart.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nps[p2][*it1]--;
					if (nps[p2][*it1]==0)
					{


							if ((npp[p2]==0) && (nss[*it1]==0))
							{
								for (it3=a1->addEffectAtStart.begin(); it3!=a1->addEffectAtStart.end(); it3++)
								{
									if (!mutextable[p2][*it3])
										continue;
									mutextable[*it3][p2]=false;
									mutextable[p2][*it3]=false;
									newmux[nnewmux][0]=p2;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
								if (!mutextable[p2][nProp+*it1])
									continue;
								mutextable[p2][nProp+*it1]=false;
								newmux[nnewmux][0]=p2;
								newmux[nnewmux][1]=*it1+nProp;
								nnewmux++;
							}

					}
					//delete a1;
				}


				for (it1=prop2->conditionOverAll.begin();it1!=prop2->conditionOverAll.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npd[p1][*it1]--;
					if (npd[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (ndd[*it1]==0))
							{

								if (!mutextable[p1][nAction+nProp+*it1])
									continue;
								mutextable[p1][nAction+nProp+*it1]=false;
								newmux[nnewmux][0]=p1;
								newmux[nnewmux][1]=*it1+nProp+nAction;
								nnewmux++;
							}

					}
					//delete a1;
				}
				for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npd[p2][*it1]--;
					if (npd[p2][*it1]==0)
					{


							if ((npp[p2]==0) && (ndd[*it1]==0))
							{

								if (!mutextable[p2][nAction+nProp+*it1])
									continue;
								mutextable[p2][nAction+nProp+*it1]=false;
								newmux[nnewmux][0]=p2;
								newmux[nnewmux][1]=*it1+nProp+nAction;
								nnewmux++;
							}

					}
					//delete a1;
				}

				for (it1=prop2->conditionAtEnd.begin();it1!=prop2->conditionAtEnd.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npe[p1][*it1]--;
					if (npe[p1][*it1]==0)
					{


							if ((npp[p1]==0) && (nee[*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[p1][*it3])
										continue;
									mutextable[*it3][p1]=false;
									mutextable[p1][*it3]=false;
									newmux[nnewmux][0]=p1;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}

							}

					}
					//delete a1;
				}

				for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
				{
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					npe[p2][*it1]--;
					if (npe[p2][*it1]==0)
					{


							if ((npp[p2]==0) && (nee[*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[p2][*it3])
										continue;
									mutextable[*it3][p2]=false;
									mutextable[p2][*it3]=false;
									newmux[nnewmux][0]=p2;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}

							}

					}
					//delete a1;
				}
				//delete prop1;
				//delete prop2;
			}
		}
		else if (p2>=nProp+nAction)
		{
				for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
				{
					if (*it1!=p2-nProp-nAction)
						continue;
					const PAction *a1 = pProblem.pAllAction.GetActionById(*it1);
					nee[*it1]--;
					nee[*it1]--;
					if (nee[*it1]==0)
					{
						for (it2=a1->addEffectAtEnd.begin(); it2!=a1->addEffectAtEnd.end(); it2++)
							for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
							{
								if (!mutextable[*it2][*it3])
									continue;
								mutextable[*it3][*it2]=false;
								mutextable[*it2][*it3]=false;
								newmux[nnewmux][0]=*it2;
								newmux[nnewmux][1]=*it3;
								nnewmux++;
							}
						for (int j=0; j<nProp; j++)
							if ((npp[j]==0) && (npe[j][*it1]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[j][*it3])
										continue;
									mutextable[*it3][j]=false;
									mutextable[j][*it3]=false;
									newmux[nnewmux][0]=j;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}
							}

					}
					//delete a1;
				}
				//for (it1=prop1->conditionAtEnd.begin();it1!=prop1->conditionAtEnd.end(); it1++)
				//{
					//if (*it1!=p2-nProp-nAction)
						//continue;
					int p2ac=p2-nProp-nAction;
					const PAction *a1 = pProblem.pAllAction.GetActionById(p2ac);
					npe[p1][p2ac]--;
					if (npe[p1][p2ac]==0)
					{


							if ((npp[p1]==0) && (nee[p2ac]==0))
							{
								for (it3=a1->addEffectAtEnd.begin(); it3!=a1->addEffectAtEnd.end(); it3++)
								{
									if (!mutextable[p1][*it3])
										continue;
									mutextable[*it3][p1]=false;
									mutextable[p1][*it3]=false;
									newmux[nnewmux][0]=p1;
									newmux[nnewmux][1]=*it3;
									nnewmux++;
								}

							}

					}
					//delete a1;
				//}				

		}

		else
		{
				for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
				{
					if (*it1!=p2-nProp)
						continue;
					int p2ac=p2-nProp;
					ndd[p2ac]--;
					ndd[p2ac]--;
					if (ndd[p2ac]==0)
					{
						for (int j=0; j<nProp; j++)
							if ((npp[j]==0) && (npd[j][p2ac]==0))
							{
								if (!mutextable[j][p2ac+nProp+nAction])
									continue;
								mutextable[j][p2ac+nProp+nAction]=false;
								newmux[nnewmux][0]=j;
								newmux[nnewmux][1]=p2ac+nProp+nAction;
								nnewmux++;
							}

					}
				}
				//for (it1=prop1->conditionOverAll.begin();it1!=prop1->conditionOverAll.end(); it1++)
				//{
					//if (*it1!=p2-nProp)
						//continue;
					int p2ac=p2-nProp;
					const PAction *a1 = pProblem.pAllAction.GetActionById(p2ac);
					npd[p1][p2ac]--;

					if (npd[p1][p2ac]==0)
					{


							if ((npp[p1]==0) && (ndd[p2ac]==0))
							{

								if (!mutextable[p1][nAction+nProp+p2ac])
									continue;
								mutextable[p1][nAction+nProp+p2ac]=false;
								newmux[nnewmux][0]=p1;
								newmux[nnewmux][1]=p2ac+nProp+nAction;
								nnewmux++;
							}

					}
					//delete a1;
				//}

		}


		//delete prop1;
	}
	/*for (int j=0; j<nProp; j++)
		for (int k=0; k<nAction; k++)
		{
			if ((npd[j][k]==0) && (nps[j][k]>0))
				cout << endl << "ERROR:   " <<pProblem.pAllProposition.GetPropositionById(j)->ToFullString() << "     " <<pProblem.pAllAction.GetActionById(k)->ToFullString() <<   endl;
			if ((npd[j][k]<0))
				cout << endl << "ERROR:   " <<pProblem.pAllProposition.GetPropositionById(j)->ToFullString() << "     " <<pProblem.pAllAction.GetActionById(k)->ToFullString() <<   endl;
		}*/
	//exit(0);
	for (int j=0; j<pProblem.pAllAction.size(); j++)
	{
		if (ndd[j]>0)
			continue;
		for (int k=0; k<pProblem.pAllAction.size(); k++)
		{
			if (k==j)
				continue;
			bool ccc=true;
			const PAction *a1 = pProblem.pAllAction.GetActionById(k);
			const PAction *a2 = pProblem.pAllAction.GetActionById(j);
			if (nss[k]>0)
				continue;
			for (it1=a1->conditionAtStart.begin(); it1!=a1->conditionAtStart.end(); it1++)
			{
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;

			
			}

			if (!ccc)
				continue;
			for (it1=a1->conditionOverAll.begin(); it1!=a1->conditionOverAll.end(); it1++)
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->delEffectAtStart.begin(); it1!=a1->delEffectAtStart.end(); it1++)
				for (it2=a2->conditionOverAll.begin(); it2!=a2->conditionOverAll.end(); it2++)
					if (*it1==*it2)
						ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->addEffectAtStart.begin(); it1!=a1->addEffectAtStart.end(); it1++)
			{
							if (!mutextable[*it1][nAction+nProp+j])
								continue;
							//cout << endl << "NEW MUTEXES   " << pProblem.pAllAction.GetActionById(k)->ToFullString()<< "    " <<pProblem.pAllProposition.GetPropositionById(*it1)->ToFullString() << "     " << k << "     " <<pProblem.pAllAction.GetActionById(j)->ToFullString() << "     " << j<<  endl;
							mutextable[*it1][nAction+nProp+j]=false;
							newmux[nnewmux][0]=*it1;
							newmux[nnewmux][1]=j+nProp+nAction;
							nnewmux++;
			}
			if (nee[k]>0)
				continue;
			if (ndd[k]>0)
				continue;
			for (it1=a1->delEffectAtEnd.begin(); it1!=a1->delEffectAtEnd.end(); it1++)
				for (it2=a2->conditionOverAll.begin(); it2!=a2->conditionOverAll.end(); it2++)
					if (*it1==*it2)
						ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->conditionAtEnd.begin(); it1!=a1->conditionAtEnd.end(); it1++)
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->conditionOverAll.begin(); it1!=a1->conditionOverAll.end(); it1++)
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->addEffectAtEnd.begin(); it1!=a1->addEffectAtEnd.end(); it1++)
			{
							if (!mutextable[*it1][nAction+nProp+j])
								continue;
							//cout << endl << "NEW MUTEXES****" << pProblem.pAllAction.GetActionById(k)->ToFullString()<< "    " <<pProblem.pAllProposition.GetPropositionById(*it1)->ToFullString() << "     " << k << "     " <<pProblem.pAllAction.GetActionById(j)->ToFullString() << "     " << j<<  endl;
							mutextable[*it1][nAction+nProp+j]=false;
							newmux[nnewmux][0]=*it1;
							newmux[nnewmux][1]=j+nProp+nAction;
							nnewmux++;
			}
		}
		/*for (int k=0; k<pProblem.pAllAction.size(); k++)
		{

			bool ccc=true;
			const PAction *a1 = pProblem.pAllAction.GetActionById(k);
			const PAction *a2 = pProblem.pAllAction.GetActionById(j);
			if (nee[k]>0)
				continue;
			for (it1=a1->conditionAtEnd.begin(); it1!=a1->conditionAtEnd.end(); it1++)
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->conditionOverAll.begin(); it1!=a1->conditionOverAll.end(); it1++)
				if ((npp[*it1]>0) || (npd[*it1][j]>0))
					ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->delEffectAtEnd.begin(); it1!=a1->delEffectAtEnd.end(); it1++)
				for (it2=a2->conditionOverAll.begin(); it2!=a2->conditionOverAll.end(); it2++)
					if (*it1==*it2)
						ccc=false;
			if (!ccc)
				continue;
			for (it1=a1->addEffectAtEnd.begin(); it1!=a1->addEffectAtEnd.end(); it1++)
			{
							if (!mutextable[*it1][nAction+nProp+j])
								continue;
							mutextable[*it1][nAction+nProp+j]=false;
							newmux[nnewmux][0]=*it1;
							newmux[nnewmux][1]=j+nProp+nAction;
							nnewmux++;
			}
		}*/
	}
	}
	/*for (int j=0; j<nProp; j++)
		for (int k=0; k<nProp; k++)
			if (mutextable[j][k])
				cout << endl << j << "   " << k;*/
	//exit(0);
	////////////////////////////NEW: COMPRESSING(Start) ////////////////////////////////////////////////////////////////////////////////////
	/*cout << endl << nAction << "    " << nProp;
	for (int k=0; k<pProblem.pAllAction.size(); k++)
		cout << endl << pProblem.pAllAction.GetActionById(k)->ToFullString();
	exit(0);*/
	cout << endl << "COMPRESSION STARTED";
	bool *compress=new bool[nAction];
	for (int j=0; j<nAction; j++)
		compress[j]=true;
		//compress[j]=false;
	
	bool thiscom;
	bool canapplys;
	bool canapplye;
	const PAction *com;
	const PAction *interfere;
	const PProposition *interp;
	//cout << endl;
	for (int j=0; j<nAction; j++)
	{
		//cout << j << "    ";
		com = pProblem.pAllAction.GetActionById(j);
		thiscom=true;
		for (int k=0; ((k<nAction) && (thiscom)); k++)
		if (j!=k)
		{
			interfere = pProblem.pAllAction.GetActionById(k);
			canapplys=true;
			canapplye=true;
			for (it1=interfere->conditionAtStart.begin(); ((it1!=interfere->conditionAtStart.end()) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "*  ";
			for (it1=interfere->conditionOverAll.begin(); ((it1!=interfere->conditionOverAll.end()) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "**  ";
			for (it1=interfere->addEffectAtStart.begin(); ((it1!=interfere->addEffectAtStart.end()) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "***  ";
			if (canapplys)
			{
				for (it1=com->addEffectAtStart.begin(); ((it1!=com->addEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->conditionAtStart.begin(); ((it2!=interfere->conditionAtStart.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***+  ";
				for (it1=com->addEffectAtStart.begin(); ((it1!=com->addEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->conditionOverAll.begin(); ((it2!=interfere->conditionOverAll.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***++  ";
				for (it1=com->delEffectAtStart.begin(); ((it1!=com->delEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->addEffectAtStart.begin(); ((it2!=interfere->addEffectAtStart.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***+++  ";
				for (it1=interfere->delEffectAtStart.begin(); ((it1!=interfere->delEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=com->conditionAtStart.begin(); ((it2!=com->conditionAtStart.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
			}
			//cout << "****  ";
			canapplys=true;


			for (it1=interfere->conditionAtEnd.begin(); (((it1!=interfere->conditionAtEnd.end()) && (thiscom)) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "*  ";
			for (it1=interfere->conditionOverAll.begin(); (((it1!=interfere->conditionOverAll.end()) && (thiscom)) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "**  ";
			for (it1=interfere->addEffectAtEnd.begin(); (((it1!=interfere->addEffectAtEnd.end()) && (thiscom)) && (canapplys)); it1++)
				if (npd[*it1][j]>0)
					canapplys=false;
			//cout << "***  ";
			if (canapplys)
			{
				for (it1=com->addEffectAtStart.begin(); ((it1!=com->addEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->conditionAtEnd.begin(); ((it2!=interfere->conditionAtEnd.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***+  ";
				for (it1=com->addEffectAtStart.begin(); ((it1!=com->addEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->conditionOverAll.begin(); ((it2!=interfere->conditionOverAll.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***++  ";
				for (it1=com->delEffectAtStart.begin(); ((it1!=com->delEffectAtStart.end()) && (thiscom)); it1++)
					for (it2=interfere->addEffectAtEnd.begin(); ((it2!=interfere->addEffectAtEnd.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
				//cout << "***+++  ";
				for (it1=interfere->delEffectAtEnd.begin(); ((it1!=interfere->delEffectAtEnd.end()) && (thiscom)); it1++)
					for (it2=com->conditionAtStart.begin(); ((it2!=com->conditionAtStart.end()) && (canapplys)); it2++)
						if (*it1==*it2)
							thiscom=false;
			}
		}
		if (!thiscom)
		{
			thiscom=true;
			for (int k=0; ((k<nAction) && (thiscom)); k++)
			if (j!=k)
			{
				interfere = pProblem.pAllAction.GetActionById(k);
				canapplys=true;
				canapplye=true;
				for (it1=interfere->conditionAtStart.begin(); ((it1!=interfere->conditionAtStart.end()) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "*  ";
				for (it1=interfere->conditionOverAll.begin(); ((it1!=interfere->conditionOverAll.end()) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "**  ";
				for (it1=interfere->addEffectAtStart.begin(); ((it1!=interfere->addEffectAtStart.end()) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "***  ";
				if (canapplys)
				{
					for (it1=interfere->addEffectAtStart.begin(); ((it1!=interfere->addEffectAtStart.end()) && (canapplys)); it1++)
						for (it2=com->conditionAtEnd.begin(); ((it2!=com->conditionAtEnd.end()) && (thiscom)); it2++)
							if (*it1==*it2)
								thiscom=false;


					for (it1=com->delEffectAtEnd.begin(); ((it1!=com->delEffectAtEnd.end()) && (thiscom)); it1++)
						for (it2=interfere->conditionOverAll.begin(); ((it2!=interfere->conditionOverAll.end()) && (canapplys)); it2++)
							if (*it1==*it2)
								thiscom=false;
					for (it1=com->delEffectAtEnd.begin(); ((it1!=com->delEffectAtEnd.end()) && (thiscom)); it1++)
						for (it2=interfere->conditionAtStart.begin(); ((it2!=interfere->conditionAtStart.end()) && (canapplys)); it2++)
							if (*it1==*it2)
								thiscom=false;

					for (it1=interfere->delEffectAtStart.begin(); ((it1!=interfere->delEffectAtStart.end()) && (canapplys)); it1++)
						for (it2=com->addEffectAtStart.begin(); ((it2!=com->addEffectAtStart.end()) && (thiscom)); it2++)
							if (*it1==*it2)
								thiscom=false;
				}
				//cout << "****  ";
				canapplys=true;


				for (it1=interfere->conditionAtEnd.begin(); (((it1!=interfere->conditionAtEnd.end()) && (thiscom)) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "*  ";
				for (it1=interfere->conditionOverAll.begin(); (((it1!=interfere->conditionOverAll.end()) && (thiscom)) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "**  ";
				for (it1=interfere->addEffectAtEnd.begin(); (((it1!=interfere->addEffectAtEnd.end()) && (thiscom)) && (canapplys)); it1++)
					if (npd[*it1][j]>0)
						canapplys=false;
				//cout << "***  ";
				if (canapplys)
				{
					for (it1=interfere->addEffectAtEnd.begin(); ((it1!=interfere->addEffectAtEnd.end()) && (canapplys)); it1++)
						for (it2=com->conditionAtEnd.begin(); ((it2!=com->conditionAtEnd.end()) && (thiscom)); it2++)
							if (*it1==*it2)
								thiscom=false;


					for (it1=com->delEffectAtEnd.begin(); ((it1!=com->delEffectAtEnd.end()) && (thiscom)); it1++)
						for (it2=interfere->conditionOverAll.begin(); ((it2!=interfere->conditionOverAll.end()) && (canapplys)); it2++)
							if (*it1==*it2)
								thiscom=false;
					for (it1=com->delEffectAtEnd.begin(); ((it1!=com->delEffectAtEnd.end()) && (thiscom)); it1++)
						for (it2=interfere->conditionAtEnd.begin(); ((it2!=interfere->conditionAtEnd.end()) && (canapplys)); it2++)
							if (*it1==*it2)
								thiscom=false;

					for (it1=interfere->delEffectAtEnd.begin(); ((it1!=interfere->delEffectAtEnd.end()) && (canapplys)); it1++)
						for (it2=com->addEffectAtStart.begin(); ((it2!=com->addEffectAtStart.end()) && (thiscom)); it2++)
							if (*it1==*it2)
								thiscom=false;
				}
			}

		}
		if (!thiscom)
			compress[j]=false;
	}
	int totalcom=0;
	for (int j=0; j<nAction; j++)
		if (compress[j])
			totalcom++;
	cout << endl << "Ratio of Compressed Actions:  " << double(totalcom)/nAction;
	//delete com;
	//delete interfere;
	
	////////////////////////////NEW: COMPRESSING(End) ////////////////////////////////////////////////////////////////////////////////////
	for (int j=0; j<nProp; j++)
	{

		delete nps[j];
		delete npd[j];
		delete npe[j];

	}
	delete nps;
	delete npe;
	delete npd;
	delete nss;
	delete npp;
	delete nee;
	delete ndd;
	//for (int j=0; j<nProp*nProp; j++)
	for (int j=0; j<10000000; j++)
		delete newmux[j];
	delete newmux;

	///////////////////////////////////////////////// New: New Graph/////////////////////////////////////////////////////////////
	for(T=p.TStart; T<=p.TEnd && p.AvailableTime - CPUTime() > 0;)
	{
		checkedT.insert(T); // do not go back to this particular T, after finding a valid timed plan
		cout << "Trying with T=" << T << "... " << endl << flush;
		float availableTime = p.AvailableTime - CPUTime();
		if(availableTime > p.StageTime)
			availableTime = p.StageTime;
		if(p.satsolver == "minisat")
		{
			solver = new SatLayerMinisat(
				T, res, p.planFileName+"x", p.detailsFileNameTemplate,
				availableTime, p.gen_cnf, p.gen_readable_cnf, p.justgencnf, p.conflictsMethod);
			
		}
		else if(p.satsolver == "precosat")
			solver = new SatLayerPrecosat(
				T, res, p.planFileName+"x", p.detailsFileNameTemplate,
				availableTime, p.gen_cnf, p.gen_readable_cnf, p.justgencnf, p.conflictsMethod);
		else return false;
		// prepare the solver
		try
		{
			if(p.graphUsage==0)
				solver->DoEncoding(mutextable, compress); // encode without graph
			else
				solver->DoEncoding(fact_mutex, &prop_layer); // encode using graph
			//solver->SplitLayers(5); // the "splitting idea"
		}
		catch(const bad_alloc &e) // out of memory
		{
			delete solver;
			// since the out of memory happened during the encoding,
			// if we are not using graph, then the only option is to quit
			if(p.graphUsage == 0) 
				throw;
			// otherwise disable graph usage and delete any memory associated with graph:
			p.graphUsage = 0;
			delete fact_mutex;
			fact_mutex = NULL;
			prop_layer.clear();
			cout << endl << "Out of memory exception from solver->DoEncoding():" << e.what() << endl;
			cout << "Graph usage disabled to save memory. Total time so far: " << CPUTime() << endl;
			continue; // now try again with current T, but without graph, to avoid out of memory
		}
		catch(const runtime_error &e) // probably timeout
		{
			// NOTE: we assume that the assigned time to DoEncoding() is less than total available time,
			//       otherwise we should abort the planner with a "throw;"
			delete solver;
			string ewhat = e.what();
			if(ewhat != "Timeout during encoding.") // Unhandled exception
				throw;
			// since the timeout happened during the encoding,
			// if we are not using graph, then the only option is to quit
			if(p.graphUsage == 0)
				throw;
			// otherwise disable graph usage and delete any memory associated with graph:
			p.graphUsage = 0;
			delete fact_mutex;
			fact_mutex = NULL;
			prop_layer.clear();
			cout << endl << "Timeout exception from solver->DoEncoding():" << e.what() << endl;
			cout << "Graph usage disabled to save time. Total time so far: " << CPUTime() << endl;
			continue; // now try again with current T, but without graph, to avoid timeout
		}
		catch(const exception &e)
		{
			cout << endl << "Unhandled exception from solver->DoEncoding(): " << e.what() << endl;
			cout << "Total time so far: " << CPUTime() << endl;
			cout << "Search for plan aborted." << endl;
			delete solver;
			if(g)
				delete g;
			throw; // abort
		}
		// add previously found negative cycles to encoding
		for(vector<vector<PlanEvent> >::const_iterator it = negcyclePool.begin(); it != negcyclePool.end(); ++it)
		{
			// AddNegCycleAutomaton(*it, T, solver);
			try
			{
				AddNegCycleAutomaton_General(*it, T, solver, mutextable, compress);
			}
			catch(const exception &e)
			{
				cout << endl << "Unhandled exception from AddNegCycleAutomaton_General(): " << e.what() << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				delete solver;
				if(g)
					delete g;
				throw; // abort
			}
		}
		// search for a plan and try to extract a timed plan
		bool reseted = false;
		for(int restart_per_T=0; ; restart_per_T++)
		{
			// now call the ->solve()
			try
			{
//		cout << endl << "finished" << endl;
//	exit(0);
				solver->Solve();
				if(restart_per_T == 0)
					if(res->outcome == SAT)
					{
						cout << "A plan found with layers = " << T << endl;
						cout << "Trying to find a satisfying timed plan:" << endl << flush;
					}
					else
						break;
			}
			catch(const bad_alloc &e) // out of memory exception
			{
				cout << endl << "Out of memory exception from solver->Solve():" << e.what() << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				break; // try the next T
			}
			catch(const exception &e)
			{
				cout << endl << "Unhandled exception from solver->Solve():" << e.what() << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				delete solver;
				if(g)
					delete g;
				throw; // abort
			}

			vector<int> negcycle;
			bool negCycleFound;
			try
			{
				negCycleFound = !FindTimedPlan(solver->plan, negcycle, p.planFileName, bestMakeSpan, planNumber);
			}
			catch(const logic_error &e)
			{
				cout << endl << "Logic_error exception from FindTimedPlan(): " << e.what() << endl;
				cout << "It may be due to some odd definitions in DOMAIN file." << endl;
				cout << "Otherwise it generally indicates a flaw in planner code." << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				delete solver;
				if(g)
					delete g;
				throw; // abort
			}
			// should never happen since no other type of exception is generated by FindTimedPlan() or its callees:
			catch(const exception &e)
			{
				cout << endl << "Unhandled exception from FindTimedPlan(): " << e.what() << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				delete solver;
				if(g)
					delete g;
				throw; // abort
			}
			if(!negCycleFound)
			{
				solutionFound = true;
				break;
			}
			cout << "restart # " << ++restarts << endl << flush;

			// convert vector<int> to vector<PlanEvent>
			vector<PlanEvent> negcycleEvent;
			negcycleEvent.clear(); // clear previous stored negative cycle, if any
			for(vector<int>::const_iterator it = negcycle.begin(); it != negcycle.end(); ++it)
			{
				// we decrease negcycle[i] by 1 because we added an special node to plan
				//    before we run bellman_ford()
				negcycleEvent.push_back(solver->plan[*it-1]);
			}
			// store the negative cycle in a pool, to add to future encodings
			negcyclePool.push_back(negcycleEvent);

			reseted = true; break; // reset the solver with current T
			// we designed this for loop to INCREMENTALLY append the negative cycles to current encoding,
			// but then we realized that, due to the "Conflict Clause" learning approach being used
			// by the Minisat2, in order to append the new negative cycle, we have to RESET the solver
			// and encode from the beginning.
			// so the following code is UNREACHABLE:

			// add the recent negative cycle to current enconding
			// AddNegCycleAutomaton(negcycleEvent, T, solver);
			try
			{
				AddNegCycleAutomaton_General(negcycleEvent, T, solver, mutextable, compress);
			}
			catch(const exception &e)
			{
				cout << endl << "Unhandled exception from AddNegCycleAutomaton_General(): " << e.what() << endl;
				cout << "Total time so far: " << CPUTime() << endl;
				cout << "Search for plan aborted." << endl;
				delete solver;
				if(g)
					delete g;
				throw; // abort
			}
		}
		delete solver;

		t2 = CPUTime();
		res->T = T;
		res->time_overall = t2 - t1;
		elapsed.push_back(res);
		cout << "Time: " << t2 - t1 << " secs" << endl << flush;
		t1 = t2;
		cout << endl << endl;
		if(reseted)
			continue;
		if(solutionFound) // if a valid timed plan is found
		{
			maxLookingAround --;
			if(maxLookingAround == 0) // enough looking around!
				break;
			do
			{
				T = T + solfoundStep;
				solfoundStep = -solfoundStep;
				if(solfoundStep > 0)
					solfoundStep ++;
				else
					solfoundStep --;
			}
			while(T < p.TStart || checkedT.find(T) != checkedT.end()); // continue if T is invalid
		}
		else
		{
			if(T >= 50) // FIXME: move to program switches
				T *= 1.2;
			else
				T = ceil(T*p.TMultiply + p.TPlus);
		}
		
	}

	cout << "Operation Total Time: " << CPUTime() << " secs" << endl;

	ofstream file3(p.resultsFileName.c_str());
	file3 << "T\toutcome\ttime_overall\ttotalClauses\ttotalMutexes\tvarTotal\tvarProp\tvarAction"
		<< "\tccInit\tccGoal\tccNotApplicable\tccCondition\tccEffect\tccAxiomDelete"
		<< "\tccAxiomAdd\tccMutexStart\tccMutexEnd\tccMutexStartEnd\tccMutexOverall" << endl;
	for(int i=0; i<elapsed.size(); i++)
	{
		SATResults *res = elapsed[i];
		file3 << res->T << "\t" << res->outcome << "\t" << res->time_overall << "\t" << res->totalClauses
			<< "\t" << res->totalMutexes << "\t" << res->varTotal << "\t" << res->varProp << "\t" << res->varAction
			<< "\t" << res->ccInit << "\t" << res->ccGoal << "\t" << res->ccNotApplicable << "\t" << res->ccCondition
			<< "\t" << res->ccEffect << "\t" << res->ccAxiomDelete << "\t" << res->ccAxiomAdd << "\t" << res->ccMutexStart
			<< "\t" << res->ccMutexEnd << "\t" << res->ccMutexStartEnd << "\t" << res->ccMutexOverall << endl;
	}
	file3.close();
	return true;
}
