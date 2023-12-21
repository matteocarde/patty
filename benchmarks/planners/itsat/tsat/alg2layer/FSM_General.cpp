#include "tsat/alg2layer/FSM_General.h"
#include "tsat/parser/ParserClasses.h"
#include "tsat/satlayer/SatLayer.h"
#include "tsat/utils.h"
#include <set>
#include <iterator>
#include <algorithm>
using namespace std;
using namespace MyParser;
using namespace nsSatLayer;

void AddNegCycleAutomaton_General(const vector<PlanEvent> &negCycle, int T, SatLayer *solver, bool **mutextable, bool *compress)
{
	//    i=0     i=1        i=2,3       i=4,5       i=6       i=7,8       i=9      i=10
	// [FrameS 0 Alone1 1 [AS ta AE] 2 [BS tb BE] 3 Alone2 4 [CS tc CE] 5 Alone3 6 FrameE] 7
	// Pos_SimilarA = [2, 4, 7]
	int sz = negCycle.size();
	int sze;
	
	//int *tarnsvar=new int[pProblem.pAllAction.size()*2];
	long long totalvars = 0;
	int ntransvar=0;
	int nstatevar=0;
	int maxtrans=1;

	//bool *compress=new bool[pProblem.pAllAction.size()];
	//for (int j=0; j<pProblem.pAllAction.size(); j++)
		//compress[j]=false;
	vector< set<int> > SimilarA;
	vector<int> Pos_SimilarA;
	for (int j=0; j<negCycle.size()-1; j++)
	{
		if (negCycle[j].id!=negCycle[j+1].id)
			continue;
		if (negCycle[j].part==ACTION_END)
			continue;
		Pos_SimilarA.push_back(j);
		j++;
	}
	set<int>::const_iterator it, it1, it2;
	for (int j=0; j<Pos_SimilarA.size(); j++)
	{
		//cout << endl << "SIMILARA: " << Pos_SimilarA[j] << endl;
		if (j>0)
		{
			if (Pos_SimilarA[j]==Pos_SimilarA[j-1]+2)
			{
				int after_e=negCycle[Pos_SimilarA[j]+2].id;
				int after_p=negCycle[Pos_SimilarA[j]+2].part;
				set<int> thisS;
				thisS.clear();
				const PAction &After = *pProblem.pAllAction.GetActionById(after_e);
				const set<int> *afterPre, *afterAdd, *afterDel, *afterDur;
				if(after_p == 0) // holds when i!=sz-3
				{
					afterPre = &After.conditionAtStart;
					afterAdd = &After.addEffectAtStart;
					afterDel = &After.delEffectAtStart;
					afterDur = &After.conditionOverAll;
				}
				else // holds when i==sz-3 (last step)
				{
					afterPre = &After.conditionAtEnd;
					afterAdd = &After.addEffectAtEnd;
					afterDel = &After.delEffectAtEnd;
					afterDur = &After.conditionOverAll;
				}
				
				for (int k=0; k<pProblem.pAllAction.all.size(); k++)
				{

					bool legitall=true;
					const PAction *A = pProblem.pAllAction.GetActionById(k);
					const PAction *CUR = pProblem.pAllAction.GetActionById(negCycle[Pos_SimilarA[j]].id);
					if (CUR->duration > A->duration)
						continue;
					if (A->id==negCycle[0].id)
						continue;
					bool legit=false;
					for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
						for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
						for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
						for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
						for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;

					for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
						for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
						for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
						for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
						for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;

					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
							if (mutextable[*it1][*it2])
								legit=true;
					for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
							if (*it1==*it2)
								legit=true;



					for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
							if (*it1==*it2)
								legit=true;
					for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
						for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
							if (*it1==*it2)
								legit=true;
					if (!legit)
						continue;

					legitall=true;

					for (it=SimilarA[j-1].begin(); ((it!=SimilarA[j-1].end()) && legitall) ; it++)
					{

						int before_e=*it;
						int before_p=1;
						const PAction &Before = *pProblem.pAllAction.GetActionById(before_e);
						const set<int> *beforePre, *beforeAdd, *beforeDel, *beforeDur;
						beforePre = &Before.conditionAtEnd;
						beforeAdd = &Before.addEffectAtEnd;
						beforeDel = &Before.delEffectAtEnd;
						beforeDur = &Before.conditionOverAll;
						bool legit=false;
						for (it1=A->conditionAtStart.begin(); it1!= A->conditionAtStart.end(); it1++)
							for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
							for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
							for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;

						for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
							for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
							for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
							for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;

						for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
							for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
							for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;
						for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
							for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
								if (mutextable[*it1][*it2])
									legit=true;



						for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
							for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
							for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
								if (*it1==*it2)
									legit=true;
						for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
							for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
								if (*it1==*it2)
								{
									legit=true;
									//if (k==81)
									//{
										//cout << endl << pProblem.pAllProposition.GetPropositionById(*it1)->ToFullString() << "   " << pProblem.pAllProposition.GetPropositionById(*it2)->ToFullString() << endl;
										//exit(0);
									//}
								}
						if (!legit)
							legitall=false;
						
					}
					if (legitall)
						thisS.insert(k);
				}
				SimilarA.push_back(thisS);
				continue;
			}
		}
		int before_e=negCycle[Pos_SimilarA[j]-1].id;
		int before_p=negCycle[Pos_SimilarA[j]-1].id;
		int after_e=negCycle[Pos_SimilarA[j]+2].id;
		int after_p=negCycle[Pos_SimilarA[j]+2].part;
		set<int> thisS;
		thisS.clear();

		const PAction &Before = *pProblem.pAllAction.GetActionById(before_e);
		//const PAction &A = *pProblem.pAllAction.GetActionById(nodeS.id); // nodeE.id is the same
		const PAction &After = *pProblem.pAllAction.GetActionById(after_e);
		const set<int> *beforePre, *beforeAdd, *beforeDel, *beforeDur;
		const set<int> *afterPre, *afterAdd, *afterDel, *afterDur;
		if( before_p == 0) // holds when i==1
		{
			beforePre = &Before.conditionAtStart;
			beforeAdd = &Before.addEffectAtStart;
			beforeDel = &Before.delEffectAtStart;
			beforeDur = &Before.conditionOverAll;

		}
		else // holds when i!=1
		{
			beforePre = &Before.conditionAtEnd;
			beforeAdd = &Before.addEffectAtEnd;
			beforeDel = &Before.delEffectAtEnd;
			beforeDur = &Before.conditionOverAll;
		}
		if(after_p == 0) // holds when i!=sz-3
		{
			afterPre = &After.conditionAtStart;
			afterAdd = &After.addEffectAtStart;
			afterDel = &After.delEffectAtStart;
			afterDur = &After.conditionOverAll;
		}
		else // holds when i==sz-3 (last step)
		{
			afterPre = &After.conditionAtEnd;
			afterAdd = &After.addEffectAtEnd;
			afterDel = &After.delEffectAtEnd;
			afterDur = &After.conditionOverAll;
		}
		//vector <MyParser::PAction>::const_iterator it;
		//for (it=pProblem.pAllAction.all.begin(); it!=pProblem.pAllAction.all.end(); it++)
		for (int k=0; k<pProblem.pAllAction.all.size(); k++)
		{
			const PAction *A = pProblem.pAllAction.GetActionById(k);
			const PAction *CUR = pProblem.pAllAction.GetActionById(negCycle[Pos_SimilarA[j]].id);
			if (CUR->duration > A->duration)
				continue;
			if (A->id==negCycle[0].id)
				continue;
			bool legit=false;
			for (it1=A->conditionAtStart.begin(); it1!= A->conditionAtStart.end(); it1++)
				for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
				for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionAtStart.begin(); ((it1!= A->conditionAtStart.end()) && !legit); it1++)
				for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;

			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;

			for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
				for (it2=beforeDel->begin(); it2!=beforeDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
				for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->addEffectAtStart.begin(); ((it1!= A->addEffectAtStart.end()) && !legit); it1++)
				for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;



			for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
				for (it2=beforeAdd->begin(); it2!=beforeAdd->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
				for (it2=beforePre->begin(); it2!=beforePre->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->delEffectAtStart.begin(); ((it1!= A->delEffectAtStart.end()) && !legit); it1++)
				for (it2=beforeDur->begin(); it2!=beforeDur->end(); it2++)
					if (*it1==*it2)
						legit=true;
			if (!legit)
				continue;

			for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
				for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
				for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
				for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionAtEnd.begin(); ((it1!= A->conditionAtEnd.end()) && !legit); it1++)
				for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;

			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->conditionOverAll.begin(); ((it1!= A->conditionOverAll.end()) && !legit); it1++)
				for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;

			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterDel->begin(); it2!=afterDel->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
					if (mutextable[*it1][*it2])
						legit=true;
			for (it1=A->addEffectAtEnd.begin(); ((it1!= A->addEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
					if (*it1==*it2)
						legit=true;



			for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterAdd->begin(); it2!=afterAdd->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterPre->begin(); it2!=afterPre->end(); it2++)
					if (*it1==*it2)
						legit=true;
			for (it1=A->delEffectAtEnd.begin(); ((it1!= A->delEffectAtEnd.end()) && !legit); it1++)
				for (it2=afterDur->begin(); it2!=afterDur->end(); it2++)
					if (*it1==*it2)
						legit=true;
			
			
			if (legit)
				thisS.insert(k);

		}
		SimilarA.push_back(thisS);
	}

	// Fill_SimilarA_Frame(negCycle, std::back_inserter(SimilarA));
	try
	{
		//Fill_SimilarA(negCycle, std::back_inserter(SimilarA), std::back_inserter(Pos_SimilarA), mutextable);
		sze = sz - Pos_SimilarA.size();
	}
	catch(const exception &e)
	{
		cout << endl << "Exception from Fill_SimilarA(): " << e.what() << endl;
		throw;
	}
	int thise=0;
	int totaltrans=0;
	int totalstates=1;
	
	for (int j=0; j<Pos_SimilarA.size(); j++)
	{
		while (thise<Pos_SimilarA[j])
		{
			thise++;
			totaltrans++;
			totalstates++;
		}
		totalstates++;
		//cout << endl << "*******************************" << endl;
		for (it=SimilarA[j].begin(); it!=SimilarA[j].end(); it++)
		{
			if (SimilarA[j].size()==0)
			{
				cout << endl << "SIMILARA EMPTY" << endl;
				exit(0);
			}
			//cout << endl << pProblem.pAllAction.GetActionById(*it)->ToFullString() << "   " << *it << endl;
			//cout << endl << *it << endl;
			if (compress[*it])
				totaltrans++;
			else
			{
				totaltrans+=2;
				totalstates++;
			}
		}
		
		thise+=2;

	}
	//exit(0);
	while (thise<negCycle.size())
	{
		thise++;
		totaltrans++;
		totalstates++;
	}
	int *alltstart = new int[totaltrans];
	int *alltend = new int[totaltrans];
	int *alltevent = new int[totaltrans];
	int *alltpart = new int[totaltrans];
	int *alltnext= new int [totaltrans];
	int *alltsame= new int [totaltrans];
	int thistrans=0;
	int thisstate=0;
	int nextstate;
	thise=0;
	for (int j=0; j<Pos_SimilarA.size(); j++)
	{
		
		while (thise<Pos_SimilarA[j])
		{
			nextstate=thisstate+1;
			alltstart[thistrans]=thisstate;
			alltend[thistrans]=nextstate;
			alltevent[thistrans]=negCycle[thise].id;
			alltpart[thistrans]=negCycle[thise].part;
			alltnext[thistrans]=thistrans+1;
			alltsame[thistrans]=-1;
			thise++;
			thistrans++;
			thisstate=nextstate;
			
		}
		nextstate=thisstate+1;
		int next=thistrans;
		for (it=SimilarA[j].begin(); it!=SimilarA[j].end(); it++)
			if (compress[*it])
				next++;
			else
			{
				next+=2;
				nextstate++;
			}
		int added=0;
		for (it=SimilarA[j].begin(); it!=SimilarA[j].end(); it++)
			if (compress[*it])
			{
				alltstart[thistrans]=thisstate;
				alltend[thistrans]=nextstate;
				alltevent[thistrans]=(*it);
				alltpart[thistrans]=ACTION_START;
				alltnext[thistrans]=next;
				it++;
				if (it==SimilarA[j].end())
					alltsame[thistrans]=-1;
				else
					alltsame[thistrans]=thistrans+1;
				it--;
				thistrans++;
			}
			else
			{
				//totaltrans+=2;
				added++;
				alltstart[thistrans]=thisstate;
				alltend[thistrans]=thisstate+added;
				alltevent[thistrans]=(*it);
				alltpart[thistrans]=ACTION_START;
				alltnext[thistrans]=thistrans+1;
				it++;
				if (it==SimilarA[j].end())
					alltsame[thistrans]=-1;
				else
					alltsame[thistrans]=thistrans+2;
				it--;
				thistrans++;
				alltstart[thistrans]=thisstate+added;
				alltend[thistrans]=nextstate;
				alltevent[thistrans]=(*it);
				alltpart[thistrans]=ACTION_END;
				alltnext[thistrans]=next;
				alltsame[thistrans]=-1;
				thistrans++;				
			}
		
		thise+=2;
		thisstate=nextstate;

	}
	while (thise<negCycle.size())
	{
		nextstate=thisstate+1;
		alltstart[thistrans]=thisstate;
		alltend[thistrans]=nextstate;
		alltevent[thistrans]=negCycle[thise].id;
		alltpart[thistrans]=negCycle[thise].part;
		alltnext[thistrans]=thistrans+1;
		alltsame[thistrans]=-1;
		thise++;
		thistrans++;
		thisstate=nextstate;
			
	}
	alltnext[totaltrans-1]=-1;
	int *thislvars=new int[totalstates];
	int *nextlvars=new int[totalstates];
	int *curlvars= new int[totaltrans];
	for (int j=0; j<totalstates; j++)
		thislvars[j]= 1 + solver->SATNewVar();
	//cout << endl << alltstart[totaltrans-1] << " " << alltend[totaltrans-1] << " " << totalvars;
	//exit(0);
	for (int t=0; t<T; t++)
	{
		for (int j=0; j<totalstates; j++)
			 nextlvars[j]= 1 + solver->SATNewVar();
		for (int j=0; j<totaltrans; j++)
			 curlvars[j]= 1 + solver->SATNewVar();
		for (int j=0; j<totalstates; j++)
		{
			int k;
			for (k=0; ((k<totaltrans) ); k++)
				if (alltstart[k]==j)
					break;
			if (k<totaltrans)
			{
				solver->ResetClause();
				solver->AddToClause(thislvars[j], false);
				solver->AddToClause(curlvars[k], true);
				solver->AddClause(totalvars);
			}
		}
		for (int j=0; j<totaltrans; j++)
		{
			int nn=alltnext[j];
			while (nn!=-1)
			{
				if (alltevent[j]*2+alltpart[j]<alltevent[nn]*2+alltpart[nn])
					break;
				nn=alltsame[nn];
			}
			if (nn!=-1)
			{
				solver->ResetClause();
				if (alltpart[j]==ACTION_START)
					solver->AddToClause(solver->ActionTime2Var(alltevent[j], t, ACTION_START), false);
				else
					solver->AddToClause(solver->ActionTime2Var(alltevent[j], t, ACTION_END), false);
				solver->AddToClause(curlvars[j], false);
				solver->AddToClause(curlvars[nn], true);
				solver->AddClause(totalvars);
			}
			else
			{
				solver->ResetClause();
				if (alltpart[j]==ACTION_START)
					solver->AddToClause(solver->ActionTime2Var(alltevent[j], t, ACTION_START), false);
				else
					solver->AddToClause(solver->ActionTime2Var(alltevent[j], t, ACTION_END), false);
				solver->AddToClause(curlvars[j], false);
				solver->AddToClause(solver->ActionTime2Var(negCycle[negCycle.size()-1].id, t, ACTION_END), true);
				solver->AddToClause(nextlvars[alltend[j]], true);
				solver->AddClause(totalvars);
			}
			nn=alltsame[j];
			if (nn!=-1)
			{
				solver->ResetClause();
				solver->AddToClause(curlvars[j], false);

				solver->AddToClause(curlvars[nn], true);
				solver->AddClause(totalvars);

			}
			else
			{
				solver->ResetClause();
				solver->AddToClause(curlvars[j], false);
				solver->AddToClause(solver->ActionTime2Var(negCycle[negCycle.size()-1].id, t, ACTION_END), true);
				solver->AddToClause(nextlvars[alltstart[j]], true);
				solver->AddClause(totalvars);

			}
		}
		for (int j=1; j<totalstates; j++)
		{
			solver->ResetClause();
			solver->AddToClause(solver->ActionTime2Var(negCycle[negCycle.size()-1].id, t, ACTION_END), false);
			solver->AddToClause(nextlvars[j], false);
			solver->AddClause(totalvars);
		}
		solver->ResetClause();
		solver->AddToClause(solver->ActionTime2Var(negCycle[negCycle.size()-1].id, t, ACTION_END), false);
		solver->AddToClause(nextlvars[0], true);
		solver->AddClause(totalvars);
		solver->ResetClause();
		solver->AddToClause(solver->ActionTime2Var(negCycle[negCycle.size()-1].id, t, ACTION_END), false);
		solver->AddToClause(curlvars[totaltrans-1], false);
		solver->AddClause(totalvars);
		if (t==0)
		{
			for (int j=1; j<totalstates; j++)
			{
				solver->ResetClause();
				solver->AddToClause(thislvars[j], false);
				solver->AddClause(totalvars);
			}
			solver->ResetClause();
			solver->AddToClause(thislvars[0], true);
			solver->AddClause(totalvars);
			solver->ResetClause();
		}
		for (int j=0; j<totalstates; j++)
			thislvars[j]= nextlvars[j];
		//delete curlvars;
	}
	delete curlvars;
	delete thislvars;
	delete nextlvars;
	delete alltstart;
	delete alltend;
	delete alltevent;
	delete alltpart;
	delete alltnext;
	delete alltsame;
	/*
	//cout << endl << "****************************** "<< SimilarA[0].size() << "  " << SimilarA[1].size() << "  "<< SimilarA[2].size() << " *****************";
	//exit(0);
	//cout << endl << "****************************** "<< SimilarA[0].size() << " *****************";
	
	int  *oldstates=new int[pProblem.pAllAction.size()*2*negCycle.size()];
	int noldstates=0;
	for (int t=0; t<1; t++)
	{
		
		int thiss=1 + solver->SATNewVar();
		int nexts;
		int thise=0;
		int *oldtrans= new int[pProblem.pAllAction.size()*2];
		int *oldevent= new int[pProblem.pAllAction.size()*2];
		int *newstates=new int[pProblem.pAllAction.size()*2*negCycle.size()];
		newstates[0]=thiss;




		int nnewstates=0;
		noldstates=0;
		int noldtrans=0;
		set<int>::const_iterator it;
		set<int> *thisset;
		if (Pos_SimilarA[0]>0)
		{
			oldtrans[noldtrans]=1 + solver->SATNewVar();
			oldevent[noldtrans]=negCycle[0].id*2+negCycle[0].part;
			noldtrans++;
		}
		else
		{
			cout << endl << "******************************ERROR*****************";

			thisset=&SimilarA[0];
			for (it=thisset->begin(); it!=thisset->end(); it++)
			{
				oldtrans[noldtrans]=1 + solver->SATNewVar();
				oldevent[noldtrans]=(*it)*2;
				noldtrans++;
			}
		}

		noldstates++;
		nnewstates++;
		for (int i=0; i<SimilarA.size(); i++)
		{
		
			while (Pos_SimilarA[i]>thise)
			{
				nexts=1 + solver->SATNewVar();
				newstates[nnewstates]=nexts;

				int *newtrans= new int[pProblem.pAllAction.size()*2];
				int *newevent= new int[pProblem.pAllAction.size()*2];
				int nnewtrans=0;
				if (Pos_SimilarA[i]>thise+1)
				{
					newtrans[nnewtrans]=1 + solver->SATNewVar();
					newevent[nnewtrans]=negCycle[thise+1].id*2+negCycle[thise+1].part;
					nnewtrans++;
				}
				else
				{
					thisset=&SimilarA[i];
					for (it=thisset->begin(); it!=thisset->end(); it++)
					{
						newtrans[nnewtrans]=1 + solver->SATNewVar();
						newevent[nnewtrans]=(*it)*2;
						nnewtrans++;
					}
				}

			


				if (noldtrans!=1)
					cout << endl << "******************************ERROR2****************";


				nnewstates++;
				noldstates++;
				thise++;
				delete oldtrans;
				delete oldevent;
				oldtrans=newtrans;
				oldevent=newevent;
				noldtrans=nnewtrans;

			}






//			while (Pos_SimilarA[i]>thise)
//			{
			nexts=1 + solver->SATNewVar();
			newstates[nnewstates]=nexts;

			//nexts=oldstates[noldstates];
			int *newtrans= new int[pProblem.pAllAction.size()*2];
			int *newevent= new int[pProblem.pAllAction.size()*2];
			int nnewtrans=0;
			if (i!=SimilarA.size()-1)
			{
				if (Pos_SimilarA[i+1]>thise+2)
				{
				
					newtrans[nnewtrans]=1 + solver->SATNewVar();
					newevent[nnewtrans]=negCycle[thise+2].id*2+negCycle[thise+2].part;
					nnewtrans++;
				}
				else
				{
					thisset=&SimilarA[i+1];
					for (it=thisset->begin(); it!=thisset->end(); it++)
					{
						newtrans[nnewtrans]=1 + solver->SATNewVar();
						newevent[nnewtrans]=(*it)*2;
						nnewtrans++;
					}
				}
			}
			else
			{
				
				newtrans[nnewtrans]=1 + solver->SATNewVar();
				newevent[nnewtrans]=negCycle[thise+2].id*2+negCycle[thise+2].part;
				nnewtrans++;
			}

			nnewstates++;
			noldstates++;
			//thisset=&SimilarA[i];
			for (int j=0; j<noldtrans; j++)
			{
				int endvar= 1 + solver->SATNewVar();


				newstates[nnewstates]= 1 + solver->SATNewVar();





				noldstates++;
				nnewstates++;


			}
			thise+=2;
			delete oldtrans;
			delete oldevent;
			oldtrans=newtrans;
			oldevent=newevent;
			noldtrans=nnewtrans;
		}
		while (thise<negCycle.size()-1)
		{
			cout << endl << "******************************ERROR8****************";
			nexts=1 + solver->SATNewVar();
			newstates[nnewstates]=nexts;

			int *newtrans= new int[pProblem.pAllAction.size()*2];
			int *newevent= new int[pProblem.pAllAction.size()*2];
			int nnewtrans=0;
			//if (Pos_SimilarA[i]>thise+1)
			//{
				newtrans[nnewtrans]=1 + solver->SATNewVar();
				newevent[nnewtrans]=negCycle[thise+1].id*2+negCycle[thise+1].part;
				nnewtrans++;
			//}


			


			if (noldtrans!=1)
				cout << endl << "******************************ERROR5****************";
			if (nnewtrans!=1)
				cout << endl << "******************************ERROR5****************";


			nnewstates++;
			noldstates++;
			thise++;
			delete oldtrans;
			delete oldevent;
			oldtrans=newtrans;
			oldevent=newevent;
			noldtrans=nnewtrans;

		}

		delete oldstates;
		oldstates=newstates;
		noldstates=nnewstates;
	}		
	for (int t=0; t<T; t++)
	{
		
		int thiss=1 + solver->SATNewVar();
		int nexts;
		int thise=0;
		int *oldtrans= new int[pProblem.pAllAction.size()*2];
		int *oldevent= new int[pProblem.pAllAction.size()*2];
		int *newstates=new int[pProblem.pAllAction.size()*2*negCycle.size()];
		newstates[0]=thiss;


		solver->ResetClause();
		//if (t>0)
			//solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t-1, ACTION_END), false);
		solver->AddToClause(oldstates[0], true);
		solver->AddClause(totalvars);


		int nnewstates=0;
		noldstates=0;
		int noldtrans=0;
		set<int>::const_iterator it;
		set<int> *thisset;
		if (Pos_SimilarA[0]>0)
		{
			oldtrans[noldtrans]=1 + solver->SATNewVar();
			oldevent[noldtrans]=negCycle[0].id*2+negCycle[0].part;
			noldtrans++;
		}
		else
		{
			cout << endl << "******************************ERROR*****************";

			thisset=&SimilarA[0];
			for (it=thisset->begin(); it!=thisset->end(); it++)
			{
				oldtrans[noldtrans]=1 + solver->SATNewVar();
				oldevent[noldtrans]=(*it)*2;
				noldtrans++;
			}
		}
		for (int i=0; i<noldtrans; i++)
		{
			solver->ResetClause();
			solver->AddToClause(oldstates[noldstates], false);
			//solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), false);
			solver->AddToClause(oldtrans[i], true);
			solver->AddClause(totalvars);
		}
		noldstates++;
		nnewstates++;
		for (int i=0; i<SimilarA.size(); i++)
		{
			
			while (Pos_SimilarA[i]>thise)
			{
				nexts=1 + solver->SATNewVar();
				newstates[nnewstates]=nexts;
				if (t>0)
				{
					solver->ResetClause();
					solver->AddToClause(oldstates[noldstates], false);
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
					solver->AddToClause(newstates[nnewstates], true);
					solver->AddClause(totalvars);

					solver->ResetClause();
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), false);
					solver->AddToClause(newstates[nnewstates], false);
					solver->AddClause(totalvars);
				}
				int *newtrans= new int[pProblem.pAllAction.size()*2];
				int *newevent= new int[pProblem.pAllAction.size()*2];
				int nnewtrans=0;
				if (Pos_SimilarA[i]>thise+1)
				{
					newtrans[nnewtrans]=1 + solver->SATNewVar();
					newevent[nnewtrans]=negCycle[thise+1].id*2+negCycle[thise+1].part;
					nnewtrans++;
				}
				else
				{
					thisset=&SimilarA[i];
					for (it=thisset->begin(); it!=thisset->end(); it++)
					{
						newtrans[nnewtrans]=1 + solver->SATNewVar();
						newevent[nnewtrans]=(*it)*2;
						nnewtrans++;
					}
				}
				for (int j=0; j<nnewtrans; j++)
				{
					solver->ResetClause();
					solver->AddToClause(oldstates[noldstates], false);
					solver->AddToClause(newtrans[j], true);

					solver->AddClause(totalvars);
				}


				for (int j=0; j<noldtrans; j++)
					for (int k=0; k<nnewtrans; k++)
						if (oldevent[j]<newevent[k])
						{
							solver->ResetClause();
							solver->AddToClause(oldtrans[j], false);
							if (oldevent[j]%2==0)
								solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_START), false);
							else
								solver->AddToClause(solver->ActionTime2Var((oldevent[j]-1)/2, t, ACTION_END), false);
							solver->AddToClause(newtrans[k], true);
							solver->AddClause(totalvars);
						}

				if (noldtrans!=1)
					cout << endl << "******************************ERROR2****************";

				solver->ResetClause();
				solver->AddToClause(oldtrans[0], false);
				if (oldevent[0]%2==0)
					solver->AddToClause(solver->ActionTime2Var(oldevent[0]/2, t, ACTION_START), false);
				else
					solver->AddToClause(solver->ActionTime2Var((oldevent[0]-1)/2, t, ACTION_END), false);

				solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
				solver->AddToClause(newstates[nnewstates], true);
				solver->AddClause(totalvars);






				nnewstates++;
				noldstates++;
				thise++;
				delete oldtrans;
				delete oldevent;
				oldtrans=newtrans;
				oldevent=newevent;
				noldtrans=nnewtrans;

			}






//			while (Pos_SimilarA[i]>thise)
//			{
			nexts=1 + solver->SATNewVar();
			newstates[nnewstates]=nexts;
				if (t>0)
				{
					solver->ResetClause();
					solver->AddToClause(oldstates[noldstates], false);
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
					solver->AddToClause(newstates[nnewstates], true);
					solver->AddClause(totalvars);

					solver->ResetClause();
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), false);
					solver->AddToClause(newstates[nnewstates], false);
					solver->AddClause(totalvars);

				}
			//nexts=oldstates[noldstates];
			int *newtrans= new int[pProblem.pAllAction.size()*2];
			int *newevent= new int[pProblem.pAllAction.size()*2];
			int nnewtrans=0;
			
			if (i!=SimilarA.size()-1)
			{
				if (Pos_SimilarA[i+1]>thise+2)
				{
				
					newtrans[nnewtrans]=1 + solver->SATNewVar();
					newevent[nnewtrans]=negCycle[thise+2].id*2+negCycle[thise+2].part;
					nnewtrans++;
				}
				else
				{
					thisset=&SimilarA[i+1];
					for (it=thisset->begin(); it!=thisset->end(); it++)
					{
						newtrans[nnewtrans]=1 + solver->SATNewVar();
						newevent[nnewtrans]=(*it)*2;
						nnewtrans++;
					}
				}
			}
			else
			{
				
				newtrans[nnewtrans]=1 + solver->SATNewVar();
				newevent[nnewtrans]=negCycle[thise+2].id*2+negCycle[thise+2].part;
				nnewtrans++;
			}

			for (int j=0; j<nnewtrans; j++)
			{

				solver->ResetClause();
				solver->AddToClause(oldstates[noldstates], false);
				solver->AddToClause(newtrans[j], true);

				solver->AddClause(totalvars);
			}
			nnewstates++;
			noldstates++;
			//thisset=&SimilarA[i];
			
			for (int j=0; j<noldtrans; j++)
			{
				//if ((negCycle[0].id==1) && (i==2) && (oldevent[j]==40))
				//{
					//cout << endl << "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%";
					//exit(0);
				//}
				int endvar= 1 + solver->SATNewVar();
				for (int k=0; k<nnewtrans; k++)
					if (oldevent[j]<newevent[k])
					{
						solver->ResetClause();
						solver->AddToClause(endvar, false);
						if (oldevent[j]%2==0)
							solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_END), false);
						else
						{
							cout << endl << "******************************ERROR3****************";
							solver->AddToClause(solver->ActionTime2Var((oldevent[j]-1)/2, t, ACTION_END), false);
						}
						solver->AddToClause(newtrans[k], true);
						solver->AddClause(totalvars);
					}
				solver->ResetClause();
				solver->AddToClause(oldtrans[j], false);
				solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_START), false);
				if (oldevent[j]%2==0)
					solver->AddToClause(endvar, true);
				else
				{
					cout << endl << "******************************ERROR3****************";
					solver->AddToClause(solver->ActionTime2Var((oldevent[j]-1)/2, t, ACTION_END), false);
				}
				solver->AddClause(totalvars);
				newstates[nnewstates]= 1 + solver->SATNewVar();

				if (t>0)
				{
					solver->ResetClause();
					solver->AddToClause(oldstates[noldstates], false);
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
					solver->AddToClause(newstates[nnewstates], true);
					solver->AddClause(totalvars);

					solver->ResetClause();
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), false);
					solver->AddToClause(newstates[nnewstates], false);
					solver->AddClause(totalvars);

				}


				solver->ResetClause();
				solver->AddToClause(oldtrans[j], false);
				solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_START), false);
				solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
				solver->AddToClause(newstates[nnewstates], true);
				solver->AddClause(totalvars);

				solver->ResetClause();
				solver->AddToClause(oldstates[noldstates], false);
				solver->AddToClause(endvar, true);
				solver->AddClause(totalvars);				

				solver->ResetClause();
				solver->AddToClause(endvar, false);
				solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_END), false);
				if (thise<negCycle.size()-3)
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
				solver->AddToClause(nexts, true);
				solver->AddClause(totalvars);
				noldstates++;
				nnewstates++;


			}
			thise+=2;
			delete oldtrans;
			delete oldevent;
			oldtrans=newtrans;
			oldevent=newevent;
			noldtrans=nnewtrans;
		}
		
		while (thise<negCycle.size()-1)
		{
			cout << endl << "******************************ERROR8****************";
			nexts=1 + solver->SATNewVar();
			newstates[nnewstates]=nexts;
				if (t>0)
				{
					solver->ResetClause();
					solver->AddToClause(oldstates[noldstates], false);
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
					solver->AddToClause(newstates[nnewstates], true);
					solver->AddClause(totalvars);

					solver->ResetClause();
					solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), false);
					solver->AddToClause(newstates[nnewstates], false);
					solver->AddClause(totalvars);


				}
			int *newtrans= new int[pProblem.pAllAction.size()*2];
			int *newevent= new int[pProblem.pAllAction.size()*2];
			int nnewtrans=0;
			//if (Pos_SimilarA[i]>thise+1)
			//{
				newtrans[nnewtrans]=1 + solver->SATNewVar();
				newevent[nnewtrans]=negCycle[thise+1].id*2+negCycle[thise+1].part;
				nnewtrans++;
			//}

			for (int j=0; j<nnewtrans; j++)
			{
				solver->ResetClause();
				solver->AddToClause(oldstates[noldstates], false);
				solver->AddToClause(newtrans[j], true);

				solver->AddClause(totalvars);
			}
			
			for (int j=0; j<noldtrans; j++)
				for (int k=0; k<nnewtrans; k++)
					if (oldevent[j]<newevent[k])
					{
						solver->ResetClause();
						solver->AddToClause(oldtrans[j], false);
						if (oldevent[j]%2==0)
							solver->AddToClause(solver->ActionTime2Var(oldevent[j]/2, t, ACTION_START), false);
						else
							solver->AddToClause(solver->ActionTime2Var((oldevent[j]-1)/2, t, ACTION_END), false);
						solver->AddToClause(newtrans[k], true);
						solver->AddClause(totalvars);
					}

			if (noldtrans!=1)
				cout << endl << "******************************ERROR5****************";
			if (nnewtrans!=1)
				cout << endl << "******************************ERROR5****************";

			solver->ResetClause();
			solver->AddToClause(oldtrans[0], false);
			if (oldevent[0]%2==0)
				solver->AddToClause(solver->ActionTime2Var(oldevent[0]/2, t, ACTION_START), false);
			else
				solver->AddToClause(solver->ActionTime2Var((oldevent[0]-1)/2, t, ACTION_END), false);
			if (thise<negCycle.size()-2)
				solver->AddToClause(solver->ActionTime2Var(negCycle[0].id, t, ACTION_END), true);
			solver->AddToClause(newstates[nnewstates], true);
			solver->AddClause(totalvars);
			nnewstates++;
			noldstates++;
			thise++;
			delete oldtrans;
			delete oldevent;
			oldtrans=newtrans;
			oldevent=newevent;
			noldtrans=nnewtrans;

		}
		solver->ResetClause();
		solver->AddToClause(nexts, false);
		solver->AddClause(totalvars);
		delete oldstates;
		oldstates=newstates;
		noldstates=nnewstates;
	}	*/

}

/*
void Fill_SimilarA(const vector<PlanEvent> &negCycle, std::back_insert_iterator< vector< set<int> > > it, std::back_insert_iterator< vector<int> > itpos)
{
	// [FrameS TAK1 [AS AE] TAK2 [BS BE] [CS CE] TAK3 FrameE]
	int sz = negCycle.size();
	PlanEvent nodeS, nodeE, nodeBeforeS, nodeAfterE;
	set<int> result;
	set<int> similar_nodeS, similar_nodeE, stmp;
	similar_nodeS.clear();
	similar_nodeE.clear();
	set<int>::const_iterator ra;
	for(int i=1; i<sz-1; i++)
	{

#pragma region init nodes && actions
		nodeS = negCycle[i];
		nodeE = negCycle[i+1];
		nodeAfterE = negCycle[i+2];
		nodeBeforeS = negCycle[i-1];
		if(nodeS.id != nodeE.id) // if this is a lonely event
			continue; // skip it
		else
		{
			*itpos++ = i; // save position of this couple
			++i; // otherwise increment i to consider its end event
		}
		const PAction &Before = *pProblem.pAllAction.GetActionById(nodeBeforeS.id);
		const PAction &A = *pProblem.pAllAction.GetActionById(nodeS.id); // nodeE.id is the same
		const PAction &After = *pProblem.pAllAction.GetActionById(nodeAfterE.id);
		const set<int> *beforePre, *beforeAdd, *beforeDel;
		const set<int> *afterPre, *afterAdd, *afterDel;
		if(nodeBeforeS.part == 0) // holds when i==1
		{
			beforePre = &Before.conditionAtStart;
			beforeAdd = &Before.addEffectAtStart;
			beforeDel = &Before.delEffectAtStart;
		}
		else // holds when i!=1
		{
			beforePre = &Before.conditionAtEnd;
			beforeAdd = &Before.addEffectAtEnd;
			beforeDel = &Before.delEffectAtEnd;
		}
		if(nodeAfterE.part == 0) // holds when i!=sz-3
		{
			afterPre = &After.conditionAtStart;
			afterAdd = &After.addEffectAtStart;
			afterDel = &After.delEffectAtStart;
		}
		else // holds when i==sz-3 (last step)
		{
			afterPre = &After.conditionAtEnd;
			afterAdd = &After.addEffectAtEnd;
			afterDel = &After.delEffectAtEnd;
		}
#pragma endregion

		// in the following code we use std::set_intersection() and std::set_union()
		// input of these functions must be sorted. but it does not need to be a "set"

#pragma region find similar_nodeS
		stmp.clear();
		result.clear();
		std::set_intersection(beforeAdd->begin(), beforeAdd->end(), A.conditionOverAll.begin(), A.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->conditionOverAll.begin(), p->conditionOverAll.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));

			//similar_nodeS.swap(stmp);
		}

		result.clear();
		std::set_intersection(beforeAdd->begin(), beforeAdd->end(), A.conditionAtStart.begin(), A.conditionAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->conditionAtStart.begin(), p->conditionAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeS.swap(stmp);
		}

		result.clear();
		std::set_intersection(beforeAdd->begin(), beforeAdd->end(), A.delEffectAtStart.begin(), A.delEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->delEffectAtStart.begin(), p->delEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeS.swap(stmp);
		}

		result.clear();
		std::set_intersection(beforeDel->begin(), beforeDel->end(), A.addEffectAtStart.begin(), A.addEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->addEffectAtStart.begin(), p->addEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeS.swap(stmp);
		}

		result.clear();
		std::set_intersection(beforePre->begin(), beforePre->end(), A.delEffectAtStart.begin(), A.delEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->delEffectAtStart.begin(), p->delEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeS.swap(stmp);
		}

		if(nodeBeforeS.part == ACTION_END)
		{
			result.clear();
			std::set_intersection(Before.conditionOverAll.begin(), Before.conditionOverAll.end(), A.delEffectAtStart.begin(), A.delEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
			for(ra = result.begin(); ra != result.end(); ++ra)
			{
				PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
				std::set_union(p->delEffectAtStart.begin(), p->delEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
				//similar_nodeS.swap(stmp);
			}
		}

		if(nodeS.part == ACTION_START) // Always holds
		{
			result.clear();
			std::set_intersection(beforeDel->begin(), beforeDel->end(), A.conditionOverAll.begin(), A.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
			for(ra = result.begin(); ra != result.end(); ++ra)
			{
				PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
				std::set_union(p->conditionOverAll.begin(), p->conditionOverAll.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
				//similar_nodeS.swap(stmp);
			}
		}
		similar_nodeS.swap(stmp);
		if(similar_nodeS.empty())
			throw logic_error("Error in negative cycle: similar_nodeS.empty()");

#pragma endregion

#pragma region find similar_nodeE
		stmp.clear();
		result.clear();
		std::set_intersection(A.addEffectAtEnd.begin(), A.addEffectAtEnd.end(), After.conditionOverAll.begin(), After.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->addEffectAtEnd.begin(), p->addEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeE.swap(stmp);
		}

		result.clear();
		std::set_intersection(A.addEffectAtEnd.begin(), A.addEffectAtEnd.end(), afterPre->begin(), afterPre->end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->addEffectAtEnd.begin(), p->addEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeE.swap(stmp);
		}

		result.clear();
		std::set_intersection(A.addEffectAtEnd.begin(), A.addEffectAtEnd.end(), afterDel->begin(), afterDel->end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->addEffectAtEnd.begin(), p->addEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeE.swap(stmp);
		}

		result.clear();
		std::set_intersection(A.delEffectAtEnd.begin(), A.delEffectAtEnd.end(), afterAdd->begin(), afterAdd->end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeE.swap(stmp);
		}

		result.clear();
		std::set_intersection(A.conditionAtEnd.begin(), A.conditionAtEnd.end(), afterDel->begin(), afterDel->end(), std::insert_iterator<set<int> >(result, result.end()));
		for(ra = result.begin(); ra != result.end(); ++ra)
		{
			PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
			std::set_union(p->conditionAtEnd.begin(), p->conditionAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
			//similar_nodeE.swap(stmp);
		}

		if(nodeE.part == ACTION_END) // Always holds
		{
			result.clear();
			std::set_intersection(A.conditionOverAll.begin(), A.conditionOverAll.end(), afterDel->begin(), afterDel->end(), std::insert_iterator<set<int> >(result, result.end()));
			for(ra = result.begin(); ra != result.end(); ++ra)
			{
				PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
				std::set_union(p->conditionOverAll.begin(), p->conditionOverAll.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
				//similar_nodeE.swap(stmp);
			}
		}

		if(nodeAfterE.part == ACTION_START)
		{
			result.clear();
			std::set_intersection(A.delEffectAtEnd.begin(), A.delEffectAtEnd.end(), After.conditionOverAll.begin(), After.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
			for(ra = result.begin(); ra != result.end(); ++ra)
			{
				PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
				std::set_union(p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
				//similar_nodeE.swap(stmp);
			}
		}
		similar_nodeE.swap(stmp);
		if(similar_nodeE.empty())
			throw logic_error("Error in negative cycle: similar_nodeE.empty()");

#pragma endregion

		// intersection(similar_nodeS, similar_nodeE) :
		stmp.clear();
		std::set_intersection(similar_nodeS.begin(), similar_nodeS.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));

		// filter the result of intersection, so that actions with duration < A.duration will be dropped
		result.clear();
		for(ra = stmp.begin(); ra != stmp.end(); ++ra)
		{
			const PAction &SimA = *pProblem.pAllAction.GetActionById(*ra);
			if(SimA.duration >= A.duration)
				result.insert(*ra);
		}

		// append A itself
		result.insert(A.id);
		*it++ = result;

		// clear temporal variables
		similar_nodeS.clear();
		similar_nodeE.clear();
		stmp.clear();
	}
}

/// FIXME: this function is not being used. remove it or find a use for it
void Fill_SimilarA_Frame(const vector<PlanEvent> &negCycle, std::back_insert_iterator< vector< set<int> > > it)
{
	// [FrameS [AS AE] [BS BE] [CS CE] FrameE]
	int sz = negCycle.size();
	PlanEvent FrameS, AS, CE, FrameE;

	FrameS = negCycle[0];
	AS = negCycle[1];
	CE = negCycle[sz-2];
	FrameE = negCycle[sz-1];

	const PAction &Frame = *pProblem.pAllAction.GetActionById(FrameS.id); // FrameS.id == FrameE.id
	const PAction &A = *pProblem.pAllAction.GetActionById(AS.id);
	const PAction &C = *pProblem.pAllAction.GetActionById(CE.id);

	set<int> result;
	set<int> similar_nodeS, similar_nodeE, stmp;
	set<int>::const_iterator ra;

	// in the following code we use std::set_intersection() and std::set_union()
	// input of these functions must be sorted. but it does not need to be a "set"

#pragma region find similar_nodeS

	result.clear();
	std::set_intersection(Frame.addEffectAtStart.begin(), Frame.addEffectAtStart.end(), A.conditionOverAll.begin(), A.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->addEffectAtStart.begin(), p->addEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	result.clear();
	std::set_intersection(Frame.addEffectAtStart.begin(), Frame.addEffectAtStart.end(), A.conditionAtStart.begin(), A.conditionAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->addEffectAtStart.begin(), p->addEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	result.clear();
	std::set_intersection(Frame.addEffectAtStart.begin(), Frame.addEffectAtStart.end(), A.delEffectAtStart.begin(), A.delEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->addEffectAtStart.begin(), p->addEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	result.clear();
	std::set_intersection(Frame.delEffectAtStart.begin(), Frame.delEffectAtStart.end(), A.addEffectAtStart.begin(), A.addEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->delEffectAtStart.begin(), p->delEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	result.clear();
	std::set_intersection(Frame.conditionAtStart.begin(), Frame.conditionAtStart.end(), A.delEffectAtStart.begin(), A.delEffectAtStart.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->conditionAtStart.begin(), p->conditionAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	//if(FrameS.part == ACTION_START) // Always holds
	result.clear();
	std::set_intersection(Frame.delEffectAtStart.begin(), Frame.delEffectAtStart.end(), A.conditionOverAll.begin(), A.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->delEffectAtStart.begin(), p->delEffectAtStart.end(), similar_nodeS.begin(), similar_nodeS.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeS.swap(stmp);
	}

	if(similar_nodeS.empty())
		throw logic_error("Error in negative cycle: similar_nodeS.empty()");

#pragma endregion

#pragma region find similar_nodeE

	result.clear();
	std::set_intersection(C.addEffectAtEnd.begin(), C.addEffectAtEnd.end(), Frame.conditionOverAll.begin(), Frame.conditionOverAll.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->conditionOverAll.begin(), p->conditionOverAll.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	result.clear();
	std::set_intersection(C.addEffectAtEnd.begin(), C.addEffectAtEnd.end(), Frame.conditionAtEnd.begin(), Frame.conditionAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->conditionAtEnd.begin(), p->conditionAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	result.clear();
	std::set_intersection(C.addEffectAtEnd.begin(), C.addEffectAtEnd.end(), Frame.delEffectAtEnd.begin(), Frame.delEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	result.clear();
	std::set_intersection(C.delEffectAtEnd.begin(), C.delEffectAtEnd.end(), Frame.addEffectAtEnd.begin(), Frame.addEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->addEffectAtEnd.begin(), p->addEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	result.clear();
	std::set_intersection(C.conditionAtEnd.begin(), C.conditionAtEnd.end(), Frame.delEffectAtEnd.begin(), Frame.delEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	// if(FrameE.part == ACTION_END) // Always holds
	result.clear();
	std::set_intersection(C.conditionOverAll.begin(), C.conditionOverAll.end(), Frame.delEffectAtEnd.begin(), Frame.delEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
	for(ra = result.begin(); ra != result.end(); ++ra)
	{
		PProposition *p = pProblem.pAllProposition.GetPropositionById(*ra);
		std::set_union(p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));
		similar_nodeE.swap(stmp);
	}

	if(similar_nodeE.empty())
		throw logic_error("Error in negative cycle: similar_nodeE.empty()");

#pragma endregion

	// intersection(similar_nodeS, similar_nodeE)
	stmp.clear();
	std::set_intersection(similar_nodeS.begin(), similar_nodeS.end(), similar_nodeE.begin(), similar_nodeE.end(), std::insert_iterator<set<int> >(stmp, stmp.end()));

	// filter the result of intersection, so that actions with duration > A.duration will be dropped
	result.clear();
	for(ra = stmp.begin(); ra != stmp.end(); ++ra)
	{
		const PAction &SimFrame = *pProblem.pAllAction.GetActionById(*ra);
		if(SimFrame.duration <= A.duration)
			result.insert(*ra);
	}

	// append the Frame itself
	result.insert(Frame.id);
	*it++ = result;
}
*/