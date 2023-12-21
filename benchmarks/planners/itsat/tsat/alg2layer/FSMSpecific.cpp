#include "tsat/alg2layer/FSM_Specific.h"
#include "tsat/satlayer/SatLayer.h"
using namespace nsSatLayer;

void AddNegCycleAutomaton(const vector<PlanEvent> &negCycle, int T, SatLayer *solver)
{
	// add a blocking clause for negative cycle, not useful at all
	//Minisat::vec<Minisat::Lit> solution;
	//for each( int i in negCycle )
	//{
	//	solution.push(~ solver->plan[i-1].var);
	//}
	//solver->AddFullClause(solution);
	int sz = negCycle.size();
	int **vars = new int*[sz];
	long long totalvars = 0;
	for(int i=0; i<sz; i++)
	{
		vars[i] = new int[T];
		for(int t=0; t<T; t++)
		{
			vars[i][t] = 1 + solver->SATNewVar();
		}
	}
	for(int t=0; t<T; t++)
	{
		solver->ResetClause();
		solver->AddToClause( vars[sz-1][t], false );
		solver->AddClause(totalvars);
	}

	PlanEvent node, nodeNext, nodeEnd;
	nodeEnd = negCycle[sz-1];
	for(int i=0; i<sz; i++)
	{
		node = negCycle[i];
		if( i<sz-1 )
		{
			nodeNext = negCycle[i+1];
		}

		int var1, var2;
		bool el1, el2;
		// as 0 bs 1 be 2 ae 3
		//       ast => 0t
		// 0t && bst => 1t
		// 1t && bet => 2t
		// 2t && aet => 3t
		for(int t=0; t<T; t++)
		{
			var1 = solver->ActionTime2Var(node.id, t, node.part);
			solver->ResetClause();
			if(i>0)
				solver->AddToClause( vars[i-1][t], false );
			solver->AddToClause( var1, false );
			solver->AddToClause( vars[i][t], true );
			solver->AddClause(totalvars);
		}
		if(i==sz-1)
			continue;
		// as 0 bs 1 be 2 ae 3
		// 0t && ~aet && ~bst => 0t+1
		// 1t && ~aet && ~bet => 1t+1
		// 2t && ~aet && ~aet => 2t+1
		// nothing for 3t
		for(int t=0; t<T-1; t++)
		{
			var1 = solver->ActionTime2Var(nodeEnd.id, t, nodeEnd.part);
			var2 = solver->ActionTime2Var(nodeNext.id, t, nodeNext.part);
			solver->ResetClause();
			solver->AddToClause( vars[i][t], false );
			solver->AddToClause( var1, true );
			solver->AddToClause( var2, true );
			solver->AddToClause( vars[i][t+1], true );
			solver->AddClause(totalvars);
		}
		// as 0 bs 1 be 2 ae 3
		// ~0t-1 && 0t =>       ast
		// ~1t-1 && 1t => 0t && bst
		// ~2t-1 && 2t => 1t && bet
		// nothing for 3t
		for(int t=0; t<T-1; t++)
		{
			var1 = solver->ActionTime2Var(node.id, t, node.part);
			solver->ResetClause();
			if(t>0)
				solver->AddToClause( vars[i][t-1], true );
			solver->AddToClause( vars[i][t], false );
			solver->AddToClause( var1, true );
			solver->AddClause(totalvars);
			// bugfix 1391/2/26: added the following for first item of RHS
			if(i>0)
			{
				solver->ResetClause();
				if(t>0)
					solver->AddToClause( vars[i][t-1], true );
				solver->AddToClause( vars[i][t], false );
				solver->AddToClause( vars[i-1][t], true );
				solver->AddClause(totalvars);
			}
		}
	}
}
