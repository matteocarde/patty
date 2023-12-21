#ifndef SATTIME_H
#define SATTIME_H

#include <fstream>
#include <vector>
#include <exception>
#include "precosat/precosat.h"
#include "tsat/zchaff.h"
#include "minisat/simp/SimpSolver.h"
#include "minisat/utils/System.h"
#include "tsat/graph/ITGraph.h" // for Mutex
#include <iostream>
using namespace std;

namespace nsSatTime
{

enum Outcome
{
	SAT, UNSAT, TIMEOUT, MEMOUT, INDET, TIMEOUT_FORMULA
};

struct SATResults
{
	int T;
	Outcome outcome;
	int varProp, varAction, varTotal;
	long long ccEvent;
	long long ccInit, ccGoal, ccNotApplicable, ccCondition, ccEffect, ccAxiomDelete, ccAxiomAdd;
	long long ccMutexStart, ccMutexEnd, ccMutexStartEnd, ccMutexOverall;
	long long totalMutexes, totalClauses;
	double time_overall;
};

struct PlanAction
{
	int id;
	int t;
};

// abstract class, contains must of implementations of encoding phase
class SatTime
{
	ofstream *cnf, *readcnf;
	string detailsFileNameTemplate;

	int T;
	int overallPercent;
	bool GEN_CNF, GEN_READABLE_CNF;

	int *index2var;

	long long ccInit, ccGoal, ccNotApplicable, ccCondition, ccEffect, ccAxiomDelete, 
		ccAxiomAdd, ccMutexStart, ccMutexEnd, ccMutexStartEnd, ccMutexOverall;

	// declared here, defined in SatTimeMinisat and SatTimeZchaff
	virtual void ResetClause()=0;
	virtual void AddToClause(int n, bool polarity)=0;
	virtual void AddClause(long long &counter)=0;
	virtual int SATNewVar()=0; // used in ActionTime2Var() and PropTime2Var()

	inline int PropTime2Var(int p, int t)
	{
		int propIndex = p+t*nProp;
		if(index2var[propIndex]==-1)
		{
			index2var[propIndex] = SATNewVar();
			var2index.push_back(propIndex);
		}
		return 1+index2var[propIndex];
	}
	int ActionTime2Var(int a, int t)
	{
		int actionIndex = nvProp + a+t*nAction;
		if(index2var[actionIndex]==-1)
		{
			index2var[actionIndex] = SATNewVar();
			var2index.push_back(actionIndex);
		}
		return 1+index2var[actionIndex];
	}

protected:
	float startTime, totalTime;
	bool DONT_SOLVE;
	SATResults *satresults;
	int nProp, nAction;
	int nvProp, nvAction;
	vector<int> var2index;

	void AddInitialState();
	void AddGoals();
	void AddConditions();
	void AddEffects();
	void AddExplanatoryAxioms_Delete();
	void AddExplanatoryAxioms_Add();
	void AddMutexStart_End();
	void OldSlow_AddMutexStart_End();
	void AddPropForbidClauses(vector<int> *prop_layer);
	void AddFactMutexes(vector< vector<Mutex> > *fact_mutex);
	void AddMutexDuring_Necessary();
	void AddMutexDuring_Redundant();
	long long MutexDuring_CalculateRedundant();

public:
	SatTime(
		int t, SATResults *results,
		string detailsfilenametemplate,
		float totaltime, int overall_percent,
		bool gen_cnf, bool gen_readable_cnf, bool dont_solve);
	~SatTime() { }

	vector<PlanAction> plan;

	void DoEncoding();
	void DoEncoding(vector< vector<Mutex> > *fact_mutex, vector<int> *prop_layer);
	void Report_CNFStats(bool silent=false);
	virtual void Solve() = 0;
	virtual void GeneratePlan() = 0;
};

class SatTimePrecosat : public SatTime
{
	PrecoSat::Solver *precosatSolver;

	inline void ResetClause()
	{
		// not needed with Precosat
	}
	inline void AddToClause(int n, bool polarity)
	{
		if(polarity)
			precosatSolver->add(2 * n);
		else
			precosatSolver->add(2 * n + 1);
	}
	inline void AddClause(long long &counter)
	{
		++counter;
		precosatSolver->add(0);
	}
	inline int SATNewVar()
	{
		return precosatSolver->next()-1;
	}
public:
	SatTimePrecosat(
		int t, SATResults *results,
		string detailsfilenametemplate,
		float totaltime, int overall_percent,
		bool gen_cnf, bool gen_readable_cnf, bool dont_solve)
		:
	SatTime(t, results, detailsfilenametemplate,
		totaltime, overall_percent, gen_cnf, gen_readable_cnf, dont_solve)
	{
		precosatSolver = new PrecoSat::Solver();
		precosatSolver->init(0);
		precosatSolver->set ("verbose", 1);
		precosatSolver->set ("quiet", 0);
		precosatSolver->set ("print", 0);
		precosatSolver->fxopts ();
	}
	~SatTimePrecosat()
	{
		if(precosatSolver)
		{
			precosatSolver->reset();
			delete precosatSolver;
		}
	}
	void Solve();
	void GeneratePlan();
};

class SatTimeMinisat : public SatTime
{
	Minisat::SimpSolver *minisatSolver;
    Minisat::vec<Minisat::Lit> lits;
	
	inline void ResetClause()
	{
		lits.clear();
	}
	inline void AddToClause(int n, bool polarity)
	{
		if(polarity)
			lits.push(Minisat::mkLit(n-1));
		else
			lits.push(~Minisat::mkLit(n-1));
	}
	inline void AddClause(long long &counter)
	{
		counter++;
		minisatSolver->addClause_(lits);
	}
	inline int SATNewVar()
	{
		return minisatSolver->newVar();
	}
public:
	SatTimeMinisat(
		int t, SATResults *results,
		string detailsfilenametemplate,
		float totaltime, int overall_percent,
		bool gen_cnf, bool gen_readable_cnf, bool dont_solve)
		:
	SatTime(t, results, detailsfilenametemplate,
		totaltime, overall_percent, gen_cnf, gen_readable_cnf, dont_solve)
	{
		minisatSolver = new Minisat::SimpSolver();
	}
	~SatTimeMinisat()
	{
		if(minisatSolver)
			delete minisatSolver;
	}
	void Solve();
	void GeneratePlan();
};

class SatTimeZchaff : public SatTime
{
	SAT_Manager zchaffSolver;
	int clause[1000];
	int clauseCount;
	
	inline void ResetClause()
	{
		clauseCount = 0;
	}
	inline void AddToClause(int n, bool polarity)
	{
		if(clauseCount > 1000)
			throw runtime_error("Maximum length of clause count reached. Currently set to 1000 literals.");
		if(polarity)
			clause[clauseCount++] = 2*n;
		else
			clause[clauseCount++] = 1 + 2*n;
	}
	inline void AddClause(long long &counter)
	{
		counter++;
		SAT_AddClause(zchaffSolver, clause, clauseCount);
	}
	inline int SATNewVar()
	{
		return SAT_AddVariable(zchaffSolver) - 1;
	}
public:
	SatTimeZchaff(
		int t, SATResults *results,
		string detailsfilenametemplate,
		float totaltime, int overall_percent,
		bool gen_cnf, bool gen_readable_cnf, bool dont_solve)
		:
	SatTime(t, results, detailsfilenametemplate,
		totaltime, overall_percent, gen_cnf, gen_readable_cnf, dont_solve)
	{
		zchaffSolver = SAT_InitManager();
	}
	~SatTimeZchaff()
	{
		if(zchaffSolver)
			SAT_ReleaseManager(zchaffSolver);
	}
	void Solve();
	void GeneratePlan();
};

}

#endif
