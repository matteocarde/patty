/* مهمترین مسأله استفاده از اشیاء و گراند کردن مسندها و عملگرها
   و تبدیل آنها به گزاره و کنش است
   همان طور که در کاغذ نوشته ام بهتر است گزاره ها به محض ایجاد برای اولین بار، در یک
   لیست ذخیره شوند. همه گزاره های ممکن باید در این لیست قرار بگیرند. حال هر وضعیت را
   می توان با یک بردار بولی به طول برابر با این لیست نشان داد. همچنین شرط ها یا اثرهای
   یک کنش را می توان با لیستی از اعداد که هر یک اندیس یک گزاره در لیست گزاره ها هستند
   نشان داد. در مراحل حل مسأله هم می توان از همین منطق ساده استفاده کرد...0

   Ground Input
   Timed Initial Literals (exogenous events)
   Numeric metrics, Functions (most of domains in recent IPC)
   ? Use split represenation of predicates and/or operators ?
*/
#pragma once

#include <string>
#include <map>
#include <vector>
#include <set>
#include "tsat/val/ptree.h"
using namespace std;
using namespace VAL;

namespace MyParser{

class PObjects;
class PProposition;
class PListProposition;
class PAction;
class PListAction;
class PProblem;
class PTypes;
class PParams;
class PPredicate;
class PListPredicate;
class POperator;
class PListOperator;
class PDomain;

extern PProblem pProblem;
extern PDomain pDomain;

void GroundOperators(const PObjects &_objects, const PListOperator &_operators, PListAction &_actions);
void GroundPredicates(const PListPredicate &_predicates, const PObjects &_objects, PListProposition &_propositions);
string GroundOperatorDuration(const PPredicate &prd, const PParams &params, const vector<int> &objects);
void GroundOperatorPredicate(const PPredicate &prd, PProposition &prp, const PParams &params, const vector<int> &objects);
int ConvertValProposition(const proposition *p, PProposition &prp);
void AddValObject(const const_symbol *obj);
bool AddParserClasses(parse_category *top_thing);
bool AddProblemClasses(parse_category *top_thing);

#pragma region problem-classes

class PObjects
{
public:
	vector<string> objects;
	vector<vector<string> > types;
	map<string, int> tofind;
	bool AddObject(string o, vector<string> &t);
	inline int size() const{return objects.size();}
	//void ClearObjects(void){objects.clear(void); types.clear(void); types2.clear(void); types3.clear(void);};
	bool RemoveLastObject(void);
	int FindObject(string o) const;
	void Print(void) const;
	
	PObjects(void){}
	~PObjects(void){}
};

class PProposition
{
public:
	int id;
	const PPredicate *prd;
	vector<int> objects;
	// reverse connection to the supporting/requiring action
	// added on 1391/2/18 monday
	set<int> addEffectAtStart, delEffectAtStart, addEffectAtEnd, delEffectAtEnd;
	set<int> conditionAtStart, conditionAtEnd, conditionOverAll;

	inline void RemoveLastObject(void){objects.pop_back();}
	string ToString(void) const;
	string ToFullString(void) const;
	PProposition(void){}
	~PProposition(void){}
};

class PListProposition
{
public:
	vector<PProposition> all;
	map<string, int> tofind;
	bool AddProposition(PProposition &p);
	int FindProposition(PProposition &p) const;
	PProposition* GetPropositionById(const int id);
	inline int size() const{return all.size();}
	void Print(void) const;

	PListProposition(void){}
	~PListProposition(void){}
};

class PAction
{
public:
	int id;
	const POperator *op;
	int n_objects;
	float duration;
	vector<int> objects;
	set<int> addEffectAtStart, delEffectAtStart, addEffectAtEnd, delEffectAtEnd;
	set<int> conditionAtStart, conditionAtEnd, conditionOverAll;
	
	string ToString(void) const;
	string ToFullString(void) const;
	bool DoesNeedAtStart(int prop) const;
	bool DoesAddAtStart(int prop) const;
	bool DoesDeleteAtStart(int prop) const;
	bool DoesNeedAtEnd(int prop) const;
	bool DoesAddAtEnd(int prop) const;
	bool DoesDeleteAtEnd(int prop) const;
	bool DoesNeedOverall(int prop) const;
	int GroundAction(void);
	PAction(void){}
	~PAction(void){}
};

class PListAction
{
public:
	vector<PAction> all;
	bool AddAction(PAction a);
	int FindAction(string name, const vector<int> &objects) const;
	const PAction* GetActionById(int id) const;
	inline int size() const{return all.size();}
	void Print(void) const;

	PListAction(void){}
	~PListAction(void){}
};

class PProblem
{
public:
	PObjects pObjects;
	PListProposition pAllProposition;
	PListAction pAllAction;
	vector<int> initialState, goals;
	map<string, float> functionValues;
	float GetFunctionValue(string f) const;

	void Print(void) const;
	void PrintTA(void);
	PProblem(void){}
	~PProblem(void){}
};

#pragma endregion

#pragma region domain-classes

class PTypes
{
public:
	vector<string> types;
	bool AddType(string t); // return true on success
	bool IsValidType(string t) const; // check validity of a type
	inline int size() const{return types.size();}

	PTypes(void){}
	~PTypes(void){}
};

class PParams
{
public:
	vector<string> paramNames;
	vector<string> paramTypes;
	//vector<string> paramTypes2;
	vector<bool> paramIsConst;
	bool either;
	string type2;
	int ntype2;
	bool AddParam(string p, string t, bool isConst = false); // add a parameter "p" with type "t"
	inline int size() const{return paramNames.size();}
	
	PParams(void){}
	~PParams(void){}
};

class PPredicate
{
public:
	string head;
	PParams params;
	bool readonly;

	inline bool operator<(const PPredicate& other) const
	{
		if(head < other.head)
			return true;
		else if(head > other.head)
			return false;
		int j=0;
		for(int i=0; i<params.size() && j<other.params.size(); ++i, ++j)
		{
			if(params.paramNames[i] < other.params.paramNames[j])
				return true;
			else if(params.paramNames[i] > other.params.paramNames[j])
				return false;
		}
		return false;
	}

	PPredicate(void){}
	~PPredicate(void){}
};

class PListPredicate
{
public:
	vector<PPredicate> all;
	map<string, int> tofind;
	bool AddPredicate(PPredicate p);
	const PPredicate* FindPredicate(string head) const;
	inline int size() const{return all.size();}
	void PrintTA(void) const;

	PListPredicate(void){}
	~PListPredicate(void){}
};

class POperator
{
public:
	string name;
	float duration;
	PParams params;
	//PParams params2;
	PPredicate durationFunction;
	PPredicate durationFunction2;
	int type;
	char durOperator;
	float durOperand;
	float durOperand2;
	PListPredicate addEffectAtStart, delEffectAtStart, addEffectAtEnd, delEffectAtEnd;
	PListPredicate conditionAtStart, conditionAtEnd, conditionOverAll;
	
	bool DoesNeedAtStart(string head) const;
	bool DoesAddAtStart(string head) const;
	bool DoesNeedAtEnd(string head) const;
	bool DoesDeleteAtStart(string head) const;
	bool DoesAddAtEnd(string head) const;
	bool DoesDeleteAtEnd(string head) const;
	bool DoesNeedOverall(string head) const;

	POperator(void){}
	~POperator(void){}
};

class PListOperator
{
public:
	vector<POperator> all;
	map<string, int> tofind;
	bool AddOperator(POperator o);
	const POperator* FindOperator(string name) const;
	inline int size() const{return all.size();}
	void PrintTA(void) const;

	PListOperator(void){}
	~PListOperator(void){}
};

class PDomain
{
public:
	string name;
	PListOperator operators; 
	PListPredicate predicates;
	PTypes pTypes;
	void PrintTA(void) const;

	PDomain(void){}
	~PDomain(void){}
};

#pragma endregion

}
