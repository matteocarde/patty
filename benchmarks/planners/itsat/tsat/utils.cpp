#include <iostream>
#include <string>
#include <vector>
#include <set> // used in ConflictCount()
#include <iterator> // used in ConflictCount()
#include <algorithm> // used in ConflictCount()
#include <climits> // for INT_MAX
#include <cmath> // for fabs(double), ceil(), pow()
#if defined(_MSC_VER) || defined(__MINGW32__)
	#include <direct.h>
#else
	#include <unistd.h>
	#include <sys/stat.h>
#endif
#include "utils.h"

using namespace std;

double roundToPrecision(double x, int prec) {
    return 
        ceil( x * pow(10,(double)prec) - .4999999999999)
        / pow(10,(double)prec);
}

int ChangeDir(const char *path)
{
	#if defined(_MSC_VER) || defined(__MINGW32__)
		return _chdir(path);
	#else
		return chdir(path);
	#endif
}

int MakeDir(const char *path)
{
	#if defined(_MSC_VER) || defined(__MINGW32__)
		return _mkdir(path);
	#else
		return mkdir(path, 0777);
	#endif
}

// the double version
bool bellman_ford(int start, int n, vector<DoubleEdge> &edges, double *d, vector<int> &negativeCycle)
{
	bool negCycle = false;
	int e = edges.size();
	int *parent = new int[n];
	for(int i=0; i<n; i++)
	{
		d[i] = INT_MAX;
		parent[i] = -1;
	}
	d[start] = 0;
	for(int i=0; i<=n-1; i++)
	{
		bool change = false;
		for(int j=0; j<e; j++)
		{
			double newWeight = d[edges[j].u] + edges[j].weight;
			if((newWeight < d[edges[j].v]) && (fabs(newWeight - d[edges[j].v]) > 0.00001)) // 0.00001 must be < epsilon
			{
				//cout << d[edges[j].v] << "  ,  " << newWeight << endl;
				//getchar();
				d[edges[j].v] = newWeight;
				parent[edges[j].v] = edges[j].u;
				change = true;
			}
		}
		if(!change)
			break;
		if(i==n-1 && change)
		{
			negCycle = true;
			break;
		}
	}
	// for debugging purposes:
	//cout << "Parents: " << endl;
	//for(int i=0; i<n; i++)
	//	cout << parent[i]+1 << "->" << i+1 << endl;
	
	// just for record: no usage of d here:
	
	if(negCycle)
	{
		vector<int> *children = new vector<int>[n];
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<n; j++)
			{
				if(parent[j] == i)
					children[i].push_back(j);
			}
		}
		int node;
		vector<int> stk, path;
		int *color = new int[n];
		for(int i=0; i<n; i++)
			color[i] = 0; // white
		path.push_back(start);
		stk.push_back(start++);
		bool negcyclefound = false;
		while(!negcyclefound)
		{
			if(stk.empty())
			{
				path.pop_back(); // or path.clear();
				path.push_back(start);
				stk.push_back(start++);
			}
			node = stk.back();
			stk.pop_back();
			if(color[node] == 0) // white
			{
				color[node] = 1; // gray
				stk.push_back(node);
				path.push_back(node);
				vector<int> &childrennode = children[node];
				int sz = childrennode.size();
				for(int i=0; i<sz; i++)
				{
					int child = childrennode[i];
					if(color[child] == 0) // white is new
						stk.push_back(child);
					else if(color[child] == 1) // negative cycle found
					{
						int from = -1;
						for(int i=0; i<path.size(); i++)
						{
							if(path[i] == child)
							{
								from = i+1;
								break;
							}
						}
						if(from == -1)
							negativeCycle = path;
						else
						{
							negativeCycle.clear();
							for(int i=from; i<path.size(); i++)
							{
								negativeCycle.push_back(path[i]);
							}
						}
						negcyclefound = true;
						break;
					}
					//else BLACK just ignore it
				}
			}
			else if(color[node] == 1) // gray
			{
				color[node] = 2; // black
				path.pop_back();
			}
		}
		delete[] children;
		delete[] color;
	}
	delete[] parent;
	return !negCycle;
}

// original integer version
bool bellman_ford(int start, int n, vector<IntEdge> &edges, int *d, vector<int> &negativeCycle)
{
	bool negCycle = false;
	int e = edges.size();
	int *parent = new int[n];
	for(int i=0; i<n; i++)
	{
		d[i] = INT_MAX - 1;
		parent[i] = -1;
	}
	d[start] = 0;
	for(int i=0; i<=n-1; i++)
	{
		bool change = false;
		for(int j=0; j<e; j++)
		{
			int newWeight = d[edges[j].u] + edges[j].weight;
			if(newWeight < d[edges[j].v])
			{
				d[edges[j].v] = newWeight;
				parent[edges[j].v] = edges[j].u;
				change = true;
			}
		}
		if(!change)
			break;
		if(i==n-1 && change)
		{
			negCycle = true;
			break;
		}
	}
	// for debugging purposes:
	//cout << "Parents: " << endl;
	//for(int i=0; i<n; i++)
	//	cout << parent[i]+1 << "->" << i+1 << endl;
	
	// just for record: no usage of d here:
	
	if(negCycle)
	{
		vector<int> *children = new vector<int>[n];
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<n; j++)
			{
				if(parent[j] == i)
					children[i].push_back(j);
			}
		}
		int node;
		vector<int> stk, path;
		int *color = new int[n];
		for(int i=0; i<n; i++)
			color[i] = 0; // white
		path.push_back(start);
		stk.push_back(start++);
		bool negcyclefound = false;
		while(!negcyclefound)
		{
			if(stk.empty())
			{
				path.pop_back(); // or path.clear();
				path.push_back(start);
				stk.push_back(start++);
			}
			node = stk.back();
			stk.pop_back();
			if(color[node] == 0) // white
			{
				color[node] = 1; // gray
				stk.push_back(node);
				path.push_back(node);
				vector<int> &childrennode = children[node];
				int sz = childrennode.size();
				for(int i=0; i<sz; i++)
				{
					int child = childrennode[i];
					if(color[child] == 0) // white is new
						stk.push_back(child);
					else if(color[child] == 1) // negative cycle found
					{
						int from = -1;
						for(int i=0; i<path.size(); i++)
						{
							if(path[i] == child)
							{
								from = i+1;
								break;
							}
						}
						if(from == -1)
							negativeCycle = path;
						else
						{
							negativeCycle.clear();
							for(int i=from; i<path.size(); i++)
							{
								negativeCycle.push_back(path[i]);
							}
						}
						negcyclefound = true;
						break;
					}
					//else BLACK just ignore it
				}
			}
			else if(color[node] == 1) // gray
			{
				color[node] = 2; // black
				path.pop_back();
			}
		}
		delete[] children;
		delete[] color;
	}
	delete[] parent;
	return !negCycle;
}

string changeExt(string filename, string ext)
{
	string::size_type idx;
	idx = filename.find_last_of('\\');
	if(idx != string::npos)
		filename = filename.substr(idx+1);
	idx = filename.find_last_of('.');
	if(idx == string::npos)
		return filename.append(ext);
	else
		return filename.substr(0, idx).append(ext);
}

bool Conflict(const vector<int> &u, const vector<int> &v)
{
	int uSize = u.size();
	int vSize = v.size();
	if(uSize==0 || vSize==0)
		return false;
	for(int i=0; i<uSize; i++)
	{
		for(int j=0; j<vSize; j++)
		{
			if(u[i]==v[j])
				return true;
		}
	}
	return false;
}

bool Conflict(const set<int> &u, const set<int> &v)
{
	set<int> result;
	std::set_intersection(u.begin(), u.end(), v.begin(), v.end(), std::insert_iterator<set<int> >(result, result.end()));
	return !result.empty();
}

int ConflictCount(const set<int> &u, const set<int> &v)
{
	int count = 0;
	set<int>::const_iterator itU, itV, uLast, vLast;
	uLast = u.end();
	vLast = v.end();
	for (itU = u.begin(), itV = v.begin(); itU != uLast && itV != vLast; )
		if (*itU < *itV)
			++itU;
		else if (*itV < *itU)
			++itV;
		else
			{	// equivalent
			++count;
			++itU;
			++itV;
			}
	return count;
}

set<int> Intersect(vector<int> u, vector<int> v)
{
	set<int> result;
	sort(u.begin(), u.end());
	sort(v.begin(), v.end());
	std::set_intersection(u.begin(), u.end(), v.begin(), v.end(), std::insert_iterator<set<int> >(result, result.end()));
	return result;
}

bool IsInList(const vector<int> &list, int item)
{
	int size = list.size();
	for(int i=0; i<size; i++)
	{
		if(list[i]==item)
			return true;
	}
	return false;
}

void PrintVectorInt(const vector<int> &v)
{
	int sV = v.size();
	if(sV == 0)
		return;
	cout << "( " << v[0];
	for( int i=1; i<sV; i++ )
		cout << ", " << v[i];
	cout << " )";
}

void PrintVectorInt(const set<int> &v)
{
	int sV = v.size();
	if(sV == 0)
		return;
	for(set<int>::const_iterator it = v.begin(); it != v.end(); ++it)
	{
		if(it == v.begin())
			cout << "( " << *it;
		else
			cout << ", " << *it;
	}
	cout << " )";
}

#if defined(_MSC_VER) || defined(__MINGW32__)

#include <Windows.h>
double CPUTime(void) {
  double res;
  //struct rusage usage;
  //getrusage(RUSAGE_SELF, &usage);
  //res = usage.ru_utime.tv_usec + usage.ru_stime.tv_usec;
  //res *= 1e-6;
  //res += usage.ru_utime.tv_sec + usage.ru_stime.tv_sec;
  FILETIME ftCreation,
         ftExit,
         ftKernel,
         ftUser;
  GetProcessTimes(GetCurrentProcess(), &ftCreation, &ftExit, &ftKernel, &ftUser);
  //__int64 i64Kernel = *((__int64 *) &ftKernel);
  __int64 i64User = *((__int64 *) &ftUser);
  res = (/*i64Kernel +*/ i64User) * 1e-7;
  return res;
}

#else
#include <sys/time.h>
#include <sys/resource.h>
#include <unistd.h>

double CPUTime(void) {
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    return (double)ru.ru_utime.tv_sec + (double)ru.ru_utime.tv_usec / 1000000; }

#endif
