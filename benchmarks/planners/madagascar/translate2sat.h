
/* 2012 (C) Jussi Rintanen, jrintanen.jr@gmail.com  */

typedef struct _seq {
  satinstance sati;
  int restart;
  int callsleft;
  int effort;
} seq;

void encoding();

typedef struct _CEstruct {
  int var;
  fma *condition;
  char disjunctive;
  struct _CEstruct *next;
} CEstruct;

typedef struct _compactCEstruct {
  int var;
  fma *condition;
  char disjunctive;
} compactCEstruct;

typedef struct _actvar {
  int *effectlits;
  int *conditionlits;
} actvar;

extern seq seqs[10000];
extern CEstruct **CEs;
extern compactCEstruct **cCEs;
extern int maxactvars;
extern actvar *actvars;

int actaffects(int,int);
