/************************************************************************

THIS SOURCE CODE IS SUPPLIED "AS IS" WITHOUT WARANTY OF ANY KIND, AND ITS AUTHOR AND THE JOURNAL OF ARTIFICIAL INTELLIGENCE RESEARCH (JAIR) AND JAIR'S PUBLISHERS AND DISTRIBUTORS, DISCLAIM ANY AND ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, AND ANY WARRANTIES OR NON INFRINGEMENT. THE USER ASSUMES ALL LIABILITY AND RESPONSIBILITY FOR USE OF THIS SOURCE CODE, AND NEITHER THE AUTHOR NOR JAIR, NOR JAIR'S PUBLISHERS AND DISTRIBUTORS WILL BE LIABLE FOR DAMAGES OF ANY KIND RESULTING FROM ITS USE. Without limiting the generality of the foregoing, neither the auther, not JAIR's publishers and distributors, warrant that the Source Code will be error-free, will operate without interruption or will meet the needs of the user.
 
 ************************************************************************/


/* PART OF THIS CODE IS FROM "VAL"
main() for the PDDL2.2 parser

$Date: 2009-02-05 10:50:26 $
$Revision: 1.2 $

This expects any number of filenames as arguments, although
it probably doesn't ever make sense to supply more than two.

stephen.cresswell@cis.strath.ac.uk

Strathclyde Planning Group

AND HERE IS THE COPYRIGHT NOTICE FROM STRATHCLYDE PLANNINF GROUP:

 ************************************************************************
 * Copyright 2008, Strathclyde Planning Group,
 * Department of Computer and Information Sciences,
 * University of Strathclyde, Glasgow, UK
 * http://planning.cis.strath.ac.uk/
 *
 * Maria Fox, Richard Howey and Derek Long - VAL
 * Stephen Cresswell - PDDL Parser
 *
 * This file is part of VAL, the PDDL validator.
 *
 * VAL is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * VAL is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with VAL.  If not, see <http://www.gnu.org/licenses/>.
 *
 ************************************************************************
*/

#ifdef NO_CLOSE_DEBUG_DIALOG
	#include <Windows.h>
#endif
#include <iostream>
#include <fstream>
#include <cstring> // for strcmp()
#include <cstdlib> // for atoi()
#include <climits> // for INT_MAX
#include "tsat/parser/ParserClasses.h"
#include "tsat/AlgCommonParams.h"
//#include "tsat/alg1time/Alg1Time.h"
#include "tsat/alg2layer/Alg2Layer.h"
#include "tsat/utils.h"
using namespace std;
using namespace MyParser;

#include "tsat/val/ptree.h"
#include "tsat/val/FlexLexer.h"
using namespace VAL;
extern int yyparse();
extern int yydebug;
char *current_filename;

// #define TA_PROJECT
// NOTE: there is another TA_PROJECT in ParserClasses.cpp

void disableCloseDebugDialog();
void copyright();
void usage(char *exeName);
bool parseCommandLine(int argc, char * argv[], char * &domainFileName, char * &problemFileName, AlgCommonParams &commonParams, bool &RunAlg1Time);
bool valParser(parse_category * &mydomain, parse_category * &myproblem, char * domainFileName, char * problemFileName);

namespace VAL {
	parse_category* top_thing=NULL;
	analysis an_analysis;
	analysis* current_analysis;
	yyFlexLexer* yfl;
};

int main(int argc, char * argv[])
{
	// no need to this. for more info look inside the function
	// disableCloseDebugDialog();

	AlgCommonParams commonParams;
	char *domainFileName = NULL, *problemFileName = NULL;
	bool RunAlg1Time = true;
	if( ! parseCommandLine(argc, argv, domainFileName, problemFileName, commonParams, RunAlg1Time) )
		return 1;

	cout << "Using SAT Solver : " << commonParams.satsolver << endl;
	
	parse_category *mydomain, *myproblem;
	if( ! valParser(mydomain, myproblem, domainFileName, problemFileName) )
		return 2;

	// PDDLParser Limitations (AI Planning Course)
#ifdef TA_PROJECT
	domain *dm = (domain *)mydomain;
	if(dm->isDurative())
	{
		cerr << "Error: The domain is not STRIPS." << endl;
		return 2;
	}
	if(dm->isTyped())
	{
		cerr << "Warning: The domain is typed; But the output of PDDLParser will be untyped." << endl;
	}
	if(dm->req & (E_EQUALITY | E_DISJUNCTIVE_PRECONDS | E_COND_EFFS | E_NEGATIVE_PRECONDITIONS
		| E_DERIVED_PREDICATES | E_TIMED_INITIAL_LITERALS | E_ACTIONCOSTS))
	{
		cerr << "Error: The domain has some unsupported requirements. PDDLParser supports pure STRIPS only." << endl;
		return 2;
	}
#endif

	// PARSE VAL OUTPUT
	try
	{
		if(!AddParserClasses(mydomain))
		{
			cout << endl << "Importing VAL parser data structures failed." << endl;
			return 3;
		}
	}
	catch(const exception &e)
	{
		cout << endl << "Exception during parse of VAL parse tree: " << e.what() << endl;
		return 3;
	}

	// INSTANTIATE and make ground version of problem
	try
	{
		if(!AddProblemClasses(myproblem))
		{
			cout << endl << "Instantiation failed." << endl;
			return 3;
		}
	}
	catch(const exception &e)
	{
		cout << endl << "Exception during instantiation: " << e.what() << endl;
		return 3;
	}

	// NOW THE REAL DEAL:

#ifdef TA_PROJECT
	string fn1 = changeExt(argv[1], ".txt");
	string fn2 = changeExt(argv[2], ".txt");
	ofstream file1(fn1); // DO THE SAME FOR Strips-Problem.txt
	streambuf* oldbuf = cout.rdbuf();
	cout.rdbuf(file1.rdbuf());
	pDomain.PrintTA();
	cout.rdbuf(oldbuf);
	file1.close();
	cout << "Output file " << fn1 << " created." << endl;
	ofstream file2(fn2);
	cout.rdbuf(file2.rdbuf());
	pProblem.PrintTA();
	cout.rdbuf(oldbuf);
	file2.close();
	cout << "Output file " << fn2 << " created." << endl;
#else
	//MakeDir("logs");
	//ChangeDir("logs");
	// output the ground version of the problem
	if(commonParams.groundVersion)
	{
		ofstream groundProblem(changeExt(problemFileName, ".grn").c_str());
		streambuf* oldbuf = cout.rdbuf();
		cout.rdbuf(groundProblem.rdbuf());
		pProblem.Print();
		cout.rdbuf(oldbuf);
		groundProblem.close();
	}
	
	try
	{
//		if(RunAlg1Time) // run algorithm 1 (planner used in seminar)
//			Alg1Time(commonParams);
//		else            // run algorithm 2 (based on 'implicit time' idea)
			Alg2Layer(commonParams);
	}
	catch(const exception &e)
	{
		if(RunAlg1Time)
			cout << endl << "Exception from Alg1Time(): " << e.what() << endl;
		else
			cout << endl << "Exception from Alg2Layer(): " << e.what() << endl;
	}
	//ChangeDir("..");
	//getchar();
#endif

	return 0;
}

void disableCloseDebugDialog()
{
	// Get rid of "Close/Debug" dialog in Microsoft Windows
//	DWORD dwMode = SetErrorMode(SEM_NOGPFAULTERRORBOX);
//	SetErrorMode(dwMode | SEM_NOGPFAULTERRORBOX);
	// This dialog is shown whenever the program fails to catch an exception.
	// The problem was that my approach to throw and catch exception was wrong:
	// try { throw "an exception"; }
	// catch(const exception &e) {}
	// I resolved the issue with:
	// throw exception("an exception");
	// I also used derived classes of exception, like overflow_error, runtime_error, etc
	// You may resolve the issue using the other way:
	// catch(const string &s) {}
	// But you will lose the opportunity to use hierarchical exception handling.
}

void copyright()
{
	cout << "TOPSAT: Temporal Optimal Planner using SATisfiability" << endl;
	cout << "        for PDDL 2.1 level 3 durative actions" << endl;
	cout << "Copyright 2011-2012, Sharif University of Technology." << endl;
	cout << "Part of this work is based on VAL: PDDL Plan Validator." << endl << endl;
}

void usage(char * exeName)
{
	cout << "Usage: " << exeName << " [switches] domain-pddl-file problem-pddl-file [plan-file]" << endl;
	cout << "       if plan-file is leaved empty, name will be generated automatically" << endl;
	cout << "       if plan-file is *, the plan output will be on the console" << endl;
	cout << "Switches:" << endl;
	cout << "  -ground: Writes the ground version of problem in .grn file" << endl;
	cout << "  -cnf: Creates CNF file for each generated encoding" << endl;
	cout << "  -readablecnf: Creates readable CNF file for each generated encoding" << endl;
	cout << "  -dontsolve: Will not try to solve encodings, use with -cnf or -readablecnf" << endl;
	cout << "  -t1 n: Starting Makespan will be n (ex. 1, default 1)" << endl;
	cout << "  -t2 n: Maximum Makespan will be n (ex. 20, default +Inf)" << endl;
	cout << "  -t+ n: Increase Makespan by n steps (ex. 1, default 1)" << endl;
	cout << "  -t* f: Increase Makespan by multiplication by f (ex. 1.2, default 1)" << endl;
	cout << "  -limit n: Sets global time limit to n (in seconds) (ex. 60, default 1800)" << endl;
	cout << "  -stagelimit n: Sets stage time limit for to n (in seconds) (ex. 60, def. 300)" << endl;
	cout << "  -overall f: Sets the percentage of redundant overall mutexes to f" << endl;
	cout << "       (ex. 100, default 0), use only with \"-alg time\"" << endl;
	cout << "  -alg time|layer: Specifies which algorithm to run (default layer)" << endl;
	cout << "  -conflicts: nlogn => reduced set - O(nlogn) clauses" << endl;
	cout << "  -conflicts: n2 ====> reduced set - O(n^2) clauses" << endl;
	cout << "  -conflicts: n2all => complete set - O(n^2) clauses (default)" << endl;
	cout << "  -graph: {nograph || fact || all} (default all)" << endl;
	cout << "  -satsolver: {precosat || minisat || zchaff} (default precosat)" << endl;
}

bool parseCommandLine(int argc, char * argv[], char * &domainFileName, char * &problemFileName, AlgCommonParams &commonParams, bool &RunAlg1Time)
{
#ifdef TA_PROJECT
	if(argc<3)
	{
		if(argc!=1)
			cout << "Usage error." << endl;
		cout << "PDDL Strips Parser" << endl;
		cout << "Copyright 2011, Sharif University of Technology." << endl << endl;
		cout << "Usage: " << argv[0] << " domain-pddl-file problem-pddl-file" << endl;
		cout << "Output files are named same as the input files with .txt extension." << endl;
		return false;
	}
	cout << "PDDL Strips Parser" << endl;

	commonParams.gen_cnf = false;
	commonParams.gen_readable_cnf = false;
	commonParams.justgencnf = false;
	commonParams.TStart = 1;
	commonParams.TEnd = INT_MAX;
	commonParams.overall = 0;
	commonParams.TMultiply = 1;
	commonParams.TPlus = 3;
	commonParams.AvailableTime = 18000;
	commonParams.StageTime = 180;
	domainFileName = argv[1];
	problemFileName = argv[2];
	if(argc>3)
		commonParams.planFileName = argv[3];
#else
	commonParams.gen_cnf = false;
	commonParams.gen_readable_cnf = false;
	commonParams.justgencnf = false;
	commonParams.TStart = 1;
	commonParams.TEnd = INT_MAX;
	commonParams.overall = 0;
	commonParams.TMultiply = 1;
	commonParams.TPlus = 3;
	commonParams.AvailableTime = 18000;
	commonParams.StageTime = 180;
	commonParams.conflictsMethod = 3; // n2all
	commonParams.graphUsage = 0; // all (fact+overall)
	commonParams.groundVersion = false;
	commonParams.satsolver = "precosat";
	//RunAlg1Time=1;
	for(int i=1, j=0; i<argc; i++)
	{
		if(argv[i][0] == '-') // a switch
		{
			if(strcmp(argv[i],"-ground") == 0)
				commonParams.groundVersion = true;
			else if(strcmp(argv[i],"-cnf") == 0)
				commonParams.gen_cnf = true;
			else if(strcmp(argv[i],"-readablecnf") == 0)
				commonParams.gen_readable_cnf = true;
			else if(strcmp(argv[i],"-dontsolve") == 0)
				commonParams.justgencnf = true;
			else if(strcmp(argv[i],"-t1") == 0)
				commonParams.TStart = atoi(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-t2") == 0)
				commonParams.TEnd = atoi(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-t+") == 0)
				commonParams.TPlus = atoi(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-t*") == 0)
				commonParams.TMultiply = atof(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-limit") == 0)
				commonParams.AvailableTime = atof(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-stagelimit") == 0)
				commonParams.StageTime = atof(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-overall") == 0)
				commonParams.overall = atof(argv[++i]); // also increments i
			else if(strcmp(argv[i],"-alg") == 0)
				RunAlg1Time = strcmp(argv[++i], "time") == 0; // also increments i
			else if(strcmp(argv[i],"-conflicts") == 0)
			{
				i++;
				if(strcmp(argv[i],"nlogn") == 0)
					commonParams.conflictsMethod = 1;
				else if(strcmp(argv[i],"n2") == 0)
					commonParams.conflictsMethod = 2;
				else if(strcmp(argv[i],"n2all") == 0)
					commonParams.conflictsMethod = 3;
				else
				{
					cout << "Invalid parameter after \"" << argv[i-1] << "\" switch: " << argv[i] << endl << endl;
					usage(argv[0]);
					return false;
				}
			}
			else if(strcmp(argv[i],"-graph") == 0)
			{
				i++;
				if(strcmp(argv[i],"nograph") == 0)
					commonParams.graphUsage = 0;
				else if(strcmp(argv[i],"fact") == 0)
					commonParams.graphUsage = 1;
				else if(strcmp(argv[i],"all") == 0)
					commonParams.graphUsage = 2;
				else
				{
					cout << "Invalid parameter after \"" << argv[i-1] << "\" switch: " << argv[i] << endl << endl;
					usage(argv[0]);
					return false;
				}
			}
			else if(strcmp(argv[i],"-satsolver") == 0)
			{
				i++;
				if(strcmp(argv[i],"minisat") == 0)
					commonParams.satsolver = "minisat";
				else if(strcmp(argv[i],"precosat") == 0)
					commonParams.satsolver = "precosat";
				else if(strcmp(argv[i],"zchaff") == 0)
					commonParams.satsolver = "zchaff";
				else
				{
					cout << "Invalid parameter after \"" << argv[i-1] << "\" switch: " << argv[i] << endl << endl;
					usage(argv[0]);
					return false;
				}
			}
			else
			{
				cout << "Invalid switch: " << argv[i] << endl << endl;
				usage(argv[0]);
				return false;
			}
		}
		else // an argument
		{
			switch(j)
			{
			case 0:
				domainFileName = argv[i];
				j++;
				break;
			case 1:
				problemFileName = argv[i];
				j++;
				break;
			case 2:
				commonParams.planFileName = argv[i];
				j++;
				break;
			}
		}
	}
	if(domainFileName == NULL || problemFileName == NULL)
	{
		if(argc!=1)
			cout << "Usage error." << endl << endl;
		usage(argv[0]);
		return false;
	}
	else
	{
		copyright();
		commonParams.detailsFileNameTemplate = changeExt(problemFileName, ".dtl");
		if(commonParams.planFileName == "")
			commonParams.planFileName = changeExt(problemFileName, "");
		commonParams.resultsFileName = changeExt(problemFileName, ".xls");
	}
#endif

	return true;
}

bool valParser(parse_category * &mydomain, parse_category * &myproblem, char * domainFileName, char * problemFileName)
{
	current_analysis= &an_analysis;
	ifstream* current_in_stream;
	yydebug=0; // Set to 1 to output yacc trace
	yfl= new yyFlexLexer;
	
	// parse DOMAIN file
	current_filename = domainFileName;
	cout << "Parsing input file: " << current_filename << '\n';
	current_in_stream = new ifstream(current_filename);
	if (current_in_stream->fail())
	{
		// Output a message now
		cout << "Failed to open \"" << current_filename << "\"\n";
		return false;
	}
	else
	{
		line_no= 1;
		// Switch the tokeniser to the current input stream
		yfl->switch_streams(current_in_stream,&cout);
		yyparse();
		// Output syntax tree
		//if (VAL::top_thing) top_thing->display(0);
		mydomain = top_thing;
	}
	delete current_in_stream;

	// parse PROBLEM file
	current_filename = problemFileName;
	cout << "Parsing input file: " << current_filename << '\n';
	current_in_stream = new ifstream(current_filename);
	if (current_in_stream->fail())
	{
		// Output a message now
		cout << "Failed to open \"" << current_filename << "\"\n";
		return false;
	}
	else
	{
		line_no= 1;
		// Switch the tokeniser to the current input stream
		yfl->switch_streams(current_in_stream,&cout);
		yyparse();
		// Output syntax tree
		//if (VAL::top_thing) top_thing->display(0);
		myproblem = top_thing;
	}
	delete current_in_stream;

	// clean up, report and return
	delete yfl;
	if(current_analysis->error_list.errors > 0)
	{
		cerr << "Parse terminated because of error:" << endl;
		current_analysis->error_list.report();
		return false;
	}
	cout << "Input files parsed successfully." << endl;
	return true;
}

