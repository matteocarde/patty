// Generated from /Users/carde/Documents/Workspace/patty/grammar/pddl.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class pddlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, LP=51, RP=52, VAR=53, 
		NAME=54, VARIABLE=55, NUMBER=56, WS=57;
	public static final int
		RULE_pddlDoc = 0, RULE_domain = 1, RULE_domainName = 2, RULE_requireKey = 3, 
		RULE_requirements = 4, RULE_parentType = 5, RULE_typeName = 6, RULE_type = 7, 
		RULE_types = 8, RULE_constantType = 9, RULE_constantName = 10, RULE_pddlConstant = 11, 
		RULE_constants = 12, RULE_atomName = 13, RULE_groundAtomParameter = 14, 
		RULE_liftedAtomParameter = 15, RULE_typedAtomParameter = 16, RULE_atomParameter = 17, 
		RULE_atom = 18, RULE_typedAtom = 19, RULE_positiveLiteral = 20, RULE_typedPositiveLiteral = 21, 
		RULE_negativeLiteral = 22, RULE_booleanLiteral = 23, RULE_predicates = 24, 
		RULE_functions = 25, RULE_modificator = 26, RULE_operator = 27, RULE_comparator = 28, 
		RULE_number = 29, RULE_delta = 30, RULE_constant = 31, RULE_assignmentSide = 32, 
		RULE_operationSide = 33, RULE_operation = 34, RULE_assignment = 35, RULE_durationAssignment = 36, 
		RULE_comparation = 37, RULE_negatedComparation = 38, RULE_modification = 39, 
		RULE_ceCond = 40, RULE_ceEff = 41, RULE_ce = 42, RULE_forallEffect = 43, 
		RULE_forall = 44, RULE_exists = 45, RULE_effect = 46, RULE_effectNoCes = 47, 
		RULE_inequality = 48, RULE_andClause = 49, RULE_orClause = 50, RULE_andEffect = 51, 
		RULE_andEffectNoCes = 52, RULE_emptyPrecondition = 53, RULE_preconditions = 54, 
		RULE_effects = 55, RULE_andDurClause = 56, RULE_atStartPre = 57, RULE_overAllPre = 58, 
		RULE_atEndPre = 59, RULE_durativeConditions = 60, RULE_atStartEffect = 61, 
		RULE_overAllEffect = 62, RULE_atEndEffect = 63, RULE_durativeEffect = 64, 
		RULE_andDurativeEffect = 65, RULE_durativeEffects = 66, RULE_parameters = 67, 
		RULE_opName = 68, RULE_opParameters = 69, RULE_opPrecondition = 70, RULE_opDurativeCondition = 71, 
		RULE_opEffect = 72, RULE_opDurativeEffect = 73, RULE_opDuration = 74, 
		RULE_action = 75, RULE_durativeAction = 76, RULE_event = 77, RULE_process = 78, 
		RULE_constraints = 79, RULE_problem = 80, RULE_problemName = 81, RULE_problemDomain = 82, 
		RULE_typedObjects = 83, RULE_objects = 84, RULE_init = 85, RULE_goal = 86, 
		RULE_metric = 87;
	private static String[] makeRuleNames() {
		return new String[] {
			"pddlDoc", "domain", "domainName", "requireKey", "requirements", "parentType", 
			"typeName", "type", "types", "constantType", "constantName", "pddlConstant", 
			"constants", "atomName", "groundAtomParameter", "liftedAtomParameter", 
			"typedAtomParameter", "atomParameter", "atom", "typedAtom", "positiveLiteral", 
			"typedPositiveLiteral", "negativeLiteral", "booleanLiteral", "predicates", 
			"functions", "modificator", "operator", "comparator", "number", "delta", 
			"constant", "assignmentSide", "operationSide", "operation", "assignment", 
			"durationAssignment", "comparation", "negatedComparation", "modification", 
			"ceCond", "ceEff", "ce", "forallEffect", "forall", "exists", "effect", 
			"effectNoCes", "inequality", "andClause", "orClause", "andEffect", "andEffectNoCes", 
			"emptyPrecondition", "preconditions", "effects", "andDurClause", "atStartPre", 
			"overAllPre", "atEndPre", "durativeConditions", "atStartEffect", "overAllEffect", 
			"atEndEffect", "durativeEffect", "andDurativeEffect", "durativeEffects", 
			"parameters", "opName", "opParameters", "opPrecondition", "opDurativeCondition", 
			"opEffect", "opDurativeEffect", "opDuration", "action", "durativeAction", 
			"event", "process", "constraints", "problem", "problemName", "problemDomain", 
			"typedObjects", "objects", "init", "goal", "metric"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'define'", "'domain'", "':'", "':requirements'", "'-'", "':types'", 
			"':constants'", "'not'", "':predicates'", "':functions'", "'assign'", 
			"'increase'", "'decrease'", "'+'", "'*'", "'/'", "'>'", "'>='", "'<='", 
			"'<'", "'='", "'#t'", "'?duration'", "'when'", "'forall'", "'exists'", 
			"'and'", "'or'", "'at start'", "'over all'", "'at end'", "'overall'", 
			"':parameters'", "':precondition'", "':condition'", "':effect'", "':duration'", 
			"':action'", "':durative-action'", "':event'", "':process'", "':constraints'", 
			"'problem'", "':domain'", "':objects'", "':init'", "':goal'", "':metric'", 
			"'maximize'", "'minimize'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "LP", "RP", "VAR", "NAME", "VARIABLE", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "pddl.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pddlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PddlDocContext extends ParserRuleContext {
		public DomainContext domain() {
			return getRuleContext(DomainContext.class,0);
		}
		public ProblemContext problem() {
			return getRuleContext(ProblemContext.class,0);
		}
		public PddlDocContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pddlDoc; }
	}

	public final PddlDocContext pddlDoc() throws RecognitionException {
		PddlDocContext _localctx = new PddlDocContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_pddlDoc);
		try {
			setState(178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				domain();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(177);
				problem();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DomainContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public DomainNameContext domainName() {
			return getRuleContext(DomainNameContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public RequirementsContext requirements() {
			return getRuleContext(RequirementsContext.class,0);
		}
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public ConstantsContext constants() {
			return getRuleContext(ConstantsContext.class,0);
		}
		public PredicatesContext predicates() {
			return getRuleContext(PredicatesContext.class,0);
		}
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<DurativeActionContext> durativeAction() {
			return getRuleContexts(DurativeActionContext.class);
		}
		public DurativeActionContext durativeAction(int i) {
			return getRuleContext(DurativeActionContext.class,i);
		}
		public List<EventContext> event() {
			return getRuleContexts(EventContext.class);
		}
		public EventContext event(int i) {
			return getRuleContext(EventContext.class,i);
		}
		public List<ProcessContext> process() {
			return getRuleContexts(ProcessContext.class);
		}
		public ProcessContext process(int i) {
			return getRuleContext(ProcessContext.class,i);
		}
		public ConstraintsContext constraints() {
			return getRuleContext(ConstraintsContext.class,0);
		}
		public DomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_domain; }
	}

	public final DomainContext domain() throws RecognitionException {
		DomainContext _localctx = new DomainContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_domain);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			match(LP);
			setState(181);
			match(T__0);
			setState(182);
			domainName();
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(183);
				requirements();
				}
				break;
			}
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(186);
				types();
				}
				break;
			}
			setState(190);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(189);
				constants();
				}
				break;
			}
			setState(193);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(192);
				predicates();
				}
				break;
			}
			setState(196);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(195);
				functions();
				}
				break;
			}
			setState(204);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(202);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						setState(198);
						action();
						}
						break;
					case 2:
						{
						setState(199);
						durativeAction();
						}
						break;
					case 3:
						{
						setState(200);
						event();
						}
						break;
					case 4:
						{
						setState(201);
						process();
						}
						break;
					}
					} 
				}
				setState(206);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LP) {
				{
				setState(207);
				constraints();
				}
			}

			setState(210);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DomainNameContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public DomainNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_domainName; }
	}

	public final DomainNameContext domainName() throws RecognitionException {
		DomainNameContext _localctx = new DomainNameContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_domainName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(LP);
			setState(213);
			match(T__1);
			setState(214);
			match(NAME);
			setState(215);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequireKeyContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public RequireKeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requireKey; }
	}

	public final RequireKeyContext requireKey() throws RecognitionException {
		RequireKeyContext _localctx = new RequireKeyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_requireKey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(T__2);
			setState(218);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RequirementsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<RequireKeyContext> requireKey() {
			return getRuleContexts(RequireKeyContext.class);
		}
		public RequireKeyContext requireKey(int i) {
			return getRuleContext(RequireKeyContext.class,i);
		}
		public RequirementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_requirements; }
	}

	public final RequirementsContext requirements() throws RecognitionException {
		RequirementsContext _localctx = new RequirementsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_requirements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(LP);
			setState(221);
			match(T__3);
			setState(225);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(222);
				requireKey();
				}
				}
				setState(227);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(228);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParentTypeContext extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public ParentTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parentType; }
	}

	public final ParentTypeContext parentType() throws RecognitionException {
		ParentTypeContext _localctx = new ParentTypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_parentType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			match(T__4);
			setState(231);
			typeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeNameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public TypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeName; }
	}

	public final TypeNameContext typeName() throws RecognitionException {
		TypeNameContext _localctx = new TypeNameContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_typeName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public ParentTypeContext parent;
		public List<TypeNameContext> typeName() {
			return getRuleContexts(TypeNameContext.class);
		}
		public TypeNameContext typeName(int i) {
			return getRuleContext(TypeNameContext.class,i);
		}
		public List<ParentTypeContext> parentType() {
			return getRuleContexts(ParentTypeContext.class);
		}
		public ParentTypeContext parentType(int i) {
			return getRuleContext(ParentTypeContext.class,i);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_type);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(236); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(235);
					typeName();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(238); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(240);
				((TypeContext)_localctx).parent = parentType();
				}
				}
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypesContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public TypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_types; }
	}

	public final TypesContext types() throws RecognitionException {
		TypesContext _localctx = new TypesContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_types);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(LP);
			setState(247);
			match(T__5);
			setState(249); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(248);
				type();
				}
				}
				setState(251); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(253);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantTypeContext extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public ConstantTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantType; }
	}

	public final ConstantTypeContext constantType() throws RecognitionException {
		ConstantTypeContext _localctx = new ConstantTypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constantType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
			match(T__4);
			setState(256);
			typeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantNameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public ConstantNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantName; }
	}

	public final ConstantNameContext constantName() throws RecognitionException {
		ConstantNameContext _localctx = new ConstantNameContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_constantName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PddlConstantContext extends ParserRuleContext {
		public ConstantTypeContext parent;
		public List<ConstantNameContext> constantName() {
			return getRuleContexts(ConstantNameContext.class);
		}
		public ConstantNameContext constantName(int i) {
			return getRuleContext(ConstantNameContext.class,i);
		}
		public List<ConstantTypeContext> constantType() {
			return getRuleContexts(ConstantTypeContext.class);
		}
		public ConstantTypeContext constantType(int i) {
			return getRuleContext(ConstantTypeContext.class,i);
		}
		public PddlConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pddlConstant; }
	}

	public final PddlConstantContext pddlConstant() throws RecognitionException {
		PddlConstantContext _localctx = new PddlConstantContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_pddlConstant);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(261); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(260);
					constantName();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(263); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(265);
				((PddlConstantContext)_localctx).parent = constantType();
				}
				}
				setState(270);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<PddlConstantContext> pddlConstant() {
			return getRuleContexts(PddlConstantContext.class);
		}
		public PddlConstantContext pddlConstant(int i) {
			return getRuleContext(PddlConstantContext.class,i);
		}
		public ConstantsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constants; }
	}

	public final ConstantsContext constants() throws RecognitionException {
		ConstantsContext _localctx = new ConstantsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_constants);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(LP);
			setState(272);
			match(T__6);
			setState(274); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(273);
				pddlConstant();
				}
				}
				setState(276); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(278);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomNameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public AtomNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomName; }
	}

	public final AtomNameContext atomName() throws RecognitionException {
		AtomNameContext _localctx = new AtomNameContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_atomName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GroundAtomParameterContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public GroundAtomParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groundAtomParameter; }
	}

	public final GroundAtomParameterContext groundAtomParameter() throws RecognitionException {
		GroundAtomParameterContext _localctx = new GroundAtomParameterContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_groundAtomParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiftedAtomParameterContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(pddlParser.VAR, 0); }
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public LiftedAtomParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_liftedAtomParameter; }
	}

	public final LiftedAtomParameterContext liftedAtomParameter() throws RecognitionException {
		LiftedAtomParameterContext _localctx = new LiftedAtomParameterContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_liftedAtomParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			_la = _input.LA(1);
			if ( !(_la==VAR || _la==NAME) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedAtomParameterContext extends ParserRuleContext {
		public TypeNameContext atomsType;
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public List<LiftedAtomParameterContext> liftedAtomParameter() {
			return getRuleContexts(LiftedAtomParameterContext.class);
		}
		public LiftedAtomParameterContext liftedAtomParameter(int i) {
			return getRuleContext(LiftedAtomParameterContext.class,i);
		}
		public TypedAtomParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedAtomParameter; }
	}

	public final TypedAtomParameterContext typedAtomParameter() throws RecognitionException {
		TypedAtomParameterContext _localctx = new TypedAtomParameterContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_typedAtomParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(286);
				liftedAtomParameter();
				}
				}
				setState(289); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VAR || _la==NAME );
			setState(291);
			match(T__4);
			setState(292);
			((TypedAtomParameterContext)_localctx).atomsType = typeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomParameterContext extends ParserRuleContext {
		public LiftedAtomParameterContext liftedAtomParameter() {
			return getRuleContext(LiftedAtomParameterContext.class,0);
		}
		public GroundAtomParameterContext groundAtomParameter() {
			return getRuleContext(GroundAtomParameterContext.class,0);
		}
		public AtomParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomParameter; }
	}

	public final AtomParameterContext atomParameter() throws RecognitionException {
		AtomParameterContext _localctx = new AtomParameterContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_atomParameter);
		try {
			setState(296);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(294);
				liftedAtomParameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				groundAtomParameter();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public AtomNameContext atomName() {
			return getRuleContext(AtomNameContext.class,0);
		}
		public List<AtomParameterContext> atomParameter() {
			return getRuleContexts(AtomParameterContext.class);
		}
		public AtomParameterContext atomParameter(int i) {
			return getRuleContext(AtomParameterContext.class,i);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_atom);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			atomName();
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==NAME) {
				{
				{
				setState(299);
				atomParameter();
				}
				}
				setState(304);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedAtomContext extends ParserRuleContext {
		public AtomNameContext atomName() {
			return getRuleContext(AtomNameContext.class,0);
		}
		public List<TypedAtomParameterContext> typedAtomParameter() {
			return getRuleContexts(TypedAtomParameterContext.class);
		}
		public TypedAtomParameterContext typedAtomParameter(int i) {
			return getRuleContext(TypedAtomParameterContext.class,i);
		}
		public TypedAtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedAtom; }
	}

	public final TypedAtomContext typedAtom() throws RecognitionException {
		TypedAtomContext _localctx = new TypedAtomContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_typedAtom);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			atomName();
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==NAME) {
				{
				{
				setState(306);
				typedAtomParameter();
				}
				}
				setState(311);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositiveLiteralContext extends ParserRuleContext {
		public LiftedAtomParameterContext param;
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public LiftedAtomParameterContext liftedAtomParameter() {
			return getRuleContext(LiftedAtomParameterContext.class,0);
		}
		public PositiveLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_positiveLiteral; }
	}

	public final PositiveLiteralContext positiveLiteral() throws RecognitionException {
		PositiveLiteralContext _localctx = new PositiveLiteralContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_positiveLiteral);
		try {
			setState(317);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(312);
				match(LP);
				setState(313);
				atom();
				setState(314);
				match(RP);
				}
				break;
			case VAR:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(316);
				((PositiveLiteralContext)_localctx).param = liftedAtomParameter();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedPositiveLiteralContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TypedAtomContext typedAtom() {
			return getRuleContext(TypedAtomContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public TypedPositiveLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedPositiveLiteral; }
	}

	public final TypedPositiveLiteralContext typedPositiveLiteral() throws RecognitionException {
		TypedPositiveLiteralContext _localctx = new TypedPositiveLiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_typedPositiveLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(LP);
			setState(320);
			typedAtom();
			setState(321);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NegativeLiteralContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public PositiveLiteralContext positiveLiteral() {
			return getRuleContext(PositiveLiteralContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public NegativeLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negativeLiteral; }
	}

	public final NegativeLiteralContext negativeLiteral() throws RecognitionException {
		NegativeLiteralContext _localctx = new NegativeLiteralContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_negativeLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(323);
			match(LP);
			setState(324);
			match(T__7);
			setState(325);
			positiveLiteral();
			setState(326);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanLiteralContext extends ParserRuleContext {
		public PositiveLiteralContext positiveLiteral() {
			return getRuleContext(PositiveLiteralContext.class,0);
		}
		public NegativeLiteralContext negativeLiteral() {
			return getRuleContext(NegativeLiteralContext.class,0);
		}
		public BooleanLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanLiteral; }
	}

	public final BooleanLiteralContext booleanLiteral() throws RecognitionException {
		BooleanLiteralContext _localctx = new BooleanLiteralContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_booleanLiteral);
		try {
			setState(330);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(328);
				positiveLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(329);
				negativeLiteral();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PredicatesContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<TypedPositiveLiteralContext> typedPositiveLiteral() {
			return getRuleContexts(TypedPositiveLiteralContext.class);
		}
		public TypedPositiveLiteralContext typedPositiveLiteral(int i) {
			return getRuleContext(TypedPositiveLiteralContext.class,i);
		}
		public PredicatesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicates; }
	}

	public final PredicatesContext predicates() throws RecognitionException {
		PredicatesContext _localctx = new PredicatesContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_predicates);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(332);
			match(LP);
			setState(333);
			match(T__8);
			setState(335); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(334);
				typedPositiveLiteral();
				}
				}
				setState(337); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(339);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<TypedPositiveLiteralContext> typedPositiveLiteral() {
			return getRuleContexts(TypedPositiveLiteralContext.class);
		}
		public TypedPositiveLiteralContext typedPositiveLiteral(int i) {
			return getRuleContext(TypedPositiveLiteralContext.class,i);
		}
		public FunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functions; }
	}

	public final FunctionsContext functions() throws RecognitionException {
		FunctionsContext _localctx = new FunctionsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(LP);
			setState(342);
			match(T__9);
			setState(344); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(343);
				typedPositiveLiteral();
				}
				}
				setState(346); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(348);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModificatorContext extends ParserRuleContext {
		public ModificatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modificator; }
	}

	public final ModificatorContext modificator() throws RecognitionException {
		ModificatorContext _localctx = new ModificatorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_modificator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14336L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 114720L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparatorContext extends ParserRuleContext {
		public ComparatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparator; }
	}

	public final ComparatorContext comparator() throws RecognitionException {
		ComparatorContext _localctx = new ComparatorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_comparator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4063232L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(pddlParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(356);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeltaContext extends ParserRuleContext {
		public DeltaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delta; }
	}

	public final DeltaContext delta() throws RecognitionException {
		DeltaContext _localctx = new DeltaContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_delta);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			match(T__21);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public DeltaContext delta() {
			return getRuleContext(DeltaContext.class,0);
		}
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_constant);
		try {
			setState(362);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(360);
				number();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				setState(361);
				delta();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentSideContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public AssignmentSideContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentSide; }
	}

	public final AssignmentSideContext assignmentSide() throws RecognitionException {
		AssignmentSideContext _localctx = new AssignmentSideContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_assignmentSide);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			number();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationSideContext extends ParserRuleContext {
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public PositiveLiteralContext positiveLiteral() {
			return getRuleContext(PositiveLiteralContext.class,0);
		}
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public OperationSideContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operationSide; }
	}

	public final OperationSideContext operationSide() throws RecognitionException {
		OperationSideContext _localctx = new OperationSideContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_operationSide);
		try {
			setState(369);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(366);
				operation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(367);
				positiveLiteral();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(368);
				constant();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public List<OperationSideContext> operationSide() {
			return getRuleContexts(OperationSideContext.class);
		}
		public OperationSideContext operationSide(int i) {
			return getRuleContext(OperationSideContext.class,i);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_operation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(371);
			match(LP);
			setState(372);
			operator();
			setState(373);
			operationSide();
			setState(374);
			operationSide();
			setState(375);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public PositiveLiteralContext positiveLiteral() {
			return getRuleContext(PositiveLiteralContext.class,0);
		}
		public AssignmentSideContext assignmentSide() {
			return getRuleContext(AssignmentSideContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(377);
			match(LP);
			setState(378);
			match(T__20);
			setState(379);
			positiveLiteral();
			setState(380);
			assignmentSide();
			setState(381);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurationAssignmentContext extends ParserRuleContext {
		public OperationSideContext op;
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OperationSideContext operationSide() {
			return getRuleContext(OperationSideContext.class,0);
		}
		public DurationAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_durationAssignment; }
	}

	public final DurationAssignmentContext durationAssignment() throws RecognitionException {
		DurationAssignmentContext _localctx = new DurationAssignmentContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_durationAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(383);
			match(LP);
			setState(384);
			match(T__20);
			setState(385);
			match(T__22);
			setState(386);
			((DurationAssignmentContext)_localctx).op = operationSide();
			setState(387);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparationContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ComparatorContext comparator() {
			return getRuleContext(ComparatorContext.class,0);
		}
		public List<OperationSideContext> operationSide() {
			return getRuleContexts(OperationSideContext.class);
		}
		public OperationSideContext operationSide(int i) {
			return getRuleContext(OperationSideContext.class,i);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ComparationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparation; }
	}

	public final ComparationContext comparation() throws RecognitionException {
		ComparationContext _localctx = new ComparationContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_comparation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			match(LP);
			setState(390);
			comparator();
			setState(391);
			operationSide();
			setState(392);
			operationSide();
			setState(393);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NegatedComparationContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public NegatedComparationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negatedComparation; }
	}

	public final NegatedComparationContext negatedComparation() throws RecognitionException {
		NegatedComparationContext _localctx = new NegatedComparationContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_negatedComparation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			match(LP);
			setState(396);
			match(T__7);
			setState(397);
			comparation();
			setState(398);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModificationContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ModificatorContext modificator() {
			return getRuleContext(ModificatorContext.class,0);
		}
		public PositiveLiteralContext positiveLiteral() {
			return getRuleContext(PositiveLiteralContext.class,0);
		}
		public OperationSideContext operationSide() {
			return getRuleContext(OperationSideContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ModificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modification; }
	}

	public final ModificationContext modification() throws RecognitionException {
		ModificationContext _localctx = new ModificationContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_modification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(400);
			match(LP);
			setState(401);
			modificator();
			setState(402);
			positiveLiteral();
			setState(403);
			operationSide();
			setState(404);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CeCondContext extends ParserRuleContext {
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public OrClauseContext orClause() {
			return getRuleContext(OrClauseContext.class,0);
		}
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NegatedComparationContext negatedComparation() {
			return getRuleContext(NegatedComparationContext.class,0);
		}
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public EmptyPreconditionContext emptyPrecondition() {
			return getRuleContext(EmptyPreconditionContext.class,0);
		}
		public CeCondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ceCond; }
	}

	public final CeCondContext ceCond() throws RecognitionException {
		CeCondContext _localctx = new CeCondContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_ceCond);
		try {
			setState(412);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(406);
				andClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(407);
				orClause();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(408);
				booleanLiteral();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(409);
				negatedComparation();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(410);
				comparation();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(411);
				emptyPrecondition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CeEffContext extends ParserRuleContext {
		public EffectNoCesContext effectNoCes() {
			return getRuleContext(EffectNoCesContext.class,0);
		}
		public AndEffectNoCesContext andEffectNoCes() {
			return getRuleContext(AndEffectNoCesContext.class,0);
		}
		public CeEffContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ceEff; }
	}

	public final CeEffContext ceEff() throws RecognitionException {
		CeEffContext _localctx = new CeEffContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_ceEff);
		try {
			setState(416);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(414);
				effectNoCes();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(415);
				andEffectNoCes();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CeContext extends ParserRuleContext {
		public CeCondContext cond;
		public CeEffContext eff;
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public CeCondContext ceCond() {
			return getRuleContext(CeCondContext.class,0);
		}
		public CeEffContext ceEff() {
			return getRuleContext(CeEffContext.class,0);
		}
		public CeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ce; }
	}

	public final CeContext ce() throws RecognitionException {
		CeContext _localctx = new CeContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_ce);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			match(LP);
			setState(419);
			match(T__23);
			setState(420);
			((CeContext)_localctx).cond = ceCond();
			setState(421);
			((CeContext)_localctx).eff = ceEff();
			setState(422);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForallEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public CeContext ce() {
			return getRuleContext(CeContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ForallEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forallEffect; }
	}

	public final ForallEffectContext forallEffect() throws RecognitionException {
		ForallEffectContext _localctx = new ForallEffectContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_forallEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			match(LP);
			setState(425);
			match(T__24);
			setState(426);
			parameters();
			setState(427);
			ce();
			setState(428);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForallContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ForallContext forall() {
			return getRuleContext(ForallContext.class,0);
		}
		public ExistsContext exists() {
			return getRuleContext(ExistsContext.class,0);
		}
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public OrClauseContext orClause() {
			return getRuleContext(OrClauseContext.class,0);
		}
		public ForallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forall; }
	}

	public final ForallContext forall() throws RecognitionException {
		ForallContext _localctx = new ForallContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_forall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(430);
			match(LP);
			setState(431);
			match(T__24);
			setState(432);
			parameters();
			setState(437);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(433);
				forall();
				}
				break;
			case 2:
				{
				setState(434);
				exists();
				}
				break;
			case 3:
				{
				setState(435);
				andClause();
				}
				break;
			case 4:
				{
				setState(436);
				orClause();
				}
				break;
			}
			setState(439);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExistsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ForallContext forall() {
			return getRuleContext(ForallContext.class,0);
		}
		public ExistsContext exists() {
			return getRuleContext(ExistsContext.class,0);
		}
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public OrClauseContext orClause() {
			return getRuleContext(OrClauseContext.class,0);
		}
		public ExistsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exists; }
	}

	public final ExistsContext exists() throws RecognitionException {
		ExistsContext _localctx = new ExistsContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_exists);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(441);
			match(LP);
			setState(442);
			match(T__25);
			setState(443);
			parameters();
			setState(448);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				{
				setState(444);
				forall();
				}
				break;
			case 2:
				{
				setState(445);
				exists();
				}
				break;
			case 3:
				{
				setState(446);
				andClause();
				}
				break;
			case 4:
				{
				setState(447);
				orClause();
				}
				break;
			}
			setState(450);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EffectContext extends ParserRuleContext {
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public CeContext ce() {
			return getRuleContext(CeContext.class,0);
		}
		public ForallEffectContext forallEffect() {
			return getRuleContext(ForallEffectContext.class,0);
		}
		public EffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effect; }
	}

	public final EffectContext effect() throws RecognitionException {
		EffectContext _localctx = new EffectContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_effect);
		try {
			setState(456);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(452);
				booleanLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(453);
				modification();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(454);
				ce();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(455);
				forallEffect();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EffectNoCesContext extends ParserRuleContext {
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public EffectNoCesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effectNoCes; }
	}

	public final EffectNoCesContext effectNoCes() throws RecognitionException {
		EffectNoCesContext _localctx = new EffectNoCesContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_effectNoCes);
		try {
			setState(460);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(458);
				booleanLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(459);
				modification();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InequalityContext extends ParserRuleContext {
		public LiftedAtomParameterContext a1;
		public LiftedAtomParameterContext a2;
		public List<TerminalNode> LP() { return getTokens(pddlParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(pddlParser.LP, i);
		}
		public List<TerminalNode> RP() { return getTokens(pddlParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(pddlParser.RP, i);
		}
		public List<LiftedAtomParameterContext> liftedAtomParameter() {
			return getRuleContexts(LiftedAtomParameterContext.class);
		}
		public LiftedAtomParameterContext liftedAtomParameter(int i) {
			return getRuleContext(LiftedAtomParameterContext.class,i);
		}
		public InequalityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inequality; }
	}

	public final InequalityContext inequality() throws RecognitionException {
		InequalityContext _localctx = new InequalityContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_inequality);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(462);
			match(LP);
			setState(463);
			match(T__7);
			setState(464);
			match(LP);
			setState(465);
			match(T__20);
			setState(466);
			((InequalityContext)_localctx).a1 = liftedAtomParameter();
			setState(467);
			((InequalityContext)_localctx).a2 = liftedAtomParameter();
			setState(468);
			match(RP);
			setState(469);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndClauseContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<AndClauseContext> andClause() {
			return getRuleContexts(AndClauseContext.class);
		}
		public AndClauseContext andClause(int i) {
			return getRuleContext(AndClauseContext.class,i);
		}
		public List<OrClauseContext> orClause() {
			return getRuleContexts(OrClauseContext.class);
		}
		public OrClauseContext orClause(int i) {
			return getRuleContext(OrClauseContext.class,i);
		}
		public List<InequalityContext> inequality() {
			return getRuleContexts(InequalityContext.class);
		}
		public InequalityContext inequality(int i) {
			return getRuleContext(InequalityContext.class,i);
		}
		public List<BooleanLiteralContext> booleanLiteral() {
			return getRuleContexts(BooleanLiteralContext.class);
		}
		public BooleanLiteralContext booleanLiteral(int i) {
			return getRuleContext(BooleanLiteralContext.class,i);
		}
		public List<NegatedComparationContext> negatedComparation() {
			return getRuleContexts(NegatedComparationContext.class);
		}
		public NegatedComparationContext negatedComparation(int i) {
			return getRuleContext(NegatedComparationContext.class,i);
		}
		public List<ComparationContext> comparation() {
			return getRuleContexts(ComparationContext.class);
		}
		public ComparationContext comparation(int i) {
			return getRuleContext(ComparationContext.class,i);
		}
		public AndClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andClause; }
	}

	public final AndClauseContext andClause() throws RecognitionException {
		AndClauseContext _localctx = new AndClauseContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_andClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(471);
			match(LP);
			setState(472);
			match(T__26);
			setState(479); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(479);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
				case 1:
					{
					setState(473);
					andClause();
					}
					break;
				case 2:
					{
					setState(474);
					orClause();
					}
					break;
				case 3:
					{
					setState(475);
					inequality();
					}
					break;
				case 4:
					{
					setState(476);
					booleanLiteral();
					}
					break;
				case 5:
					{
					setState(477);
					negatedComparation();
					}
					break;
				case 6:
					{
					setState(478);
					comparation();
					}
					break;
				}
				}
				setState(481); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(483);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrClauseContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<AndClauseContext> andClause() {
			return getRuleContexts(AndClauseContext.class);
		}
		public AndClauseContext andClause(int i) {
			return getRuleContext(AndClauseContext.class,i);
		}
		public List<OrClauseContext> orClause() {
			return getRuleContexts(OrClauseContext.class);
		}
		public OrClauseContext orClause(int i) {
			return getRuleContext(OrClauseContext.class,i);
		}
		public List<InequalityContext> inequality() {
			return getRuleContexts(InequalityContext.class);
		}
		public InequalityContext inequality(int i) {
			return getRuleContext(InequalityContext.class,i);
		}
		public List<BooleanLiteralContext> booleanLiteral() {
			return getRuleContexts(BooleanLiteralContext.class);
		}
		public BooleanLiteralContext booleanLiteral(int i) {
			return getRuleContext(BooleanLiteralContext.class,i);
		}
		public List<NegatedComparationContext> negatedComparation() {
			return getRuleContexts(NegatedComparationContext.class);
		}
		public NegatedComparationContext negatedComparation(int i) {
			return getRuleContext(NegatedComparationContext.class,i);
		}
		public List<ComparationContext> comparation() {
			return getRuleContexts(ComparationContext.class);
		}
		public ComparationContext comparation(int i) {
			return getRuleContext(ComparationContext.class,i);
		}
		public OrClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orClause; }
	}

	public final OrClauseContext orClause() throws RecognitionException {
		OrClauseContext _localctx = new OrClauseContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_orClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(485);
			match(LP);
			setState(486);
			match(T__27);
			setState(493); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(493);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
				case 1:
					{
					setState(487);
					andClause();
					}
					break;
				case 2:
					{
					setState(488);
					orClause();
					}
					break;
				case 3:
					{
					setState(489);
					inequality();
					}
					break;
				case 4:
					{
					setState(490);
					booleanLiteral();
					}
					break;
				case 5:
					{
					setState(491);
					negatedComparation();
					}
					break;
				case 6:
					{
					setState(492);
					comparation();
					}
					break;
				}
				}
				setState(495); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(497);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<EffectContext> effect() {
			return getRuleContexts(EffectContext.class);
		}
		public EffectContext effect(int i) {
			return getRuleContext(EffectContext.class,i);
		}
		public AndEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andEffect; }
	}

	public final AndEffectContext andEffect() throws RecognitionException {
		AndEffectContext _localctx = new AndEffectContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_andEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(499);
			match(LP);
			setState(500);
			match(T__26);
			setState(502); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(501);
				effect();
				}
				}
				setState(504); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(506);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndEffectNoCesContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<EffectNoCesContext> effectNoCes() {
			return getRuleContexts(EffectNoCesContext.class);
		}
		public EffectNoCesContext effectNoCes(int i) {
			return getRuleContext(EffectNoCesContext.class,i);
		}
		public AndEffectNoCesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andEffectNoCes; }
	}

	public final AndEffectNoCesContext andEffectNoCes() throws RecognitionException {
		AndEffectNoCesContext _localctx = new AndEffectNoCesContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_andEffectNoCes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(508);
			match(LP);
			setState(509);
			match(T__26);
			setState(511); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(510);
				effectNoCes();
				}
				}
				setState(513); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(515);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EmptyPreconditionContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public EmptyPreconditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emptyPrecondition; }
	}

	public final EmptyPreconditionContext emptyPrecondition() throws RecognitionException {
		EmptyPreconditionContext _localctx = new EmptyPreconditionContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_emptyPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			match(LP);
			setState(518);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PreconditionsContext extends ParserRuleContext {
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public OrClauseContext orClause() {
			return getRuleContext(OrClauseContext.class,0);
		}
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NegatedComparationContext negatedComparation() {
			return getRuleContext(NegatedComparationContext.class,0);
		}
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public EmptyPreconditionContext emptyPrecondition() {
			return getRuleContext(EmptyPreconditionContext.class,0);
		}
		public PreconditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preconditions; }
	}

	public final PreconditionsContext preconditions() throws RecognitionException {
		PreconditionsContext _localctx = new PreconditionsContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_preconditions);
		try {
			setState(526);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(520);
				andClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(521);
				orClause();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(522);
				booleanLiteral();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(523);
				negatedComparation();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(524);
				comparation();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(525);
				emptyPrecondition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EffectsContext extends ParserRuleContext {
		public EffectContext effect() {
			return getRuleContext(EffectContext.class,0);
		}
		public AndEffectContext andEffect() {
			return getRuleContext(AndEffectContext.class,0);
		}
		public EffectsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effects; }
	}

	public final EffectsContext effects() throws RecognitionException {
		EffectsContext _localctx = new EffectsContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_effects);
		try {
			setState(530);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(528);
				effect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(529);
				andEffect();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndDurClauseContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<AtStartPreContext> atStartPre() {
			return getRuleContexts(AtStartPreContext.class);
		}
		public AtStartPreContext atStartPre(int i) {
			return getRuleContext(AtStartPreContext.class,i);
		}
		public List<OverAllPreContext> overAllPre() {
			return getRuleContexts(OverAllPreContext.class);
		}
		public OverAllPreContext overAllPre(int i) {
			return getRuleContext(OverAllPreContext.class,i);
		}
		public List<AtEndPreContext> atEndPre() {
			return getRuleContexts(AtEndPreContext.class);
		}
		public AtEndPreContext atEndPre(int i) {
			return getRuleContext(AtEndPreContext.class,i);
		}
		public AndDurClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andDurClause; }
	}

	public final AndDurClauseContext andDurClause() throws RecognitionException {
		AndDurClauseContext _localctx = new AndDurClauseContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_andDurClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(532);
			match(LP);
			setState(533);
			match(T__26);
			setState(537); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(537);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
				case 1:
					{
					setState(534);
					atStartPre();
					}
					break;
				case 2:
					{
					setState(535);
					overAllPre();
					}
					break;
				case 3:
					{
					setState(536);
					atEndPre();
					}
					break;
				}
				}
				setState(539); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(541);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtStartPreContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NegatedComparationContext negatedComparation() {
			return getRuleContext(NegatedComparationContext.class,0);
		}
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public AtStartPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atStartPre; }
	}

	public final AtStartPreContext atStartPre() throws RecognitionException {
		AtStartPreContext _localctx = new AtStartPreContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_atStartPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(543);
			match(LP);
			setState(544);
			match(T__28);
			setState(549);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				{
				setState(545);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(546);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(547);
				comparation();
				}
				break;
			case 4:
				{
				setState(548);
				andClause();
				}
				break;
			}
			setState(551);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverAllPreContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NegatedComparationContext negatedComparation() {
			return getRuleContext(NegatedComparationContext.class,0);
		}
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public OverAllPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overAllPre; }
	}

	public final OverAllPreContext overAllPre() throws RecognitionException {
		OverAllPreContext _localctx = new OverAllPreContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_overAllPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(553);
			match(LP);
			setState(554);
			match(T__29);
			setState(559);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				{
				setState(555);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(556);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(557);
				comparation();
				}
				break;
			case 4:
				{
				setState(558);
				andClause();
				}
				break;
			}
			setState(561);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtEndPreContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public NegatedComparationContext negatedComparation() {
			return getRuleContext(NegatedComparationContext.class,0);
		}
		public ComparationContext comparation() {
			return getRuleContext(ComparationContext.class,0);
		}
		public AndClauseContext andClause() {
			return getRuleContext(AndClauseContext.class,0);
		}
		public AtEndPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atEndPre; }
	}

	public final AtEndPreContext atEndPre() throws RecognitionException {
		AtEndPreContext _localctx = new AtEndPreContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_atEndPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(563);
			match(LP);
			setState(564);
			match(T__30);
			setState(569);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				{
				setState(565);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(566);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(567);
				comparation();
				}
				break;
			case 4:
				{
				setState(568);
				andClause();
				}
				break;
			}
			setState(571);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurativeConditionsContext extends ParserRuleContext {
		public AndDurClauseContext andDurClause() {
			return getRuleContext(AndDurClauseContext.class,0);
		}
		public AtStartPreContext atStartPre() {
			return getRuleContext(AtStartPreContext.class,0);
		}
		public OverAllPreContext overAllPre() {
			return getRuleContext(OverAllPreContext.class,0);
		}
		public AtEndPreContext atEndPre() {
			return getRuleContext(AtEndPreContext.class,0);
		}
		public EmptyPreconditionContext emptyPrecondition() {
			return getRuleContext(EmptyPreconditionContext.class,0);
		}
		public DurativeConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_durativeConditions; }
	}

	public final DurativeConditionsContext durativeConditions() throws RecognitionException {
		DurativeConditionsContext _localctx = new DurativeConditionsContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_durativeConditions);
		try {
			setState(578);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(573);
				andDurClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(574);
				atStartPre();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(575);
				overAllPre();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(576);
				atEndPre();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(577);
				emptyPrecondition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtStartEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public AndEffectContext andEffect() {
			return getRuleContext(AndEffectContext.class,0);
		}
		public AtStartEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atStartEffect; }
	}

	public final AtStartEffectContext atStartEffect() throws RecognitionException {
		AtStartEffectContext _localctx = new AtStartEffectContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_atStartEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(580);
			match(LP);
			setState(581);
			match(T__28);
			setState(585);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(582);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(583);
				modification();
				}
				break;
			case 3:
				{
				setState(584);
				andEffect();
				}
				break;
			}
			setState(587);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverAllEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public AndEffectContext andEffect() {
			return getRuleContext(AndEffectContext.class,0);
		}
		public OverAllEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overAllEffect; }
	}

	public final OverAllEffectContext overAllEffect() throws RecognitionException {
		OverAllEffectContext _localctx = new OverAllEffectContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_overAllEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(589);
			match(LP);
			setState(590);
			match(T__31);
			setState(594);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				{
				setState(591);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(592);
				modification();
				}
				break;
			case 3:
				{
				setState(593);
				andEffect();
				}
				break;
			}
			setState(596);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtEndEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public AndEffectContext andEffect() {
			return getRuleContext(AndEffectContext.class,0);
		}
		public AtEndEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atEndEffect; }
	}

	public final AtEndEffectContext atEndEffect() throws RecognitionException {
		AtEndEffectContext _localctx = new AtEndEffectContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_atEndEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(598);
			match(LP);
			setState(599);
			match(T__30);
			setState(603);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				{
				setState(600);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(601);
				modification();
				}
				break;
			case 3:
				{
				setState(602);
				andEffect();
				}
				break;
			}
			setState(605);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurativeEffectContext extends ParserRuleContext {
		public AtStartEffectContext atStartEffect() {
			return getRuleContext(AtStartEffectContext.class,0);
		}
		public OverAllEffectContext overAllEffect() {
			return getRuleContext(OverAllEffectContext.class,0);
		}
		public AtEndEffectContext atEndEffect() {
			return getRuleContext(AtEndEffectContext.class,0);
		}
		public DurativeEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_durativeEffect; }
	}

	public final DurativeEffectContext durativeEffect() throws RecognitionException {
		DurativeEffectContext _localctx = new DurativeEffectContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_durativeEffect);
		try {
			setState(610);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(607);
				atStartEffect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(608);
				overAllEffect();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(609);
				atEndEffect();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndDurativeEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<DurativeEffectContext> durativeEffect() {
			return getRuleContexts(DurativeEffectContext.class);
		}
		public DurativeEffectContext durativeEffect(int i) {
			return getRuleContext(DurativeEffectContext.class,i);
		}
		public AndDurativeEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andDurativeEffect; }
	}

	public final AndDurativeEffectContext andDurativeEffect() throws RecognitionException {
		AndDurativeEffectContext _localctx = new AndDurativeEffectContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_andDurativeEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(612);
			match(LP);
			setState(613);
			match(T__26);
			setState(615); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(614);
				durativeEffect();
				}
				}
				setState(617); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(619);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurativeEffectsContext extends ParserRuleContext {
		public DurativeEffectContext durativeEffect() {
			return getRuleContext(DurativeEffectContext.class,0);
		}
		public AndDurativeEffectContext andDurativeEffect() {
			return getRuleContext(AndDurativeEffectContext.class,0);
		}
		public DurativeEffectsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_durativeEffects; }
	}

	public final DurativeEffectsContext durativeEffects() throws RecognitionException {
		DurativeEffectsContext _localctx = new DurativeEffectsContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_durativeEffects);
		try {
			setState(623);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(621);
				durativeEffect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(622);
				andDurativeEffect();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<TypedAtomParameterContext> typedAtomParameter() {
			return getRuleContexts(TypedAtomParameterContext.class);
		}
		public TypedAtomParameterContext typedAtomParameter(int i) {
			return getRuleContext(TypedAtomParameterContext.class,i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(625);
			match(LP);
			setState(629);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==NAME) {
				{
				{
				setState(626);
				typedAtomParameter();
				}
				}
				setState(631);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(632);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpNameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public OpNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opName; }
	}

	public final OpNameContext opName() throws RecognitionException {
		OpNameContext _localctx = new OpNameContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_opName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(634);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpParametersContext extends ParserRuleContext {
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public OpParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opParameters; }
	}

	public final OpParametersContext opParameters() throws RecognitionException {
		OpParametersContext _localctx = new OpParametersContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_opParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(636);
			match(T__32);
			setState(637);
			parameters();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpPreconditionContext extends ParserRuleContext {
		public PreconditionsContext preconditions() {
			return getRuleContext(PreconditionsContext.class,0);
		}
		public OpPreconditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opPrecondition; }
	}

	public final OpPreconditionContext opPrecondition() throws RecognitionException {
		OpPreconditionContext _localctx = new OpPreconditionContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_opPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(639);
			match(T__33);
			setState(640);
			preconditions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpDurativeConditionContext extends ParserRuleContext {
		public DurativeConditionsContext c;
		public DurativeConditionsContext durativeConditions() {
			return getRuleContext(DurativeConditionsContext.class,0);
		}
		public OpDurativeConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opDurativeCondition; }
	}

	public final OpDurativeConditionContext opDurativeCondition() throws RecognitionException {
		OpDurativeConditionContext _localctx = new OpDurativeConditionContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_opDurativeCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(642);
			match(T__34);
			setState(643);
			((OpDurativeConditionContext)_localctx).c = durativeConditions();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpEffectContext extends ParserRuleContext {
		public EffectsContext effects() {
			return getRuleContext(EffectsContext.class,0);
		}
		public OpEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opEffect; }
	}

	public final OpEffectContext opEffect() throws RecognitionException {
		OpEffectContext _localctx = new OpEffectContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_opEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(645);
			match(T__35);
			setState(646);
			effects();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpDurativeEffectContext extends ParserRuleContext {
		public DurativeEffectsContext e;
		public DurativeEffectsContext durativeEffects() {
			return getRuleContext(DurativeEffectsContext.class,0);
		}
		public OpDurativeEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opDurativeEffect; }
	}

	public final OpDurativeEffectContext opDurativeEffect() throws RecognitionException {
		OpDurativeEffectContext _localctx = new OpDurativeEffectContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_opDurativeEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(648);
			match(T__35);
			setState(649);
			((OpDurativeEffectContext)_localctx).e = durativeEffects();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpDurationContext extends ParserRuleContext {
		public DurationAssignmentContext durationAssignment() {
			return getRuleContext(DurationAssignmentContext.class,0);
		}
		public OpDurationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opDuration; }
	}

	public final OpDurationContext opDuration() throws RecognitionException {
		OpDurationContext _localctx = new OpDurationContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_opDuration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(651);
			match(T__36);
			setState(652);
			durationAssignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public OpNameContext opName() {
			return getRuleContext(OpNameContext.class,0);
		}
		public OpEffectContext opEffect() {
			return getRuleContext(OpEffectContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OpParametersContext opParameters() {
			return getRuleContext(OpParametersContext.class,0);
		}
		public OpPreconditionContext opPrecondition() {
			return getRuleContext(OpPreconditionContext.class,0);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(654);
			match(LP);
			setState(655);
			match(T__37);
			setState(656);
			opName();
			setState(658);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(657);
				opParameters();
				}
			}

			setState(661);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__33) {
				{
				setState(660);
				opPrecondition();
				}
			}

			setState(663);
			opEffect();
			setState(664);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DurativeActionContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public OpNameContext opName() {
			return getRuleContext(OpNameContext.class,0);
		}
		public OpDurativeEffectContext opDurativeEffect() {
			return getRuleContext(OpDurativeEffectContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OpParametersContext opParameters() {
			return getRuleContext(OpParametersContext.class,0);
		}
		public OpDurationContext opDuration() {
			return getRuleContext(OpDurationContext.class,0);
		}
		public OpDurativeConditionContext opDurativeCondition() {
			return getRuleContext(OpDurativeConditionContext.class,0);
		}
		public DurativeActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_durativeAction; }
	}

	public final DurativeActionContext durativeAction() throws RecognitionException {
		DurativeActionContext _localctx = new DurativeActionContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_durativeAction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(666);
			match(LP);
			setState(667);
			match(T__38);
			setState(668);
			opName();
			setState(670);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(669);
				opParameters();
				}
			}

			setState(673);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__36) {
				{
				setState(672);
				opDuration();
				}
			}

			setState(676);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__34) {
				{
				setState(675);
				opDurativeCondition();
				}
			}

			setState(678);
			opDurativeEffect();
			setState(679);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EventContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public OpNameContext opName() {
			return getRuleContext(OpNameContext.class,0);
		}
		public OpEffectContext opEffect() {
			return getRuleContext(OpEffectContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OpParametersContext opParameters() {
			return getRuleContext(OpParametersContext.class,0);
		}
		public OpPreconditionContext opPrecondition() {
			return getRuleContext(OpPreconditionContext.class,0);
		}
		public EventContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_event; }
	}

	public final EventContext event() throws RecognitionException {
		EventContext _localctx = new EventContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_event);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(681);
			match(LP);
			setState(682);
			match(T__39);
			setState(683);
			opName();
			setState(685);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(684);
				opParameters();
				}
			}

			setState(688);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__33) {
				{
				setState(687);
				opPrecondition();
				}
			}

			setState(690);
			opEffect();
			setState(691);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProcessContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public OpNameContext opName() {
			return getRuleContext(OpNameContext.class,0);
		}
		public OpEffectContext opEffect() {
			return getRuleContext(OpEffectContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OpParametersContext opParameters() {
			return getRuleContext(OpParametersContext.class,0);
		}
		public OpPreconditionContext opPrecondition() {
			return getRuleContext(OpPreconditionContext.class,0);
		}
		public ProcessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process; }
	}

	public final ProcessContext process() throws RecognitionException {
		ProcessContext _localctx = new ProcessContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_process);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(693);
			match(LP);
			setState(694);
			match(T__40);
			setState(695);
			opName();
			setState(697);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(696);
				opParameters();
				}
			}

			setState(700);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__33) {
				{
				setState(699);
				opPrecondition();
				}
			}

			setState(702);
			opEffect();
			setState(703);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstraintsContext extends ParserRuleContext {
		public List<TerminalNode> LP() { return getTokens(pddlParser.LP); }
		public TerminalNode LP(int i) {
			return getToken(pddlParser.LP, i);
		}
		public List<TerminalNode> RP() { return getTokens(pddlParser.RP); }
		public TerminalNode RP(int i) {
			return getToken(pddlParser.RP, i);
		}
		public List<ForallContext> forall() {
			return getRuleContexts(ForallContext.class);
		}
		public ForallContext forall(int i) {
			return getRuleContext(ForallContext.class,i);
		}
		public List<ExistsContext> exists() {
			return getRuleContexts(ExistsContext.class);
		}
		public ExistsContext exists(int i) {
			return getRuleContext(ExistsContext.class,i);
		}
		public ConstraintsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constraints; }
	}

	public final ConstraintsContext constraints() throws RecognitionException {
		ConstraintsContext _localctx = new ConstraintsContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_constraints);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(705);
			match(LP);
			setState(706);
			match(T__41);
			setState(707);
			match(LP);
			setState(708);
			match(T__26);
			setState(711); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(711);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,62,_ctx) ) {
				case 1:
					{
					setState(709);
					forall();
					}
					break;
				case 2:
					{
					setState(710);
					exists();
					}
					break;
				}
				}
				setState(713); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(715);
			match(RP);
			setState(716);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProblemContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public ProblemNameContext problemName() {
			return getRuleContext(ProblemNameContext.class,0);
		}
		public ProblemDomainContext problemDomain() {
			return getRuleContext(ProblemDomainContext.class,0);
		}
		public InitContext init() {
			return getRuleContext(InitContext.class,0);
		}
		public GoalContext goal() {
			return getRuleContext(GoalContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ObjectsContext objects() {
			return getRuleContext(ObjectsContext.class,0);
		}
		public MetricContext metric() {
			return getRuleContext(MetricContext.class,0);
		}
		public ProblemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_problem; }
	}

	public final ProblemContext problem() throws RecognitionException {
		ProblemContext _localctx = new ProblemContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_problem);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(718);
			match(LP);
			setState(719);
			match(T__0);
			setState(720);
			problemName();
			setState(721);
			problemDomain();
			setState(723);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				{
				setState(722);
				objects();
				}
				break;
			}
			setState(725);
			init();
			setState(726);
			goal();
			setState(728);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LP) {
				{
				setState(727);
				metric();
				}
			}

			setState(730);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProblemNameContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ProblemNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_problemName; }
	}

	public final ProblemNameContext problemName() throws RecognitionException {
		ProblemNameContext _localctx = new ProblemNameContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_problemName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(732);
			match(LP);
			setState(733);
			match(T__42);
			setState(734);
			match(NAME);
			setState(735);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProblemDomainContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode NAME() { return getToken(pddlParser.NAME, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public ProblemDomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_problemDomain; }
	}

	public final ProblemDomainContext problemDomain() throws RecognitionException {
		ProblemDomainContext _localctx = new ProblemDomainContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_problemDomain);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(737);
			match(LP);
			setState(738);
			match(T__43);
			setState(739);
			match(NAME);
			setState(740);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypedObjectsContext extends ParserRuleContext {
		public TypeNameContext typeName() {
			return getRuleContext(TypeNameContext.class,0);
		}
		public List<GroundAtomParameterContext> groundAtomParameter() {
			return getRuleContexts(GroundAtomParameterContext.class);
		}
		public GroundAtomParameterContext groundAtomParameter(int i) {
			return getRuleContext(GroundAtomParameterContext.class,i);
		}
		public TypedObjectsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedObjects; }
	}

	public final TypedObjectsContext typedObjects() throws RecognitionException {
		TypedObjectsContext _localctx = new TypedObjectsContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_typedObjects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(743); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(742);
				groundAtomParameter();
				}
				}
				setState(745); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(747);
			match(T__4);
			setState(748);
			typeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<TypedObjectsContext> typedObjects() {
			return getRuleContexts(TypedObjectsContext.class);
		}
		public TypedObjectsContext typedObjects(int i) {
			return getRuleContext(TypedObjectsContext.class,i);
		}
		public ObjectsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objects; }
	}

	public final ObjectsContext objects() throws RecognitionException {
		ObjectsContext _localctx = new ObjectsContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_objects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(750);
			match(LP);
			setState(751);
			match(T__44);
			setState(755);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(752);
				typedObjects();
				}
				}
				setState(757);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(758);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public List<PositiveLiteralContext> positiveLiteral() {
			return getRuleContexts(PositiveLiteralContext.class);
		}
		public PositiveLiteralContext positiveLiteral(int i) {
			return getRuleContext(PositiveLiteralContext.class,i);
		}
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(760);
			match(LP);
			setState(761);
			match(T__45);
			setState(764); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(764);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,68,_ctx) ) {
				case 1:
					{
					setState(762);
					positiveLiteral();
					}
					break;
				case 2:
					{
					setState(763);
					assignment();
					}
					break;
				}
				}
				setState(766); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 29273397577908224L) != 0) );
			setState(768);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GoalContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public PreconditionsContext preconditions() {
			return getRuleContext(PreconditionsContext.class,0);
		}
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public GoalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_goal; }
	}

	public final GoalContext goal() throws RecognitionException {
		GoalContext _localctx = new GoalContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_goal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(770);
			match(LP);
			setState(771);
			match(T__46);
			setState(772);
			preconditions();
			setState(773);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MetricContext extends ParserRuleContext {
		public Token sign;
		public OperationSideContext op;
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public OperationSideContext operationSide() {
			return getRuleContext(OperationSideContext.class,0);
		}
		public MetricContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_metric; }
	}

	public final MetricContext metric() throws RecognitionException {
		MetricContext _localctx = new MetricContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_metric);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(775);
			match(LP);
			setState(776);
			match(T__47);
			setState(777);
			((MetricContext)_localctx).sign = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__48 || _la==T__49) ) {
				((MetricContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(778);
			((MetricContext)_localctx).op = operationSide();
			setState(779);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00019\u030e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u00076\u0002"+
		"7\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007;\u0002"+
		"<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007@\u0002"+
		"A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007E\u0002"+
		"F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007J\u0002"+
		"K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0002O\u0007O\u0002"+
		"P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007S\u0002T\u0007T\u0002"+
		"U\u0007U\u0002V\u0007V\u0002W\u0007W\u0001\u0000\u0001\u0000\u0003\u0000"+
		"\u00b3\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u00b9\b\u0001\u0001\u0001\u0003\u0001\u00bc\b\u0001\u0001\u0001\u0003"+
		"\u0001\u00bf\b\u0001\u0001\u0001\u0003\u0001\u00c2\b\u0001\u0001\u0001"+
		"\u0003\u0001\u00c5\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u0001\u00cb\b\u0001\n\u0001\f\u0001\u00ce\t\u0001\u0001\u0001\u0003"+
		"\u0001\u00d1\b\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00e0\b\u0004\n\u0004\f\u0004"+
		"\u00e3\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007\u00ed\b\u0007\u000b\u0007"+
		"\f\u0007\u00ee\u0001\u0007\u0005\u0007\u00f2\b\u0007\n\u0007\f\u0007\u00f5"+
		"\t\u0007\u0001\b\u0001\b\u0001\b\u0004\b\u00fa\b\b\u000b\b\f\b\u00fb\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0004\u000b"+
		"\u0106\b\u000b\u000b\u000b\f\u000b\u0107\u0001\u000b\u0005\u000b\u010b"+
		"\b\u000b\n\u000b\f\u000b\u010e\t\u000b\u0001\f\u0001\f\u0001\f\u0004\f"+
		"\u0113\b\f\u000b\f\f\f\u0114\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010\u0120\b\u0010"+
		"\u000b\u0010\f\u0010\u0121\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u0129\b\u0011\u0001\u0012\u0001\u0012\u0005\u0012"+
		"\u012d\b\u0012\n\u0012\f\u0012\u0130\t\u0012\u0001\u0013\u0001\u0013\u0005"+
		"\u0013\u0134\b\u0013\n\u0013\f\u0013\u0137\t\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u013e\b\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0003\u0017\u014b\b\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0004\u0018\u0150\b\u0018\u000b\u0018"+
		"\f\u0018\u0151\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0004\u0019\u0159\b\u0019\u000b\u0019\f\u0019\u015a\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001"+
		"\u001f\u0003\u001f\u016b\b\u001f\u0001 \u0001 \u0001!\u0001!\u0001!\u0003"+
		"!\u0172\b!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001&\u0001&\u0001&\u0001"+
		"&\u0001&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001(\u0001"+
		"(\u0001(\u0001(\u0001(\u0001(\u0003(\u019d\b(\u0001)\u0001)\u0003)\u01a1"+
		"\b)\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0001+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0003"+
		",\u01b6\b,\u0001,\u0001,\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001"+
		"-\u0003-\u01c1\b-\u0001-\u0001-\u0001.\u0001.\u0001.\u0001.\u0003.\u01c9"+
		"\b.\u0001/\u0001/\u0003/\u01cd\b/\u00010\u00010\u00010\u00010\u00010\u0001"+
		"0\u00010\u00010\u00010\u00011\u00011\u00011\u00011\u00011\u00011\u0001"+
		"1\u00011\u00041\u01e0\b1\u000b1\f1\u01e1\u00011\u00011\u00012\u00012\u0001"+
		"2\u00012\u00012\u00012\u00012\u00012\u00042\u01ee\b2\u000b2\f2\u01ef\u0001"+
		"2\u00012\u00013\u00013\u00013\u00043\u01f7\b3\u000b3\f3\u01f8\u00013\u0001"+
		"3\u00014\u00014\u00014\u00044\u0200\b4\u000b4\f4\u0201\u00014\u00014\u0001"+
		"5\u00015\u00015\u00016\u00016\u00016\u00016\u00016\u00016\u00036\u020f"+
		"\b6\u00017\u00017\u00037\u0213\b7\u00018\u00018\u00018\u00018\u00018\u0004"+
		"8\u021a\b8\u000b8\f8\u021b\u00018\u00018\u00019\u00019\u00019\u00019\u0001"+
		"9\u00019\u00039\u0226\b9\u00019\u00019\u0001:\u0001:\u0001:\u0001:\u0001"+
		":\u0001:\u0003:\u0230\b:\u0001:\u0001:\u0001;\u0001;\u0001;\u0001;\u0001"+
		";\u0001;\u0003;\u023a\b;\u0001;\u0001;\u0001<\u0001<\u0001<\u0001<\u0001"+
		"<\u0003<\u0243\b<\u0001=\u0001=\u0001=\u0001=\u0001=\u0003=\u024a\b=\u0001"+
		"=\u0001=\u0001>\u0001>\u0001>\u0001>\u0001>\u0003>\u0253\b>\u0001>\u0001"+
		">\u0001?\u0001?\u0001?\u0001?\u0001?\u0003?\u025c\b?\u0001?\u0001?\u0001"+
		"@\u0001@\u0001@\u0003@\u0263\b@\u0001A\u0001A\u0001A\u0004A\u0268\bA\u000b"+
		"A\fA\u0269\u0001A\u0001A\u0001B\u0001B\u0003B\u0270\bB\u0001C\u0001C\u0005"+
		"C\u0274\bC\nC\fC\u0277\tC\u0001C\u0001C\u0001D\u0001D\u0001E\u0001E\u0001"+
		"E\u0001F\u0001F\u0001F\u0001G\u0001G\u0001G\u0001H\u0001H\u0001H\u0001"+
		"I\u0001I\u0001I\u0001J\u0001J\u0001J\u0001K\u0001K\u0001K\u0001K\u0003"+
		"K\u0293\bK\u0001K\u0003K\u0296\bK\u0001K\u0001K\u0001K\u0001L\u0001L\u0001"+
		"L\u0001L\u0003L\u029f\bL\u0001L\u0003L\u02a2\bL\u0001L\u0003L\u02a5\b"+
		"L\u0001L\u0001L\u0001L\u0001M\u0001M\u0001M\u0001M\u0003M\u02ae\bM\u0001"+
		"M\u0003M\u02b1\bM\u0001M\u0001M\u0001M\u0001N\u0001N\u0001N\u0001N\u0003"+
		"N\u02ba\bN\u0001N\u0003N\u02bd\bN\u0001N\u0001N\u0001N\u0001O\u0001O\u0001"+
		"O\u0001O\u0001O\u0001O\u0004O\u02c8\bO\u000bO\fO\u02c9\u0001O\u0001O\u0001"+
		"O\u0001P\u0001P\u0001P\u0001P\u0001P\u0003P\u02d4\bP\u0001P\u0001P\u0001"+
		"P\u0003P\u02d9\bP\u0001P\u0001P\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0001"+
		"R\u0001R\u0001R\u0001R\u0001R\u0001S\u0004S\u02e8\bS\u000bS\fS\u02e9\u0001"+
		"S\u0001S\u0001S\u0001T\u0001T\u0001T\u0005T\u02f2\bT\nT\fT\u02f5\tT\u0001"+
		"T\u0001T\u0001U\u0001U\u0001U\u0001U\u0004U\u02fd\bU\u000bU\fU\u02fe\u0001"+
		"U\u0001U\u0001V\u0001V\u0001V\u0001V\u0001V\u0001W\u0001W\u0001W\u0001"+
		"W\u0001W\u0001W\u0001W\u0000\u0000X\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDF"+
		"HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c"+
		"\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4"+
		"\u00a6\u00a8\u00aa\u00ac\u00ae\u0000\u0005\u0001\u000056\u0001\u0000\u000b"+
		"\r\u0002\u0000\u0005\u0005\u000e\u0010\u0001\u0000\u0011\u0015\u0001\u0000"+
		"12\u0322\u0000\u00b2\u0001\u0000\u0000\u0000\u0002\u00b4\u0001\u0000\u0000"+
		"\u0000\u0004\u00d4\u0001\u0000\u0000\u0000\u0006\u00d9\u0001\u0000\u0000"+
		"\u0000\b\u00dc\u0001\u0000\u0000\u0000\n\u00e6\u0001\u0000\u0000\u0000"+
		"\f\u00e9\u0001\u0000\u0000\u0000\u000e\u00ec\u0001\u0000\u0000\u0000\u0010"+
		"\u00f6\u0001\u0000\u0000\u0000\u0012\u00ff\u0001\u0000\u0000\u0000\u0014"+
		"\u0102\u0001\u0000\u0000\u0000\u0016\u0105\u0001\u0000\u0000\u0000\u0018"+
		"\u010f\u0001\u0000\u0000\u0000\u001a\u0118\u0001\u0000\u0000\u0000\u001c"+
		"\u011a\u0001\u0000\u0000\u0000\u001e\u011c\u0001\u0000\u0000\u0000 \u011f"+
		"\u0001\u0000\u0000\u0000\"\u0128\u0001\u0000\u0000\u0000$\u012a\u0001"+
		"\u0000\u0000\u0000&\u0131\u0001\u0000\u0000\u0000(\u013d\u0001\u0000\u0000"+
		"\u0000*\u013f\u0001\u0000\u0000\u0000,\u0143\u0001\u0000\u0000\u0000."+
		"\u014a\u0001\u0000\u0000\u00000\u014c\u0001\u0000\u0000\u00002\u0155\u0001"+
		"\u0000\u0000\u00004\u015e\u0001\u0000\u0000\u00006\u0160\u0001\u0000\u0000"+
		"\u00008\u0162\u0001\u0000\u0000\u0000:\u0164\u0001\u0000\u0000\u0000<"+
		"\u0166\u0001\u0000\u0000\u0000>\u016a\u0001\u0000\u0000\u0000@\u016c\u0001"+
		"\u0000\u0000\u0000B\u0171\u0001\u0000\u0000\u0000D\u0173\u0001\u0000\u0000"+
		"\u0000F\u0179\u0001\u0000\u0000\u0000H\u017f\u0001\u0000\u0000\u0000J"+
		"\u0185\u0001\u0000\u0000\u0000L\u018b\u0001\u0000\u0000\u0000N\u0190\u0001"+
		"\u0000\u0000\u0000P\u019c\u0001\u0000\u0000\u0000R\u01a0\u0001\u0000\u0000"+
		"\u0000T\u01a2\u0001\u0000\u0000\u0000V\u01a8\u0001\u0000\u0000\u0000X"+
		"\u01ae\u0001\u0000\u0000\u0000Z\u01b9\u0001\u0000\u0000\u0000\\\u01c8"+
		"\u0001\u0000\u0000\u0000^\u01cc\u0001\u0000\u0000\u0000`\u01ce\u0001\u0000"+
		"\u0000\u0000b\u01d7\u0001\u0000\u0000\u0000d\u01e5\u0001\u0000\u0000\u0000"+
		"f\u01f3\u0001\u0000\u0000\u0000h\u01fc\u0001\u0000\u0000\u0000j\u0205"+
		"\u0001\u0000\u0000\u0000l\u020e\u0001\u0000\u0000\u0000n\u0212\u0001\u0000"+
		"\u0000\u0000p\u0214\u0001\u0000\u0000\u0000r\u021f\u0001\u0000\u0000\u0000"+
		"t\u0229\u0001\u0000\u0000\u0000v\u0233\u0001\u0000\u0000\u0000x\u0242"+
		"\u0001\u0000\u0000\u0000z\u0244\u0001\u0000\u0000\u0000|\u024d\u0001\u0000"+
		"\u0000\u0000~\u0256\u0001\u0000\u0000\u0000\u0080\u0262\u0001\u0000\u0000"+
		"\u0000\u0082\u0264\u0001\u0000\u0000\u0000\u0084\u026f\u0001\u0000\u0000"+
		"\u0000\u0086\u0271\u0001\u0000\u0000\u0000\u0088\u027a\u0001\u0000\u0000"+
		"\u0000\u008a\u027c\u0001\u0000\u0000\u0000\u008c\u027f\u0001\u0000\u0000"+
		"\u0000\u008e\u0282\u0001\u0000\u0000\u0000\u0090\u0285\u0001\u0000\u0000"+
		"\u0000\u0092\u0288\u0001\u0000\u0000\u0000\u0094\u028b\u0001\u0000\u0000"+
		"\u0000\u0096\u028e\u0001\u0000\u0000\u0000\u0098\u029a\u0001\u0000\u0000"+
		"\u0000\u009a\u02a9\u0001\u0000\u0000\u0000\u009c\u02b5\u0001\u0000\u0000"+
		"\u0000\u009e\u02c1\u0001\u0000\u0000\u0000\u00a0\u02ce\u0001\u0000\u0000"+
		"\u0000\u00a2\u02dc\u0001\u0000\u0000\u0000\u00a4\u02e1\u0001\u0000\u0000"+
		"\u0000\u00a6\u02e7\u0001\u0000\u0000\u0000\u00a8\u02ee\u0001\u0000\u0000"+
		"\u0000\u00aa\u02f8\u0001\u0000\u0000\u0000\u00ac\u0302\u0001\u0000\u0000"+
		"\u0000\u00ae\u0307\u0001\u0000\u0000\u0000\u00b0\u00b3\u0003\u0002\u0001"+
		"\u0000\u00b1\u00b3\u0003\u00a0P\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000"+
		"\u00b2\u00b1\u0001\u0000\u0000\u0000\u00b3\u0001\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b5\u00053\u0000\u0000\u00b5\u00b6\u0005\u0001\u0000\u0000\u00b6"+
		"\u00b8\u0003\u0004\u0002\u0000\u00b7\u00b9\u0003\b\u0004\u0000\u00b8\u00b7"+
		"\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000\u0000\u0000\u00b9\u00bb"+
		"\u0001\u0000\u0000\u0000\u00ba\u00bc\u0003\u0010\b\u0000\u00bb\u00ba\u0001"+
		"\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00be\u0001"+
		"\u0000\u0000\u0000\u00bd\u00bf\u0003\u0018\f\u0000\u00be\u00bd\u0001\u0000"+
		"\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c1\u0001\u0000"+
		"\u0000\u0000\u00c0\u00c2\u00030\u0018\u0000\u00c1\u00c0\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u00c4\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c5\u00032\u0019\u0000\u00c4\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5\u00cc\u0001\u0000\u0000\u0000"+
		"\u00c6\u00cb\u0003\u0096K\u0000\u00c7\u00cb\u0003\u0098L\u0000\u00c8\u00cb"+
		"\u0003\u009aM\u0000\u00c9\u00cb\u0003\u009cN\u0000\u00ca\u00c6\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c7\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c9\u0001\u0000\u0000\u0000\u00cb\u00ce\u0001\u0000"+
		"\u0000\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000"+
		"\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001\u0000"+
		"\u0000\u0000\u00cf\u00d1\u0003\u009eO\u0000\u00d0\u00cf\u0001\u0000\u0000"+
		"\u0000\u00d0\u00d1\u0001\u0000\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000"+
		"\u0000\u00d2\u00d3\u00054\u0000\u0000\u00d3\u0003\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d5\u00053\u0000\u0000\u00d5\u00d6\u0005\u0002\u0000\u0000\u00d6"+
		"\u00d7\u00056\u0000\u0000\u00d7\u00d8\u00054\u0000\u0000\u00d8\u0005\u0001"+
		"\u0000\u0000\u0000\u00d9\u00da\u0005\u0003\u0000\u0000\u00da\u00db\u0005"+
		"6\u0000\u0000\u00db\u0007\u0001\u0000\u0000\u0000\u00dc\u00dd\u00053\u0000"+
		"\u0000\u00dd\u00e1\u0005\u0004\u0000\u0000\u00de\u00e0\u0003\u0006\u0003"+
		"\u0000\u00df\u00de\u0001\u0000\u0000\u0000\u00e0\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e1\u00df\u0001\u0000\u0000\u0000\u00e1\u00e2\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e4\u0001\u0000\u0000\u0000\u00e3\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e5\u00054\u0000\u0000\u00e5\t\u0001\u0000\u0000\u0000"+
		"\u00e6\u00e7\u0005\u0005\u0000\u0000\u00e7\u00e8\u0003\f\u0006\u0000\u00e8"+
		"\u000b\u0001\u0000\u0000\u0000\u00e9\u00ea\u00056\u0000\u0000\u00ea\r"+
		"\u0001\u0000\u0000\u0000\u00eb\u00ed\u0003\f\u0006\u0000\u00ec\u00eb\u0001"+
		"\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000\u0000\u00ee\u00ec\u0001"+
		"\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f0\u00f2\u0003\n\u0005\u0000\u00f1\u00f0\u0001\u0000"+
		"\u0000\u0000\u00f2\u00f5\u0001\u0000\u0000\u0000\u00f3\u00f1\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\u000f\u0001\u0000"+
		"\u0000\u0000\u00f5\u00f3\u0001\u0000\u0000\u0000\u00f6\u00f7\u00053\u0000"+
		"\u0000\u00f7\u00f9\u0005\u0006\u0000\u0000\u00f8\u00fa\u0003\u000e\u0007"+
		"\u0000\u00f9\u00f8\u0001\u0000\u0000\u0000\u00fa\u00fb\u0001\u0000\u0000"+
		"\u0000\u00fb\u00f9\u0001\u0000\u0000\u0000\u00fb\u00fc\u0001\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0001\u0000\u0000\u0000\u00fd\u00fe\u00054\u0000\u0000"+
		"\u00fe\u0011\u0001\u0000\u0000\u0000\u00ff\u0100\u0005\u0005\u0000\u0000"+
		"\u0100\u0101\u0003\f\u0006\u0000\u0101\u0013\u0001\u0000\u0000\u0000\u0102"+
		"\u0103\u00056\u0000\u0000\u0103\u0015\u0001\u0000\u0000\u0000\u0104\u0106"+
		"\u0003\u0014\n\u0000\u0105\u0104\u0001\u0000\u0000\u0000\u0106\u0107\u0001"+
		"\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000\u0107\u0108\u0001"+
		"\u0000\u0000\u0000\u0108\u010c\u0001\u0000\u0000\u0000\u0109\u010b\u0003"+
		"\u0012\t\u0000\u010a\u0109\u0001\u0000\u0000\u0000\u010b\u010e\u0001\u0000"+
		"\u0000\u0000\u010c\u010a\u0001\u0000\u0000\u0000\u010c\u010d\u0001\u0000"+
		"\u0000\u0000\u010d\u0017\u0001\u0000\u0000\u0000\u010e\u010c\u0001\u0000"+
		"\u0000\u0000\u010f\u0110\u00053\u0000\u0000\u0110\u0112\u0005\u0007\u0000"+
		"\u0000\u0111\u0113\u0003\u0016\u000b\u0000\u0112\u0111\u0001\u0000\u0000"+
		"\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0112\u0001\u0000\u0000"+
		"\u0000\u0114\u0115\u0001\u0000\u0000\u0000\u0115\u0116\u0001\u0000\u0000"+
		"\u0000\u0116\u0117\u00054\u0000\u0000\u0117\u0019\u0001\u0000\u0000\u0000"+
		"\u0118\u0119\u00056\u0000\u0000\u0119\u001b\u0001\u0000\u0000\u0000\u011a"+
		"\u011b\u00056\u0000\u0000\u011b\u001d\u0001\u0000\u0000\u0000\u011c\u011d"+
		"\u0007\u0000\u0000\u0000\u011d\u001f\u0001\u0000\u0000\u0000\u011e\u0120"+
		"\u0003\u001e\u000f\u0000\u011f\u011e\u0001\u0000\u0000\u0000\u0120\u0121"+
		"\u0001\u0000\u0000\u0000\u0121\u011f\u0001\u0000\u0000\u0000\u0121\u0122"+
		"\u0001\u0000\u0000\u0000\u0122\u0123\u0001\u0000\u0000\u0000\u0123\u0124"+
		"\u0005\u0005\u0000\u0000\u0124\u0125\u0003\f\u0006\u0000\u0125!\u0001"+
		"\u0000\u0000\u0000\u0126\u0129\u0003\u001e\u000f\u0000\u0127\u0129\u0003"+
		"\u001c\u000e\u0000\u0128\u0126\u0001\u0000\u0000\u0000\u0128\u0127\u0001"+
		"\u0000\u0000\u0000\u0129#\u0001\u0000\u0000\u0000\u012a\u012e\u0003\u001a"+
		"\r\u0000\u012b\u012d\u0003\"\u0011\u0000\u012c\u012b\u0001\u0000\u0000"+
		"\u0000\u012d\u0130\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000\u0000"+
		"\u0000\u012e\u012f\u0001\u0000\u0000\u0000\u012f%\u0001\u0000\u0000\u0000"+
		"\u0130\u012e\u0001\u0000\u0000\u0000\u0131\u0135\u0003\u001a\r\u0000\u0132"+
		"\u0134\u0003 \u0010\u0000\u0133\u0132\u0001\u0000\u0000\u0000\u0134\u0137"+
		"\u0001\u0000\u0000\u0000\u0135\u0133\u0001\u0000\u0000\u0000\u0135\u0136"+
		"\u0001\u0000\u0000\u0000\u0136\'\u0001\u0000\u0000\u0000\u0137\u0135\u0001"+
		"\u0000\u0000\u0000\u0138\u0139\u00053\u0000\u0000\u0139\u013a\u0003$\u0012"+
		"\u0000\u013a\u013b\u00054\u0000\u0000\u013b\u013e\u0001\u0000\u0000\u0000"+
		"\u013c\u013e\u0003\u001e\u000f\u0000\u013d\u0138\u0001\u0000\u0000\u0000"+
		"\u013d\u013c\u0001\u0000\u0000\u0000\u013e)\u0001\u0000\u0000\u0000\u013f"+
		"\u0140\u00053\u0000\u0000\u0140\u0141\u0003&\u0013\u0000\u0141\u0142\u0005"+
		"4\u0000\u0000\u0142+\u0001\u0000\u0000\u0000\u0143\u0144\u00053\u0000"+
		"\u0000\u0144\u0145\u0005\b\u0000\u0000\u0145\u0146\u0003(\u0014\u0000"+
		"\u0146\u0147\u00054\u0000\u0000\u0147-\u0001\u0000\u0000\u0000\u0148\u014b"+
		"\u0003(\u0014\u0000\u0149\u014b\u0003,\u0016\u0000\u014a\u0148\u0001\u0000"+
		"\u0000\u0000\u014a\u0149\u0001\u0000\u0000\u0000\u014b/\u0001\u0000\u0000"+
		"\u0000\u014c\u014d\u00053\u0000\u0000\u014d\u014f\u0005\t\u0000\u0000"+
		"\u014e\u0150\u0003*\u0015\u0000\u014f\u014e\u0001\u0000\u0000\u0000\u0150"+
		"\u0151\u0001\u0000\u0000\u0000\u0151\u014f\u0001\u0000\u0000\u0000\u0151"+
		"\u0152\u0001\u0000\u0000\u0000\u0152\u0153\u0001\u0000\u0000\u0000\u0153"+
		"\u0154\u00054\u0000\u0000\u01541\u0001\u0000\u0000\u0000\u0155\u0156\u0005"+
		"3\u0000\u0000\u0156\u0158\u0005\n\u0000\u0000\u0157\u0159\u0003*\u0015"+
		"\u0000\u0158\u0157\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000"+
		"\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000\u0000"+
		"\u0000\u015b\u015c\u0001\u0000\u0000\u0000\u015c\u015d\u00054\u0000\u0000"+
		"\u015d3\u0001\u0000\u0000\u0000\u015e\u015f\u0007\u0001\u0000\u0000\u015f"+
		"5\u0001\u0000\u0000\u0000\u0160\u0161\u0007\u0002\u0000\u0000\u01617\u0001"+
		"\u0000\u0000\u0000\u0162\u0163\u0007\u0003\u0000\u0000\u01639\u0001\u0000"+
		"\u0000\u0000\u0164\u0165\u00058\u0000\u0000\u0165;\u0001\u0000\u0000\u0000"+
		"\u0166\u0167\u0005\u0016\u0000\u0000\u0167=\u0001\u0000\u0000\u0000\u0168"+
		"\u016b\u0003:\u001d\u0000\u0169\u016b\u0003<\u001e\u0000\u016a\u0168\u0001"+
		"\u0000\u0000\u0000\u016a\u0169\u0001\u0000\u0000\u0000\u016b?\u0001\u0000"+
		"\u0000\u0000\u016c\u016d\u0003:\u001d\u0000\u016dA\u0001\u0000\u0000\u0000"+
		"\u016e\u0172\u0003D\"\u0000\u016f\u0172\u0003(\u0014\u0000\u0170\u0172"+
		"\u0003>\u001f\u0000\u0171\u016e\u0001\u0000\u0000\u0000\u0171\u016f\u0001"+
		"\u0000\u0000\u0000\u0171\u0170\u0001\u0000\u0000\u0000\u0172C\u0001\u0000"+
		"\u0000\u0000\u0173\u0174\u00053\u0000\u0000\u0174\u0175\u00036\u001b\u0000"+
		"\u0175\u0176\u0003B!\u0000\u0176\u0177\u0003B!\u0000\u0177\u0178\u0005"+
		"4\u0000\u0000\u0178E\u0001\u0000\u0000\u0000\u0179\u017a\u00053\u0000"+
		"\u0000\u017a\u017b\u0005\u0015\u0000\u0000\u017b\u017c\u0003(\u0014\u0000"+
		"\u017c\u017d\u0003@ \u0000\u017d\u017e\u00054\u0000\u0000\u017eG\u0001"+
		"\u0000\u0000\u0000\u017f\u0180\u00053\u0000\u0000\u0180\u0181\u0005\u0015"+
		"\u0000\u0000\u0181\u0182\u0005\u0017\u0000\u0000\u0182\u0183\u0003B!\u0000"+
		"\u0183\u0184\u00054\u0000\u0000\u0184I\u0001\u0000\u0000\u0000\u0185\u0186"+
		"\u00053\u0000\u0000\u0186\u0187\u00038\u001c\u0000\u0187\u0188\u0003B"+
		"!\u0000\u0188\u0189\u0003B!\u0000\u0189\u018a\u00054\u0000\u0000\u018a"+
		"K\u0001\u0000\u0000\u0000\u018b\u018c\u00053\u0000\u0000\u018c\u018d\u0005"+
		"\b\u0000\u0000\u018d\u018e\u0003J%\u0000\u018e\u018f\u00054\u0000\u0000"+
		"\u018fM\u0001\u0000\u0000\u0000\u0190\u0191\u00053\u0000\u0000\u0191\u0192"+
		"\u00034\u001a\u0000\u0192\u0193\u0003(\u0014\u0000\u0193\u0194\u0003B"+
		"!\u0000\u0194\u0195\u00054\u0000\u0000\u0195O\u0001\u0000\u0000\u0000"+
		"\u0196\u019d\u0003b1\u0000\u0197\u019d\u0003d2\u0000\u0198\u019d\u0003"+
		".\u0017\u0000\u0199\u019d\u0003L&\u0000\u019a\u019d\u0003J%\u0000\u019b"+
		"\u019d\u0003j5\u0000\u019c\u0196\u0001\u0000\u0000\u0000\u019c\u0197\u0001"+
		"\u0000\u0000\u0000\u019c\u0198\u0001\u0000\u0000\u0000\u019c\u0199\u0001"+
		"\u0000\u0000\u0000\u019c\u019a\u0001\u0000\u0000\u0000\u019c\u019b\u0001"+
		"\u0000\u0000\u0000\u019dQ\u0001\u0000\u0000\u0000\u019e\u01a1\u0003^/"+
		"\u0000\u019f\u01a1\u0003h4\u0000\u01a0\u019e\u0001\u0000\u0000\u0000\u01a0"+
		"\u019f\u0001\u0000\u0000\u0000\u01a1S\u0001\u0000\u0000\u0000\u01a2\u01a3"+
		"\u00053\u0000\u0000\u01a3\u01a4\u0005\u0018\u0000\u0000\u01a4\u01a5\u0003"+
		"P(\u0000\u01a5\u01a6\u0003R)\u0000\u01a6\u01a7\u00054\u0000\u0000\u01a7"+
		"U\u0001\u0000\u0000\u0000\u01a8\u01a9\u00053\u0000\u0000\u01a9\u01aa\u0005"+
		"\u0019\u0000\u0000\u01aa\u01ab\u0003\u0086C\u0000\u01ab\u01ac\u0003T*"+
		"\u0000\u01ac\u01ad\u00054\u0000\u0000\u01adW\u0001\u0000\u0000\u0000\u01ae"+
		"\u01af\u00053\u0000\u0000\u01af\u01b0\u0005\u0019\u0000\u0000\u01b0\u01b5"+
		"\u0003\u0086C\u0000\u01b1\u01b6\u0003X,\u0000\u01b2\u01b6\u0003Z-\u0000"+
		"\u01b3\u01b6\u0003b1\u0000\u01b4\u01b6\u0003d2\u0000\u01b5\u01b1\u0001"+
		"\u0000\u0000\u0000\u01b5\u01b2\u0001\u0000\u0000\u0000\u01b5\u01b3\u0001"+
		"\u0000\u0000\u0000\u01b5\u01b4\u0001\u0000\u0000\u0000\u01b6\u01b7\u0001"+
		"\u0000\u0000\u0000\u01b7\u01b8\u00054\u0000\u0000\u01b8Y\u0001\u0000\u0000"+
		"\u0000\u01b9\u01ba\u00053\u0000\u0000\u01ba\u01bb\u0005\u001a\u0000\u0000"+
		"\u01bb\u01c0\u0003\u0086C\u0000\u01bc\u01c1\u0003X,\u0000\u01bd\u01c1"+
		"\u0003Z-\u0000\u01be\u01c1\u0003b1\u0000\u01bf\u01c1\u0003d2\u0000\u01c0"+
		"\u01bc\u0001\u0000\u0000\u0000\u01c0\u01bd\u0001\u0000\u0000\u0000\u01c0"+
		"\u01be\u0001\u0000\u0000\u0000\u01c0\u01bf\u0001\u0000\u0000\u0000\u01c1"+
		"\u01c2\u0001\u0000\u0000\u0000\u01c2\u01c3\u00054\u0000\u0000\u01c3[\u0001"+
		"\u0000\u0000\u0000\u01c4\u01c9\u0003.\u0017\u0000\u01c5\u01c9\u0003N\'"+
		"\u0000\u01c6\u01c9\u0003T*\u0000\u01c7\u01c9\u0003V+\u0000\u01c8\u01c4"+
		"\u0001\u0000\u0000\u0000\u01c8\u01c5\u0001\u0000\u0000\u0000\u01c8\u01c6"+
		"\u0001\u0000\u0000\u0000\u01c8\u01c7\u0001\u0000\u0000\u0000\u01c9]\u0001"+
		"\u0000\u0000\u0000\u01ca\u01cd\u0003.\u0017\u0000\u01cb\u01cd\u0003N\'"+
		"\u0000\u01cc\u01ca\u0001\u0000\u0000\u0000\u01cc\u01cb\u0001\u0000\u0000"+
		"\u0000\u01cd_\u0001\u0000\u0000\u0000\u01ce\u01cf\u00053\u0000\u0000\u01cf"+
		"\u01d0\u0005\b\u0000\u0000\u01d0\u01d1\u00053\u0000\u0000\u01d1\u01d2"+
		"\u0005\u0015\u0000\u0000\u01d2\u01d3\u0003\u001e\u000f\u0000\u01d3\u01d4"+
		"\u0003\u001e\u000f\u0000\u01d4\u01d5\u00054\u0000\u0000\u01d5\u01d6\u0005"+
		"4\u0000\u0000\u01d6a\u0001\u0000\u0000\u0000\u01d7\u01d8\u00053\u0000"+
		"\u0000\u01d8\u01df\u0005\u001b\u0000\u0000\u01d9\u01e0\u0003b1\u0000\u01da"+
		"\u01e0\u0003d2\u0000\u01db\u01e0\u0003`0\u0000\u01dc\u01e0\u0003.\u0017"+
		"\u0000\u01dd\u01e0\u0003L&\u0000\u01de\u01e0\u0003J%\u0000\u01df\u01d9"+
		"\u0001\u0000\u0000\u0000\u01df\u01da\u0001\u0000\u0000\u0000\u01df\u01db"+
		"\u0001\u0000\u0000\u0000\u01df\u01dc\u0001\u0000\u0000\u0000\u01df\u01dd"+
		"\u0001\u0000\u0000\u0000\u01df\u01de\u0001\u0000\u0000\u0000\u01e0\u01e1"+
		"\u0001\u0000\u0000\u0000\u01e1\u01df\u0001\u0000\u0000\u0000\u01e1\u01e2"+
		"\u0001\u0000\u0000\u0000\u01e2\u01e3\u0001\u0000\u0000\u0000\u01e3\u01e4"+
		"\u00054\u0000\u0000\u01e4c\u0001\u0000\u0000\u0000\u01e5\u01e6\u00053"+
		"\u0000\u0000\u01e6\u01ed\u0005\u001c\u0000\u0000\u01e7\u01ee\u0003b1\u0000"+
		"\u01e8\u01ee\u0003d2\u0000\u01e9\u01ee\u0003`0\u0000\u01ea\u01ee\u0003"+
		".\u0017\u0000\u01eb\u01ee\u0003L&\u0000\u01ec\u01ee\u0003J%\u0000\u01ed"+
		"\u01e7\u0001\u0000\u0000\u0000\u01ed\u01e8\u0001\u0000\u0000\u0000\u01ed"+
		"\u01e9\u0001\u0000\u0000\u0000\u01ed\u01ea\u0001\u0000\u0000\u0000\u01ed"+
		"\u01eb\u0001\u0000\u0000\u0000\u01ed\u01ec\u0001\u0000\u0000\u0000\u01ee"+
		"\u01ef\u0001\u0000\u0000\u0000\u01ef\u01ed\u0001\u0000\u0000\u0000\u01ef"+
		"\u01f0\u0001\u0000\u0000\u0000\u01f0\u01f1\u0001\u0000\u0000\u0000\u01f1"+
		"\u01f2\u00054\u0000\u0000\u01f2e\u0001\u0000\u0000\u0000\u01f3\u01f4\u0005"+
		"3\u0000\u0000\u01f4\u01f6\u0005\u001b\u0000\u0000\u01f5\u01f7\u0003\\"+
		".\u0000\u01f6\u01f5\u0001\u0000\u0000\u0000\u01f7\u01f8\u0001\u0000\u0000"+
		"\u0000\u01f8\u01f6\u0001\u0000\u0000\u0000\u01f8\u01f9\u0001\u0000\u0000"+
		"\u0000\u01f9\u01fa\u0001\u0000\u0000\u0000\u01fa\u01fb\u00054\u0000\u0000"+
		"\u01fbg\u0001\u0000\u0000\u0000\u01fc\u01fd\u00053\u0000\u0000\u01fd\u01ff"+
		"\u0005\u001b\u0000\u0000\u01fe\u0200\u0003^/\u0000\u01ff\u01fe\u0001\u0000"+
		"\u0000\u0000\u0200\u0201\u0001\u0000\u0000\u0000\u0201\u01ff\u0001\u0000"+
		"\u0000\u0000\u0201\u0202\u0001\u0000\u0000\u0000\u0202\u0203\u0001\u0000"+
		"\u0000\u0000\u0203\u0204\u00054\u0000\u0000\u0204i\u0001\u0000\u0000\u0000"+
		"\u0205\u0206\u00053\u0000\u0000\u0206\u0207\u00054\u0000\u0000\u0207k"+
		"\u0001\u0000\u0000\u0000\u0208\u020f\u0003b1\u0000\u0209\u020f\u0003d"+
		"2\u0000\u020a\u020f\u0003.\u0017\u0000\u020b\u020f\u0003L&\u0000\u020c"+
		"\u020f\u0003J%\u0000\u020d\u020f\u0003j5\u0000\u020e\u0208\u0001\u0000"+
		"\u0000\u0000\u020e\u0209\u0001\u0000\u0000\u0000\u020e\u020a\u0001\u0000"+
		"\u0000\u0000\u020e\u020b\u0001\u0000\u0000\u0000\u020e\u020c\u0001\u0000"+
		"\u0000\u0000\u020e\u020d\u0001\u0000\u0000\u0000\u020fm\u0001\u0000\u0000"+
		"\u0000\u0210\u0213\u0003\\.\u0000\u0211\u0213\u0003f3\u0000\u0212\u0210"+
		"\u0001\u0000\u0000\u0000\u0212\u0211\u0001\u0000\u0000\u0000\u0213o\u0001"+
		"\u0000\u0000\u0000\u0214\u0215\u00053\u0000\u0000\u0215\u0219\u0005\u001b"+
		"\u0000\u0000\u0216\u021a\u0003r9\u0000\u0217\u021a\u0003t:\u0000\u0218"+
		"\u021a\u0003v;\u0000\u0219\u0216\u0001\u0000\u0000\u0000\u0219\u0217\u0001"+
		"\u0000\u0000\u0000\u0219\u0218\u0001\u0000\u0000\u0000\u021a\u021b\u0001"+
		"\u0000\u0000\u0000\u021b\u0219\u0001\u0000\u0000\u0000\u021b\u021c\u0001"+
		"\u0000\u0000\u0000\u021c\u021d\u0001\u0000\u0000\u0000\u021d\u021e\u0005"+
		"4\u0000\u0000\u021eq\u0001\u0000\u0000\u0000\u021f\u0220\u00053\u0000"+
		"\u0000\u0220\u0225\u0005\u001d\u0000\u0000\u0221\u0226\u0003.\u0017\u0000"+
		"\u0222\u0226\u0003L&\u0000\u0223\u0226\u0003J%\u0000\u0224\u0226\u0003"+
		"b1\u0000\u0225\u0221\u0001\u0000\u0000\u0000\u0225\u0222\u0001\u0000\u0000"+
		"\u0000\u0225\u0223\u0001\u0000\u0000\u0000\u0225\u0224\u0001\u0000\u0000"+
		"\u0000\u0226\u0227\u0001\u0000\u0000\u0000\u0227\u0228\u00054\u0000\u0000"+
		"\u0228s\u0001\u0000\u0000\u0000\u0229\u022a\u00053\u0000\u0000\u022a\u022f"+
		"\u0005\u001e\u0000\u0000\u022b\u0230\u0003.\u0017\u0000\u022c\u0230\u0003"+
		"L&\u0000\u022d\u0230\u0003J%\u0000\u022e\u0230\u0003b1\u0000\u022f\u022b"+
		"\u0001\u0000\u0000\u0000\u022f\u022c\u0001\u0000\u0000\u0000\u022f\u022d"+
		"\u0001\u0000\u0000\u0000\u022f\u022e\u0001\u0000\u0000\u0000\u0230\u0231"+
		"\u0001\u0000\u0000\u0000\u0231\u0232\u00054\u0000\u0000\u0232u\u0001\u0000"+
		"\u0000\u0000\u0233\u0234\u00053\u0000\u0000\u0234\u0239\u0005\u001f\u0000"+
		"\u0000\u0235\u023a\u0003.\u0017\u0000\u0236\u023a\u0003L&\u0000\u0237"+
		"\u023a\u0003J%\u0000\u0238\u023a\u0003b1\u0000\u0239\u0235\u0001\u0000"+
		"\u0000\u0000\u0239\u0236\u0001\u0000\u0000\u0000\u0239\u0237\u0001\u0000"+
		"\u0000\u0000\u0239\u0238\u0001\u0000\u0000\u0000\u023a\u023b\u0001\u0000"+
		"\u0000\u0000\u023b\u023c\u00054\u0000\u0000\u023cw\u0001\u0000\u0000\u0000"+
		"\u023d\u0243\u0003p8\u0000\u023e\u0243\u0003r9\u0000\u023f\u0243\u0003"+
		"t:\u0000\u0240\u0243\u0003v;\u0000\u0241\u0243\u0003j5\u0000\u0242\u023d"+
		"\u0001\u0000\u0000\u0000\u0242\u023e\u0001\u0000\u0000\u0000\u0242\u023f"+
		"\u0001\u0000\u0000\u0000\u0242\u0240\u0001\u0000\u0000\u0000\u0242\u0241"+
		"\u0001\u0000\u0000\u0000\u0243y\u0001\u0000\u0000\u0000\u0244\u0245\u0005"+
		"3\u0000\u0000\u0245\u0249\u0005\u001d\u0000\u0000\u0246\u024a\u0003.\u0017"+
		"\u0000\u0247\u024a\u0003N\'\u0000\u0248\u024a\u0003f3\u0000\u0249\u0246"+
		"\u0001\u0000\u0000\u0000\u0249\u0247\u0001\u0000\u0000\u0000\u0249\u0248"+
		"\u0001\u0000\u0000\u0000\u024a\u024b\u0001\u0000\u0000\u0000\u024b\u024c"+
		"\u00054\u0000\u0000\u024c{\u0001\u0000\u0000\u0000\u024d\u024e\u00053"+
		"\u0000\u0000\u024e\u0252\u0005 \u0000\u0000\u024f\u0253\u0003.\u0017\u0000"+
		"\u0250\u0253\u0003N\'\u0000\u0251\u0253\u0003f3\u0000\u0252\u024f\u0001"+
		"\u0000\u0000\u0000\u0252\u0250\u0001\u0000\u0000\u0000\u0252\u0251\u0001"+
		"\u0000\u0000\u0000\u0253\u0254\u0001\u0000\u0000\u0000\u0254\u0255\u0005"+
		"4\u0000\u0000\u0255}\u0001\u0000\u0000\u0000\u0256\u0257\u00053\u0000"+
		"\u0000\u0257\u025b\u0005\u001f\u0000\u0000\u0258\u025c\u0003.\u0017\u0000"+
		"\u0259\u025c\u0003N\'\u0000\u025a\u025c\u0003f3\u0000\u025b\u0258\u0001"+
		"\u0000\u0000\u0000\u025b\u0259\u0001\u0000\u0000\u0000\u025b\u025a\u0001"+
		"\u0000\u0000\u0000\u025c\u025d\u0001\u0000\u0000\u0000\u025d\u025e\u0005"+
		"4\u0000\u0000\u025e\u007f\u0001\u0000\u0000\u0000\u025f\u0263\u0003z="+
		"\u0000\u0260\u0263\u0003|>\u0000\u0261\u0263\u0003~?\u0000\u0262\u025f"+
		"\u0001\u0000\u0000\u0000\u0262\u0260\u0001\u0000\u0000\u0000\u0262\u0261"+
		"\u0001\u0000\u0000\u0000\u0263\u0081\u0001\u0000\u0000\u0000\u0264\u0265"+
		"\u00053\u0000\u0000\u0265\u0267\u0005\u001b\u0000\u0000\u0266\u0268\u0003"+
		"\u0080@\u0000\u0267\u0266\u0001\u0000\u0000\u0000\u0268\u0269\u0001\u0000"+
		"\u0000\u0000\u0269\u0267\u0001\u0000\u0000\u0000\u0269\u026a\u0001\u0000"+
		"\u0000\u0000\u026a\u026b\u0001\u0000\u0000\u0000\u026b\u026c\u00054\u0000"+
		"\u0000\u026c\u0083\u0001\u0000\u0000\u0000\u026d\u0270\u0003\u0080@\u0000"+
		"\u026e\u0270\u0003\u0082A\u0000\u026f\u026d\u0001\u0000\u0000\u0000\u026f"+
		"\u026e\u0001\u0000\u0000\u0000\u0270\u0085\u0001\u0000\u0000\u0000\u0271"+
		"\u0275\u00053\u0000\u0000\u0272\u0274\u0003 \u0010\u0000\u0273\u0272\u0001"+
		"\u0000\u0000\u0000\u0274\u0277\u0001\u0000\u0000\u0000\u0275\u0273\u0001"+
		"\u0000\u0000\u0000\u0275\u0276\u0001\u0000\u0000\u0000\u0276\u0278\u0001"+
		"\u0000\u0000\u0000\u0277\u0275\u0001\u0000\u0000\u0000\u0278\u0279\u0005"+
		"4\u0000\u0000\u0279\u0087\u0001\u0000\u0000\u0000\u027a\u027b\u00056\u0000"+
		"\u0000\u027b\u0089\u0001\u0000\u0000\u0000\u027c\u027d\u0005!\u0000\u0000"+
		"\u027d\u027e\u0003\u0086C\u0000\u027e\u008b\u0001\u0000\u0000\u0000\u027f"+
		"\u0280\u0005\"\u0000\u0000\u0280\u0281\u0003l6\u0000\u0281\u008d\u0001"+
		"\u0000\u0000\u0000\u0282\u0283\u0005#\u0000\u0000\u0283\u0284\u0003x<"+
		"\u0000\u0284\u008f\u0001\u0000\u0000\u0000\u0285\u0286\u0005$\u0000\u0000"+
		"\u0286\u0287\u0003n7\u0000\u0287\u0091\u0001\u0000\u0000\u0000\u0288\u0289"+
		"\u0005$\u0000\u0000\u0289\u028a\u0003\u0084B\u0000\u028a\u0093\u0001\u0000"+
		"\u0000\u0000\u028b\u028c\u0005%\u0000\u0000\u028c\u028d\u0003H$\u0000"+
		"\u028d\u0095\u0001\u0000\u0000\u0000\u028e\u028f\u00053\u0000\u0000\u028f"+
		"\u0290\u0005&\u0000\u0000\u0290\u0292\u0003\u0088D\u0000\u0291\u0293\u0003"+
		"\u008aE\u0000\u0292\u0291\u0001\u0000\u0000\u0000\u0292\u0293\u0001\u0000"+
		"\u0000\u0000\u0293\u0295\u0001\u0000\u0000\u0000\u0294\u0296\u0003\u008c"+
		"F\u0000\u0295\u0294\u0001\u0000\u0000\u0000\u0295\u0296\u0001\u0000\u0000"+
		"\u0000\u0296\u0297\u0001\u0000\u0000\u0000\u0297\u0298\u0003\u0090H\u0000"+
		"\u0298\u0299\u00054\u0000\u0000\u0299\u0097\u0001\u0000\u0000\u0000\u029a"+
		"\u029b\u00053\u0000\u0000\u029b\u029c\u0005\'\u0000\u0000\u029c\u029e"+
		"\u0003\u0088D\u0000\u029d\u029f\u0003\u008aE\u0000\u029e\u029d\u0001\u0000"+
		"\u0000\u0000\u029e\u029f\u0001\u0000\u0000\u0000\u029f\u02a1\u0001\u0000"+
		"\u0000\u0000\u02a0\u02a2\u0003\u0094J\u0000\u02a1\u02a0\u0001\u0000\u0000"+
		"\u0000\u02a1\u02a2\u0001\u0000\u0000\u0000\u02a2\u02a4\u0001\u0000\u0000"+
		"\u0000\u02a3\u02a5\u0003\u008eG\u0000\u02a4\u02a3\u0001\u0000\u0000\u0000"+
		"\u02a4\u02a5\u0001\u0000\u0000\u0000\u02a5\u02a6\u0001\u0000\u0000\u0000"+
		"\u02a6\u02a7\u0003\u0092I\u0000\u02a7\u02a8\u00054\u0000\u0000\u02a8\u0099"+
		"\u0001\u0000\u0000\u0000\u02a9\u02aa\u00053\u0000\u0000\u02aa\u02ab\u0005"+
		"(\u0000\u0000\u02ab\u02ad\u0003\u0088D\u0000\u02ac\u02ae\u0003\u008aE"+
		"\u0000\u02ad\u02ac\u0001\u0000\u0000\u0000\u02ad\u02ae\u0001\u0000\u0000"+
		"\u0000\u02ae\u02b0\u0001\u0000\u0000\u0000\u02af\u02b1\u0003\u008cF\u0000"+
		"\u02b0\u02af\u0001\u0000\u0000\u0000\u02b0\u02b1\u0001\u0000\u0000\u0000"+
		"\u02b1\u02b2\u0001\u0000\u0000\u0000\u02b2\u02b3\u0003\u0090H\u0000\u02b3"+
		"\u02b4\u00054\u0000\u0000\u02b4\u009b\u0001\u0000\u0000\u0000\u02b5\u02b6"+
		"\u00053\u0000\u0000\u02b6\u02b7\u0005)\u0000\u0000\u02b7\u02b9\u0003\u0088"+
		"D\u0000\u02b8\u02ba\u0003\u008aE\u0000\u02b9\u02b8\u0001\u0000\u0000\u0000"+
		"\u02b9\u02ba\u0001\u0000\u0000\u0000\u02ba\u02bc\u0001\u0000\u0000\u0000"+
		"\u02bb\u02bd\u0003\u008cF\u0000\u02bc\u02bb\u0001\u0000\u0000\u0000\u02bc"+
		"\u02bd\u0001\u0000\u0000\u0000\u02bd\u02be\u0001\u0000\u0000\u0000\u02be"+
		"\u02bf\u0003\u0090H\u0000\u02bf\u02c0\u00054\u0000\u0000\u02c0\u009d\u0001"+
		"\u0000\u0000\u0000\u02c1\u02c2\u00053\u0000\u0000\u02c2\u02c3\u0005*\u0000"+
		"\u0000\u02c3\u02c4\u00053\u0000\u0000\u02c4\u02c7\u0005\u001b\u0000\u0000"+
		"\u02c5\u02c8\u0003X,\u0000\u02c6\u02c8\u0003Z-\u0000\u02c7\u02c5\u0001"+
		"\u0000\u0000\u0000\u02c7\u02c6\u0001\u0000\u0000\u0000\u02c8\u02c9\u0001"+
		"\u0000\u0000\u0000\u02c9\u02c7\u0001\u0000\u0000\u0000\u02c9\u02ca\u0001"+
		"\u0000\u0000\u0000\u02ca\u02cb\u0001\u0000\u0000\u0000\u02cb\u02cc\u0005"+
		"4\u0000\u0000\u02cc\u02cd\u00054\u0000\u0000\u02cd\u009f\u0001\u0000\u0000"+
		"\u0000\u02ce\u02cf\u00053\u0000\u0000\u02cf\u02d0\u0005\u0001\u0000\u0000"+
		"\u02d0\u02d1\u0003\u00a2Q\u0000\u02d1\u02d3\u0003\u00a4R\u0000\u02d2\u02d4"+
		"\u0003\u00a8T\u0000\u02d3\u02d2\u0001\u0000\u0000\u0000\u02d3\u02d4\u0001"+
		"\u0000\u0000\u0000\u02d4\u02d5\u0001\u0000\u0000\u0000\u02d5\u02d6\u0003"+
		"\u00aaU\u0000\u02d6\u02d8\u0003\u00acV\u0000\u02d7\u02d9\u0003\u00aeW"+
		"\u0000\u02d8\u02d7\u0001\u0000\u0000\u0000\u02d8\u02d9\u0001\u0000\u0000"+
		"\u0000\u02d9\u02da\u0001\u0000\u0000\u0000\u02da\u02db\u00054\u0000\u0000"+
		"\u02db\u00a1\u0001\u0000\u0000\u0000\u02dc\u02dd\u00053\u0000\u0000\u02dd"+
		"\u02de\u0005+\u0000\u0000\u02de\u02df\u00056\u0000\u0000\u02df\u02e0\u0005"+
		"4\u0000\u0000\u02e0\u00a3\u0001\u0000\u0000\u0000\u02e1\u02e2\u00053\u0000"+
		"\u0000\u02e2\u02e3\u0005,\u0000\u0000\u02e3\u02e4\u00056\u0000\u0000\u02e4"+
		"\u02e5\u00054\u0000\u0000\u02e5\u00a5\u0001\u0000\u0000\u0000\u02e6\u02e8"+
		"\u0003\u001c\u000e\u0000\u02e7\u02e6\u0001\u0000\u0000\u0000\u02e8\u02e9"+
		"\u0001\u0000\u0000\u0000\u02e9\u02e7\u0001\u0000\u0000\u0000\u02e9\u02ea"+
		"\u0001\u0000\u0000\u0000\u02ea\u02eb\u0001\u0000\u0000\u0000\u02eb\u02ec"+
		"\u0005\u0005\u0000\u0000\u02ec\u02ed\u0003\f\u0006\u0000\u02ed\u00a7\u0001"+
		"\u0000\u0000\u0000\u02ee\u02ef\u00053\u0000\u0000\u02ef\u02f3\u0005-\u0000"+
		"\u0000\u02f0\u02f2\u0003\u00a6S\u0000\u02f1\u02f0\u0001\u0000\u0000\u0000"+
		"\u02f2\u02f5\u0001\u0000\u0000\u0000\u02f3\u02f1\u0001\u0000\u0000\u0000"+
		"\u02f3\u02f4\u0001\u0000\u0000\u0000\u02f4\u02f6\u0001\u0000\u0000\u0000"+
		"\u02f5\u02f3\u0001\u0000\u0000\u0000\u02f6\u02f7\u00054\u0000\u0000\u02f7"+
		"\u00a9\u0001\u0000\u0000\u0000\u02f8\u02f9\u00053\u0000\u0000\u02f9\u02fc"+
		"\u0005.\u0000\u0000\u02fa\u02fd\u0003(\u0014\u0000\u02fb\u02fd\u0003F"+
		"#\u0000\u02fc\u02fa\u0001\u0000\u0000\u0000\u02fc\u02fb\u0001\u0000\u0000"+
		"\u0000\u02fd\u02fe\u0001\u0000\u0000\u0000\u02fe\u02fc\u0001\u0000\u0000"+
		"\u0000\u02fe\u02ff\u0001\u0000\u0000\u0000\u02ff\u0300\u0001\u0000\u0000"+
		"\u0000\u0300\u0301\u00054\u0000\u0000\u0301\u00ab\u0001\u0000\u0000\u0000"+
		"\u0302\u0303\u00053\u0000\u0000\u0303\u0304\u0005/\u0000\u0000\u0304\u0305"+
		"\u0003l6\u0000\u0305\u0306\u00054\u0000\u0000\u0306\u00ad\u0001\u0000"+
		"\u0000\u0000\u0307\u0308\u00053\u0000\u0000\u0308\u0309\u00050\u0000\u0000"+
		"\u0309\u030a\u0007\u0004\u0000\u0000\u030a\u030b\u0003B!\u0000\u030b\u030c"+
		"\u00054\u0000\u0000\u030c\u00af\u0001\u0000\u0000\u0000F\u00b2\u00b8\u00bb"+
		"\u00be\u00c1\u00c4\u00ca\u00cc\u00d0\u00e1\u00ee\u00f3\u00fb\u0107\u010c"+
		"\u0114\u0121\u0128\u012e\u0135\u013d\u014a\u0151\u015a\u016a\u0171\u019c"+
		"\u01a0\u01b5\u01c0\u01c8\u01cc\u01df\u01e1\u01ed\u01ef\u01f8\u0201\u020e"+
		"\u0212\u0219\u021b\u0225\u022f\u0239\u0242\u0249\u0252\u025b\u0262\u0269"+
		"\u026f\u0275\u0292\u0295\u029e\u02a1\u02a4\u02ad\u02b0\u02b9\u02bc\u02c7"+
		"\u02c9\u02d3\u02d8\u02e9\u02f3\u02fc\u02fe";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}