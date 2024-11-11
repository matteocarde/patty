#ifndef ALGCOMMONPARAMS_H
#define ALGCOMMONPARAMS_H

#include <string>
using namespace std;

struct AlgCommonParams
{
	string satsolver; // name of satsolver, eg. "minisat"
	string planFileName, resultsFileName; // eg. "pfile01.pddl", "pfile01.sol"
	string detailsFileNameTemplate; // eg. "pfile01.xls"
	float AvailableTime; // remaining time in seconds, initialized by total available time (usually 1800)
	float StageTime; // time available for each pair of Encode+Solve, could be set to total available time or less
	bool gen_cnf; // generate DIMACS compliant CNF file for each encoding
	bool gen_readable_cnf; // generate a somewhat "readable" CNF file
	bool justgencnf; // do not try to solve any encoding, just generate CNF file(s)
	int TStart, TEnd; // specify the range of makespan, or number of layers in case of ITSAT, to search
	int TPlus; // T will be added TPlus units each time, eg. T += TPlus
	float TMultiply; // T will be multiplied by TMultiply each time, eg. T *= TMultiply
	int overall; // special for Explicit Time version, for more info look inside AddMutexDuring_redundant() in SATTime.cpp
	int conflictsMethod; // the way to treat with conflicts: "n2", "n2all", "nlogn"
	int graphUsage; // 0: no use, 1: mutex between facts, 2: mutex between facts and overall part of actions
	bool groundVersion; // generate ground version of the given problem in .grn file
};

#endif
