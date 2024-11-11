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
		T__45=46, LP=47, RP=48, VAR=49, NAME=50, VARIABLE=51, NUMBER=52, WS=53;
	public static final int
		RULE_pddlDoc = 0, RULE_domain = 1, RULE_domainName = 2, RULE_requireKey = 3, 
		RULE_requirements = 4, RULE_parentType = 5, RULE_typeName = 6, RULE_type = 7, 
		RULE_types = 8, RULE_atomName = 9, RULE_groundAtomParameter = 10, RULE_liftedAtomParameter = 11, 
		RULE_typedAtomParameter = 12, RULE_atomParameter = 13, RULE_atom = 14, 
		RULE_typedAtom = 15, RULE_positiveLiteral = 16, RULE_typedPositiveLiteral = 17, 
		RULE_negativeLiteral = 18, RULE_booleanLiteral = 19, RULE_predicates = 20, 
		RULE_functions = 21, RULE_modificator = 22, RULE_operator = 23, RULE_comparator = 24, 
		RULE_number = 25, RULE_delta = 26, RULE_constant = 27, RULE_assignmentSide = 28, 
		RULE_operationSide = 29, RULE_operation = 30, RULE_assignment = 31, RULE_durationAssignment = 32, 
		RULE_comparation = 33, RULE_negatedComparation = 34, RULE_modification = 35, 
		RULE_ceCond = 36, RULE_ceEff = 37, RULE_ce = 38, RULE_effect = 39, RULE_effectNoCes = 40, 
		RULE_andClause = 41, RULE_orClause = 42, RULE_andEffect = 43, RULE_andEffectNoCes = 44, 
		RULE_emptyPrecondition = 45, RULE_preconditions = 46, RULE_effects = 47, 
		RULE_andDurClause = 48, RULE_atStartPre = 49, RULE_overAllPre = 50, RULE_atEndPre = 51, 
		RULE_durativeConditions = 52, RULE_atStartEffect = 53, RULE_overAllEffect = 54, 
		RULE_atEndEffect = 55, RULE_durativeEffect = 56, RULE_andDurativeEffect = 57, 
		RULE_durativeEffects = 58, RULE_parameters = 59, RULE_opName = 60, RULE_opParameters = 61, 
		RULE_opPrecondition = 62, RULE_opDurativeCondition = 63, RULE_opEffect = 64, 
		RULE_opDurativeEffect = 65, RULE_opDuration = 66, RULE_action = 67, RULE_durativeAction = 68, 
		RULE_event = 69, RULE_process = 70, RULE_problem = 71, RULE_problemName = 72, 
		RULE_problemDomain = 73, RULE_typedObjects = 74, RULE_objects = 75, RULE_init = 76, 
		RULE_goal = 77, RULE_metric = 78;
	private static String[] makeRuleNames() {
		return new String[] {
			"pddlDoc", "domain", "domainName", "requireKey", "requirements", "parentType", 
			"typeName", "type", "types", "atomName", "groundAtomParameter", "liftedAtomParameter", 
			"typedAtomParameter", "atomParameter", "atom", "typedAtom", "positiveLiteral", 
			"typedPositiveLiteral", "negativeLiteral", "booleanLiteral", "predicates", 
			"functions", "modificator", "operator", "comparator", "number", "delta", 
			"constant", "assignmentSide", "operationSide", "operation", "assignment", 
			"durationAssignment", "comparation", "negatedComparation", "modification", 
			"ceCond", "ceEff", "ce", "effect", "effectNoCes", "andClause", "orClause", 
			"andEffect", "andEffectNoCes", "emptyPrecondition", "preconditions", 
			"effects", "andDurClause", "atStartPre", "overAllPre", "atEndPre", "durativeConditions", 
			"atStartEffect", "overAllEffect", "atEndEffect", "durativeEffect", "andDurativeEffect", 
			"durativeEffects", "parameters", "opName", "opParameters", "opPrecondition", 
			"opDurativeCondition", "opEffect", "opDurativeEffect", "opDuration", 
			"action", "durativeAction", "event", "process", "problem", "problemName", 
			"problemDomain", "typedObjects", "objects", "init", "goal", "metric"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'define'", "'domain'", "':'", "':requirements'", "'-'", "':types'", 
			"'not'", "':predicates'", "':functions'", "'assign'", "'increase'", "'decrease'", 
			"'+'", "'*'", "'/'", "'>'", "'>='", "'<='", "'<'", "'='", "'#t'", "'?duration'", 
			"'when'", "'and'", "'or'", "'at start'", "'over all'", "'at end'", "'overall'", 
			"':parameters'", "':precondition'", "':condition'", "':effect'", "':duration'", 
			"':action'", "':durative-action'", "':event'", "':process'", "'problem'", 
			"':domain'", "':objects'", "':init'", "':goal'", "':metric'", "'maximize'", 
			"'minimize'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "LP", 
			"RP", "VAR", "NAME", "VARIABLE", "NUMBER", "WS"
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
			setState(160);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				domain();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(LP);
			setState(163);
			match(T__0);
			setState(164);
			domainName();
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(165);
				requirements();
				}
				break;
			}
			setState(169);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(168);
				types();
				}
				break;
			}
			setState(172);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(171);
				predicates();
				}
				break;
			}
			setState(175);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(174);
				functions();
				}
				break;
			}
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LP) {
				{
				setState(181);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(177);
					action();
					}
					break;
				case 2:
					{
					setState(178);
					durativeAction();
					}
					break;
				case 3:
					{
					setState(179);
					event();
					}
					break;
				case 4:
					{
					setState(180);
					process();
					}
					break;
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(186);
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
			setState(188);
			match(LP);
			setState(189);
			match(T__1);
			setState(190);
			match(NAME);
			setState(191);
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
			setState(193);
			match(T__2);
			setState(194);
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
			setState(196);
			match(LP);
			setState(197);
			match(T__3);
			setState(201);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(198);
				requireKey();
				}
				}
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(204);
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
			setState(206);
			match(T__4);
			setState(207);
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
			setState(209);
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
			setState(212); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(211);
					typeName();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(214); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(219);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(216);
				((TypeContext)_localctx).parent = parentType();
				}
				}
				setState(221);
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
			setState(222);
			match(LP);
			setState(223);
			match(T__5);
			setState(225); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(224);
				type();
				}
				}
				setState(227); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(229);
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
		enterRule(_localctx, 18, RULE_atomName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
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
		enterRule(_localctx, 20, RULE_groundAtomParameter);
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
	public static class LiftedAtomParameterContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(pddlParser.VAR, 0); }
		public LiftedAtomParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_liftedAtomParameter; }
	}

	public final LiftedAtomParameterContext liftedAtomParameter() throws RecognitionException {
		LiftedAtomParameterContext _localctx = new LiftedAtomParameterContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_liftedAtomParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(VAR);
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
		enterRule(_localctx, 24, RULE_typedAtomParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(237);
				liftedAtomParameter();
				}
				}
				setState(240); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VAR );
			setState(242);
			match(T__4);
			setState(243);
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
		enterRule(_localctx, 26, RULE_atomParameter);
		try {
			setState(247);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(245);
				liftedAtomParameter();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(246);
				groundAtomParameter();
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
		enterRule(_localctx, 28, RULE_atom);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			atomName();
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==NAME) {
				{
				{
				setState(250);
				atomParameter();
				}
				}
				setState(255);
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
		enterRule(_localctx, 30, RULE_typedAtom);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			atomName();
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(257);
				typedAtomParameter();
				}
				}
				setState(262);
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
		enterRule(_localctx, 32, RULE_positiveLiteral);
		try {
			setState(268);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(263);
				match(LP);
				setState(264);
				atom();
				setState(265);
				match(RP);
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(267);
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
		enterRule(_localctx, 34, RULE_typedPositiveLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(LP);
			setState(271);
			typedAtom();
			setState(272);
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
		enterRule(_localctx, 36, RULE_negativeLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			match(LP);
			setState(275);
			match(T__6);
			setState(276);
			positiveLiteral();
			setState(277);
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
		enterRule(_localctx, 38, RULE_booleanLiteral);
		try {
			setState(281);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(279);
				positiveLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(280);
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
		enterRule(_localctx, 40, RULE_predicates);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(LP);
			setState(284);
			match(T__7);
			setState(286); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(285);
				typedPositiveLiteral();
				}
				}
				setState(288); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(290);
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
		enterRule(_localctx, 42, RULE_functions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(LP);
			setState(293);
			match(T__8);
			setState(295); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(294);
				typedPositiveLiteral();
				}
				}
				setState(297); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(299);
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
		enterRule(_localctx, 44, RULE_modificator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(301);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7168L) != 0)) ) {
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
		enterRule(_localctx, 46, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 57376L) != 0)) ) {
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
		enterRule(_localctx, 48, RULE_comparator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(305);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2031616L) != 0)) ) {
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
		enterRule(_localctx, 50, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
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
		enterRule(_localctx, 52, RULE_delta);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(T__20);
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
		enterRule(_localctx, 54, RULE_constant);
		try {
			setState(313);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				number();
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 2);
				{
				setState(312);
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
		enterRule(_localctx, 56, RULE_assignmentSide);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
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
		enterRule(_localctx, 58, RULE_operationSide);
		try {
			setState(320);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(317);
				operation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(318);
				positiveLiteral();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(319);
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
		enterRule(_localctx, 60, RULE_operation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			match(LP);
			setState(323);
			operator();
			setState(324);
			operationSide();
			setState(325);
			operationSide();
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
		enterRule(_localctx, 62, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			match(LP);
			setState(329);
			match(T__19);
			setState(330);
			positiveLiteral();
			setState(331);
			assignmentSide();
			setState(332);
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
		enterRule(_localctx, 64, RULE_durationAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			match(LP);
			setState(335);
			match(T__19);
			setState(336);
			match(T__21);
			setState(337);
			((DurationAssignmentContext)_localctx).op = operationSide();
			setState(338);
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
		enterRule(_localctx, 66, RULE_comparation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			match(LP);
			setState(341);
			comparator();
			setState(342);
			operationSide();
			setState(343);
			operationSide();
			setState(344);
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
		enterRule(_localctx, 68, RULE_negatedComparation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			match(LP);
			setState(347);
			match(T__6);
			setState(348);
			comparation();
			setState(349);
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
		enterRule(_localctx, 70, RULE_modification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			match(LP);
			setState(352);
			modificator();
			setState(353);
			positiveLiteral();
			setState(354);
			operationSide();
			setState(355);
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
		enterRule(_localctx, 72, RULE_ceCond);
		try {
			setState(363);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				andClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(358);
				orClause();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(359);
				booleanLiteral();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(360);
				negatedComparation();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(361);
				comparation();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(362);
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
		enterRule(_localctx, 74, RULE_ceEff);
		try {
			setState(367);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(365);
				effectNoCes();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(366);
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
		enterRule(_localctx, 76, RULE_ce);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(369);
			match(LP);
			setState(370);
			match(T__22);
			setState(371);
			((CeContext)_localctx).cond = ceCond();
			setState(372);
			((CeContext)_localctx).eff = ceEff();
			setState(373);
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
		public EffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effect; }
	}

	public final EffectContext effect() throws RecognitionException {
		EffectContext _localctx = new EffectContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_effect);
		try {
			setState(378);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(375);
				booleanLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(376);
				modification();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(377);
				ce();
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
		enterRule(_localctx, 80, RULE_effectNoCes);
		try {
			setState(382);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(380);
				booleanLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(381);
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
		enterRule(_localctx, 82, RULE_andClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			match(LP);
			setState(385);
			match(T__23);
			setState(391); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(391);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
				case 1:
					{
					setState(386);
					andClause();
					}
					break;
				case 2:
					{
					setState(387);
					orClause();
					}
					break;
				case 3:
					{
					setState(388);
					booleanLiteral();
					}
					break;
				case 4:
					{
					setState(389);
					negatedComparation();
					}
					break;
				case 5:
					{
					setState(390);
					comparation();
					}
					break;
				}
				}
				setState(393); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(395);
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
		enterRule(_localctx, 84, RULE_orClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			match(LP);
			setState(398);
			match(T__24);
			setState(404); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(404);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(399);
					andClause();
					}
					break;
				case 2:
					{
					setState(400);
					orClause();
					}
					break;
				case 3:
					{
					setState(401);
					booleanLiteral();
					}
					break;
				case 4:
					{
					setState(402);
					negatedComparation();
					}
					break;
				case 5:
					{
					setState(403);
					comparation();
					}
					break;
				}
				}
				setState(406); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(408);
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
		enterRule(_localctx, 86, RULE_andEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(410);
			match(LP);
			setState(411);
			match(T__23);
			setState(413); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(412);
				effect();
				}
				}
				setState(415); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(417);
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
		enterRule(_localctx, 88, RULE_andEffectNoCes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			match(LP);
			setState(420);
			match(T__23);
			setState(422); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(421);
				effectNoCes();
				}
				}
				setState(424); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(426);
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
		enterRule(_localctx, 90, RULE_emptyPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			match(LP);
			setState(429);
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
		enterRule(_localctx, 92, RULE_preconditions);
		try {
			setState(437);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(431);
				andClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(432);
				orClause();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(433);
				booleanLiteral();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(434);
				negatedComparation();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(435);
				comparation();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(436);
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
		enterRule(_localctx, 94, RULE_effects);
		try {
			setState(441);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(439);
				effect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(440);
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
		enterRule(_localctx, 96, RULE_andDurClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(443);
			match(LP);
			setState(444);
			match(T__23);
			setState(448); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(448);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
				case 1:
					{
					setState(445);
					atStartPre();
					}
					break;
				case 2:
					{
					setState(446);
					overAllPre();
					}
					break;
				case 3:
					{
					setState(447);
					atEndPre();
					}
					break;
				}
				}
				setState(450); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(452);
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
		enterRule(_localctx, 98, RULE_atStartPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(454);
			match(LP);
			setState(455);
			match(T__25);
			setState(460);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(456);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(457);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(458);
				comparation();
				}
				break;
			case 4:
				{
				setState(459);
				andClause();
				}
				break;
			}
			setState(462);
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
		enterRule(_localctx, 100, RULE_overAllPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(464);
			match(LP);
			setState(465);
			match(T__26);
			setState(470);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(466);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(467);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(468);
				comparation();
				}
				break;
			case 4:
				{
				setState(469);
				andClause();
				}
				break;
			}
			setState(472);
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
		enterRule(_localctx, 102, RULE_atEndPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(474);
			match(LP);
			setState(475);
			match(T__27);
			setState(480);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(476);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(477);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(478);
				comparation();
				}
				break;
			case 4:
				{
				setState(479);
				andClause();
				}
				break;
			}
			setState(482);
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
		enterRule(_localctx, 104, RULE_durativeConditions);
		try {
			setState(489);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(484);
				andDurClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(485);
				atStartPre();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(486);
				overAllPre();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(487);
				atEndPre();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(488);
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
		enterRule(_localctx, 106, RULE_atStartEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			match(LP);
			setState(492);
			match(T__25);
			setState(496);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(493);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(494);
				modification();
				}
				break;
			case 3:
				{
				setState(495);
				andEffect();
				}
				break;
			}
			setState(498);
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
		enterRule(_localctx, 108, RULE_overAllEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(500);
			match(LP);
			setState(501);
			match(T__28);
			setState(505);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				{
				setState(502);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(503);
				modification();
				}
				break;
			case 3:
				{
				setState(504);
				andEffect();
				}
				break;
			}
			setState(507);
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
		enterRule(_localctx, 110, RULE_atEndEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(509);
			match(LP);
			setState(510);
			match(T__27);
			setState(514);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				{
				setState(511);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(512);
				modification();
				}
				break;
			case 3:
				{
				setState(513);
				andEffect();
				}
				break;
			}
			setState(516);
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
		enterRule(_localctx, 112, RULE_durativeEffect);
		try {
			setState(521);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,42,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(518);
				atStartEffect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(519);
				overAllEffect();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(520);
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
		enterRule(_localctx, 114, RULE_andDurativeEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(523);
			match(LP);
			setState(524);
			match(T__23);
			setState(526); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(525);
				durativeEffect();
				}
				}
				setState(528); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(530);
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
		enterRule(_localctx, 116, RULE_durativeEffects);
		try {
			setState(534);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(532);
				durativeEffect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(533);
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
		enterRule(_localctx, 118, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(536);
			match(LP);
			setState(540);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(537);
				typedAtomParameter();
				}
				}
				setState(542);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(543);
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
		enterRule(_localctx, 120, RULE_opName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(545);
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
		enterRule(_localctx, 122, RULE_opParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(547);
			match(T__29);
			setState(548);
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
		enterRule(_localctx, 124, RULE_opPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(550);
			match(T__30);
			setState(551);
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
		enterRule(_localctx, 126, RULE_opDurativeCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(553);
			match(T__31);
			setState(554);
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
		enterRule(_localctx, 128, RULE_opEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			match(T__32);
			setState(557);
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
		enterRule(_localctx, 130, RULE_opDurativeEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(559);
			match(T__32);
			setState(560);
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
		enterRule(_localctx, 132, RULE_opDuration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(562);
			match(T__33);
			setState(563);
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
		enterRule(_localctx, 134, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(565);
			match(LP);
			setState(566);
			match(T__34);
			setState(567);
			opName();
			setState(569);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(568);
				opParameters();
				}
			}

			setState(572);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__30) {
				{
				setState(571);
				opPrecondition();
				}
			}

			setState(574);
			opEffect();
			setState(575);
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
		enterRule(_localctx, 136, RULE_durativeAction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(577);
			match(LP);
			setState(578);
			match(T__35);
			setState(579);
			opName();
			setState(581);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(580);
				opParameters();
				}
			}

			setState(584);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__33) {
				{
				setState(583);
				opDuration();
				}
			}

			setState(587);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__31) {
				{
				setState(586);
				opDurativeCondition();
				}
			}

			setState(589);
			opDurativeEffect();
			setState(590);
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
		enterRule(_localctx, 138, RULE_event);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(592);
			match(LP);
			setState(593);
			match(T__36);
			setState(594);
			opName();
			setState(596);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(595);
				opParameters();
				}
			}

			setState(599);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__30) {
				{
				setState(598);
				opPrecondition();
				}
			}

			setState(601);
			opEffect();
			setState(602);
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
		enterRule(_localctx, 140, RULE_process);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(604);
			match(LP);
			setState(605);
			match(T__37);
			setState(606);
			opName();
			setState(608);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(607);
				opParameters();
				}
			}

			setState(611);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__30) {
				{
				setState(610);
				opPrecondition();
				}
			}

			setState(613);
			opEffect();
			setState(614);
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
		enterRule(_localctx, 142, RULE_problem);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(616);
			match(LP);
			setState(617);
			match(T__0);
			setState(618);
			problemName();
			setState(619);
			problemDomain();
			setState(621);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				{
				setState(620);
				objects();
				}
				break;
			}
			setState(623);
			init();
			setState(624);
			goal();
			setState(626);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LP) {
				{
				setState(625);
				metric();
				}
			}

			setState(628);
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
		enterRule(_localctx, 144, RULE_problemName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(630);
			match(LP);
			setState(631);
			match(T__38);
			setState(632);
			match(NAME);
			setState(633);
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
		enterRule(_localctx, 146, RULE_problemDomain);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(635);
			match(LP);
			setState(636);
			match(T__39);
			setState(637);
			match(NAME);
			setState(638);
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
		enterRule(_localctx, 148, RULE_typedObjects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(641); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(640);
				groundAtomParameter();
				}
				}
				setState(643); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(645);
			match(T__4);
			setState(646);
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
		enterRule(_localctx, 150, RULE_objects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(648);
			match(LP);
			setState(649);
			match(T__40);
			setState(653);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(650);
				typedObjects();
				}
				}
				setState(655);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(656);
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
		enterRule(_localctx, 152, RULE_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(658);
			match(LP);
			setState(659);
			match(T__41);
			setState(662); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(662);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,59,_ctx) ) {
				case 1:
					{
					setState(660);
					positiveLiteral();
					}
					break;
				case 2:
					{
					setState(661);
					assignment();
					}
					break;
				}
				}
				setState(664); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(666);
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
		enterRule(_localctx, 154, RULE_goal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(668);
			match(LP);
			setState(669);
			match(T__42);
			setState(670);
			preconditions();
			setState(671);
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
		enterRule(_localctx, 156, RULE_metric);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(673);
			match(LP);
			setState(674);
			match(T__43);
			setState(675);
			((MetricContext)_localctx).sign = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__44 || _la==T__45) ) {
				((MetricContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(676);
			((MetricContext)_localctx).op = operationSide();
			setState(677);
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
		"\u0004\u00015\u02a8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0001\u0000\u0001\u0000"+
		"\u0003\u0000\u00a1\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001\u00a7\b\u0001\u0001\u0001\u0003\u0001\u00aa\b\u0001\u0001"+
		"\u0001\u0003\u0001\u00ad\b\u0001\u0001\u0001\u0003\u0001\u00b0\b\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u00b6\b\u0001"+
		"\n\u0001\f\u0001\u00b9\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00c8\b\u0004\n"+
		"\u0004\f\u0004\u00cb\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007\u00d5"+
		"\b\u0007\u000b\u0007\f\u0007\u00d6\u0001\u0007\u0005\u0007\u00da\b\u0007"+
		"\n\u0007\f\u0007\u00dd\t\u0007\u0001\b\u0001\b\u0001\b\u0004\b\u00e2\b"+
		"\b\u000b\b\f\b\u00e3\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0004\f\u00ef\b\f\u000b\f\f\f\u00f0\u0001\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0003\r\u00f8\b\r\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u00fc\b\u000e\n\u000e\f\u000e\u00ff\t\u000e\u0001\u000f\u0001"+
		"\u000f\u0005\u000f\u0103\b\u000f\n\u000f\f\u000f\u0106\t\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u010d\b\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0003\u0013"+
		"\u011a\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0004\u0014\u011f\b"+
		"\u0014\u000b\u0014\f\u0014\u0120\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0004\u0015\u0128\b\u0015\u000b\u0015\f\u0015\u0129"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0003\u001b\u013a\b\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0141\b\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001#"+
		"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0003$\u016c"+
		"\b$\u0001%\u0001%\u0003%\u0170\b%\u0001&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"&\u0001\'\u0001\'\u0001\'\u0003\'\u017b\b\'\u0001(\u0001(\u0003(\u017f"+
		"\b(\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0004)\u0188\b)\u000b"+
		")\f)\u0189\u0001)\u0001)\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0004*\u0195\b*\u000b*\f*\u0196\u0001*\u0001*\u0001+\u0001+\u0001+\u0004"+
		"+\u019e\b+\u000b+\f+\u019f\u0001+\u0001+\u0001,\u0001,\u0001,\u0004,\u01a7"+
		"\b,\u000b,\f,\u01a8\u0001,\u0001,\u0001-\u0001-\u0001-\u0001.\u0001.\u0001"+
		".\u0001.\u0001.\u0001.\u0003.\u01b6\b.\u0001/\u0001/\u0003/\u01ba\b/\u0001"+
		"0\u00010\u00010\u00010\u00010\u00040\u01c1\b0\u000b0\f0\u01c2\u00010\u0001"+
		"0\u00011\u00011\u00011\u00011\u00011\u00011\u00031\u01cd\b1\u00011\u0001"+
		"1\u00012\u00012\u00012\u00012\u00012\u00012\u00032\u01d7\b2\u00012\u0001"+
		"2\u00013\u00013\u00013\u00013\u00013\u00013\u00033\u01e1\b3\u00013\u0001"+
		"3\u00014\u00014\u00014\u00014\u00014\u00034\u01ea\b4\u00015\u00015\u0001"+
		"5\u00015\u00015\u00035\u01f1\b5\u00015\u00015\u00016\u00016\u00016\u0001"+
		"6\u00016\u00036\u01fa\b6\u00016\u00016\u00017\u00017\u00017\u00017\u0001"+
		"7\u00037\u0203\b7\u00017\u00017\u00018\u00018\u00018\u00038\u020a\b8\u0001"+
		"9\u00019\u00019\u00049\u020f\b9\u000b9\f9\u0210\u00019\u00019\u0001:\u0001"+
		":\u0003:\u0217\b:\u0001;\u0001;\u0005;\u021b\b;\n;\f;\u021e\t;\u0001;"+
		"\u0001;\u0001<\u0001<\u0001=\u0001=\u0001=\u0001>\u0001>\u0001>\u0001"+
		"?\u0001?\u0001?\u0001@\u0001@\u0001@\u0001A\u0001A\u0001A\u0001B\u0001"+
		"B\u0001B\u0001C\u0001C\u0001C\u0001C\u0003C\u023a\bC\u0001C\u0003C\u023d"+
		"\bC\u0001C\u0001C\u0001C\u0001D\u0001D\u0001D\u0001D\u0003D\u0246\bD\u0001"+
		"D\u0003D\u0249\bD\u0001D\u0003D\u024c\bD\u0001D\u0001D\u0001D\u0001E\u0001"+
		"E\u0001E\u0001E\u0003E\u0255\bE\u0001E\u0003E\u0258\bE\u0001E\u0001E\u0001"+
		"E\u0001F\u0001F\u0001F\u0001F\u0003F\u0261\bF\u0001F\u0003F\u0264\bF\u0001"+
		"F\u0001F\u0001F\u0001G\u0001G\u0001G\u0001G\u0001G\u0003G\u026e\bG\u0001"+
		"G\u0001G\u0001G\u0003G\u0273\bG\u0001G\u0001G\u0001H\u0001H\u0001H\u0001"+
		"H\u0001H\u0001I\u0001I\u0001I\u0001I\u0001I\u0001J\u0004J\u0282\bJ\u000b"+
		"J\fJ\u0283\u0001J\u0001J\u0001J\u0001K\u0001K\u0001K\u0005K\u028c\bK\n"+
		"K\fK\u028f\tK\u0001K\u0001K\u0001L\u0001L\u0001L\u0001L\u0004L\u0297\b"+
		"L\u000bL\fL\u0298\u0001L\u0001L\u0001M\u0001M\u0001M\u0001M\u0001M\u0001"+
		"N\u0001N\u0001N\u0001N\u0001N\u0001N\u0001N\u0000\u0000O\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086"+
		"\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u0000"+
		"\u0004\u0001\u0000\n\f\u0002\u0000\u0005\u0005\r\u000f\u0001\u0000\u0010"+
		"\u0014\u0001\u0000-.\u02b5\u0000\u00a0\u0001\u0000\u0000\u0000\u0002\u00a2"+
		"\u0001\u0000\u0000\u0000\u0004\u00bc\u0001\u0000\u0000\u0000\u0006\u00c1"+
		"\u0001\u0000\u0000\u0000\b\u00c4\u0001\u0000\u0000\u0000\n\u00ce\u0001"+
		"\u0000\u0000\u0000\f\u00d1\u0001\u0000\u0000\u0000\u000e\u00d4\u0001\u0000"+
		"\u0000\u0000\u0010\u00de\u0001\u0000\u0000\u0000\u0012\u00e7\u0001\u0000"+
		"\u0000\u0000\u0014\u00e9\u0001\u0000\u0000\u0000\u0016\u00eb\u0001\u0000"+
		"\u0000\u0000\u0018\u00ee\u0001\u0000\u0000\u0000\u001a\u00f7\u0001\u0000"+
		"\u0000\u0000\u001c\u00f9\u0001\u0000\u0000\u0000\u001e\u0100\u0001\u0000"+
		"\u0000\u0000 \u010c\u0001\u0000\u0000\u0000\"\u010e\u0001\u0000\u0000"+
		"\u0000$\u0112\u0001\u0000\u0000\u0000&\u0119\u0001\u0000\u0000\u0000("+
		"\u011b\u0001\u0000\u0000\u0000*\u0124\u0001\u0000\u0000\u0000,\u012d\u0001"+
		"\u0000\u0000\u0000.\u012f\u0001\u0000\u0000\u00000\u0131\u0001\u0000\u0000"+
		"\u00002\u0133\u0001\u0000\u0000\u00004\u0135\u0001\u0000\u0000\u00006"+
		"\u0139\u0001\u0000\u0000\u00008\u013b\u0001\u0000\u0000\u0000:\u0140\u0001"+
		"\u0000\u0000\u0000<\u0142\u0001\u0000\u0000\u0000>\u0148\u0001\u0000\u0000"+
		"\u0000@\u014e\u0001\u0000\u0000\u0000B\u0154\u0001\u0000\u0000\u0000D"+
		"\u015a\u0001\u0000\u0000\u0000F\u015f\u0001\u0000\u0000\u0000H\u016b\u0001"+
		"\u0000\u0000\u0000J\u016f\u0001\u0000\u0000\u0000L\u0171\u0001\u0000\u0000"+
		"\u0000N\u017a\u0001\u0000\u0000\u0000P\u017e\u0001\u0000\u0000\u0000R"+
		"\u0180\u0001\u0000\u0000\u0000T\u018d\u0001\u0000\u0000\u0000V\u019a\u0001"+
		"\u0000\u0000\u0000X\u01a3\u0001\u0000\u0000\u0000Z\u01ac\u0001\u0000\u0000"+
		"\u0000\\\u01b5\u0001\u0000\u0000\u0000^\u01b9\u0001\u0000\u0000\u0000"+
		"`\u01bb\u0001\u0000\u0000\u0000b\u01c6\u0001\u0000\u0000\u0000d\u01d0"+
		"\u0001\u0000\u0000\u0000f\u01da\u0001\u0000\u0000\u0000h\u01e9\u0001\u0000"+
		"\u0000\u0000j\u01eb\u0001\u0000\u0000\u0000l\u01f4\u0001\u0000\u0000\u0000"+
		"n\u01fd\u0001\u0000\u0000\u0000p\u0209\u0001\u0000\u0000\u0000r\u020b"+
		"\u0001\u0000\u0000\u0000t\u0216\u0001\u0000\u0000\u0000v\u0218\u0001\u0000"+
		"\u0000\u0000x\u0221\u0001\u0000\u0000\u0000z\u0223\u0001\u0000\u0000\u0000"+
		"|\u0226\u0001\u0000\u0000\u0000~\u0229\u0001\u0000\u0000\u0000\u0080\u022c"+
		"\u0001\u0000\u0000\u0000\u0082\u022f\u0001\u0000\u0000\u0000\u0084\u0232"+
		"\u0001\u0000\u0000\u0000\u0086\u0235\u0001\u0000\u0000\u0000\u0088\u0241"+
		"\u0001\u0000\u0000\u0000\u008a\u0250\u0001\u0000\u0000\u0000\u008c\u025c"+
		"\u0001\u0000\u0000\u0000\u008e\u0268\u0001\u0000\u0000\u0000\u0090\u0276"+
		"\u0001\u0000\u0000\u0000\u0092\u027b\u0001\u0000\u0000\u0000\u0094\u0281"+
		"\u0001\u0000\u0000\u0000\u0096\u0288\u0001\u0000\u0000\u0000\u0098\u0292"+
		"\u0001\u0000\u0000\u0000\u009a\u029c\u0001\u0000\u0000\u0000\u009c\u02a1"+
		"\u0001\u0000\u0000\u0000\u009e\u00a1\u0003\u0002\u0001\u0000\u009f\u00a1"+
		"\u0003\u008eG\u0000\u00a0\u009e\u0001\u0000\u0000\u0000\u00a0\u009f\u0001"+
		"\u0000\u0000\u0000\u00a1\u0001\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005"+
		"/\u0000\u0000\u00a3\u00a4\u0005\u0001\u0000\u0000\u00a4\u00a6\u0003\u0004"+
		"\u0002\u0000\u00a5\u00a7\u0003\b\u0004\u0000\u00a6\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00a9\u0001\u0000\u0000"+
		"\u0000\u00a8\u00aa\u0003\u0010\b\u0000\u00a9\u00a8\u0001\u0000\u0000\u0000"+
		"\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ad\u0003(\u0014\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ad\u0001\u0000\u0000\u0000\u00ad\u00af\u0001\u0000\u0000\u0000\u00ae"+
		"\u00b0\u0003*\u0015\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00af\u00b0"+
		"\u0001\u0000\u0000\u0000\u00b0\u00b7\u0001\u0000\u0000\u0000\u00b1\u00b6"+
		"\u0003\u0086C\u0000\u00b2\u00b6\u0003\u0088D\u0000\u00b3\u00b6\u0003\u008a"+
		"E\u0000\u00b4\u00b6\u0003\u008cF\u0000\u00b5\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b2\u0001\u0000\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000"+
		"\u00b8\u00ba\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000"+
		"\u00ba\u00bb\u00050\u0000\u0000\u00bb\u0003\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bd\u0005/\u0000\u0000\u00bd\u00be\u0005\u0002\u0000\u0000\u00be\u00bf"+
		"\u00052\u0000\u0000\u00bf\u00c0\u00050\u0000\u0000\u00c0\u0005\u0001\u0000"+
		"\u0000\u0000\u00c1\u00c2\u0005\u0003\u0000\u0000\u00c2\u00c3\u00052\u0000"+
		"\u0000\u00c3\u0007\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005/\u0000\u0000"+
		"\u00c5\u00c9\u0005\u0004\u0000\u0000\u00c6\u00c8\u0003\u0006\u0003\u0000"+
		"\u00c7\u00c6\u0001\u0000\u0000\u0000\u00c8\u00cb\u0001\u0000\u0000\u0000"+
		"\u00c9\u00c7\u0001\u0000\u0000\u0000\u00c9\u00ca\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cc\u0001\u0000\u0000\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000"+
		"\u00cc\u00cd\u00050\u0000\u0000\u00cd\t\u0001\u0000\u0000\u0000\u00ce"+
		"\u00cf\u0005\u0005\u0000\u0000\u00cf\u00d0\u0003\f\u0006\u0000\u00d0\u000b"+
		"\u0001\u0000\u0000\u0000\u00d1\u00d2\u00052\u0000\u0000\u00d2\r\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d5\u0003\f\u0006\u0000\u00d4\u00d3\u0001\u0000"+
		"\u0000\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d4\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00db\u0001\u0000"+
		"\u0000\u0000\u00d8\u00da\u0003\n\u0005\u0000\u00d9\u00d8\u0001\u0000\u0000"+
		"\u0000\u00da\u00dd\u0001\u0000\u0000\u0000\u00db\u00d9\u0001\u0000\u0000"+
		"\u0000\u00db\u00dc\u0001\u0000\u0000\u0000\u00dc\u000f\u0001\u0000\u0000"+
		"\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00de\u00df\u0005/\u0000\u0000"+
		"\u00df\u00e1\u0005\u0006\u0000\u0000\u00e0\u00e2\u0003\u000e\u0007\u0000"+
		"\u00e1\u00e0\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5\u00e6\u00050\u0000\u0000\u00e6"+
		"\u0011\u0001\u0000\u0000\u0000\u00e7\u00e8\u00052\u0000\u0000\u00e8\u0013"+
		"\u0001\u0000\u0000\u0000\u00e9\u00ea\u00052\u0000\u0000\u00ea\u0015\u0001"+
		"\u0000\u0000\u0000\u00eb\u00ec\u00051\u0000\u0000\u00ec\u0017\u0001\u0000"+
		"\u0000\u0000\u00ed\u00ef\u0003\u0016\u000b\u0000\u00ee\u00ed\u0001\u0000"+
		"\u0000\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001\u0000"+
		"\u0000\u0000\u00f0\u00f1\u0001\u0000\u0000\u0000\u00f1\u00f2\u0001\u0000"+
		"\u0000\u0000\u00f2\u00f3\u0005\u0005\u0000\u0000\u00f3\u00f4\u0003\f\u0006"+
		"\u0000\u00f4\u0019\u0001\u0000\u0000\u0000\u00f5\u00f8\u0003\u0016\u000b"+
		"\u0000\u00f6\u00f8\u0003\u0014\n\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f6\u0001\u0000\u0000\u0000\u00f8\u001b\u0001\u0000\u0000\u0000"+
		"\u00f9\u00fd\u0003\u0012\t\u0000\u00fa\u00fc\u0003\u001a\r\u0000\u00fb"+
		"\u00fa\u0001\u0000\u0000\u0000\u00fc\u00ff\u0001\u0000\u0000\u0000\u00fd"+
		"\u00fb\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000\u0000\u0000\u00fe"+
		"\u001d\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u0100"+
		"\u0104\u0003\u0012\t\u0000\u0101\u0103\u0003\u0018\f\u0000\u0102\u0101"+
		"\u0001\u0000\u0000\u0000\u0103\u0106\u0001\u0000\u0000\u0000\u0104\u0102"+
		"\u0001\u0000\u0000\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105\u001f"+
		"\u0001\u0000\u0000\u0000\u0106\u0104\u0001\u0000\u0000\u0000\u0107\u0108"+
		"\u0005/\u0000\u0000\u0108\u0109\u0003\u001c\u000e\u0000\u0109\u010a\u0005"+
		"0\u0000\u0000\u010a\u010d\u0001\u0000\u0000\u0000\u010b\u010d\u0003\u0016"+
		"\u000b\u0000\u010c\u0107\u0001\u0000\u0000\u0000\u010c\u010b\u0001\u0000"+
		"\u0000\u0000\u010d!\u0001\u0000\u0000\u0000\u010e\u010f\u0005/\u0000\u0000"+
		"\u010f\u0110\u0003\u001e\u000f\u0000\u0110\u0111\u00050\u0000\u0000\u0111"+
		"#\u0001\u0000\u0000\u0000\u0112\u0113\u0005/\u0000\u0000\u0113\u0114\u0005"+
		"\u0007\u0000\u0000\u0114\u0115\u0003 \u0010\u0000\u0115\u0116\u00050\u0000"+
		"\u0000\u0116%\u0001\u0000\u0000\u0000\u0117\u011a\u0003 \u0010\u0000\u0118"+
		"\u011a\u0003$\u0012\u0000\u0119\u0117\u0001\u0000\u0000\u0000\u0119\u0118"+
		"\u0001\u0000\u0000\u0000\u011a\'\u0001\u0000\u0000\u0000\u011b\u011c\u0005"+
		"/\u0000\u0000\u011c\u011e\u0005\b\u0000\u0000\u011d\u011f\u0003\"\u0011"+
		"\u0000\u011e\u011d\u0001\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000"+
		"\u0000\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000"+
		"\u0000\u0121\u0122\u0001\u0000\u0000\u0000\u0122\u0123\u00050\u0000\u0000"+
		"\u0123)\u0001\u0000\u0000\u0000\u0124\u0125\u0005/\u0000\u0000\u0125\u0127"+
		"\u0005\t\u0000\u0000\u0126\u0128\u0003\"\u0011\u0000\u0127\u0126\u0001"+
		"\u0000\u0000\u0000\u0128\u0129\u0001\u0000\u0000\u0000\u0129\u0127\u0001"+
		"\u0000\u0000\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a\u012b\u0001"+
		"\u0000\u0000\u0000\u012b\u012c\u00050\u0000\u0000\u012c+\u0001\u0000\u0000"+
		"\u0000\u012d\u012e\u0007\u0000\u0000\u0000\u012e-\u0001\u0000\u0000\u0000"+
		"\u012f\u0130\u0007\u0001\u0000\u0000\u0130/\u0001\u0000\u0000\u0000\u0131"+
		"\u0132\u0007\u0002\u0000\u0000\u01321\u0001\u0000\u0000\u0000\u0133\u0134"+
		"\u00054\u0000\u0000\u01343\u0001\u0000\u0000\u0000\u0135\u0136\u0005\u0015"+
		"\u0000\u0000\u01365\u0001\u0000\u0000\u0000\u0137\u013a\u00032\u0019\u0000"+
		"\u0138\u013a\u00034\u001a\u0000\u0139\u0137\u0001\u0000\u0000\u0000\u0139"+
		"\u0138\u0001\u0000\u0000\u0000\u013a7\u0001\u0000\u0000\u0000\u013b\u013c"+
		"\u00032\u0019\u0000\u013c9\u0001\u0000\u0000\u0000\u013d\u0141\u0003<"+
		"\u001e\u0000\u013e\u0141\u0003 \u0010\u0000\u013f\u0141\u00036\u001b\u0000"+
		"\u0140\u013d\u0001\u0000\u0000\u0000\u0140\u013e\u0001\u0000\u0000\u0000"+
		"\u0140\u013f\u0001\u0000\u0000\u0000\u0141;\u0001\u0000\u0000\u0000\u0142"+
		"\u0143\u0005/\u0000\u0000\u0143\u0144\u0003.\u0017\u0000\u0144\u0145\u0003"+
		":\u001d\u0000\u0145\u0146\u0003:\u001d\u0000\u0146\u0147\u00050\u0000"+
		"\u0000\u0147=\u0001\u0000\u0000\u0000\u0148\u0149\u0005/\u0000\u0000\u0149"+
		"\u014a\u0005\u0014\u0000\u0000\u014a\u014b\u0003 \u0010\u0000\u014b\u014c"+
		"\u00038\u001c\u0000\u014c\u014d\u00050\u0000\u0000\u014d?\u0001\u0000"+
		"\u0000\u0000\u014e\u014f\u0005/\u0000\u0000\u014f\u0150\u0005\u0014\u0000"+
		"\u0000\u0150\u0151\u0005\u0016\u0000\u0000\u0151\u0152\u0003:\u001d\u0000"+
		"\u0152\u0153\u00050\u0000\u0000\u0153A\u0001\u0000\u0000\u0000\u0154\u0155"+
		"\u0005/\u0000\u0000\u0155\u0156\u00030\u0018\u0000\u0156\u0157\u0003:"+
		"\u001d\u0000\u0157\u0158\u0003:\u001d\u0000\u0158\u0159\u00050\u0000\u0000"+
		"\u0159C\u0001\u0000\u0000\u0000\u015a\u015b\u0005/\u0000\u0000\u015b\u015c"+
		"\u0005\u0007\u0000\u0000\u015c\u015d\u0003B!\u0000\u015d\u015e\u00050"+
		"\u0000\u0000\u015eE\u0001\u0000\u0000\u0000\u015f\u0160\u0005/\u0000\u0000"+
		"\u0160\u0161\u0003,\u0016\u0000\u0161\u0162\u0003 \u0010\u0000\u0162\u0163"+
		"\u0003:\u001d\u0000\u0163\u0164\u00050\u0000\u0000\u0164G\u0001\u0000"+
		"\u0000\u0000\u0165\u016c\u0003R)\u0000\u0166\u016c\u0003T*\u0000\u0167"+
		"\u016c\u0003&\u0013\u0000\u0168\u016c\u0003D\"\u0000\u0169\u016c\u0003"+
		"B!\u0000\u016a\u016c\u0003Z-\u0000\u016b\u0165\u0001\u0000\u0000\u0000"+
		"\u016b\u0166\u0001\u0000\u0000\u0000\u016b\u0167\u0001\u0000\u0000\u0000"+
		"\u016b\u0168\u0001\u0000\u0000\u0000\u016b\u0169\u0001\u0000\u0000\u0000"+
		"\u016b\u016a\u0001\u0000\u0000\u0000\u016cI\u0001\u0000\u0000\u0000\u016d"+
		"\u0170\u0003P(\u0000\u016e\u0170\u0003X,\u0000\u016f\u016d\u0001\u0000"+
		"\u0000\u0000\u016f\u016e\u0001\u0000\u0000\u0000\u0170K\u0001\u0000\u0000"+
		"\u0000\u0171\u0172\u0005/\u0000\u0000\u0172\u0173\u0005\u0017\u0000\u0000"+
		"\u0173\u0174\u0003H$\u0000\u0174\u0175\u0003J%\u0000\u0175\u0176\u0005"+
		"0\u0000\u0000\u0176M\u0001\u0000\u0000\u0000\u0177\u017b\u0003&\u0013"+
		"\u0000\u0178\u017b\u0003F#\u0000\u0179\u017b\u0003L&\u0000\u017a\u0177"+
		"\u0001\u0000\u0000\u0000\u017a\u0178\u0001\u0000\u0000\u0000\u017a\u0179"+
		"\u0001\u0000\u0000\u0000\u017bO\u0001\u0000\u0000\u0000\u017c\u017f\u0003"+
		"&\u0013\u0000\u017d\u017f\u0003F#\u0000\u017e\u017c\u0001\u0000\u0000"+
		"\u0000\u017e\u017d\u0001\u0000\u0000\u0000\u017fQ\u0001\u0000\u0000\u0000"+
		"\u0180\u0181\u0005/\u0000\u0000\u0181\u0187\u0005\u0018\u0000\u0000\u0182"+
		"\u0188\u0003R)\u0000\u0183\u0188\u0003T*\u0000\u0184\u0188\u0003&\u0013"+
		"\u0000\u0185\u0188\u0003D\"\u0000\u0186\u0188\u0003B!\u0000\u0187\u0182"+
		"\u0001\u0000\u0000\u0000\u0187\u0183\u0001\u0000\u0000\u0000\u0187\u0184"+
		"\u0001\u0000\u0000\u0000\u0187\u0185\u0001\u0000\u0000\u0000\u0187\u0186"+
		"\u0001\u0000\u0000\u0000\u0188\u0189\u0001\u0000\u0000\u0000\u0189\u0187"+
		"\u0001\u0000\u0000\u0000\u0189\u018a\u0001\u0000\u0000\u0000\u018a\u018b"+
		"\u0001\u0000\u0000\u0000\u018b\u018c\u00050\u0000\u0000\u018cS\u0001\u0000"+
		"\u0000\u0000\u018d\u018e\u0005/\u0000\u0000\u018e\u0194\u0005\u0019\u0000"+
		"\u0000\u018f\u0195\u0003R)\u0000\u0190\u0195\u0003T*\u0000\u0191\u0195"+
		"\u0003&\u0013\u0000\u0192\u0195\u0003D\"\u0000\u0193\u0195\u0003B!\u0000"+
		"\u0194\u018f\u0001\u0000\u0000\u0000\u0194\u0190\u0001\u0000\u0000\u0000"+
		"\u0194\u0191\u0001\u0000\u0000\u0000\u0194\u0192\u0001\u0000\u0000\u0000"+
		"\u0194\u0193\u0001\u0000\u0000\u0000\u0195\u0196\u0001\u0000\u0000\u0000"+
		"\u0196\u0194\u0001\u0000\u0000\u0000\u0196\u0197\u0001\u0000\u0000\u0000"+
		"\u0197\u0198\u0001\u0000\u0000\u0000\u0198\u0199\u00050\u0000\u0000\u0199"+
		"U\u0001\u0000\u0000\u0000\u019a\u019b\u0005/\u0000\u0000\u019b\u019d\u0005"+
		"\u0018\u0000\u0000\u019c\u019e\u0003N\'\u0000\u019d\u019c\u0001\u0000"+
		"\u0000\u0000\u019e\u019f\u0001\u0000\u0000\u0000\u019f\u019d\u0001\u0000"+
		"\u0000\u0000\u019f\u01a0\u0001\u0000\u0000\u0000\u01a0\u01a1\u0001\u0000"+
		"\u0000\u0000\u01a1\u01a2\u00050\u0000\u0000\u01a2W\u0001\u0000\u0000\u0000"+
		"\u01a3\u01a4\u0005/\u0000\u0000\u01a4\u01a6\u0005\u0018\u0000\u0000\u01a5"+
		"\u01a7\u0003P(\u0000\u01a6\u01a5\u0001\u0000\u0000\u0000\u01a7\u01a8\u0001"+
		"\u0000\u0000\u0000\u01a8\u01a6\u0001\u0000\u0000\u0000\u01a8\u01a9\u0001"+
		"\u0000\u0000\u0000\u01a9\u01aa\u0001\u0000\u0000\u0000\u01aa\u01ab\u0005"+
		"0\u0000\u0000\u01abY\u0001\u0000\u0000\u0000\u01ac\u01ad\u0005/\u0000"+
		"\u0000\u01ad\u01ae\u00050\u0000\u0000\u01ae[\u0001\u0000\u0000\u0000\u01af"+
		"\u01b6\u0003R)\u0000\u01b0\u01b6\u0003T*\u0000\u01b1\u01b6\u0003&\u0013"+
		"\u0000\u01b2\u01b6\u0003D\"\u0000\u01b3\u01b6\u0003B!\u0000\u01b4\u01b6"+
		"\u0003Z-\u0000\u01b5\u01af\u0001\u0000\u0000\u0000\u01b5\u01b0\u0001\u0000"+
		"\u0000\u0000\u01b5\u01b1\u0001\u0000\u0000\u0000\u01b5\u01b2\u0001\u0000"+
		"\u0000\u0000\u01b5\u01b3\u0001\u0000\u0000\u0000\u01b5\u01b4\u0001\u0000"+
		"\u0000\u0000\u01b6]\u0001\u0000\u0000\u0000\u01b7\u01ba\u0003N\'\u0000"+
		"\u01b8\u01ba\u0003V+\u0000\u01b9\u01b7\u0001\u0000\u0000\u0000\u01b9\u01b8"+
		"\u0001\u0000\u0000\u0000\u01ba_\u0001\u0000\u0000\u0000\u01bb\u01bc\u0005"+
		"/\u0000\u0000\u01bc\u01c0\u0005\u0018\u0000\u0000\u01bd\u01c1\u0003b1"+
		"\u0000\u01be\u01c1\u0003d2\u0000\u01bf\u01c1\u0003f3\u0000\u01c0\u01bd"+
		"\u0001\u0000\u0000\u0000\u01c0\u01be\u0001\u0000\u0000\u0000\u01c0\u01bf"+
		"\u0001\u0000\u0000\u0000\u01c1\u01c2\u0001\u0000\u0000\u0000\u01c2\u01c0"+
		"\u0001\u0000\u0000\u0000\u01c2\u01c3\u0001\u0000\u0000\u0000\u01c3\u01c4"+
		"\u0001\u0000\u0000\u0000\u01c4\u01c5\u00050\u0000\u0000\u01c5a\u0001\u0000"+
		"\u0000\u0000\u01c6\u01c7\u0005/\u0000\u0000\u01c7\u01cc\u0005\u001a\u0000"+
		"\u0000\u01c8\u01cd\u0003&\u0013\u0000\u01c9\u01cd\u0003D\"\u0000\u01ca"+
		"\u01cd\u0003B!\u0000\u01cb\u01cd\u0003R)\u0000\u01cc\u01c8\u0001\u0000"+
		"\u0000\u0000\u01cc\u01c9\u0001\u0000\u0000\u0000\u01cc\u01ca\u0001\u0000"+
		"\u0000\u0000\u01cc\u01cb\u0001\u0000\u0000\u0000\u01cd\u01ce\u0001\u0000"+
		"\u0000\u0000\u01ce\u01cf\u00050\u0000\u0000\u01cfc\u0001\u0000\u0000\u0000"+
		"\u01d0\u01d1\u0005/\u0000\u0000\u01d1\u01d6\u0005\u001b\u0000\u0000\u01d2"+
		"\u01d7\u0003&\u0013\u0000\u01d3\u01d7\u0003D\"\u0000\u01d4\u01d7\u0003"+
		"B!\u0000\u01d5\u01d7\u0003R)\u0000\u01d6\u01d2\u0001\u0000\u0000\u0000"+
		"\u01d6\u01d3\u0001\u0000\u0000\u0000\u01d6\u01d4\u0001\u0000\u0000\u0000"+
		"\u01d6\u01d5\u0001\u0000\u0000\u0000\u01d7\u01d8\u0001\u0000\u0000\u0000"+
		"\u01d8\u01d9\u00050\u0000\u0000\u01d9e\u0001\u0000\u0000\u0000\u01da\u01db"+
		"\u0005/\u0000\u0000\u01db\u01e0\u0005\u001c\u0000\u0000\u01dc\u01e1\u0003"+
		"&\u0013\u0000\u01dd\u01e1\u0003D\"\u0000\u01de\u01e1\u0003B!\u0000\u01df"+
		"\u01e1\u0003R)\u0000\u01e0\u01dc\u0001\u0000\u0000\u0000\u01e0\u01dd\u0001"+
		"\u0000\u0000\u0000\u01e0\u01de\u0001\u0000\u0000\u0000\u01e0\u01df\u0001"+
		"\u0000\u0000\u0000\u01e1\u01e2\u0001\u0000\u0000\u0000\u01e2\u01e3\u0005"+
		"0\u0000\u0000\u01e3g\u0001\u0000\u0000\u0000\u01e4\u01ea\u0003`0\u0000"+
		"\u01e5\u01ea\u0003b1\u0000\u01e6\u01ea\u0003d2\u0000\u01e7\u01ea\u0003"+
		"f3\u0000\u01e8\u01ea\u0003Z-\u0000\u01e9\u01e4\u0001\u0000\u0000\u0000"+
		"\u01e9\u01e5\u0001\u0000\u0000\u0000\u01e9\u01e6\u0001\u0000\u0000\u0000"+
		"\u01e9\u01e7\u0001\u0000\u0000\u0000\u01e9\u01e8\u0001\u0000\u0000\u0000"+
		"\u01eai\u0001\u0000\u0000\u0000\u01eb\u01ec\u0005/\u0000\u0000\u01ec\u01f0"+
		"\u0005\u001a\u0000\u0000\u01ed\u01f1\u0003&\u0013\u0000\u01ee\u01f1\u0003"+
		"F#\u0000\u01ef\u01f1\u0003V+\u0000\u01f0\u01ed\u0001\u0000\u0000\u0000"+
		"\u01f0\u01ee\u0001\u0000\u0000\u0000\u01f0\u01ef\u0001\u0000\u0000\u0000"+
		"\u01f1\u01f2\u0001\u0000\u0000\u0000\u01f2\u01f3\u00050\u0000\u0000\u01f3"+
		"k\u0001\u0000\u0000\u0000\u01f4\u01f5\u0005/\u0000\u0000\u01f5\u01f9\u0005"+
		"\u001d\u0000\u0000\u01f6\u01fa\u0003&\u0013\u0000\u01f7\u01fa\u0003F#"+
		"\u0000\u01f8\u01fa\u0003V+\u0000\u01f9\u01f6\u0001\u0000\u0000\u0000\u01f9"+
		"\u01f7\u0001\u0000\u0000\u0000\u01f9\u01f8\u0001\u0000\u0000\u0000\u01fa"+
		"\u01fb\u0001\u0000\u0000\u0000\u01fb\u01fc\u00050\u0000\u0000\u01fcm\u0001"+
		"\u0000\u0000\u0000\u01fd\u01fe\u0005/\u0000\u0000\u01fe\u0202\u0005\u001c"+
		"\u0000\u0000\u01ff\u0203\u0003&\u0013\u0000\u0200\u0203\u0003F#\u0000"+
		"\u0201\u0203\u0003V+\u0000\u0202\u01ff\u0001\u0000\u0000\u0000\u0202\u0200"+
		"\u0001\u0000\u0000\u0000\u0202\u0201\u0001\u0000\u0000\u0000\u0203\u0204"+
		"\u0001\u0000\u0000\u0000\u0204\u0205\u00050\u0000\u0000\u0205o\u0001\u0000"+
		"\u0000\u0000\u0206\u020a\u0003j5\u0000\u0207\u020a\u0003l6\u0000\u0208"+
		"\u020a\u0003n7\u0000\u0209\u0206\u0001\u0000\u0000\u0000\u0209\u0207\u0001"+
		"\u0000\u0000\u0000\u0209\u0208\u0001\u0000\u0000\u0000\u020aq\u0001\u0000"+
		"\u0000\u0000\u020b\u020c\u0005/\u0000\u0000\u020c\u020e\u0005\u0018\u0000"+
		"\u0000\u020d\u020f\u0003p8\u0000\u020e\u020d\u0001\u0000\u0000\u0000\u020f"+
		"\u0210\u0001\u0000\u0000\u0000\u0210\u020e\u0001\u0000\u0000\u0000\u0210"+
		"\u0211\u0001\u0000\u0000\u0000\u0211\u0212\u0001\u0000\u0000\u0000\u0212"+
		"\u0213\u00050\u0000\u0000\u0213s\u0001\u0000\u0000\u0000\u0214\u0217\u0003"+
		"p8\u0000\u0215\u0217\u0003r9\u0000\u0216\u0214\u0001\u0000\u0000\u0000"+
		"\u0216\u0215\u0001\u0000\u0000\u0000\u0217u\u0001\u0000\u0000\u0000\u0218"+
		"\u021c\u0005/\u0000\u0000\u0219\u021b\u0003\u0018\f\u0000\u021a\u0219"+
		"\u0001\u0000\u0000\u0000\u021b\u021e\u0001\u0000\u0000\u0000\u021c\u021a"+
		"\u0001\u0000\u0000\u0000\u021c\u021d\u0001\u0000\u0000\u0000\u021d\u021f"+
		"\u0001\u0000\u0000\u0000\u021e\u021c\u0001\u0000\u0000\u0000\u021f\u0220"+
		"\u00050\u0000\u0000\u0220w\u0001\u0000\u0000\u0000\u0221\u0222\u00052"+
		"\u0000\u0000\u0222y\u0001\u0000\u0000\u0000\u0223\u0224\u0005\u001e\u0000"+
		"\u0000\u0224\u0225\u0003v;\u0000\u0225{\u0001\u0000\u0000\u0000\u0226"+
		"\u0227\u0005\u001f\u0000\u0000\u0227\u0228\u0003\\.\u0000\u0228}\u0001"+
		"\u0000\u0000\u0000\u0229\u022a\u0005 \u0000\u0000\u022a\u022b\u0003h4"+
		"\u0000\u022b\u007f\u0001\u0000\u0000\u0000\u022c\u022d\u0005!\u0000\u0000"+
		"\u022d\u022e\u0003^/\u0000\u022e\u0081\u0001\u0000\u0000\u0000\u022f\u0230"+
		"\u0005!\u0000\u0000\u0230\u0231\u0003t:\u0000\u0231\u0083\u0001\u0000"+
		"\u0000\u0000\u0232\u0233\u0005\"\u0000\u0000\u0233\u0234\u0003@ \u0000"+
		"\u0234\u0085\u0001\u0000\u0000\u0000\u0235\u0236\u0005/\u0000\u0000\u0236"+
		"\u0237\u0005#\u0000\u0000\u0237\u0239\u0003x<\u0000\u0238\u023a\u0003"+
		"z=\u0000\u0239\u0238\u0001\u0000\u0000\u0000\u0239\u023a\u0001\u0000\u0000"+
		"\u0000\u023a\u023c\u0001\u0000\u0000\u0000\u023b\u023d\u0003|>\u0000\u023c"+
		"\u023b\u0001\u0000\u0000\u0000\u023c\u023d\u0001\u0000\u0000\u0000\u023d"+
		"\u023e\u0001\u0000\u0000\u0000\u023e\u023f\u0003\u0080@\u0000\u023f\u0240"+
		"\u00050\u0000\u0000\u0240\u0087\u0001\u0000\u0000\u0000\u0241\u0242\u0005"+
		"/\u0000\u0000\u0242\u0243\u0005$\u0000\u0000\u0243\u0245\u0003x<\u0000"+
		"\u0244\u0246\u0003z=\u0000\u0245\u0244\u0001\u0000\u0000\u0000\u0245\u0246"+
		"\u0001\u0000\u0000\u0000\u0246\u0248\u0001\u0000\u0000\u0000\u0247\u0249"+
		"\u0003\u0084B\u0000\u0248\u0247\u0001\u0000\u0000\u0000\u0248\u0249\u0001"+
		"\u0000\u0000\u0000\u0249\u024b\u0001\u0000\u0000\u0000\u024a\u024c\u0003"+
		"~?\u0000\u024b\u024a\u0001\u0000\u0000\u0000\u024b\u024c\u0001\u0000\u0000"+
		"\u0000\u024c\u024d\u0001\u0000\u0000\u0000\u024d\u024e\u0003\u0082A\u0000"+
		"\u024e\u024f\u00050\u0000\u0000\u024f\u0089\u0001\u0000\u0000\u0000\u0250"+
		"\u0251\u0005/\u0000\u0000\u0251\u0252\u0005%\u0000\u0000\u0252\u0254\u0003"+
		"x<\u0000\u0253\u0255\u0003z=\u0000\u0254\u0253\u0001\u0000\u0000\u0000"+
		"\u0254\u0255\u0001\u0000\u0000\u0000\u0255\u0257\u0001\u0000\u0000\u0000"+
		"\u0256\u0258\u0003|>\u0000\u0257\u0256\u0001\u0000\u0000\u0000\u0257\u0258"+
		"\u0001\u0000\u0000\u0000\u0258\u0259\u0001\u0000\u0000\u0000\u0259\u025a"+
		"\u0003\u0080@\u0000\u025a\u025b\u00050\u0000\u0000\u025b\u008b\u0001\u0000"+
		"\u0000\u0000\u025c\u025d\u0005/\u0000\u0000\u025d\u025e\u0005&\u0000\u0000"+
		"\u025e\u0260\u0003x<\u0000\u025f\u0261\u0003z=\u0000\u0260\u025f\u0001"+
		"\u0000\u0000\u0000\u0260\u0261\u0001\u0000\u0000\u0000\u0261\u0263\u0001"+
		"\u0000\u0000\u0000\u0262\u0264\u0003|>\u0000\u0263\u0262\u0001\u0000\u0000"+
		"\u0000\u0263\u0264\u0001\u0000\u0000\u0000\u0264\u0265\u0001\u0000\u0000"+
		"\u0000\u0265\u0266\u0003\u0080@\u0000\u0266\u0267\u00050\u0000\u0000\u0267"+
		"\u008d\u0001\u0000\u0000\u0000\u0268\u0269\u0005/\u0000\u0000\u0269\u026a"+
		"\u0005\u0001\u0000\u0000\u026a\u026b\u0003\u0090H\u0000\u026b\u026d\u0003"+
		"\u0092I\u0000\u026c\u026e\u0003\u0096K\u0000\u026d\u026c\u0001\u0000\u0000"+
		"\u0000\u026d\u026e\u0001\u0000\u0000\u0000\u026e\u026f\u0001\u0000\u0000"+
		"\u0000\u026f\u0270\u0003\u0098L\u0000\u0270\u0272\u0003\u009aM\u0000\u0271"+
		"\u0273\u0003\u009cN\u0000\u0272\u0271\u0001\u0000\u0000\u0000\u0272\u0273"+
		"\u0001\u0000\u0000\u0000\u0273\u0274\u0001\u0000\u0000\u0000\u0274\u0275"+
		"\u00050\u0000\u0000\u0275\u008f\u0001\u0000\u0000\u0000\u0276\u0277\u0005"+
		"/\u0000\u0000\u0277\u0278\u0005\'\u0000\u0000\u0278\u0279\u00052\u0000"+
		"\u0000\u0279\u027a\u00050\u0000\u0000\u027a\u0091\u0001\u0000\u0000\u0000"+
		"\u027b\u027c\u0005/\u0000\u0000\u027c\u027d\u0005(\u0000\u0000\u027d\u027e"+
		"\u00052\u0000\u0000\u027e\u027f\u00050\u0000\u0000\u027f\u0093\u0001\u0000"+
		"\u0000\u0000\u0280\u0282\u0003\u0014\n\u0000\u0281\u0280\u0001\u0000\u0000"+
		"\u0000\u0282\u0283\u0001\u0000\u0000\u0000\u0283\u0281\u0001\u0000\u0000"+
		"\u0000\u0283\u0284\u0001\u0000\u0000\u0000\u0284\u0285\u0001\u0000\u0000"+
		"\u0000\u0285\u0286\u0005\u0005\u0000\u0000\u0286\u0287\u0003\f\u0006\u0000"+
		"\u0287\u0095\u0001\u0000\u0000\u0000\u0288\u0289\u0005/\u0000\u0000\u0289"+
		"\u028d\u0005)\u0000\u0000\u028a\u028c\u0003\u0094J\u0000\u028b\u028a\u0001"+
		"\u0000\u0000\u0000\u028c\u028f\u0001\u0000\u0000\u0000\u028d\u028b\u0001"+
		"\u0000\u0000\u0000\u028d\u028e\u0001\u0000\u0000\u0000\u028e\u0290\u0001"+
		"\u0000\u0000\u0000\u028f\u028d\u0001\u0000\u0000\u0000\u0290\u0291\u0005"+
		"0\u0000\u0000\u0291\u0097\u0001\u0000\u0000\u0000\u0292\u0293\u0005/\u0000"+
		"\u0000\u0293\u0296\u0005*\u0000\u0000\u0294\u0297\u0003 \u0010\u0000\u0295"+
		"\u0297\u0003>\u001f\u0000\u0296\u0294\u0001\u0000\u0000\u0000\u0296\u0295"+
		"\u0001\u0000\u0000\u0000\u0297\u0298\u0001\u0000\u0000\u0000\u0298\u0296"+
		"\u0001\u0000\u0000\u0000\u0298\u0299\u0001\u0000\u0000\u0000\u0299\u029a"+
		"\u0001\u0000\u0000\u0000\u029a\u029b\u00050\u0000\u0000\u029b\u0099\u0001"+
		"\u0000\u0000\u0000\u029c\u029d\u0005/\u0000\u0000\u029d\u029e\u0005+\u0000"+
		"\u0000\u029e\u029f\u0003\\.\u0000\u029f\u02a0\u00050\u0000\u0000\u02a0"+
		"\u009b\u0001\u0000\u0000\u0000\u02a1\u02a2\u0005/\u0000\u0000\u02a2\u02a3"+
		"\u0005,\u0000\u0000\u02a3\u02a4\u0007\u0003\u0000\u0000\u02a4\u02a5\u0003"+
		":\u001d\u0000\u02a5\u02a6\u00050\u0000\u0000\u02a6\u009d\u0001\u0000\u0000"+
		"\u0000=\u00a0\u00a6\u00a9\u00ac\u00af\u00b5\u00b7\u00c9\u00d6\u00db\u00e3"+
		"\u00f0\u00f7\u00fd\u0104\u010c\u0119\u0120\u0129\u0139\u0140\u016b\u016f"+
		"\u017a\u017e\u0187\u0189\u0194\u0196\u019f\u01a8\u01b5\u01b9\u01c0\u01c2"+
		"\u01cc\u01d6\u01e0\u01e9\u01f0\u01f9\u0202\u0209\u0210\u0216\u021c\u0239"+
		"\u023c\u0245\u0248\u024b\u0254\u0257\u0260\u0263\u026d\u0272\u0283\u028d"+
		"\u0296\u0298";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}