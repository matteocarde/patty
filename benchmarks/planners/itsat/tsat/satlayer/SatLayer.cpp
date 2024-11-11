#include <fstream>
#include <set> // used in *AddMutex*()
#include <algorithm> // used in SplitLayer(), *AddMutex*()
#include <iterator> // used in *AddMutex*()
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/satlayer/SatLayer.h"

using namespace std;
using namespace MyParser;
using namespace nsSatLayer;

#pragma region MACROS
#define CheckForTimeOut() if(totalTime - (CPUTime() - startTime) < 0) throw runtime_error("Timeout during encoding.")

//#define PropTime_Var(p,t) (1+p+(t)*nProp)
//#define ActionTime_Var(a,t) (1+nGap+a+(t)*nAction)

// used with *cnf<< to create CNF file (ToSolve.cnf)
#define cnf_True(n) (n)
#define cnf_False(n) (-n)

// used with *readcnf<< to create readable CNF file (ToRead.txt)
#define readcnf_TProp(p,t) "p("<<p<<","<<t<<")"
#define readcnf_NProp(p,t) "~p("<<p<<","<<t<<")"
#define readcnf_TPre(p,t) "pre("<<p<<","<<t<<")"
#define readcnf_NPre(p,t) "~pre("<<p<<","<<t<<")"
#define readcnf_TActionS(a,t) "as("<<a<<","<<t<<")"
#define readcnf_NActionS(a,t) "~as("<<a<<","<<t<<")"
#define readcnf_TActionE(a,t) "ae("<<a<<","<<t<<")"
#define readcnf_NActionE(a,t) "~ae("<<a<<","<<t<<")"
#define readcnf_TActionO(a,t) "ao("<<a<<","<<t<<")"
#define readcnf_NActionO(a,t) "~ao("<<a<<","<<t<<")"
#pragma endregion

SatLayer::SatLayer(
	int t, SATResults *results,
	string planfilename, string detailsfilenametemplate, float totaltime=60,
	bool gen_cnf=false, bool gen_readable_cnf=false, bool dont_solve=false, int conflictsMethod=1)
	:
		T(t), satresults(results),
		planFileName(planfilename), detailsFileNameTemplate(detailsfilenametemplate), totalTime(totaltime),
		ccEvent(0), ccInit(0), ccGoal(0), ccNotApplicable(0), ccCondition(0), ccEffect(0), ccAxiomDelete(0),
		ccAxiomAdd(0), ccMutexStart(0), ccMutexEnd(0), ccMutexStartEnd(0), ccMutexOverall(0),
		GEN_CNF(gen_cnf), GEN_READABLE_CNF(gen_readable_cnf), DONT_SOLVE(dont_solve),
		CONFLICTS_METHOD(conflictsMethod)
{
	startTime = CPUTime();

	nProp = pProblem.pAllProposition.size();
	nAction = pProblem.pAllAction.size();
	nvProp = nProp * (T+1);
	nvEvent = 3 * nAction*T;
	index2var = new int[2*nvProp + nvEvent];
	for(int i=0; i<2*nvProp + nvEvent; i++)
		index2var[i] = -1;
	
	if(GEN_CNF)
	{
		char tosolvefilename[256];
		sprintf(tosolvefilename, "%s-T=%d.cnf", detailsFileNameTemplate.c_str(), T);
		cnf = new ofstream(tosolvefilename);
		// first argument is the number of variables
		// second argument is said to be the number of clauses. but it is not used in zchaff.exe
		*cnf << "p cnf " << nvProp + nvEvent <<" 0" << "\n";
	}

	if(GEN_READABLE_CNF)
	{
		char toreadfilename[256];
		sprintf(toreadfilename, "%s-T=%d.txt", detailsFileNameTemplate.c_str(), T);
		readcnf = new ofstream(toreadfilename);
	}
}

void SatLayer::DoEncoding(bool **mutextable, bool *compress)
{
	AddActionVariableRelations(compress);

	AddInitialState();
	AddGoals();
//	if(CONFLICTS_METHOD == 3)
		//Old_AddConditionsEffects();
//	else
//		AddConditionsEffects();
//	AddExplanatoryAxioms();
//	if(CONFLICTS_METHOD == 1)
//		AddMutexStart_End_nlogn();
//	else if(CONFLICTS_METHOD == 2)
//		AddMutexStart_End_n2();
//	else //if(CONFLICTS_METHOD == 3)
		Old_AddMutexStart_End(mutextable,compress);

	for(int t=0; t<=T; t++)
		for (int i=0; i<nProp; i++)
			for (int j=i; j<nProp; j++)
				if (mutextable[i][j])
				{
					ResetClause();
					AddToClause(PropTime2Var(i, t), false);
					AddToClause(PropTime2Var(j, t), false);
					AddClause(ccCondition);

				}

	if(GEN_CNF)
		cnf->close();
	if(GEN_READABLE_CNF)
		readcnf->close();
	Report_CNFStats();
}

void SatLayer::DoEncoding(vector< vector<Mutex> > *fact_mutex, vector<int> *prop_layer)
{
	AddActionVariableRelations(0);
	AddInitialState();
	AddGoals();

//	if(CONFLICTS_METHOD == 3)
	Old_AddConditionsEffects();
//	else
//		AddConditionsEffects();

	//AddExplanatoryAxioms();

	if(CONFLICTS_METHOD == 1)
		AddMutexStart_End_nlogn();
	else if(CONFLICTS_METHOD == 2)
		AddMutexStart_End_n2();
	else //if(CONFLICTS_METHOD == 3)
		Old_AddMutexStart_End(0,0);

	if(fact_mutex)
		AddFactMutexes(fact_mutex);
	if(prop_layer)
		AddPropForbidClauses(prop_layer);

	/////////////////////////////////////////////////// NEW: ACTION MUTEXES //////////////////////////////////////////////////////
	int graphLayers = fact_mutex->size();
	int effective_t;
	effective_t = graphLayers - 1;
	set<int>::const_iterator it1, it2, it3;
	vector<Mutex> &vm = (*fact_mutex)[effective_t];	
	bool **mutextable = new bool*[nProp];
	for (int j=0; j<nProp; j++)
	{
		mutextable[j]=new bool[nProp];
		for (int k=0; k<nProp; k++)
			mutextable[j][k]=false;
	}

	for (int j=0; j<nAction; j++)
	{
		for(vector<Mutex>::const_iterator it = vm.begin(); it != vm.end(); ++it)
		{
			if((it->first >= nProp) || (it->second >= nProp))
				continue;
			mutextable[it->first][it->second]=true;
			mutextable[it->second][it->first]=true;
			//cout << endl << it->first << "   " << it->second;
		}
		//exit(0);
		const PAction *a1 = pProblem.pAllAction.GetActionById(j);
		for (int k=j+1; k<nAction; k++)
		{
			const PAction *a2 = pProblem.pAllAction.GetActionById(k);
			bool foundss=false;
			bool foundse=false;
			bool foundes=false;
			bool foundee=false;
			for (it1=a1->conditionAtStart.begin(); it1 != a1->conditionAtStart.end(); ++it1)
			{
				int p1=*it1;
				for (it2=a1->addEffectAtStart.begin(); it2 != a1->addEffectAtStart.end(); ++it2)
					mutextable[*it1][*it2]=false;
				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				

				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
						
				if (!foundss)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
			}


			for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
			{
				int p1=*it1;
				for (it2=a1->addEffectAtStart.begin(); it2 != a1->addEffectAtStart.end(); ++it2)
					mutextable[*it1][*it2]=false;
				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				
				if (!foundss)
				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
						
				if (!foundss)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
			}
			for (it1=a1->addEffectAtStart.begin(); it1 != a1->addEffectAtStart.end(); ++it1)
			{
				int p1=*it1;
				for (it2=a1->addEffectAtStart.begin(); it2 != a1->addEffectAtStart.end(); ++it2)
					mutextable[*it1][*it2]=false;
				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				
				if (!foundss)
				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
						
				if (!foundss)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundss=true;
					}
					if (foundss)
						break;
				}
			}
////////////////////////////////////////////////////////////////////////////////////////////////////////
			for (it1=a1->conditionAtEnd.begin(); it1 != a1->conditionAtEnd.end(); ++it1)
			{
				int p1=*it1;

				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				

				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
						
				if (!foundes)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
			}


			for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
			{
				int p1=*it1;

				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				
				if (!foundes)
				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
						
				if (!foundes)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
			}
			for (it1=a1->addEffectAtEnd.begin(); it1 != a1->addEffectAtEnd.end(); ++it1)
			{
				int p1=*it1;
				
				for (it2=a1->addEffectAtEnd.begin(); it2 != a1->addEffectAtEnd.end(); ++it2)
					mutextable[*it1][*it2]=false;				
				if (!foundes)
				for (it2=a2->conditionAtStart.begin(); it2 != a2->conditionAtStart.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
						
				if (!foundes)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_START), false);					
							AddClause(ccMutexStartEnd);
						}
						foundes=true;
					}
					if (foundes)
						break;
				}
			}

			for (it2=a2->addEffectAtStart.begin(); it2 != a2->addEffectAtStart.end(); ++it2)
			{
				for (it1=a1->conditionAtStart.begin(); it1 != a1->conditionAtStart.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->addEffectAtStart.begin(); it1 != a1->addEffectAtStart.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->conditionAtEnd.begin(); it1 != a1->conditionAtEnd.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->addEffectAtEnd.begin(); it1 != a1->addEffectAtEnd.end(); ++it1)
					mutextable[*it1][*it2]=false;
			}
//////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
			for (it1=a1->conditionAtStart.begin(); it1 != a1->conditionAtStart.end(); ++it1)
			{
				int p1=*it1;
			

				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
						
				if (!foundse)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
			}


			for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
			{
				int p1=*it1;
				
				if (!foundse)
				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
						
				if (!foundse)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
			}
			for (it1=a1->addEffectAtStart.begin(); it1 != a1->addEffectAtStart.end(); ++it1)
			{
				int p1=*it1;
			
				if (!foundse)
				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
						
				if (!foundse)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_START), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundse=true;
					}
					if (foundse)
						break;
				}
			}
////////////////////////////////////////////////////////////////////////////////////////////////////////
			for (it1=a1->conditionAtEnd.begin(); it1 != a1->conditionAtEnd.end(); ++it1)
			{
				int p1=*it1;

				

				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
						
				if (!foundee)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
			}


			for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
			{
				int p1=*it1;

			
				if (!foundee)
				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
						
				if (!foundee)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
			}
			for (it1=a1->addEffectAtEnd.begin(); it1 != a1->addEffectAtEnd.end(); ++it1)
			{
				int p1=*it1;
			
				if (!foundee)
				for (it2=a2->conditionAtEnd.begin(); it2 != a2->conditionAtEnd.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
						
				if (!foundee)	
				for (it2=a2->conditionOverAll.begin(); it2 != a2->conditionOverAll.end(); ++it2)
				{
					if (mutextable[p1][*it2])
					{
						for(int t=0; t<T; t++)
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t, ACTION_END), false);

							AddToClause(ActionTime2Var(k, t, ACTION_END), false);					
							AddClause(ccMutexStartEnd);
						}
						foundee=true;
					}
					if (foundee)
						break;
				}
			}

			for (it2=a2->addEffectAtEnd.begin(); it2 != a2->addEffectAtEnd.end(); ++it2)
			{
				for (it1=a1->conditionAtStart.begin(); it1 != a1->conditionAtStart.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->conditionOverAll.begin(); it1 != a1->conditionOverAll.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->addEffectAtStart.begin(); it1 != a1->addEffectAtStart.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->conditionAtEnd.begin(); it1 != a1->conditionAtEnd.end(); ++it1)
					mutextable[*it1][*it2]=false;
				for (it1=a1->addEffectAtEnd.begin(); it1 != a1->addEffectAtEnd.end(); ++it1)
					mutextable[*it1][*it2]=false;
			}
		}
	}




	/////////////////////////////////////////////////// NEW: ACTION MUTEXES //////////////////////////////////////////////////////

	if(GEN_CNF)
		cnf->close();
	if(GEN_READABLE_CNF)
		readcnf->close();
	Report_CNFStats();
}

void SatLayer::SplitLayers(int factor)
{
	int nEvent = nAction*2;
	// int sectionSize = ceil((float)nEvent / (float)factor);
	vector<pair<int,int> > idActions;
	for(int i=0; i<nAction; i++)
	{
		pair<int,int> ev;
		ev.first = i;
		ev.second = 0;
		idActions.push_back(ev);
		ev.second = 1;
		idActions.push_back(ev);
	}
	random_shuffle(idActions.begin(), idActions.end());
	
	vector<int> eventLayers (nEvent);
	for(int i=0; i<nEvent; i++)
	{
		eventLayers[idActions[i].first * 2 + idActions[i].second] = i / (nEvent/factor);
	}

	for(int t=0; t<T; t++)
	{
		int tmod = t % factor;
		for(int i=0; i<nAction; i++)
		{
			for(int j=0; j<=1; j++)
			{
				if( tmod != eventLayers[i*2+j] )
				{
					ResetClause();
					AddToClause(ActionTime2Var(i, t, j), false);
					AddClause(ccEvent);
					//if(GEN_CNF)
					//	*cnf << cnf_False(ActionTime2Var(i, t, j)) << " 0\n";
					//if(GEN_READABLE_CNF)
					//{
					//	switch(j)
					//	{
					//	case 0:
					//		*readcnf << readcnf_NActionS(i, t) << "\n";
					//		break;
					//	case 1:
					//		*readcnf << readcnf_NActionE(i, t) << "\n";
					//		break;
					//	case 2:
					//		*readcnf << readcnf_NActionO(i, t) << "\n";
					//		break;
					//	}
					//}
				}
			}
		}
	}
}

//void SatLayer::SplitLayers(int factor)
//{
//	vector<pair<int,int>> idActions;
//	pair<int,int> ev;
//	int nEvent = nAction*3;
//	for(int i=0; i<nAction; i++)
//	{
//		ev.first = i;
//		ev.second = 0;
//		idActions.push_back(ev);
//		ev.second = 1;
//		idActions.push_back(ev);
//		ev.second = 2;
//		idActions.push_back(ev);
//	}
//	random_shuffle(idActions.begin(), idActions.end());
//	for(int t=0; t<T; t+=factor)
//	{
//		int sectionSize = ceil((float)nEvent / (float)factor);
//		cout << endl << "t = " << t << " sectionSize = " << sectionSize << endl;
//		for(int sectionBegin=0, sectionNumber=0; sectionBegin<nEvent; sectionBegin += sectionSize, sectionNumber++)
//		{
//			int sectionEnd = sectionBegin + sectionSize;
//			int effectiveFactor = factor;
//			if(T-t < factor)
//				effectiveFactor = T-t;
//			cout << "[" << sectionNumber << "," << effectiveFactor << "," << sectionBegin << "]  ";
//			for(int i=0; i < effectiveFactor; i++)
//			{
//				if(i == sectionNumber)
//					continue;
//				for(int j=sectionBegin; j<sectionEnd; j++)
//				{
//					ResetClause();
//					AddToClause(ActionTime2Var(idActions[j].first, t+i, idActions[j].second), false);
//					AddClause(ccEvent);
//					if(GEN_CNF)
//						*cnf << cnf_False(ActionTime2Var(idActions[j].first, t+i, idActions[j].second)) << " 0\n";
//					if(GEN_READABLE_CNF)
//					{
//						switch(idActions[j].second)
//						{
//						case 0:
//							*readcnf << readcnf_NActionS(i, 0) << "\n";
//							break;
//						case 1:
//							*readcnf << readcnf_NActionE(i, 0) << "\n";
//							break;
//						case 2:
//							*readcnf << readcnf_NActionO(i, 0) << "\n";
//							break;
//						}
//					}
//				}
//			}
//		}
//	}
//}

void SatLayer::AddPropForbidClauses(vector<int> *prop_layer)
{
	int i=0;
	for(vector<int>::const_iterator it = prop_layer->begin(); it != prop_layer->end(); ++it, i++)
	{
		int tmax;
		if(*it == -1)
			tmax = T;
		else
		{
			continue;
			tmax = *it - 1;
			if(tmax > T)
				tmax = T;
		}
		if(i<nProp)
			for(int t=0; t<=tmax; t++)
			{
				ResetClause();
				AddToClause(PropTime2Var(i, t), false);
				AddClause(ccNotApplicable); // FIXME: fix stats
				if(GEN_CNF)
					*cnf << cnf_False(PropTime2Var(i, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NProp(i, t) << " 0\n";
			}
		else
			for(int t=0; t<tmax; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i-nProp, t, ACTION_OVERALL), false);
				AddClause(ccNotApplicable); // FIXME: fix stats
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i-nProp, t, ACTION_OVERALL)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionO(i-nProp, t) << " 0\n";
			}
	}
}

void SatLayer::AddFactMutexes(vector< vector<Mutex> > *fact_mutex)
{
	int graphLayers = fact_mutex->size();
	for(int t=0; t<=T; t++)
	{
		CheckForTimeOut();
		int effective_t;
		//if(t >= graphLayers)
			effective_t = graphLayers - 1;
		//else
			//effective_t = t;
		vector<Mutex> &vm = (*fact_mutex)[effective_t];
		for(vector<Mutex>::const_iterator it = vm.begin(); it != vm.end(); ++it)
		{
			
			//if(t==T)
				//if(!(it->first < nProp && it->second < nProp))
					//continue;
			if(t==T)
				if((it->first >= nProp) || (it->second >= nProp))
					continue;
			ResetClause();
			if(it->first < nProp)
				AddToClause(PropTime2Var(it->first, t), false);
			else
				AddToClause(ActionTime2Var(it->first - nProp, t, ACTION_OVERALL), false);
			if(it->second < nProp)
				AddToClause(PropTime2Var(it->second, t), false);
			else
				AddToClause(ActionTime2Var(it->second - nProp, t, ACTION_OVERALL), false);
			AddClause(ccNotApplicable); // FIXME: fix stats
			// FIXME: fix these rules:
			//if(GEN_CNF)
			//	*cnf << cnf_False(PropTime2Var(it->a, t)) << " " << cnf_False(PropTime2Var(it->b, t)) << " 0\n";
			//if(GEN_READABLE_CNF)
			//	*readcnf << readcnf_NProp(it->a, t) << " " <<  readcnf_NProp(it->b, t) << " 0\n";
		}
	}
}

void SatLayer::AddActionVariableRelations(bool *compress)
{
	//cout << "$$$$$$$$$$$$$$$$$$$$$$$$$$" << endl; 
	for(int i=0; i<nAction; i++)
	{
		//CheckForTimeOut();
		// ~ao(0)
		if (!compress[i])
		{
			ResetClause();
			AddToClause(ActionTime2Var(i, 0, 2), false);
			AddClause(ccEvent);
		}
		// ao(T-1) => ae(T-1) 
		if (!compress[i])
		{
			ResetClause();
			AddToClause(ActionTime2Var(i, T-1, 2), false);
			AddToClause(ActionTime2Var(i, T-1, 1), true);
			AddClause(ccEvent);
		}
		// ~as(T-1) || ae(T-1)
		if (!compress[i])
		{
			ResetClause();
			AddToClause(ActionTime2Var(i, T-1, 0), false);
			AddToClause(ActionTime2Var(i, T-1, 1), true);
			AddClause(ccEvent);
		}
		for(int t=0; t<T; t++)
		{
			// as(i) => ~ao(i)
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(ActionTime2Var(i, t, 2), false);
				AddClause(ccEvent);
			}

			// ae(i) => ao(i) || as(i)
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(ActionTime2Var(i, t, 2), true);
				AddToClause(ActionTime2Var(i, t, 0), true);
				AddClause(ccEvent);
			}
			// ae(i) <=> as(i) ************************************ SHOULD BE REMOVED IF COMPRESSION IS OMITTED *******************************************************
			if (compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(ActionTime2Var(i, t, 1), true);
				AddClause(ccEvent);
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(ActionTime2Var(i, t, 0), true);
				AddClause(ccEvent);
				const PAction *a1 = pProblem.pAllAction.GetActionById(i);
				set<int>::const_iterator it1, it2, it3;
				bool flag=false;
				bool found=false;
				for (it1=a1->addEffectAtEnd.begin(); it1!=a1->addEffectAtEnd.end(); it1++)
				{
					found=false;
					for (it2=a1->conditionAtStart.begin(); it2!=a1->conditionAtStart.end(); it2++)
						if (*it1==*it2)
							found=true;
					if (found==false)
						flag=true;
				}
				if ((flag==false) && (a1->addEffectAtStart.size()==0))
				{
					ResetClause();
					AddToClause(ActionTime2Var(i, t, 0), false);
					AddClause(ccEvent);
				}
			}
			//******************************************************************************************************************************
		}
		for(int t=0; t<T-1; t++)
		{
			// as(i) => ao(i+1) || ae(i)   
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(ActionTime2Var(i, t, 1), true);
				AddToClause(ActionTime2Var(i, t+1, 2), true);
				AddClause(ccEvent);
			}
			// ae(i) => ~ao(i+1) 
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(ActionTime2Var(i, t+1, 2), false);
				AddClause(ccEvent);
			}
			// ao(i) && ~ao(i+1) => ae(i) 
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 2), false);
				AddToClause(ActionTime2Var(i, t+1, 2), true);
				AddToClause(ActionTime2Var(i, t, 1), true);

				AddClause(ccEvent);
			}


			// ~ao(i) && ao(i+1) => as(i)
			if (!compress[i])
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 2), true);
				AddToClause(ActionTime2Var(i, t+1, 2), false);
				AddToClause(ActionTime2Var(i, t, 0), true);
				AddClause(ccEvent);
			}
			// ~ao(i) && ao(i+1) => ~ae(i)
			/*ResetClause();
			AddToClause(ActionTime2Var(i, t, 2), true);
			AddToClause(ActionTime2Var(i, t+1, 2), false);
			AddToClause(ActionTime2Var(i, t, 1), false);
			AddClause(ccEvent);*/


		}
	}
}

void SatLayer::AddInitialState()
{
	bool *initialPositive = new bool[pProblem.pAllProposition.size()];
	for(int i=0; i<pProblem.pAllProposition.size(); i++)
	{
		initialPositive[i] = false;
	}
	for(int i=0; i<pProblem.initialState.size(); i++)
	{
		ResetClause();
		AddToClause(PropTime2Var(pProblem.initialState[i], 0), true);
		AddClause(ccInit);
		initialPositive[pProblem.initialState[i]] = true;
		if(GEN_CNF)
			*cnf << cnf_True(PropTime2Var(pProblem.initialState[i], 0)) << " 0\n";
		if(GEN_READABLE_CNF)
			*readcnf << readcnf_TProp(pProblem.initialState[i], 0) << "\n";
	}
	for(int i=0; i<pProblem.pAllProposition.size(); i++)
	{
		if(!initialPositive[i])
		{
			ResetClause();
			AddToClause(PropTime2Var(i, 0), false);
			AddClause(ccInit);
			if(GEN_CNF)
				*cnf << cnf_False(PropTime2Var(i, 0)) << " 0\n";
			if(GEN_READABLE_CNF)
				*readcnf << readcnf_NProp(i, 0) << "\n";
		}
	}
	delete[] initialPositive;
}

void SatLayer::AddGoals()
{
	for(int i=0; i<pProblem.goals.size(); i++)
	{
		ResetClause();
		AddToClause(PropTime2Var(pProblem.goals[i], T), true);
		AddClause(ccGoal);
		if(GEN_CNF)
			*cnf << cnf_True(PropTime2Var(pProblem.goals[i], T)) << " 0\n";
		if(GEN_READABLE_CNF)
			*readcnf << readcnf_TProp(pProblem.goals[i], T) << "\n";
	}
}

// includes a variable for Pre(precondition)
void SatLayer::AddConditionsEffects()
{
	for(int i=0; i<nAction; i++)
	{
		CheckForTimeOut();
		const PAction *a = pProblem.pAllAction.GetActionById(i);
		int prp;
		set<int>::const_iterator it;
		for(it = a->conditionAtStart.begin(); it != a->conditionAtStart.end(); ++it)
		{
			prp = *it;
			// assert precondition on t
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(prp, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TProp(prp, t) << "\n";
			}
			// assert Pre(precondtion) on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t+1, 1), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(prp, t+1, 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TPre(prp, t+1) << "\n";
			}
			if(a->DoesDeleteAtStart(prp))
				continue;
			// assert precondition on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t+1), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(prp, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TProp(prp, t+1) << "\n";
			}
		}
		for(it = a->addEffectAtStart.begin(); it != a->addEffectAtStart.end(); ++it)
		{
			prp = *it;
			// assert effect on t
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t+1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(prp, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TProp(prp, t+1) << "\n";
			}
		}
		for(it = a->delEffectAtStart.begin(); it != a->delEffectAtStart.end(); ++it)
		{
			prp = *it;
			// assert ~effect on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t+1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_False(PropTime2Var(prp, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_NProp(prp, t+1) << "\n";
			}
			if(a->DoesNeedAtStart(prp))
				continue;
			// else assert ~Pre(effect) on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(prp, t+1, 1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_False(PropTime2Var(prp, t+1, 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_NPre(prp, t+1) << "\n";
			}
		}
		for(it = a->conditionAtEnd.begin(); it != a->conditionAtEnd.end(); ++it)
		{
			prp = *it;
			// assert precondition on t
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(prp, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TProp(prp, t) << "\n";
			}
			// assert Pre(precondtion) on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t+1, 1), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(prp, t+1, 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TPre(prp, t+1) << "\n";
			}
			if(a->DoesDeleteAtEnd(prp))
				continue;
			// assert precondition on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t+1), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(prp, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TProp(prp, t+1) << "\n";
			}
		}
		for(it = a->addEffectAtEnd.begin(); it != a->addEffectAtEnd.end(); ++it)
		{
			prp = *it;
			// assert effect on t
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t + 1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(prp, t + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TProp(prp, t + 1) << "\n";
			}
		}
		for(it = a->delEffectAtEnd.begin(); it != a->delEffectAtEnd.end(); ++it)
		{
			prp = *it;
			// assert ~effect on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t + 1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_False(PropTime2Var(prp, t + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_NProp(prp, t + 1) << "\n";
			}
			if(a->DoesNeedAtEnd(prp))
				continue;
			// else assert ~Pre(effect) on t+1
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(prp, t + 1, 1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_False(PropTime2Var(prp, t + 1, 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_NPre(prp, t + 1) << "\n";
			}
		}
		for(it = a->conditionOverAll.begin(); it != a->conditionOverAll.end(); ++it)
		{
			prp = *it;
			for(int t=0; t<T; t++)
			{
				// overall conditions are asserted on the open range (start,start+duration)
				// we are asserting the additional case start+duration, actually the range (start,start+duration]
				// so we don't need the AddMutexDuring_Necessary()
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 2), false);
				AddToClause(PropTime2Var(prp, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 2)) << " " << cnf_True(PropTime2Var(prp, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionO(i, t) << " " << readcnf_TProp(prp, t) << "\n";
			}
		}
	}
}

void SatLayer::Old_AddConditionsEffects()
{
	for(int i=0; i<nAction; i++)
	{
		CheckForTimeOut();
		const PAction *a = pProblem.pAllAction.GetActionById(i);
		set<int>::const_iterator it;
		/*for(it = a->conditionAtStart.begin(); it != a->conditionAtStart.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(*it, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(*it, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TProp(*it, t) << "\n";
			}
		}
		for(it = a->addEffectAtStart.begin(); it != a->addEffectAtStart.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(*it, t+1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_True(PropTime2Var(*it, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_TProp(*it, t+1) << "\n";
			}
		}
		for(it = a->delEffectAtStart.begin(); it != a->delEffectAtStart.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 0), false);
				AddToClause(PropTime2Var(*it, t+1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 0)) << " " << cnf_False(PropTime2Var(*it, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionS(i, t) << " " << readcnf_NProp(*it, t+1) << "\n";
			}
		}
		for(it = a->conditionAtEnd.begin(); it != a->conditionAtEnd.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(*it, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(*it, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TProp(*it, t) << "\n";
			}
		}
		for(it = a->addEffectAtEnd.begin(); it != a->addEffectAtEnd.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(*it, t + 1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_True(PropTime2Var(*it, t + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_TProp(*it, t + 1) << "\n";
			}
		}
		for(it = a->delEffectAtEnd.begin(); it != a->delEffectAtEnd.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 1), false);
				AddToClause(PropTime2Var(*it, t + 1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 1)) << " " << cnf_False(PropTime2Var(*it, t + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionE(i, t) << " " << readcnf_NProp(*it, t + 1) << "\n";
			}
		}*/
		for(it = a->conditionOverAll.begin(); it != a->conditionOverAll.end(); ++it)
		{
			for(int t=0; t<T; t++)
			{
				// overall conditions are asserted on the open range (start,start+duration)
				// we are asserting the additional case start+duration, actually the range (start,start+duration]
				// so we don't need the AddMutexDuring_Necessary()
				ResetClause();
				AddToClause(ActionTime2Var(i, t, 2), false);
				AddToClause(PropTime2Var(*it, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t, 2)) << " " << cnf_True(PropTime2Var(*it, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionO(i, t) << " " << readcnf_TProp(*it, t) << "\n";
			}
		}
	}
}

void SatLayer::AddExplanatoryAxioms()
{
	set<int>::const_iterator it;
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<nProp; i++)
		{
			CheckForTimeOut();
			const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);

			#pragma region Add Axiom
			ResetClause();
			AddToClause(PropTime2Var(i, t), true);
			AddToClause(PropTime2Var(i, t+1), false);
			if(GEN_CNF)
				*cnf << cnf_True(PropTime2Var(i, t)) << " " << cnf_False(PropTime2Var(i, t+1));
			if(GEN_READABLE_CNF)
				*readcnf << readcnf_TProp(i, t) << " " << readcnf_NProp(i, t+1);
			for(it = p->addEffectAtStart.begin(); it != p->addEffectAtStart.end(); ++it)
			{
				//if (*it%2==t%2)
					AddToClause(ActionTime2Var(*it, t, 0), true);
				if(GEN_CNF)
					*cnf << " " << cnf_True(ActionTime2Var(*it, t, 0));
				if(GEN_READABLE_CNF)
					*readcnf << " " << readcnf_TActionS(*it, t);
			}
			for(it = p->addEffectAtEnd.begin(); it != p->addEffectAtEnd.end(); ++it)
			{
				//if (*it%2==t%2)
					AddToClause(ActionTime2Var(*it, t, 1), true);
				if(GEN_CNF)
					*cnf << " " << cnf_True(ActionTime2Var(*it, t, 1));
				if(GEN_READABLE_CNF)
					*readcnf << " " << readcnf_TActionE(*it, t);
			}
			AddClause(ccAxiomAdd);
			if(GEN_CNF)
				*cnf << " 0\n";
			if(GEN_READABLE_CNF)
				*readcnf << "\n";
			#pragma endregion

			#pragma region Delete Axiom
			ResetClause();
			AddToClause(PropTime2Var(i, t), false);
			AddToClause(PropTime2Var(i, t+1), true);
			if(GEN_CNF)
				*cnf << cnf_False(PropTime2Var(i, t)) << " " << cnf_True(PropTime2Var(i, t+1));
			if(GEN_READABLE_CNF)
				*readcnf << readcnf_NProp(i, t) << " " << readcnf_TProp(i, t+1);
			for(it = p->delEffectAtStart.begin(); it != p->delEffectAtStart.end(); ++it)
			{
				AddToClause(ActionTime2Var(*it, t, 0), true);
				if(GEN_CNF)
					*cnf << " " << cnf_True(ActionTime2Var(*it, t, 0));
				if(GEN_READABLE_CNF)
					*readcnf << " " << readcnf_TActionS(*it, t);
			}
			for(it = p->delEffectAtEnd.begin(); it != p->delEffectAtEnd.end(); ++it)
			{
				AddToClause(ActionTime2Var(*it, t, 1), true);
				if(GEN_CNF)
				{
					const PAction *a = pProblem.pAllAction.GetActionById(*it);
					*cnf << " " << cnf_True(ActionTime2Var(*it, t - a->duration, 1));
				}
				if(GEN_READABLE_CNF)
				{
					const PAction *a = pProblem.pAllAction.GetActionById(*it);
					*readcnf << " " << readcnf_TActionE(*it, t - a->duration);
				}
			}
			AddClause(ccAxiomDelete);
			if(GEN_CNF)
				*cnf << " 0\n";
			if(GEN_READABLE_CNF)
				*readcnf << "\n";
			#pragma endregion

		} // end of 5
	}
}

void SatLayer::AddMutexStart_End_n2()
{
	cout << " n2 ";
	set<int> result;
	set<int>::iterator it;
	vector<int> mutexActions;
	for(int i=0; i<nProp; i++)
	{
		CheckForTimeOut();
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		mutexActions.clear();
		result.clear();
		std::set_intersection(p->conditionAtStart.begin(), p->conditionAtStart.end(), p->delEffectAtStart.begin(), p->delEffectAtStart.end(), std::insert_iterator<vector<int> >(mutexActions, mutexActions.end()));
		std::set_intersection(p->conditionAtEnd.begin(), p->conditionAtEnd.end(), p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(it = result.begin(); it != result.end(); ++it)
		{
			mutexActions.push_back(-*it);
		}
		int sz = mutexActions.size();
		for(int j=0; j<sz; j++)
		{
			int part_a, a = mutexActions[j];
			part_a = a >= 0 ? 0 : 1;
			a = abs(a);
			for(int k=j+1; k<sz; k++)
			{
				int part_b, b = mutexActions[k];
				part_b = b >= 0 ? 0 : 1;
				b = abs(b);
				for(int t=0; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, part_a), false);
					AddToClause(ActionTime2Var(b, t, part_b), false);
					AddClause(ccMutexStart);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t, part_a)) << " " << cnf_False(ActionTime2Var(a, t, part_a)) << " 0\n";
					if(GEN_READABLE_CNF)
					{
						if(part_a == 0)
							*readcnf << readcnf_NActionS(a, t);
						else
							*readcnf << readcnf_NActionE(a, t);
						if(part_b == 0)
							*readcnf << " " << readcnf_NActionS(b, t) << " 0\n";
						else
							*readcnf << " " << readcnf_NActionE(b, t) << " 0\n";
					}
				}
			}
		}
	}
}
				
void SatLayer::AddMutexStart_End_nlogn()
{
	cout << " nlogn ";
	set<int> result;
	set<int>::iterator it;
	vector<int> mutexActions;
	for(int i=0; i<nProp; i++)
	{
		CheckForTimeOut();
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		mutexActions.clear();
		result.clear();
		std::set_intersection(p->conditionAtStart.begin(), p->conditionAtStart.end(), p->delEffectAtStart.begin(), p->delEffectAtStart.end(), std::insert_iterator<vector<int> >(mutexActions, mutexActions.end()));
		std::set_intersection(p->conditionAtEnd.begin(), p->conditionAtEnd.end(), p->delEffectAtEnd.begin(), p->delEffectAtEnd.end(), std::insert_iterator<set<int> >(result, result.end()));
		for(it = result.begin(); it != result.end(); ++it)
		{
			mutexActions.push_back(-*it);
		}
		int sz = mutexActions.size();

		int nbits = ceil(log((float)sz) / log((float)2));
		int *bitVars = new int[nbits];
		for(int t=0; t<T; t++)
		{
			for(int j=0; j<nbits; j++)
			{
				bitVars[j] = SATNewVar();
			}
			for(int j=0; j<sz; j++)
			{
				int part, a = mutexActions[j];
				part = a >= 0 ? 0 : 1;
				a = abs(a);
				int x = j;
				for(int k=0; k<nbits; k++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, part), false);
					AddToClause(bitVars[k], x & 1 ? true : false);
					AddClause(ccMutexOverall);
					x >>= 1;
				}
			}
		}
	}
}

// works with Old_AddConditionsEffects()
void SatLayer::Old_AddMutexStart_End(bool **mutextable, bool *compress)
{
	set<int>::const_iterator it1, it2, it3;
	
	
	int *acbanned= new int[nAction*2];
	long int *predur = new long int[nAction*2];
	long int *predurvar = new long int[nAction*2];
	bool *predurb= new bool[nAction*2];
	int *predurtype = new int[nAction*2];
	long int *delbeforevar = new long int[nAction*2];
	long int *delaftervar = new long int[nAction*2];
	long int delbeforet1var;
	long int delaftertvar;
	long int npredur=0;
//	int ndelexist=0;
//	bool *delexistb= new bool[nAction*2];
	long int npredurvar=0;
//	int *nextpredur= new int[nAction*2];

//	int *delexist = new int[nAction*2];
	for(long int i=0; i<nAction*2; i++)
	{	
		//delexistb[i]=false;
		predurb[i]=false;
		predurtype[i]=-1;
	}

	
	for(long int i=0; i<nProp; i++)
	{
		for(long int j=0; j<nAction*2; j++)
		{	
			//delexistb[i]=false;
			//predurb[i]=false;
			predurtype[j]=-1;
		}
		npredur=0;
		//ndelexist=0;
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		for (it1=p->conditionAtStart.begin(); it1 != p->conditionAtStart.end(); ++it1)
		{
			if (!compress[*it1])
			{
			predurb[(*it1)*2]=true;
			predurtype[(*it1)*2]=2;
			}
			else
			{
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=2;
			}
		}
		for (it1=p->conditionOverAll.begin(); it1 != p->conditionOverAll.end(); ++it1)
		{
			if (!compress[*it1])
			{
			predurb[(*it1)*2]=true;
			predurtype[(*it1)*2]=4;
			
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=4;
			}
			else 
			{
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=2;
			}
		}
		for (it1=p->conditionAtEnd.begin(); it1 != p->conditionAtEnd.end(); ++it1)
		{

			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=2;
		}
		for (it1=p->addEffectAtStart.begin(); it1 != p->addEffectAtStart.end(); ++it1)
		{

			if (!compress[*it1])
			{
			predurb[(*it1)*2]=true;
			predurtype[(*it1)*2]=1;
			}
			else if ((predurtype[(*it1)*2+1]!=2) && (predurtype[(*it1)*2+1]!=4))
			{
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=1;
			}
		}
		for (it1=p->delEffectAtStart.begin(); it1 != p->delEffectAtStart.end(); ++it1)
		{
			if (!compress[*it1])
			{
			if (predurb[(*it1)*2])
				predurtype[(*it1)*2]=3;
			else
				predurtype[(*it1)*2]=0;
			predurb[(*it1)*2]=true;
			}
			else
			{
			if (predurb[(*it1)*2+1])
				predurtype[(*it1)*2+1]=3;
			else
				predurtype[(*it1)*2+1]=0;
			predurb[(*it1)*2+1]=true;
			}
			
		}
		for (it1=p->addEffectAtEnd.begin(); it1 != p->addEffectAtEnd.end(); ++it1)
		{
			if (((predurtype[(*it1)*2+1]!=2) && (predurtype[(*it1)*2+1]!=4)) && (predurtype[(*it1)*2+1]!=3))
			{
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=1;
			}
			if ((predurtype[(*it1)*2+1]==3) )
			{
			predurb[(*it1)*2+1]=true;
			predurtype[(*it1)*2+1]=2;
			}
		}

		for (it1=p->delEffectAtEnd.begin(); it1 != p->delEffectAtEnd.end(); ++it1)
		{
			if ((predurtype[(*it1)*2+1]==2) || (predurtype[(*it1)*2+1]==4) || (predurtype[(*it1)*2+1]==3))
				predurtype[(*it1)*2+1]=3;
			else
				predurtype[(*it1)*2+1]=0;
			predurb[(*it1)*2+1]=true;
		}
		for (long int j=0; j<nAction*2; j++)
			if (predurb[j])
			{
				predur[npredur]=j;
				predurtype[npredur]=predurtype[j];
				predurb[j]=false;
				
				npredur++;
			}
		///////////////////////////////////////////////NEW: Action Proposition Mutex (Start)///////////////////////////////////////////////
			int proporder=0;
			bool foundbanned;
			
			for (int j=0; j<nAction; j++)
			{
				foundbanned=false;
				acbanned[j*2]=-1;
				const PAction *ac = pProblem.pAllAction.GetActionById(j);
				for (it1=ac->addEffectAtStart.begin(); it1!=ac->addEffectAtStart.end(); it1++)
					if (mutextable[*it1][i])
						foundbanned=true;
				if (foundbanned)
				{
					while ((predur[proporder]<=j*2))
						if (proporder==npredur)
							break;
						else
							proporder++;
					if (proporder<npredur)
						acbanned[j*2]=proporder;
				}
				foundbanned=false;
				acbanned[j*2+1]=-1;
				for (it1=ac->addEffectAtEnd.begin(); it1!=ac->addEffectAtEnd.end(); it1++)
					if (mutextable[*it1][i])
						foundbanned=true;
				if (foundbanned)
				{
					while ((predur[proporder]<=j*2+1))
						if (proporder==npredur)
							break;
						else
							proporder++;
					if (proporder<npredur)
						acbanned[j*2+1]=proporder;
				}
			}
		bool durneeded=false;
		for (it3=p->conditionOverAll.begin(); it3!=p->conditionOverAll.end(); it3++)
			if (!compress[*it3])
				durneeded=true;
		///////////////////////////////////////////////NEW: Action Proposition Mutex (End)///////////////////////////////////////////////
		for (int t=0; t<T; t++)
		{
			
			for (long int j=0; j<npredur; j++)
			{
		////////////////////////////////////// NEW: REDUCE VARIABLES (Start)///////////////////////////////////////////
				
				if ((j==0))
				{
					predurvar[j]=SATNewVar()+1;
					if (durneeded)
						delbeforevar[j]=SATNewVar()+1;
					//delaftervar[j]=SATNewVar()+1;
				}
				else if ((predurtype[j-1]!=2) && (predurtype[j-1]!=4))
				{
					predurvar[j]=SATNewVar()+1;
					if (durneeded)
						delbeforevar[j]=SATNewVar()+1;
					//delaftervar[j]=SATNewVar()+1;
				}
				else
				{
					predurvar[j]=predurvar[j-1];
					if (durneeded)
						delbeforevar[j]=delbeforevar[j-1];
					//delaftervar[j]=delaftervar[j-1];
					//delbeforevar[j]=SATNewVar()+1;
					//delaftervar[j]=SATNewVar()+1;
					//predurvar[j]=SATNewVar()+1;
				}
			}
			for (long int j=npredur-1; j>=0; j--)
			{
				if ((j==npredur-1) )
				{
					if (durneeded)
						delaftervar[j]=SATNewVar()+1;
				}
				else if ((predurtype[j+1]!=2) && (predurtype[j+1]!=4))
				{
					//predurvar[j]=SATNewVar()+1;
					//delbeforevar[j]=SATNewVar()+1;
					if (durneeded)
						delaftervar[j]=SATNewVar()+1;
				}
				else
				{
					//predurvar[j]=predurvar[j-1];
					//delbeforevar[j]=delbeforevar[j-1];
					if (durneeded)
						delaftervar[j]=delaftervar[j+1];
					//delbeforevar[j]=SATNewVar()+1;
					//delaftervar[j]=SATNewVar()+1;
					//predurvar[j]=SATNewVar()+1;
				}
			}
		////////////////////////////////////// NEW: REDUCE VARIABLES (End)///////////////////////////////////////////
			/*cout << endl;
			if (i==0)
			for (int j=0; j<8; j++)
				if (predur[j]%2==0)
					cout << endl << j << "    "  << predur[j] << "    " << pProblem.pAllAction.GetActionById(predur[j]/2)->ToFullString() << predur[j]%2 << "    " << predurtype[j] << "     " << delbeforevar[j] << endl;
				else
					cout << endl << j << "    "  << predur[j] << "    " << pProblem.pAllAction.GetActionById((predur[j]-1)/2)->ToFullString()  << predur[j]%2<< "    " << predurtype[j] << "     " << delbeforevar[j] << endl;
				//cout << endl << j<< "   "<< pProblem.pAllProposition.GetPropositionById(j)->ToFullString() << endl;
			exit(0);*/
			if (durneeded)
			{
				delbeforet1var=SATNewVar()+1;
				delaftertvar=SATNewVar()+1;
			}
			///////////////////////////////////////////////NEW: Action Proposition Mutex (Start)///////////////////////////////////////////////
/*			for (int j=0; j<nAction; j++)
			{
				if (acbanned[j*2]!=-1)
				{
					ResetClause();
					AddToClause(ActionTime2Var(j, t, ACTION_START), false);
					AddToClause(predurvar[acbanned[j*2]], false);
					AddClause(ccMutexStartEnd);
				}
				if (acbanned[j*2+1]!=-1)
				{
					ResetClause();
					AddToClause(ActionTime2Var(j, t, ACTION_END), false);
					AddToClause(predurvar[acbanned[j*2+1]], false);
					AddClause(ccMutexStartEnd);
				}
			}*/
			///////////////////////////////////////////////NEW: Action Proposition Mutex (End)///////////////////////////////////////////////
			if (npredur>0)
			{
				ResetClause();
				AddToClause(PropTime2Var(i,t),false);
				AddToClause(predurvar[0], true);
				AddClause(ccMutexStartEnd);

				ResetClause();
				AddToClause(PropTime2Var(i,t),true);
				AddToClause(predurvar[0], false);
				AddClause(ccMutexStartEnd);
				if (durneeded)
				{
					ResetClause();
					AddToClause(delbeforevar[0], false);
					AddClause(ccMutexStartEnd);

					ResetClause();
					AddToClause(delaftervar[npredur-1], false);
					AddClause(ccMutexStartEnd);
				}

			}
			else
			{
				ResetClause();
				AddToClause(PropTime2Var(i,t),false);
				AddToClause(PropTime2Var(i,t+1), true);
				AddClause(ccMutexStartEnd);

				ResetClause();
				AddToClause(PropTime2Var(i,t),true);
				AddToClause(PropTime2Var(i,t+1), false);
				AddClause(ccMutexStartEnd);
			}
			if (durneeded)
			{
				for (long int j=0; j<npredur; j++)
				{
					if ((predurtype[j]!=0) && (predurtype[j]!=3))
					{
						ResetClause();
						AddToClause(delbeforevar[j], false);
						if (j==npredur-1)
							AddToClause(delbeforet1var,true);
						else
							AddToClause(delbeforevar[j+1], true);
						AddClause(ccMutexStartEnd);

						ResetClause();
						AddToClause(delbeforevar[j], true);
						if (j==npredur-1)
							AddToClause(delbeforet1var,false);
						else
							AddToClause(delbeforevar[j+1], false);
						AddClause(ccMutexStartEnd);


					}
					if ((predurtype[j]==0) || (predurtype[j]==3))
					{
						ResetClause();
						
						if (predur[j]%2==0)
							AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
						else
							AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
						if (j==npredur-1)
							AddToClause(delbeforet1var,true);
						else
							AddToClause(delbeforevar[j+1], true);
						AddClause(ccMutexStartEnd);


						ResetClause();
						AddToClause(delbeforevar[j], false);
						if (j==npredur-1)
							AddToClause(delbeforet1var,true);
						else
							AddToClause(delbeforevar[j+1], true);
						AddClause(ccMutexStartEnd);
					}
					if ((predurtype[j]==4) && (predur[j]%2==1))
					{
						ResetClause();
						AddToClause(delbeforevar[j], false);
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);

						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_START), true);					
						AddClause(ccMutexStartEnd);
					}

				}
				if (t<T-1)
					for (it1=p->conditionOverAll.begin(); it1 != p->conditionOverAll.end(); ++it1)
					if (!compress[*it1])
					{
							ResetClause();
							AddToClause(delbeforet1var, false);
							AddToClause(ActionTime2Var(*it1, t+1, ACTION_OVERALL), false);

							AddToClause(ActionTime2Var(*it1, t, ACTION_START), true);					
							AddClause(ccMutexStartEnd);
					}
			

				for (long int j=npredur-1; j>=0; j--)
				{
					if ((predurtype[j]!=0) && (predurtype[j]!=3))
					{
						ResetClause();
						AddToClause(delaftervar[j], false);
						if (j==0)
							AddToClause(delaftertvar,true);
						else
							AddToClause(delaftervar[j-1], true);
						AddClause(ccMutexStartEnd);

						ResetClause();
						AddToClause(delaftervar[j], true);
						if (j==0)
							AddToClause(delaftertvar,false);
						else
							AddToClause(delaftervar[j-1], false);
						AddClause(ccMutexStartEnd);


					}
					if ((predurtype[j]==0) || (predurtype[j]==3))
					{
						ResetClause();
					
						if (predur[j]%2==0)
							AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
						else
							AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
						if (j==0)
							AddToClause(delaftertvar,true);
						else
							AddToClause(delaftervar[j-1], true);
						AddClause(ccMutexStartEnd);

						ResetClause();
					
						AddToClause(delaftervar[j], false);
						if (j==0)
							AddToClause(delaftertvar,true);
						else
							AddToClause(delaftervar[j-1], true);
						AddClause(ccMutexStartEnd);

					}
					if ((predurtype[j]==4) && (predur[j]%2==0))
					{
						ResetClause();
						AddToClause(delaftervar[j], false);
						AddToClause(ActionTime2Var((predur[j])/2, t, ACTION_START), false);

						AddToClause(ActionTime2Var((predur[j])/2, t, ACTION_END), true);					
						AddClause(ccMutexStartEnd);
					}

				}
				if (t>0)
					for (it1=p->conditionOverAll.begin(); it1 != p->conditionOverAll.end(); ++it1)
					if (!compress[*it1])
					{
							ResetClause();
							AddToClause(delaftertvar, false);
							AddToClause(ActionTime2Var(*it1, t, ACTION_OVERALL), false);

							AddToClause(ActionTime2Var(*it1, t, ACTION_END), true);					
							AddClause(ccMutexStartEnd);
					}


			}
			for (long int j=0; j<npredur; j++)
			{
				if ((predurtype[j]==2) || (predurtype[j]==4))
				{
					/*if(j!=npredur-1)
					{
						if (predurvar[j]!=predurvar[j+1])
						{
							ResetClause();
							AddToClause(predurvar[j], false);
							AddToClause(predurvar[j+1], true);
							AddClause(ccMutexStartEnd);

							ResetClause();
							AddToClause(predurvar[j], true);
							AddToClause(predurvar[j+1], false);
							AddClause(ccMutexStartEnd);
						}
					}*/
					if (j==npredur-1)
					{
						ResetClause();
						AddToClause(predurvar[j], false);
						AddToClause(PropTime2Var(i,t+1),true);
						AddClause(ccMutexStartEnd);

						ResetClause();
						AddToClause(predurvar[j], true);
						AddToClause(PropTime2Var(i,t+1),false);
						AddClause(ccMutexStartEnd);
					}
					ResetClause();
					AddToClause(predurvar[j], true);
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
					AddClause(ccMutexStartEnd);
				}
				if (predurtype[j]==1)
				{
					ResetClause();
					//if (predur[j]%2==0)
						//AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					//else
						//AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),true);
					else
						AddToClause(predurvar[j+1], true);
					AddClause(ccMutexStartEnd);

					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], true);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),false);
					else
						AddToClause(predurvar[j+1], false);
					AddClause(ccMutexStartEnd);

					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),true);
					else
						AddToClause(predurvar[j+1], true);
					AddClause(ccMutexStartEnd);
				}
				if (predurtype[j]==0)
				{
					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),true);
					else
						AddToClause(predurvar[j+1], true);
					AddClause(ccMutexStartEnd);

					ResetClause();
					//if (predur[j]%2==0)
						//AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					//else
						//AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], true);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),false);
					else
						AddToClause(predurvar[j+1], false);
					AddClause(ccMutexStartEnd);

					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),false);
					else
						AddToClause(predurvar[j+1], false);
					AddClause(ccMutexStartEnd);
				}
				if (predurtype[j]==3)
				{
					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),true);
					else
						AddToClause(predurvar[j+1], true);
					AddClause(ccMutexStartEnd);

					ResetClause();
					//if (predur[j]%2==0)
						//AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), true);
					//else
						//AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), true);
					AddToClause(predurvar[j], true);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),false);
					else
						AddToClause(predurvar[j+1], false);
					AddClause(ccMutexStartEnd);

					ResetClause();
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
					if (j==npredur-1)
						AddToClause(PropTime2Var(i,t+1),false);
					else
						AddToClause(predurvar[j+1], false);
					AddClause(ccMutexStartEnd);

					ResetClause();
					AddToClause(predurvar[j], true);
					if (predur[j]%2==0)
						AddToClause(ActionTime2Var(predur[j]/2, t, ACTION_START), false);
					else
						AddToClause(ActionTime2Var((predur[j]-1)/2, t, ACTION_END), false);
					AddClause(ccMutexStartEnd);

				}


			}


		}
	}
	delete predur;
	delete predurvar;
	delete predurb;
	delete predurtype;
	delete delbeforevar;
	delete delaftervar;

	/*
	int **predel = new int*[nProp];
	int **duradd = new int*[nProp];
	int **delvar = new int*[nProp];
	int **delpre = new int*[nProp];
	for(int i=0; i<nProp; i++)
	{
		predel[i] = new int[T];
		
		duradd[i] = new int[T];
		delvar[i] = new int[T];
		delpre[i] = new int[T];

		for(int t=0; t<T; t++)
		{

			predel[i][t]=SATNewVar()+1;

			duradd[i][t]=SATNewVar()+1;
			delvar[i][t]=SATNewVar()+1;
			delpre[i][t]=SATNewVar()+1;
		}
	}

	for(int i=0; i<nAction; i++)
	{
		//cout << "*" << i << "*";
		const PAction *a = pProblem.pAllAction.GetActionById(i);
		
		for(int t=0; t<T-1; t++)
		{

			ResetClause();
			AddToClause(ActionTime2Var(i, t, ACTION_START), false);
			AddToClause(ActionTime2Var(i, t+1, ACTION_END), true);

			for (it1=a->addEffectAtStart.begin(); it1 != a->addEffectAtStart.end(); ++it1)
			{
				AddToClause(predel[*it1][t+1],true);
				AddToClause(duradd[*it1][t],true);
				AddToClause(PropTime2Var(*it1,t+2),false);
			}


			for (it1=a->delEffectAtStart.begin(); it1 != a->delEffectAtStart.end(); ++it1)
			{
				AddToClause(PropTime2Var(*it1,t+2),true);
			}


			for (it1=a->conditionAtStart.begin(); it1 != a->conditionAtStart.end(); ++it1)
			{
				int p=*it1;
				bool fnd=false;
				for (it2=a->delEffectAtStart.begin(); it2 != a->delEffectAtStart.end(); ++it2)
					if (p==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(PropTime2Var(p,t+2),false);
				else 
					AddToClause(delpre[*it1][t+1],true);
			}
			AddClause(ccMutexStartEnd);
			ResetClause();
			AddToClause(ActionTime2Var(i, t, ACTION_END), false);
			AddToClause(ActionTime2Var(i, t+1, ACTION_START), true);
			for (it1=a->addEffectAtEnd.begin(); it1 != a->addEffectAtEnd.end(); ++it1)
			{
				AddToClause(predel[*it1][t+1],true);
				AddToClause(duradd[*it1][t],true);
				AddToClause(PropTime2Var(*it1,t+2),false);
			}


			for (it1=a->delEffectAtEnd.begin(); it1 != a->delEffectAtEnd.end(); ++it1)
			{
				AddToClause(PropTime2Var(*it1,t+2),true);
			}


			for (it1=a->conditionAtEnd.begin(); it1 != a->conditionAtEnd.end(); ++it1)
			{
				int p=*it1;
				bool fnd=false;
				for (it2=a->delEffectAtEnd.begin(); it2 != a->delEffectAtEnd.end(); ++it2)
					if (p==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(PropTime2Var(p,t+2),false);
				else 
					AddToClause(delpre[*it1][t+1],true);
			}
			for (it1=a->conditionOverAll.begin(); it1 != a->conditionOverAll.end(); ++it1)
			{
				int p=*it1;
				bool fnd=false;
				for (it2=a->delEffectAtEnd.begin(); it2 != a->delEffectAtEnd.end(); ++it2)
					if (p==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(PropTime2Var(p,t+1),false);
				else
					AddToClause(delvar[*it1][t],true);
			}
			AddClause(ccMutexStartEnd);
		}
	}
	//cout << endl << "*************************";
	for (int i=0; i<nProp; i++)
	{
		//cout  << endl << i;
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		for (int t=0; t<T; t++)
		{

			ResetClause();
			AddToClause(delvar[i][t],false);
			for (it1=p->delEffectAtStart.begin(); it1 != p->delEffectAtStart.end(); ++it1)
				AddToClause(ActionTime2Var(*it1, t, ACTION_START), true);
			for (it1=p->delEffectAtEnd.begin(); it1 != p->delEffectAtEnd.end(); ++it1)
				AddToClause(ActionTime2Var(*it1, t, ACTION_END), true);
			AddClause(ccMutexStartEnd);
			ResetClause();
			AddToClause(duradd[i][t],false);
			for (it1=p->conditionOverAll.begin(); it1 != p->conditionOverAll.end(); ++it1)
			{
				int a=*it1;
				bool fnd=false;
				for (it2=p->addEffectAtStart.begin(); it2 != p->addEffectAtStart.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_START),true);
				fnd=false;
				for (it2=p->addEffectAtEnd.begin(); it2 != p->addEffectAtEnd.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_END),true);
			}
			AddClause(ccMutexStartEnd);
			ResetClause();
			AddToClause(predel[i][t],false);
			for (it1=p->conditionAtStart.begin(); it1 != p->conditionAtStart.end(); ++it1)
			{
				int a=*it1;
				bool fnd=false;
				for (it2=p->delEffectAtStart.begin(); it2 != p->delEffectAtStart.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_START),true);
			}
			for (it1=p->conditionAtEnd.begin(); it1 != p->conditionAtEnd.end(); ++it1)
			{
				int a=*it1;
				bool fnd=false;
				for (it2=p->delEffectAtEnd.begin(); it2 != p->delEffectAtEnd.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_END),true);
			}
			AddClause(ccMutexStartEnd);
			ResetClause();
			AddToClause(delpre[i][t],false);
			for (it1=p->delEffectAtStart.begin(); it1 != p->delEffectAtStart.end(); ++it1)
			{
				int a=*it1;
				bool fnd=false;
				for (it2=p->conditionAtStart.begin(); it2 != p->conditionAtStart.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_START),true);
			}
			for (it1=p->delEffectAtEnd.begin(); it1 != p->delEffectAtEnd.end(); ++it1)
			{
				int a=*it1;
				bool fnd=false;
				for (it2=p->conditionAtEnd.begin(); it2 != p->conditionAtEnd.end(); ++it2)
					if (a==*it2)
						fnd=true;
				if (!fnd)
					AddToClause(ActionTime2Var(a,t,ACTION_END),true);
			}
			AddClause(ccMutexStartEnd);
		}
	}

	

	*/










/*

	cout << " n2all ";

	for(int i=0; i<nProp; i++)
	{
		CheckForTimeOut();
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);

		// START-START
		for(it1 = p->conditionAtStart.begin(); it1 != p->conditionAtStart.end(); ++it1)
		{
			int a = *it1;
			for(it2 = p->delEffectAtStart.begin(); it2 != p->delEffectAtStart.end(); ++it2)
			{
				int b = *it2;
				if(a==b)
					continue;
				for(int t=0; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, ACTION_START), false);
					AddToClause(ActionTime2Var(b, t, ACTION_START), false);
					AddClause(ccMutexStart);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t, ACTION_START)) << " " << cnf_False(ActionTime2Var(a, t, ACTION_START)) << " 0\n";
					if(GEN_READABLE_CNF)
					{
						*readcnf << readcnf_NActionS(a, t);
						*readcnf << " " << readcnf_NActionS(b, t) << " 0\n";
					}
				}
			}
		}
		// END-END
		for(it1 = p->conditionAtEnd.begin(); it1 != p->conditionAtEnd.end(); ++it1)
		{
			int a = *it1;
			for(it2 = p->delEffectAtEnd.begin(); it2 != p->delEffectAtEnd.end(); ++it2)
			{
				int b = *it2;
				if(a==b)
					continue;
				for(int t=0; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, ACTION_END), false);
					AddToClause(ActionTime2Var(b, t, ACTION_END), false);
					AddClause(ccMutexEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t, ACTION_END)) << " " << cnf_False(ActionTime2Var(a, t, ACTION_END)) << " 0\n";
					if(GEN_READABLE_CNF)
					{
						*readcnf << readcnf_NActionE(a, t);
						*readcnf << " " << readcnf_NActionE(b, t) << " 0\n";
					}
				}
			}
		}
		// START-END
		for(it1 = p->conditionAtStart.begin(); it1 != p->conditionAtStart.end(); ++it1)
		{
			int a = *it1;
			for(it2 = p->delEffectAtEnd.begin(); it2 != p->delEffectAtEnd.end(); ++it2)
			{
				int b = *it2;
				for(int t=0; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, ACTION_START), false);
					AddToClause(ActionTime2Var(b, t, ACTION_END), false);
					AddClause(ccMutexStartEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t, ACTION_START)) << " " << cnf_False(ActionTime2Var(a, t, ACTION_END)) << " 0\n";
					if(GEN_READABLE_CNF)
					{
						*readcnf << readcnf_NActionS(a, t);
						*readcnf << " " << readcnf_NActionE(b, t) << " 0\n";
					}
				}
			}
		}
		// END-START
		for(it1 = p->conditionAtEnd.begin(); it1 != p->conditionAtEnd.end(); ++it1)
		{
			int a = *it1;
			for(it2 = p->delEffectAtStart.begin(); it2 != p->delEffectAtStart.end(); ++it2)
			{
				int b = *it2;
				for(int t=0; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t, ACTION_END), false);
					AddToClause(ActionTime2Var(b, t, ACTION_START), false);
					AddClause(ccMutexStartEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t, ACTION_END)) << " " << cnf_False(ActionTime2Var(a, t, ACTION_START)) << " 0\n";
					if(GEN_READABLE_CNF)
					{
						*readcnf << readcnf_NActionE(a, t);
						*readcnf << " " << readcnf_NActionS(b, t) << " 0\n";
					}
				}
			}
		}
	}
	*/
}

void SatLayer::Report_CNFStats(bool silent)
{
	long long totalMutexes = ccMutexStart + ccMutexEnd + ccMutexStartEnd  + ccMutexOverall;
	long long totalClauses = ccEvent + ccInit + ccGoal + ccNotApplicable + ccCondition + ccEffect + ccAxiomDelete + 
								ccAxiomAdd + totalMutexes;
	satresults->varProp = nvProp;
	satresults->varAction = nvEvent;
	satresults->varTotal = satresults->varProp + satresults->varAction;
	satresults->ccEvent = ccEvent;
	satresults->ccInit = ccInit;
	satresults->ccGoal = ccGoal;
	satresults->ccNotApplicable = ccNotApplicable;
	satresults->ccCondition = ccCondition;
	satresults->ccEffect = ccEffect;
	satresults->ccAxiomDelete = ccAxiomDelete;
	satresults->ccAxiomAdd = ccAxiomAdd;
	satresults->ccMutexStart = ccMutexStart;
	satresults->ccMutexEnd = ccMutexEnd;
	satresults->ccMutexStartEnd = ccMutexStartEnd;
	satresults->ccMutexOverall = ccMutexOverall;
	satresults->totalMutexes = totalMutexes;
	satresults->totalClauses = totalClauses;

	if(silent)
		return;
	cout << "Variables: total=" << satresults->varTotal << "\tprop=" << satresults->varProp << "\taction= " << satresults->varAction << endl;
	//cout << "Clauses: initital state=" << ccInit << " pProblem.goals=" << ccGoal << " not-applicable actions=" << ccNotApplicable << endl;
	//cout << "         imply conditions=" << ccCondition << " imply effects=" << ccEffect << endl;
	//cout << "         delete axioms=" << ccAxiomDelete << " add axioms=" << ccAxiomAdd << endl;
	//cout << "Mutex Clauses: start-start=" << ccMutexStart << " end-end=" << ccMutexEnd
	//	 << " start-end=" << ccMutexStartEnd << " overall=" << ccMutexOverall<< endl;
	cout << "Total Mutex Clauses=" << totalMutexes << "\tratio=" << (double)totalMutexes/totalClauses << endl;
	cout << "Total Event Clauses=" << satresults->ccEvent << "\tTotal Clauses=" << totalClauses << endl << flush;
}
