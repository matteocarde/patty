#include <fstream>
#include <set> // used in *AddMutex*()
#include <algorithm> // used in *AddMutex*()
#include <iterator> // used in *AddMutex*()
#include "tsat/parser/ParserClasses.h"
#include "tsat/utils.h"
#include "tsat/sattime/SatTime.h"

using namespace std;
using namespace MyParser;

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
#define readcnf_TAction(a,t) "a("<<a<<","<<t<<")"
#define readcnf_NAction(a,t) "~a("<<a<<","<<t<<")"
#pragma endregion

namespace nsSatTime
{

SatTime::SatTime(
	int t, SATResults *results,
	string detailsfilenametemplate,
	float totaltime=60, int overall_percent=0,
	bool gen_cnf=false, bool gen_readable_cnf=false, bool dont_solve=false)
	:
		T(t), satresults(results),
		detailsFileNameTemplate(detailsfilenametemplate),
		overallPercent(overall_percent), totalTime(totaltime),
		ccInit(0), ccGoal(0), ccNotApplicable(0), ccCondition(0), ccEffect(0), ccAxiomDelete(0),
		ccAxiomAdd(0), ccMutexStart(0), ccMutexEnd(0), ccMutexStartEnd(0), ccMutexOverall(0),
		GEN_CNF(gen_cnf), GEN_READABLE_CNF(gen_readable_cnf), DONT_SOLVE(dont_solve)
{
	startTime = CPUTime();

	nProp = pProblem.pAllProposition.size();
	nAction = pProblem.pAllAction.size();
	nvProp = nProp * (T+1);
	nvAction = nAction * T;
	index2var = new int[nvProp + nvAction];
	for(int i=0; i<nvProp + nvAction; i++)
		index2var[i] = -1;
	
	if(GEN_CNF)
	{
		char tosolvefilename[256];
		sprintf(tosolvefilename, "%s-T=%d.cnf", detailsFileNameTemplate.c_str(), T);
		cnf = new ofstream(tosolvefilename);
		// first argument is the number of variables
		// second argument is said to be the number of clauses. but it is not used in zchaff.exe
		*cnf << "p cnf " << nvProp + nvAction <<" 0" << "\n";
	}

	if(GEN_READABLE_CNF)
	{
		char toreadfilename[256];
		sprintf(toreadfilename, "%s-T=%d.txt", detailsFileNameTemplate.c_str(), T);
		readcnf = new ofstream(toreadfilename);
	}
}

void SatTime::DoEncoding()
{
	AddInitialState();
	AddGoals();
	AddConditions();
	AddEffects();
	AddExplanatoryAxioms_Delete();
	AddExplanatoryAxioms_Add();
	OldSlow_AddMutexStart_End();
	//AddMutexStart_End();
	AddMutexDuring_Redundant();
	if(GEN_CNF)
		cnf->close();
	if(GEN_READABLE_CNF)
		readcnf->close();
	Report_CNFStats();
}

void SatTime::DoEncoding(vector< vector<Mutex> > *fact_mutex, vector<int> *prop_layer)
{
	AddInitialState();
	AddGoals();
	AddConditions();
	AddEffects();
	AddExplanatoryAxioms_Delete();
	AddExplanatoryAxioms_Add();
	OldSlow_AddMutexStart_End();
	//AddMutexStart_End();
	AddMutexDuring_Redundant();

	if(fact_mutex)
		AddFactMutexes(fact_mutex);
	if(prop_layer)
		AddPropForbidClauses(prop_layer);

	if(GEN_CNF)
		cnf->close();
	if(GEN_READABLE_CNF)
		readcnf->close();
	Report_CNFStats();
}

void SatTime::AddInitialState()
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

void SatTime::AddGoals()
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

void SatTime::AddConditions()
{
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<nAction; i++)
		{
			CheckForTimeOut();
			const PAction *a = pProblem.pAllAction.GetActionById(i);
			if(!(t + a->duration < T)) // if a can't start at t
			{
				ccNotApplicable++;
				continue;
			}
			set<int>::const_iterator it;
			for(it = a->conditionAtStart.begin(); it != a->conditionAtStart.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_True(PropTime2Var(*it, t)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_TProp(*it, t) << "\n";
			}
			for(it = a->conditionAtEnd.begin(); it != a->conditionAtEnd.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t + a->duration), true);
				AddClause(ccCondition);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_True(PropTime2Var(*it, t + a->duration)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_TProp(*it, t + a->duration) << "\n";
			}
			for(it = a->conditionOverAll.begin(); it != a->conditionOverAll.end(); ++it)
			{
				// overall conditions are asserted on the open range (start,start+duration)
				// we are asserting the additional case start+duration, actually the range (start,start+duration]
				// so we don't need the AddMutexDuring_Necessary()
				for(int t2=t+1; t2<=t + a->duration; t2++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(i, t), false);
					AddToClause(PropTime2Var(*it, t2), true);
					AddClause(ccCondition);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_True(PropTime2Var(*it, t2)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(i, t) << " " << readcnf_TProp(*it, t2) << "\n";
				}
			}
		}
	}
}

void SatTime::AddEffects()
{
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<nAction; i++)
		{
			CheckForTimeOut();
			const PAction *a = pProblem.pAllAction.GetActionById(i);
			if(!(t + a->duration < T)) // if a can't start at t
				continue;

			set<int>::const_iterator it;
			for(it = a->addEffectAtStart.begin(); it != a->addEffectAtStart.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t+1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_True(PropTime2Var(*it, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_TProp(*it, t+1) << "\n";
			}
			for(it = a->delEffectAtStart.begin(); it != a->delEffectAtStart.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t+1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_False(PropTime2Var(*it, t+1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_NProp(*it, t+1) << "\n";
			}
			for(it = a->addEffectAtEnd.begin(); it != a->addEffectAtEnd.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t + a->duration + 1), true);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_True(PropTime2Var(*it, t + a->duration + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_TProp(*it, t + a->duration + 1) << "\n";
			}
			for(it = a->delEffectAtEnd.begin(); it != a->delEffectAtEnd.end(); ++it)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i, t), false);
				AddToClause(PropTime2Var(*it, t + a->duration + 1), false);
				AddClause(ccEffect);
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_False(PropTime2Var(*it, t + a->duration + 1)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NAction(i, t) << " " << readcnf_NProp(*it, t + a->duration + 1) << "\n";
			}
		}
	}
}

void SatTime::AddExplanatoryAxioms_Delete()
{
	set<int>::const_iterator it;
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<nProp; i++)
		{
			CheckForTimeOut();
			const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);

			ResetClause();
			AddToClause(PropTime2Var(i, t), false);
			AddToClause(PropTime2Var(i, t+1), true);
			if(GEN_CNF)
				*cnf << cnf_False(PropTime2Var(i, t)) << " " << cnf_True(PropTime2Var(i, t+1));
			if(GEN_READABLE_CNF)
				*readcnf << readcnf_NProp(i, t) << " " << readcnf_TProp(i, t+1);
			for(it = p->delEffectAtStart.begin(); it != p->delEffectAtStart.end(); ++it)
			{
				const PAction *a = pProblem.pAllAction.GetActionById(*it);
				if(t + a->duration < T) // if a can start at t
				{
					AddToClause(ActionTime2Var(*it, t), true);
					if(GEN_CNF)
						*cnf << " " << cnf_True(ActionTime2Var(*it, t));
					if(GEN_READABLE_CNF)
						*readcnf << " " << readcnf_TAction(*it, t);
				}
			}
			for(it = p->delEffectAtEnd.begin(); it != p->delEffectAtEnd.end(); ++it)
			{
				const PAction *a = pProblem.pAllAction.GetActionById(*it);
				if(t >= a->duration) // if a can finish at t
				{
					AddToClause(ActionTime2Var(*it, t - a->duration), true);
					if(GEN_CNF)
						*cnf << " " << cnf_True(ActionTime2Var(*it, t - a->duration));
					if(GEN_READABLE_CNF)
						*readcnf << " " << readcnf_TAction(*it, t - a->duration);
				}
			}
			AddClause(ccAxiomDelete);
			if(GEN_CNF)
				*cnf << " 0\n";
			if(GEN_READABLE_CNF)
				*readcnf << "\n";
		} // end of 5
	}
}

void SatTime::AddExplanatoryAxioms_Add()
{
	set<int>::const_iterator it;
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<nProp; i++)
		{
			CheckForTimeOut();
			const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);

			ResetClause();
			AddToClause(PropTime2Var(i, t), true);
			AddToClause(PropTime2Var(i, t+1), false);
			if(GEN_CNF)
				*cnf << cnf_True(PropTime2Var(i, t)) << " " << cnf_False(PropTime2Var(i, t+1));
			if(GEN_READABLE_CNF)
				*readcnf << readcnf_TProp(i, t) << " " << readcnf_NProp(i, t+1);
			for(it = p->addEffectAtStart.begin(); it != p->addEffectAtStart.end(); ++it)
			{
				const PAction *a = pProblem.pAllAction.GetActionById(*it);
				if(t + a->duration < T) // if a can start at t
				{
					AddToClause(ActionTime2Var(*it, t), true);
					if(GEN_CNF)
						*cnf << " " << cnf_True(ActionTime2Var(*it, t));
					if(GEN_READABLE_CNF)
						*readcnf << " " << readcnf_TAction(*it, t);
				}
			}
			for(it = p->addEffectAtEnd.begin(); it != p->addEffectAtEnd.end(); ++it)
			{
				const PAction *a = pProblem.pAllAction.GetActionById(*it);
				if(t >= a->duration) // if a can finish at t
				{
					AddToClause(ActionTime2Var(*it, t - a->duration), true);
					if(GEN_CNF)
						*cnf << " " << cnf_True(ActionTime2Var(*it, t - a->duration));
					if(GEN_READABLE_CNF)
						*readcnf << " " << readcnf_TAction(*it, t - a->duration);
				}
			}
			AddClause(ccAxiomAdd);
			if(GEN_CNF)
				*cnf << " 0\n";
			if(GEN_READABLE_CNF)
				*readcnf << "\n";
		} // end of 5
	}
}

// quick and dirty , bug on parking domain
void SatTime::AddMutexStart_End()
{
	cout << " n2 ";
	set<int>::const_iterator itJ, itK;
	for(int i=0; i<nProp; i++)
	{
		CheckForTimeOut();
		const PProposition *p = pProblem.pAllProposition.GetPropositionById(i);
		
		/// start - start
		for(itJ = p->conditionAtStart.begin(); itJ != p->conditionAtStart.end(); ++itJ)
		{
			int a = *itJ;
			const PAction *A = pProblem.pAllAction.GetActionById(a);
			for(itK = p->delEffectAtStart.begin(); itK != p->delEffectAtStart.end(); ++itK)
			{
				int b = *itK;
				if(a == b)
					continue;
				const PAction *B = pProblem.pAllAction.GetActionById(b);
				for(int t=0; t<T; t++)
				{
					if(!(t + A->duration < T)) // if A can't start at t
						break;
					if(!(t + B->duration < T)) // if B can't start at t
						break;
					ResetClause();
					AddToClause(ActionTime2Var(a, t), false);
					AddToClause(ActionTime2Var(b, t), false);
					AddClause(ccMutexStart);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t)) << " " << cnf_False(ActionTime2Var(b, t)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(a, t) << " " << readcnf_NAction(b, t) << " 0\n";
				}
			}
		}

		/// end - end
		for(itJ = p->conditionAtEnd.begin(); itJ != p->conditionAtEnd.end(); ++itJ)
		{
			int a = *itJ;
			const PAction *A = pProblem.pAllAction.GetActionById(a);
			for(itK = p->delEffectAtEnd.begin(); itK != p->delEffectAtEnd.end(); ++itK)
			{
				int b = *itK;
				if(a == b)
					continue;
				const PAction *B = pProblem.pAllAction.GetActionById(b);
				
				int biggerEndPoint = A->duration;
				if(biggerEndPoint < B->duration)
					biggerEndPoint = B->duration;
				for(int t=biggerEndPoint; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(a, t - A->duration), false);
					AddToClause(ActionTime2Var(b, t - B->duration), false);
					AddClause(ccMutexEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t - A->duration)) << " " << cnf_False(ActionTime2Var(b, t - B->duration)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(a, t - A->duration) << " " << readcnf_NAction(b, t - B->duration) << " 0\n";
				}
			}
		}

		/// start - end
		for(itJ = p->conditionAtStart.begin(); itJ != p->conditionAtStart.end(); ++itJ)
		{
			int a = *itJ;
			const PAction *A = pProblem.pAllAction.GetActionById(a);
			for(itK = p->delEffectAtEnd.begin(); itK != p->delEffectAtEnd.end(); ++itK)
			{
				int b = *itK;
				if(a == b)
					continue;
				const PAction *B = pProblem.pAllAction.GetActionById(b);
				
				// assume : a starts at t, b finishes at t (so starts at t-d)
				for(int t=B->duration; t < T; t++)
				{
					if(!(t + A->duration < T)) // if a can't start at t
						break;
					ResetClause();
					AddToClause(ActionTime2Var(a, t), false);
					AddToClause(ActionTime2Var(b, t - B->duration), false);
					AddClause(ccMutexStartEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t)) << " " << cnf_False(ActionTime2Var(b, t - B->duration)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(a, t) << " " << readcnf_NAction(b, t - B->duration) << " 0\n";
				}
			}
		}

		/// start - end 2
		for(itJ = p->delEffectAtStart.begin(); itJ != p->delEffectAtStart.end(); ++itJ)
		{
			int a = *itJ;
			const PAction *A = pProblem.pAllAction.GetActionById(a);
			for(itK = p->conditionAtEnd.begin(); itK != p->conditionAtEnd.end(); ++itK)
			{
				int b = *itK;
				if(a == b)
					continue;
				const PAction *B = pProblem.pAllAction.GetActionById(b);
				
				// assume : a starts at t, b finishes at t (so starts at t-d)
				for(int t=B->duration; t < T; t++)
				{
					if(!(t + A->duration < T)) // if a can't start at t
						break;
					ResetClause();
					AddToClause(ActionTime2Var(a, t), false);
					AddToClause(ActionTime2Var(b, t - B->duration), false);
					AddClause(ccMutexStartEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(a, t)) << " " << cnf_False(ActionTime2Var(b, t - B->duration)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(a, t) << " " << readcnf_NAction(b, t - B->duration) << " 0\n";
				}
			}
		}
	}
}

// slow but more accurate
void SatTime::OldSlow_AddMutexStart_End()
{
	for(int i=0; i<nAction; i++)
	{
	for(int j=0; j<nAction; j++)
	{
			CheckForTimeOut();
			const PAction *a = pProblem.pAllAction.GetActionById(i);
			const PAction *b = pProblem.pAllAction.GetActionById(j);
			
			if(j>i)
			{
			//shorter:
			if(Conflict(a->delEffectAtStart, b->conditionAtStart)
				|| Conflict(b->delEffectAtStart, a->conditionAtStart))
			//if(Conflict(a->delEffectAtStart, b->addEffectAtStart)
			//	|| Conflict(a->delEffectAtStart, b->conditionAtStart)
			//	|| Conflict(b->delEffectAtStart, a->addEffectAtStart)
			//	|| Conflict(b->delEffectAtStart, a->conditionAtStart))
			{
				for(int t=0; t<T; t++)
				{
					if(!(t + a->duration < T)) // if a can't start at t
						break;
					if(!(t + b->duration < T)) // if b can't start at t
						break;
					ResetClause();
					AddToClause(ActionTime2Var(i, t), false);
					AddToClause(ActionTime2Var(j, t), false);
					AddClause(ccMutexStart);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_False(ActionTime2Var(j, t)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(i, t) << " " << readcnf_NAction(j, t) << " 0\n";
				}
			}

			//shorter:
			if(Conflict(a->delEffectAtEnd, b->conditionAtEnd)
				|| Conflict(b->delEffectAtEnd, a->conditionAtEnd))
			//if(Conflict(a->delEffectAtEnd, b->addEffectAtEnd)
			//	|| Conflict(a->delEffectAtEnd, b->conditionAtEnd)
			//	|| Conflict(b->delEffectAtEnd, a->addEffectAtEnd)
			//	|| Conflict(b->delEffectAtEnd, a->conditionAtEnd))
			{
				int biggerEndPoint = a->duration;
				if(biggerEndPoint < b->duration)
					biggerEndPoint = b->duration;
				for(int t=biggerEndPoint; t<T; t++)
				{
					ResetClause();
					AddToClause(ActionTime2Var(i, t - a->duration), false);
					AddToClause(ActionTime2Var(j, t - b->duration), false);
					AddClause(ccMutexEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(i, t - a->duration)) << " " << cnf_False(ActionTime2Var(j, t - b->duration)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(i, t - a->duration) << " " << readcnf_NAction(j, t - b->duration) << " 0\n";
				}
			}
			}

			if(j!=i)
			{
			//shorter:
			if( Conflict(a->delEffectAtStart, b->conditionAtEnd)
				|| Conflict(a->conditionAtStart, b->delEffectAtEnd))
			//if(Conflict(a->delEffectAtStart, b->addEffectAtEnd)
			//	|| Conflict(a->delEffectAtStart, b->conditionAtEnd)
			//	|| Conflict(a->conditionAtStart, b->delEffectAtEnd)
			//	|| Conflict(a->addEffectAtStart, b->delEffectAtEnd))
			{
				// assume : a starts at t, b finishes at t (so starts at t-d)
				for(int t=b->duration; t < T; t++)
				{
					if(!(t + a->duration < T)) // if a can't start at t
						break;
					ResetClause();
					AddToClause(ActionTime2Var(i, t), false);
					AddToClause(ActionTime2Var(j, t - b->duration), false);
					AddClause(ccMutexStartEnd);
					if(GEN_CNF)
						*cnf << cnf_False(ActionTime2Var(i, t)) << " " << cnf_False(ActionTime2Var(j, t - b->duration)) << " 0\n";
					if(GEN_READABLE_CNF)
						*readcnf << readcnf_NAction(i, t) << " " << readcnf_NAction(j, t - b->duration) << " 0\n";
				}
			}
			}
	}
	}
}

void SatTime::AddPropForbidClauses(vector<int> *prop_layer)
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
		/*else
			for(int t=0; t<tmax; t++)
			{
				ResetClause();
				AddToClause(ActionTime2Var(i-nProp, t, ACTION_OVERALL), false);
				AddClause(ccNotApplicable); // FIXME: fix stats
				if(GEN_CNF)
					*cnf << cnf_False(ActionTime2Var(i-nProp, t, ACTION_OVERALL)) << " 0\n";
				if(GEN_READABLE_CNF)
					*readcnf << readcnf_NActionO(i-nProp, t) << " 0\n";
			}*/
	}
}

void SatTime::AddFactMutexes(vector< vector<Mutex> > *fact_mutex)
{
	int graphLayers = fact_mutex->size();
	for(int t=0; t<=T; t++)
	{
		CheckForTimeOut();
		int effective_t;
		if(t >= graphLayers)
			effective_t = graphLayers - 1;
		else
			effective_t = t;
		vector<Mutex> &vm = (*fact_mutex)[effective_t];
		for(vector<Mutex>::const_iterator it = vm.begin(); it != vm.end(); ++it)
		{
			if(it->first < nProp && it->second < nProp)
			{
				ResetClause();
				AddToClause(PropTime2Var(it->first, t), false);
				AddToClause(PropTime2Var(it->second, t), false);
				AddClause(ccNotApplicable); // FIXME: fix stats
			}

			//ResetClause();
			//if(t==T)
			//	if(!(it->first < nProp && it->second < nProp))
			//		continue;
			//if(it->first < nProp)
			//	AddToClause(PropTime2Var(it->first, t), false);
			//else
			//	AddToClause(ActionTime2Var(it->first - nProp, t, ACTION_OVERALL), false);
			//if(it->second < nProp)
			//	AddToClause(PropTime2Var(it->second, t), false);
			//else
			//	AddToClause(ActionTime2Var(it->second - nProp, t, ACTION_OVERALL), false);
			//AddClause(ccNotApplicable); // FIXME: fix stats
			// FIXME: fix these rules:
			//if(GEN_CNF)
			//	*cnf << cnf_False(PropTime2Var(it->a, t)) << " " << cnf_False(PropTime2Var(it->b, t)) << " 0\n";
			//if(GEN_READABLE_CNF)
			//	*readcnf << readcnf_NProp(it->a, t) << " " <<  readcnf_NProp(it->b, t) << " 0\n";
		}
	}
}

void SatTime::AddMutexDuring_Redundant()
{
	long long counterMax = 0;
	if(overallPercent == 0)
		return;
	if(overallPercent == 100)
		counterMax = INTMAX_MAX;
	else
		counterMax = overallPercent * MutexDuring_CalculateRedundant() / 100;
	for(int i=0; i<nAction; i++)
	{
		const PAction *b = pProblem.pAllAction.GetActionById(i); // running action (overall condition)
		if(b->duration <= 2)
			continue;
		for(int j=0; j<nAction; j++)
		{
			if(i==j)
				continue;
			if(counterMax!=0 && ccMutexOverall>counterMax)
				return;
			CheckForTimeOut();
			const PAction *a = pProblem.pAllAction.GetActionById(j); // starting action or ending action
			if(Conflict(a->delEffectAtStart, b->conditionOverAll))
				// assume : b finishes at t (so starts at t-d)
				for(int t=b->duration; t < T; t++)
				{
					// t2 changes over [t-d+1,t-1]
					for(int t2=t - b->duration + 1; t2<t; t2++)
					{
						if(t2 + a->duration < T) // if a can start at t2
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t2), false);
							AddToClause(ActionTime2Var(i, t - b->duration), false);
							AddClause(ccMutexOverall);
							if(GEN_CNF)
								*cnf << cnf_False(ActionTime2Var(j, t2)) << " " << cnf_False(ActionTime2Var(i, t - b->duration)) << " 0\n";
							if(GEN_READABLE_CNF)
								*readcnf << readcnf_NAction(j, t2) << " " << readcnf_NAction(i, t - b->duration) << " 0\n";
						}
						else
							break;
					}
				}
			if(Conflict(a->delEffectAtEnd, b->conditionOverAll))
				// assume : b finishes at t (so starts at t-d)
				for(int t=b->duration; t < T; t++)
				{
					// t2 changes over [t-d+1,t-1] (in reverse orders)
					for(int t2=t-1; t2 >= t-b->duration+1; t2--)
					{
						if(t2 >= a->duration ) // if a can finish at t2
						{
							ResetClause();
							AddToClause(ActionTime2Var(j, t2 - a->duration), false);
							AddToClause(ActionTime2Var(i, t - b->duration), false);
							AddClause(ccMutexOverall);
							if(GEN_CNF)
								*cnf << cnf_False(ActionTime2Var(j, t2 - a->duration)) << " " << cnf_False(ActionTime2Var(i, t - b->duration)) << " 0\n";
							if(GEN_READABLE_CNF)
								*readcnf << readcnf_NAction(j, t2 - a->duration) << " " << readcnf_NAction(i, t - b->duration) << " 0\n";
						}
						else
							break;
					}
				}
		}
	}
}

long long SatTime::MutexDuring_CalculateRedundant()
{
	long long counter = 0;
	for(int i=0; i<nAction; i++)
	{
		const PAction *b = pProblem.pAllAction.GetActionById(i); // running action (overall condition)
		if(b->duration <= 2)
			continue;
		for(int j=0; j<nAction; j++)
		{
			if(i==j)
				continue;
		CheckForTimeOut();
			const PAction *a = pProblem.pAllAction.GetActionById(j); // starting action or ending action
			if(Conflict(a->delEffectAtStart, b->conditionOverAll))
			{
				// assume : b finishes at t (so starts at t-d)
				for(int t=b->duration; t < T; t++)
				{
					// t2 changes over [t-d+1,t-1]
					for(int t2=t - b->duration + 1; t2<t; t2++)
					{
						if(t2 + a->duration < T) // if a can start at t2
							counter++;
						else
							break;
					}
				}
			}
			if(Conflict(a->delEffectAtEnd, b->conditionOverAll))
			{
				// assume : b finishes at t (so starts at t-d)
				for(int t=b->duration; t < T; t++)
				{
					// t2 changes over [t-d+1,t-1] (in reverse orders)
					for(int t2=t-1; t2 >= t-b->duration+1; t2--)
					{
						if(t2 >= a->duration ) // if a can finish at t2
							counter++;
						else
							break;
					}
				}
			}
		}
	}
	return counter;
}

void SatTime::Report_CNFStats(bool silent)
{
	long long totalMutexes = ccMutexStart + ccMutexEnd + ccMutexStartEnd + ccMutexOverall;
	long long totalClauses = ccInit + ccGoal + ccNotApplicable + ccCondition + ccEffect + ccAxiomDelete + 
								ccAxiomAdd + totalMutexes;
	satresults->varProp = nvProp;
	satresults->varAction = nvAction;
	satresults->varTotal = satresults->varProp + satresults->varAction;
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
	cout << "Variables: total=" << satresults->varTotal << "\tpropositions=" << satresults->varProp << "\tactions: " << satresults->varAction << endl;
	//cout << "Clauses: initital state=" << ccInit << " pProblem.goals=" << ccGoal << " not-applicable actions=" << ccNotApplicable << endl;
	//cout << "         imply conditions=" << ccCondition << " imply effects=" << ccEffect << endl;
	//cout << "         delete axioms=" << ccAxiomDelete << " add axioms=" << ccAxiomAdd << endl;
	//cout << "Mutex Clauses: start-start=" << ccMutexStart << " end-end=" << ccMutexEnd
	//	 << " start-end=" << ccMutexStartEnd << " overall=" << ccMutexOverall << endl;
	cout << "Total Mutex Clauses=" << totalMutexes << "\tratio=" << (double)totalMutexes/totalClauses;
	cout << "\tTotal Clauses=" << totalClauses << endl << flush;
}

}
