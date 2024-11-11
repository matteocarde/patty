#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <vector>
#if defined(_MSC_VER) || defined(__MINGW32__)
	#include <direct.h>
#else
	#include <unistd.h>
#endif

using namespace std;

struct IntEdge // used in bellman_ford(..., int *d, ...)
{
	int u,v;
	int weight;
};

struct DoubleEdge // used in bellman_ford(..., double *d, ...)
{
	int u,v;
	double weight;
};

double roundToPrecision(double x, int prec);
int ChangeDir(const char *path);
int MakeDir(const char *path);
double CPUTime(void); // returns the CPU time consumed by the process
bool bellman_ford(int start, int n, vector<DoubleEdge> &edges, double *d, vector<int> &negativeCycle);
bool bellman_ford(int start, int n, vector<IntEdge> &edges, int *d, vector<int> &negativeCycle);
string changeExt(string filename, string ext); // replace the extension of filename with ext
bool Conflict(const vector<int> &u, const vector<int> &v); // checks whether there is a common item between u and v
bool Conflict(const set<int> &u, const set<int> &v); // checks whether there is a common item between u and v
int ConflictCount(const set<int> &u, const set<int> &v); // returns the number of common items between u and v
set<int> Intersect(vector<int> u, vector<int> v); // returns intersection of u and v
bool IsInList(const vector<int> &list, int item); // checks whether the item is contained by the list
void PrintVectorInt(const vector<int> &v); // prints an integer vector in form of ( n1, n2, ..., nm )
void PrintVectorInt(const set<int> &v); // prints an integer vector in form of ( n1, n2, ..., nm )

#endif
