

/* 2012 (C) Jussi Rintanen   */

#define feNEG(a) ((a)^1)
#define fePLIT(a) ((a) << 1)
#define feNLIT(a) (feNEG(fePLIT(a)))
#define feVAR(l) ((l) >> 1)

/* An atomic fact (or schema) P(t1 t2 t3 ... tn) */

typedef struct _intlist { int hd; struct _intlist *tl; } intlist;
typedef struct _ptrlist { int *hd; struct _ptrlist *tl; } ptrlist;
typedef struct _stringlist { char *hd; struct _stringlist *tl; } stringlist;
typedef struct _typedvarlist { int v; int t; struct _typedvarlist *tl; } typedvarlist;

/* An atom is represented as an int vector.
   a[0] is the predicate
   a[1] is the number of parameters n
   a[2..n+2] are the parameters */

typedef int *atom;

/******************* Schematic formulae ******************/

/* Definition */

typedef enum {
  STRUE,SFALSE,
  Spatom, Snatom,
  Sconj, Sdisj,
  Sforall, Sforsome,
  Seq, Sneq } Sfmatype;

typedef struct _Sfma {
  Sfmatype t;
  union {
    atom a;
    typedvarlist *ss; /* parameters for quantification */
    int p1;
    struct _Sfmalist0 { struct _Sfma *hd; struct _Sfmalist0 *tl; } *juncts;
  };
#ifdef CFMA
    int cnt;
#endif
  int p2;
  struct _Sfma *f;
} Sfma;

typedef struct _Sfmalist { Sfma *hd; struct _Sfmalist *tl; } Sfmalist;

/* Constructors formulas */

Sfma *Sfalse();
Sfma *Strue();
Sfma *Sconjunction(Sfmalist *);
Sfma *Sdisjunction(Sfmalist *);
Sfma *Satom(atom);
Sfma *Sneg(Sfma *);
Sfma *SfmaEQ(int,int);
Sfma *Sfmaforall(typedvarlist *,Sfma *);
Sfma *Sfmaforsome(typedvarlist *,Sfma *);

extern Sfma *Sgoal;

/* Accessors */

Sfmatype Sfmatypeof(Sfma *);

/******************** Schematic effects *********************/

typedef enum { SEpatom, SEnatom, SEwhen, SEconj, SEforall, SEoneof } Sefftype;

/* schematic effects */

typedef struct _Seff {
  Sefftype t;
  union {
    atom a;
    Sfma *cond; /* condition for when */
    struct _Sefflist0 { struct _Seff *hd; struct _Sefflist0 *tl; } *juncts; /* list of effects for conj */
    typedvarlist *ss; /* parameter in forall quantification */
  };
  struct _Seff *effect; /* effect for when, forall */
} Seff;

/* Lists */

typedef struct _Sefflist { Seff *hd; struct _Sefflist* tl; } Sefflist;
typedef struct _atomlist { atom hd; struct _atomlist* tl; } atomlist;

Sfmalist *Sfmacons(Sfma *,Sfmalist *);
Sefflist *Seffcons(Seff *,Sefflist *);
intlist *intcons(int,intlist *);
atomlist *atomcons(atom,atomlist *);
ptrlist *ptrcons(int *,ptrlist *);

#define EMPTYLIST NULL

/* Domain */

void storedomain(int);
void checkdomain(int);
char *domainname();

void storeconstants(typedvarlist *);
void storetypes(typedvarlist *);
void storepredicates();

void checkrequirements(intlist *);


/* Problem */

void addproblem(int);
char *problemname();

void storeinit(atomlist *);
void storegoal(Sfma *);
extern atom *Sinit;

/* Type variables */

extern int UNIVTYPE;
typedvarlist *withtype(int,intlist *);
typedvarlist *TVappend(typedvarlist *,typedvarlist *);


/* An operator schema */

typedef struct _Saction {
  int name;
  typedvarlist *params;
  int cost;
  Sfma *precon;
  Seff *effect;
} Saction;

extern int maxSActions;
extern Saction *Sactions;
extern int nOfSActions;
void checkSactionsSize();

atom newatom(int,intlist *);

/* Types, with elements. */

typedef struct _obtype {
  int typename;
  intlist *elements;
  intlist *supertypes;
  intlist *subtypes;
} obtype;

int *getdomain(int);
int getdomainsize(int);
void bindingaslist(int *,int *,int);

void storeobjects(typedvarlist *);

void showatom(atom);

extern int linenumber;
extern char *errorstring;

void readfile();
int lexeropen(char *);
int lexeropenstdin(void);

/* Constructors */

/* schematic effects */
Seff* Seffconjunction(Sefflist *);
Seff* Seffwhen(Sfma*, Seff*);
Seff* Seffforall(typedvarlist *,Seff *);
Seff* SPeffatom(atom);
Seff* SNeffatom(atom);
Seff* Seffoneof(Sefflist *);

/* create new schematic op */
void addnewaction(int);
void addactionparameters(typedvarlist *);
void addactionprecond(Sfma *);
void addactioneffect(Seff *);
void addactioncost(int);

/* Grounding */

void preprocessoperators();
void groundoperators();
void NEWgroundoperators(void);
void simplifysillyconditionals();
