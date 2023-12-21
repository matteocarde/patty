#ifndef ETGRAPHUSAGE_H
#define ETGRAPHUSAGE_H

#include "tsat/graph/ETGraph.h"

void GraphInit(ETGraph &g);
void GraphPrintFactMutex(ETGraph &g);
int GraphExtractFactMutex(ETGraph &g, vector< vector<Mutex> > *&fm, bool includeOveralls);

#endif
