#ifndef ITGRAPHUSAGE_H
#define ITGRAPHUSAGE_H

#include "tsat/graph/ITGraph.h"

void GraphInit(ITGraph &g);
void GraphPrintFactMutex(ITGraph &g);
int GraphExtractFactMutex(ITGraph &g, vector< vector<Mutex> > *&fm, bool includeOveralls);

#endif
