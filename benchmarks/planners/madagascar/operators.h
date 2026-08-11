
/*  2012 (C) Jussi Rintanen  */

/**************** compact ground formulae */

#ifdef CFMA

/* Compact formula representation:
  Formula is a pointer.
  If the lsb is 1, it is TRUE, FALSE or a literal.
  If the lsb is 0, it is a pointer to an integer array for con/disjunction.
  For conjunctions and disjunctions the first int is (length << 1) | cnj,
  where cnj == 1 if it is a conjunction and cnj = 0 if it is a disjunction.
*/

typedef int **cfma;

/* If the lsb == 1, the 3 lsbs represent the type. */

#define cTRUEtag 1
#define cFALSEtag 3
#define cPATOMtag 5
#define cNATOMtag 7

/* Literals are represented as (var << 3) | c?ATOM. */

#define cPATOM(v) ((cfma)(((v) << 3) | cPATOMtag))
#define cNATOM(v) ((cfma)(((v) << 3) | cNATOMtag))
#define cTRUE ((cfma)cTRUEtag)
#define cFALSE ((cfma)cFALSEtag)

#endif

/**************** ground formulae */

typedef enum { patom, natom, conj, disj, TRUE, FALSE } fmatype;

typedef struct _fma {
  fmatype t;
  union {
    int a;
    struct _fmalist0 { struct _fma *hd; struct _fmalist0 *tl; } *juncts;
  };
} fma;


/***************** ground effects */

typedef struct _eff {
  fma *condition;
#ifdef CFMA
  cfma ccondition;
#endif
  int *effectlits;
  struct _eff *tl;
} eff;

typedef struct _fmalist { fma *hd; struct _fmalist* tl; } fmalist;

fmalist *fmacons(fma *,fmalist *);

fma *Fconj(fmalist *);
fma *Fdisj(fmalist *);
fma *Fconj2(fma *,fma *);
fma *Fdisj2(fma *,fma *);
fma *Fatom(int);
fma *Fnatom(int);
fma *Fneg(fma *);
fma *Fimpl(fma *,fma *);
fma *Ftrue();
fma *Ffalse();

typedef struct _action {
  int *name;
  fma *precon;
#ifdef CFMA
  cfma cprecon;
#endif
  eff effects;
  int cost;
} action;

extern int nOfActions;
extern int maxActions;
extern action *actions;

int disjunctivep(fma *);
void initactions();

int ptruep(fma *,int *);	/* Test for truth of a formula in a state. */
int execute(int,int *,int *);	/* Execute an action. */
void executeNOprecon(int,int *,int *);	/* Execute an action without testin precondition. */

int fprintactionname(FILE *,int);
int printactionname(int);
int fprintactionnameIPC(FILE *,int);
int printactionnameIPC(int);
void printaction(int);
void printfma(fma *);

typedef enum { STRIPS, Conjunctive, GeneralPDDL } syntacticclass;

syntacticclass actionclass(int);

syntacticclass goalclass();

extern int *initialstate;
extern fma *goal;
extern int goalisdisjunctive;

void simplifyoperators();
void simplifyoperatorsstatic();

extern ordintset *effectoccP; /* operators in which var is a positive effect */
extern ordintset *effectoccN; /* operators in which var is a negative effect */
extern ordintset *forcedeffectoccP; /* operators in which var is a positive effect */
extern ordintset *forcedeffectoccN; /* operators in which var is a negative effect */


extern ordintset *preconoccN; /* operators in which var is negative in precondition */
extern ordintset *preconoccP; /* operators in which var is positive in precondition */

extern ordintset *condocc; /* operators in which var occurs in a condition for effect */

extern ordintset *forcedeffectsP; /* variables the operator always makes true */
extern ordintset *forcedeffectsN; /* variables the operator always makes false */

extern ordintset *preconP; /* variable that must be true for operator */
extern ordintset *preconN; /* variable that must be false for operator */

/* Same as preconP and preconN, but including lits inferred with invariants. */
extern ordintset *necessarypreconP; /* variable that must be true for operator */
extern ordintset *necessarypreconN; /* variable that must be false for operator */

extern ordintset *necessarypreconofP; /* operators in which atom is a nec precon */
extern ordintset *necessarypreconofN; /* operators in which atom is a nec precon */

int canmaketrue(int,int);
int isaffectedby(int,int);
int opaffects(int,int);
int opaffectsinstate(int *,int,int);
int parallel(int,int);
int Lparallel(int,int);

void findoccurrences();

void sortactions();

void collectliterals(ordintset,int);

void eliminatestaticvariables();

extern int *converse;
void mergecontras();

extern int **AeffectoccP; /* operators in which var is a positive effect */
extern int **AeffectoccN; /* operators in which var is a negative effect */
extern int **ApreconP; /* variable that must be true for operator */
extern int **ApreconN; /* variable that must be false for operator */
extern int **AforcedeffectsP; /* variables the operator always makes true */
extern int **AforcedeffectsN; /* variables the operator always makes false */
extern int **AnecessarypreconP; /* variable that must be true for operator */
extern int **AnecessarypreconN; /* variable that must be false for operator */
extern int **ApreconoccN; /* operators in which var is negative in precondition */
extern int **ApreconoccP; /* operators in which var is positive in precondition */
extern int **Acondocc; /* operators in which var occurs in a condition for effect */

void constructoperatorarrays();
