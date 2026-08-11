
/*  2010 (C) Jussi Rintanen  */

/* Symboltable for IDs and VARs in lexer */

#include <stdio.h>

typedef struct _stbucket {
  int index;
  char staticpredicate;
  char *s;
  struct _stbucket *next;
} stentry;

#define MAXBUCKETS 0x20000

extern stentry symboltable[MAXBUCKETS];

extern stentry **index2stentry;

void initsymboltable();
int symbolindex(char *);
char *symbol(int);

int isvar(int);
int staticp(int);
void setnonstatic(int);

/* Symboltable for p(o1,...,on) atoms. */

extern int nOfAtoms;

void initatomtable();

int atomindex(atom,int *);

int bvalue(int,int *);

int printatomi(int i);	/* Print an atom and return its length in chars. */
int fprintatomi(FILE *,int i);	/* Print an atom and return its length in chars. */

void renameatomtable(int,int *); /* Rename atoms by using a mapping. */
