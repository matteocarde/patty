
/*  2010 (C) Jussi Rintanen  */

extern int SATheuristic;
extern int PLANheuristic;
extern int planFrontend;
extern int flagShowInput;
extern int flagShowInvariants;
extern int flagRestartInterval;
extern int flagRestartScheme;
extern int flagTimeout;
extern int flagRealTimeout;
extern int debugOutput;
extern int flagPDDLadddel;
extern int flagPreprocessing;
extern int flagIPCplans;
extern int flagCEvariables;	/* Create a variable for each conditional effect. */
extern int flagRandomSeedTime; /* Use the time as a random seed (instead of 0). */
extern int flagNoInvariants;
extern int flagEliminateConverses; /* Eliminate redundant converse literals. */
extern int flagExternalPreprocessor;
extern int flagAtLeastOneAction;
extern float flagMemoryLimit; /* Max. MB of memory allowed to allocate. */

extern long TIMEstartReal,TIMEstart,TIMEpreprocess,TIMEdisabling,TIMEdisaprepro,TIMEinvariants;

#ifdef MULTICORE
extern int nOfThreads;
#endif

float timefromstart();

extern double allocatedbyFE;

typedef enum { Sequ, EStep, EStepOgata, AStep } semantics;

extern semantics planSemantics;

extern int currentInputFile;
extern int nOfInputFiles;
extern char *inputfiles[10];
extern char *outputfile;

extern int flagOutputDIMACS;

void *statmalloc(int,int);
//#define statmalloc(a,b) malloc(b)

extern int firstTimePoint;
extern int lastTimePoint;
extern int outputTimeStep;

extern char *filenamebase;

extern int evalAlgorithm;	/* 0 = A, 1 = B, 2 = C */
extern int paramA;
extern float paramB;
extern float paramC;
extern int paramM; /* Max. processes for algorithm B. */

/* Heuristics */

extern int HEURordmode; /* 0 = earliest, 1 = latest, 2 = difference */
extern int HEURordmin; /* 0 = smaller is better, 1 = bigger is better */
extern int HEURordrnd; /* 1 = randomly shuffle (to break ties) */
extern int HEURtime; /* 0 = earliest, 1 = latest, 2 = all */
extern int HEURops; /* 0 = first, 1 = all */
extern int HEURchoice; /* 0 = random, 1 = weight */
extern int HEURactions; /* How many suggested actions found? */
extern int HEURactionchoice; /* choose action 0 = randomly, 1 = minimal time stamp */
extern int HEURactiondepthlimit;

extern int stats_longest_learned;
