grammar pddl;



/************* LEXER ****************************/

LP : '(';
RP : ')';

VAR: '?' NAME;
NAME:    LETTER ANY_CHAR* ;
fragment LETTER : 'a'..'z' | 'A'..'Z';
fragment ANY_CHAR : LETTER | '0'..'9' | '-' | '_';
VARIABLE : '?' NAME ;
fragment DIGIT: '0'..'9';
NUMBER : (('-')? DIGIT+ ('.' DIGIT+)?) | '#t' ;
WS : [ \t\r\n]+ -> skip ;

/************* Start of src *******************/

pddlDoc : domain | problem;

/************* DOMAINS ****************************/

domain : LP 'define' domainName requirements? types? predicates? functions? (action | event | process)* RP;

//DOMAIN NAME
domainName: LP 'domain' NAME RP;

//REQUIREMENTS
requireKey: ':' NAME;
requirements: LP ':requirements' requireKey* RP;

//TYPES
parentType: '-' typeName;
typeName: NAME;
type: typeName+ parent=parentType*;
types: LP ':types' type+ RP;

//ATOM AND LITERALS
atomName: NAME;
groundAtomParameter: NAME;
liftedAtomParameter: VAR;
typedAtomParameter: liftedAtomParameter+ '-' atomsType=typeName;
atomParameter: liftedAtomParameter | groundAtomParameter ;

atom: atomName atomParameter*;
typedAtom: atomName typedAtomParameter*;

//positiveLiteral: (name a b c d)
//negativeLiteral: (not (name a b c d))
positiveLiteral: LP atom RP | param=liftedAtomParameter;
typedPositiveLiteral: LP typedAtom RP;
negativeLiteral: LP 'not' positiveLiteral RP;
booleanLiteral: positiveLiteral | negativeLiteral;

//PREDICATES
predicates: LP ':predicates' typedPositiveLiteral+ RP;

//FUNCTIONS
functions: LP ':functions' typedPositiveLiteral+ RP;


modificator: 'assign'|'increase'|'decrease';
operator: '+'|'-'|'*'|'/';
comparator: '>'|'>='|'<='|'<'|'=';
number: NUMBER;
delta: '#t';
constant: number | delta;

assignmentSide: number;
operationSide: operation | positiveLiteral | constant;
operation: LP operator operationSide operationSide RP;

assignment: LP '=' positiveLiteral assignmentSide RP;
comparation: LP comparator operationSide operationSide RP;
negatedComparation: LP 'not' comparation RP;
modification: LP modificator positiveLiteral operationSide RP;

effect:  booleanLiteral | modification;

andClause: LP 'and' (andClause | orClause | booleanLiteral | negatedComparation  | comparation)+ RP;
orClause: LP 'or' (andClause | orClause | booleanLiteral | negatedComparation  | comparation)+ RP;
andEffect : LP 'and' effect+ RP;
emptyPrecondition: LP RP;
preconditions: andClause | orClause | booleanLiteral | negatedComparation | comparation | emptyPrecondition;
effects: effect | andEffect;

parameters: LP typedAtomParameter* RP;

opName: NAME;
opParameters: ':parameters' parameters;
opPrecondition: ':precondition' preconditions;
opEffect: ':effect' effects;

//ACTION
action:  LP ':action' opName
	        opParameters?
            opPrecondition?
            opEffect
		    RP;
//EVENT
event:  LP ':event' opName
	        opParameters?
            opPrecondition?
            opEffect
		    RP;

//PROCESS
process:  LP ':process' opName
	        opParameters?
            opPrecondition?
            opEffect
		    RP;

/************* PROBLEM ****************************/

problem : LP 'define' problemName problemDomain objects? init goal metric? RP;

//Problem Name
problemName: LP 'problem' NAME RP;

//Problem Domain
problemDomain: LP ':domain' NAME RP;

//Objects
typedObjects: groundAtomParameter+ '-' typeName;
objects: LP ':objects' typedObjects* RP;

//Init
init: LP ':init' (positiveLiteral|assignment)+ RP;

//Goal
goal : LP ':goal' preconditions RP;

//Metric
metric : LP ':metric' sign=('maximize'|'minimize') op=operationSide RP;