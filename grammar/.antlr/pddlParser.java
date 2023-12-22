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
		LP=46, RP=47, VAR=48, NAME=49, VARIABLE=50, NUMBER=51, WS=52;
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
		RULE_effect = 36, RULE_andClause = 37, RULE_orClause = 38, RULE_andEffect = 39, 
		RULE_emptyPrecondition = 40, RULE_preconditions = 41, RULE_effects = 42, 
		RULE_andDurClause = 43, RULE_atStartPre = 44, RULE_overAllPre = 45, RULE_atEndPre = 46, 
		RULE_durativeConditions = 47, RULE_atStartEffect = 48, RULE_overAllEffect = 49, 
		RULE_atEndEffect = 50, RULE_durativeEffect = 51, RULE_andDurativeEffect = 52, 
		RULE_durativeEffects = 53, RULE_parameters = 54, RULE_opName = 55, RULE_opParameters = 56, 
		RULE_opPrecondition = 57, RULE_opDurativeCondition = 58, RULE_opEffect = 59, 
		RULE_opDurativeEffect = 60, RULE_opDuration = 61, RULE_action = 62, RULE_durativeAction = 63, 
		RULE_event = 64, RULE_process = 65, RULE_problem = 66, RULE_problemName = 67, 
		RULE_problemDomain = 68, RULE_typedObjects = 69, RULE_objects = 70, RULE_init = 71, 
		RULE_goal = 72, RULE_metric = 73;
	private static String[] makeRuleNames() {
		return new String[] {
			"pddlDoc", "domain", "domainName", "requireKey", "requirements", "parentType", 
			"typeName", "type", "types", "atomName", "groundAtomParameter", "liftedAtomParameter", 
			"typedAtomParameter", "atomParameter", "atom", "typedAtom", "positiveLiteral", 
			"typedPositiveLiteral", "negativeLiteral", "booleanLiteral", "predicates", 
			"functions", "modificator", "operator", "comparator", "number", "delta", 
			"constant", "assignmentSide", "operationSide", "operation", "assignment", 
			"durationAssignment", "comparation", "negatedComparation", "modification", 
			"effect", "andClause", "orClause", "andEffect", "emptyPrecondition", 
			"preconditions", "effects", "andDurClause", "atStartPre", "overAllPre", 
			"atEndPre", "durativeConditions", "atStartEffect", "overAllEffect", "atEndEffect", 
			"durativeEffect", "andDurativeEffect", "durativeEffects", "parameters", 
			"opName", "opParameters", "opPrecondition", "opDurativeCondition", "opEffect", 
			"opDurativeEffect", "opDuration", "action", "durativeAction", "event", 
			"process", "problem", "problemName", "problemDomain", "typedObjects", 
			"objects", "init", "goal", "metric"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'define'", "'domain'", "':'", "':requirements'", "'-'", "':types'", 
			"'not'", "':predicates'", "':functions'", "'assign'", "'increase'", "'decrease'", 
			"'+'", "'*'", "'/'", "'>'", "'>='", "'<='", "'<'", "'='", "'#t'", "'?duration'", 
			"'and'", "'or'", "'at start'", "'over all'", "'at end'", "'overall'", 
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
			null, null, null, null, null, null, null, null, null, null, "LP", "RP", 
			"VAR", "NAME", "VARIABLE", "NUMBER", "WS"
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
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				domain();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
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
			setState(152);
			match(LP);
			setState(153);
			match(T__0);
			setState(154);
			domainName();
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(155);
				requirements();
				}
				break;
			}
			setState(159);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(158);
				types();
				}
				break;
			}
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(161);
				predicates();
				}
				break;
			}
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(164);
				functions();
				}
				break;
			}
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LP) {
				{
				setState(171);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(167);
					action();
					}
					break;
				case 2:
					{
					setState(168);
					durativeAction();
					}
					break;
				case 3:
					{
					setState(169);
					event();
					}
					break;
				case 4:
					{
					setState(170);
					process();
					}
					break;
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(176);
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
			setState(178);
			match(LP);
			setState(179);
			match(T__1);
			setState(180);
			match(NAME);
			setState(181);
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
			setState(183);
			match(T__2);
			setState(184);
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
			setState(186);
			match(LP);
			setState(187);
			match(T__3);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(188);
				requireKey();
				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(194);
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
			setState(196);
			match(T__4);
			setState(197);
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
			setState(199);
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
			setState(202); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(201);
					typeName();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(204); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(206);
				((TypeContext)_localctx).parent = parentType();
				}
				}
				setState(211);
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
			setState(212);
			match(LP);
			setState(213);
			match(T__5);
			setState(215); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(214);
				type();
				}
				}
				setState(217); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(219);
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
			setState(221);
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
			setState(223);
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
			setState(225);
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
			setState(228); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(227);
				liftedAtomParameter();
				}
				}
				setState(230); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VAR );
			setState(232);
			match(T__4);
			setState(233);
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
			setState(237);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(235);
				liftedAtomParameter();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
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
			setState(239);
			atomName();
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==NAME) {
				{
				{
				setState(240);
				atomParameter();
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
			setState(246);
			atomName();
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(247);
				typedAtomParameter();
				}
				}
				setState(252);
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
			setState(258);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				match(LP);
				setState(254);
				atom();
				setState(255);
				match(RP);
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(257);
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
			setState(260);
			match(LP);
			setState(261);
			typedAtom();
			setState(262);
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
			setState(264);
			match(LP);
			setState(265);
			match(T__6);
			setState(266);
			positiveLiteral();
			setState(267);
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
			setState(271);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				positiveLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
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
			setState(273);
			match(LP);
			setState(274);
			match(T__7);
			setState(276); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(275);
				typedPositiveLiteral();
				}
				}
				setState(278); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(280);
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
			setState(282);
			match(LP);
			setState(283);
			match(T__8);
			setState(285); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(284);
				typedPositiveLiteral();
				}
				}
				setState(287); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(289);
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
			setState(291);
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
			setState(293);
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
			setState(295);
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
			setState(297);
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
			setState(299);
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
			setState(303);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(301);
				number();
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 2);
				{
				setState(302);
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
			setState(305);
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
			setState(310);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(307);
				operation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(308);
				positiveLiteral();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(309);
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
			setState(312);
			match(LP);
			setState(313);
			operator();
			setState(314);
			operationSide();
			setState(315);
			operationSide();
			setState(316);
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
			setState(318);
			match(LP);
			setState(319);
			match(T__19);
			setState(320);
			positiveLiteral();
			setState(321);
			assignmentSide();
			setState(322);
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
			setState(324);
			match(LP);
			setState(325);
			match(T__19);
			setState(326);
			match(T__21);
			setState(327);
			((DurationAssignmentContext)_localctx).op = operationSide();
			setState(328);
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
			setState(330);
			match(LP);
			setState(331);
			comparator();
			setState(332);
			operationSide();
			setState(333);
			operationSide();
			setState(334);
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
			setState(336);
			match(LP);
			setState(337);
			match(T__6);
			setState(338);
			comparation();
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
			setState(341);
			match(LP);
			setState(342);
			modificator();
			setState(343);
			positiveLiteral();
			setState(344);
			operationSide();
			setState(345);
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
		public EffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_effect; }
	}

	public final EffectContext effect() throws RecognitionException {
		EffectContext _localctx = new EffectContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_effect);
		try {
			setState(349);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				booleanLiteral();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(348);
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
		enterRule(_localctx, 74, RULE_andClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			match(LP);
			setState(352);
			match(T__22);
			setState(358); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(358);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(353);
					andClause();
					}
					break;
				case 2:
					{
					setState(354);
					orClause();
					}
					break;
				case 3:
					{
					setState(355);
					booleanLiteral();
					}
					break;
				case 4:
					{
					setState(356);
					negatedComparation();
					}
					break;
				case 5:
					{
					setState(357);
					comparation();
					}
					break;
				}
				}
				setState(360); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(362);
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
		enterRule(_localctx, 76, RULE_orClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			match(LP);
			setState(365);
			match(T__23);
			setState(371); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(371);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
				case 1:
					{
					setState(366);
					andClause();
					}
					break;
				case 2:
					{
					setState(367);
					orClause();
					}
					break;
				case 3:
					{
					setState(368);
					booleanLiteral();
					}
					break;
				case 4:
					{
					setState(369);
					negatedComparation();
					}
					break;
				case 5:
					{
					setState(370);
					comparation();
					}
					break;
				}
				}
				setState(373); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
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
		enterRule(_localctx, 78, RULE_andEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(377);
			match(LP);
			setState(378);
			match(T__22);
			setState(380); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(379);
				effect();
				}
				}
				setState(382); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(384);
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
		enterRule(_localctx, 80, RULE_emptyPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			match(LP);
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
		enterRule(_localctx, 82, RULE_preconditions);
		try {
			setState(395);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(389);
				andClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(390);
				orClause();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(391);
				booleanLiteral();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(392);
				negatedComparation();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(393);
				comparation();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(394);
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
		enterRule(_localctx, 84, RULE_effects);
		try {
			setState(399);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(397);
				effect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(398);
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
		enterRule(_localctx, 86, RULE_andDurClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(401);
			match(LP);
			setState(402);
			match(T__22);
			setState(406); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(406);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
				case 1:
					{
					setState(403);
					atStartPre();
					}
					break;
				case 2:
					{
					setState(404);
					overAllPre();
					}
					break;
				case 3:
					{
					setState(405);
					atEndPre();
					}
					break;
				}
				}
				setState(408); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
			setState(410);
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
		public AtStartPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atStartPre; }
	}

	public final AtStartPreContext atStartPre() throws RecognitionException {
		AtStartPreContext _localctx = new AtStartPreContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_atStartPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(412);
			match(LP);
			setState(413);
			match(T__24);
			setState(417);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				{
				setState(414);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(415);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(416);
				comparation();
				}
				break;
			}
			setState(419);
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
		public OverAllPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overAllPre; }
	}

	public final OverAllPreContext overAllPre() throws RecognitionException {
		OverAllPreContext _localctx = new OverAllPreContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_overAllPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(421);
			match(LP);
			setState(422);
			match(T__25);
			setState(426);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				{
				setState(423);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(424);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(425);
				comparation();
				}
				break;
			}
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
		public AtEndPreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atEndPre; }
	}

	public final AtEndPreContext atEndPre() throws RecognitionException {
		AtEndPreContext _localctx = new AtEndPreContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_atEndPre);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(430);
			match(LP);
			setState(431);
			match(T__26);
			setState(435);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				{
				setState(432);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(433);
				negatedComparation();
				}
				break;
			case 3:
				{
				setState(434);
				comparation();
				}
				break;
			}
			setState(437);
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
		enterRule(_localctx, 94, RULE_durativeConditions);
		try {
			setState(444);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(439);
				andDurClause();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(440);
				atStartPre();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(441);
				overAllPre();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(442);
				atEndPre();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(443);
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
		public AtStartEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atStartEffect; }
	}

	public final AtStartEffectContext atStartEffect() throws RecognitionException {
		AtStartEffectContext _localctx = new AtStartEffectContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_atStartEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(446);
			match(LP);
			setState(447);
			match(T__24);
			setState(450);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(448);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(449);
				modification();
				}
				break;
			}
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
	public static class OverAllEffectContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(pddlParser.LP, 0); }
		public TerminalNode RP() { return getToken(pddlParser.RP, 0); }
		public BooleanLiteralContext booleanLiteral() {
			return getRuleContext(BooleanLiteralContext.class,0);
		}
		public ModificationContext modification() {
			return getRuleContext(ModificationContext.class,0);
		}
		public OverAllEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overAllEffect; }
	}

	public final OverAllEffectContext overAllEffect() throws RecognitionException {
		OverAllEffectContext _localctx = new OverAllEffectContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_overAllEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(454);
			match(LP);
			setState(455);
			match(T__27);
			setState(458);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(456);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(457);
				modification();
				}
				break;
			}
			setState(460);
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
		public AtEndEffectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atEndEffect; }
	}

	public final AtEndEffectContext atEndEffect() throws RecognitionException {
		AtEndEffectContext _localctx = new AtEndEffectContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_atEndEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(462);
			match(LP);
			setState(463);
			match(T__26);
			setState(466);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(464);
				booleanLiteral();
				}
				break;
			case 2:
				{
				setState(465);
				modification();
				}
				break;
			}
			setState(468);
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
		enterRule(_localctx, 102, RULE_durativeEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				{
				setState(470);
				atStartEffect();
				}
				break;
			case 2:
				{
				setState(471);
				overAllEffect();
				}
				break;
			case 3:
				{
				setState(472);
				atEndEffect();
				}
				break;
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
		enterRule(_localctx, 104, RULE_andDurativeEffect);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(475);
			match(LP);
			setState(476);
			match(T__22);
			setState(478); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(477);
				durativeEffect();
				}
				}
				setState(480); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP );
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
		enterRule(_localctx, 106, RULE_durativeEffects);
		try {
			setState(486);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(484);
				durativeEffect();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(485);
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
		enterRule(_localctx, 108, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(488);
			match(LP);
			setState(492);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(489);
				typedAtomParameter();
				}
				}
				setState(494);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(495);
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
		enterRule(_localctx, 110, RULE_opName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(497);
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
		enterRule(_localctx, 112, RULE_opParameters);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(499);
			match(T__28);
			setState(500);
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
		enterRule(_localctx, 114, RULE_opPrecondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(502);
			match(T__29);
			setState(503);
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
		enterRule(_localctx, 116, RULE_opDurativeCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(505);
			match(T__30);
			setState(506);
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
		enterRule(_localctx, 118, RULE_opEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(508);
			match(T__31);
			setState(509);
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
		enterRule(_localctx, 120, RULE_opDurativeEffect);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(511);
			match(T__31);
			setState(512);
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
		enterRule(_localctx, 122, RULE_opDuration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(514);
			match(T__32);
			setState(515);
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
		enterRule(_localctx, 124, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			match(LP);
			setState(518);
			match(T__33);
			setState(519);
			opName();
			setState(521);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28) {
				{
				setState(520);
				opParameters();
				}
			}

			setState(524);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(523);
				opPrecondition();
				}
			}

			setState(526);
			opEffect();
			setState(527);
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
		enterRule(_localctx, 126, RULE_durativeAction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(529);
			match(LP);
			setState(530);
			match(T__34);
			setState(531);
			opName();
			setState(533);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28) {
				{
				setState(532);
				opParameters();
				}
			}

			setState(536);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(535);
				opDuration();
				}
			}

			setState(539);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__30) {
				{
				setState(538);
				opDurativeCondition();
				}
			}

			setState(541);
			opDurativeEffect();
			setState(542);
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
		enterRule(_localctx, 128, RULE_event);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(544);
			match(LP);
			setState(545);
			match(T__35);
			setState(546);
			opName();
			setState(548);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28) {
				{
				setState(547);
				opParameters();
				}
			}

			setState(551);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(550);
				opPrecondition();
				}
			}

			setState(553);
			opEffect();
			setState(554);
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
		enterRule(_localctx, 130, RULE_process);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			match(LP);
			setState(557);
			match(T__36);
			setState(558);
			opName();
			setState(560);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28) {
				{
				setState(559);
				opParameters();
				}
			}

			setState(563);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(562);
				opPrecondition();
				}
			}

			setState(565);
			opEffect();
			setState(566);
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
		enterRule(_localctx, 132, RULE_problem);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(568);
			match(LP);
			setState(569);
			match(T__0);
			setState(570);
			problemName();
			setState(571);
			problemDomain();
			setState(573);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
			case 1:
				{
				setState(572);
				objects();
				}
				break;
			}
			setState(575);
			init();
			setState(576);
			goal();
			setState(578);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LP) {
				{
				setState(577);
				metric();
				}
			}

			setState(580);
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
		enterRule(_localctx, 134, RULE_problemName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(582);
			match(LP);
			setState(583);
			match(T__37);
			setState(584);
			match(NAME);
			setState(585);
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
		enterRule(_localctx, 136, RULE_problemDomain);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(587);
			match(LP);
			setState(588);
			match(T__38);
			setState(589);
			match(NAME);
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
		enterRule(_localctx, 138, RULE_typedObjects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(593); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(592);
				groundAtomParameter();
				}
				}
				setState(595); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NAME );
			setState(597);
			match(T__4);
			setState(598);
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
		enterRule(_localctx, 140, RULE_objects);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(600);
			match(LP);
			setState(601);
			match(T__39);
			setState(605);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NAME) {
				{
				{
				setState(602);
				typedObjects();
				}
				}
				setState(607);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(608);
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
		enterRule(_localctx, 142, RULE_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(610);
			match(LP);
			setState(611);
			match(T__40);
			setState(614); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(614);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
				case 1:
					{
					setState(612);
					positiveLiteral();
					}
					break;
				case 2:
					{
					setState(613);
					assignment();
					}
					break;
				}
				}
				setState(616); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LP || _la==VAR );
			setState(618);
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
		enterRule(_localctx, 144, RULE_goal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(620);
			match(LP);
			setState(621);
			match(T__41);
			setState(622);
			preconditions();
			setState(623);
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
		enterRule(_localctx, 146, RULE_metric);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(625);
			match(LP);
			setState(626);
			match(T__42);
			setState(627);
			((MetricContext)_localctx).sign = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__43 || _la==T__44) ) {
				((MetricContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(628);
			((MetricContext)_localctx).op = operationSide();
			setState(629);
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
		"\u0004\u00014\u0278\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0001\u0000\u0001\u0000"+
		"\u0003\u0000\u0097\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001\u009d\b\u0001\u0001\u0001\u0003\u0001\u00a0\b\u0001\u0001"+
		"\u0001\u0003\u0001\u00a3\b\u0001\u0001\u0001\u0003\u0001\u00a6\b\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u00ac\b\u0001"+
		"\n\u0001\f\u0001\u00af\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00be\b\u0004\n"+
		"\u0004\f\u0004\u00c1\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007\u00cb"+
		"\b\u0007\u000b\u0007\f\u0007\u00cc\u0001\u0007\u0005\u0007\u00d0\b\u0007"+
		"\n\u0007\f\u0007\u00d3\t\u0007\u0001\b\u0001\b\u0001\b\u0004\b\u00d8\b"+
		"\b\u000b\b\f\b\u00d9\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0004\f\u00e5\b\f\u000b\f\f\f\u00e6\u0001\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0003\r\u00ee\b\r\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u00f2\b\u000e\n\u000e\f\u000e\u00f5\t\u000e\u0001\u000f\u0001"+
		"\u000f\u0005\u000f\u00f9\b\u000f\n\u000f\f\u000f\u00fc\t\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0103\b\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0003\u0013"+
		"\u0110\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0004\u0014\u0115\b"+
		"\u0014\u000b\u0014\f\u0014\u0116\u0001\u0014\u0001\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0004\u0015\u011e\b\u0015\u000b\u0015\f\u0015\u011f"+
		"\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0003\u001b\u0130\b\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0137\b\u001d\u0001\u001e"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001#"+
		"\u0001#\u0001#\u0001$\u0001$\u0003$\u015e\b$\u0001%\u0001%\u0001%\u0001"+
		"%\u0001%\u0001%\u0001%\u0004%\u0167\b%\u000b%\f%\u0168\u0001%\u0001%\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0004&\u0174\b&\u000b&\f&"+
		"\u0175\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0004\'\u017d\b\'\u000b\'"+
		"\f\'\u017e\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001"+
		")\u0001)\u0001)\u0003)\u018c\b)\u0001*\u0001*\u0003*\u0190\b*\u0001+\u0001"+
		"+\u0001+\u0001+\u0001+\u0004+\u0197\b+\u000b+\f+\u0198\u0001+\u0001+\u0001"+
		",\u0001,\u0001,\u0001,\u0001,\u0003,\u01a2\b,\u0001,\u0001,\u0001-\u0001"+
		"-\u0001-\u0001-\u0001-\u0003-\u01ab\b-\u0001-\u0001-\u0001.\u0001.\u0001"+
		".\u0001.\u0001.\u0003.\u01b4\b.\u0001.\u0001.\u0001/\u0001/\u0001/\u0001"+
		"/\u0001/\u0003/\u01bd\b/\u00010\u00010\u00010\u00010\u00030\u01c3\b0\u0001"+
		"0\u00010\u00011\u00011\u00011\u00011\u00031\u01cb\b1\u00011\u00011\u0001"+
		"2\u00012\u00012\u00012\u00032\u01d3\b2\u00012\u00012\u00013\u00013\u0001"+
		"3\u00033\u01da\b3\u00014\u00014\u00014\u00044\u01df\b4\u000b4\f4\u01e0"+
		"\u00014\u00014\u00015\u00015\u00035\u01e7\b5\u00016\u00016\u00056\u01eb"+
		"\b6\n6\f6\u01ee\t6\u00016\u00016\u00017\u00017\u00018\u00018\u00018\u0001"+
		"9\u00019\u00019\u0001:\u0001:\u0001:\u0001;\u0001;\u0001;\u0001<\u0001"+
		"<\u0001<\u0001=\u0001=\u0001=\u0001>\u0001>\u0001>\u0001>\u0003>\u020a"+
		"\b>\u0001>\u0003>\u020d\b>\u0001>\u0001>\u0001>\u0001?\u0001?\u0001?\u0001"+
		"?\u0003?\u0216\b?\u0001?\u0003?\u0219\b?\u0001?\u0003?\u021c\b?\u0001"+
		"?\u0001?\u0001?\u0001@\u0001@\u0001@\u0001@\u0003@\u0225\b@\u0001@\u0003"+
		"@\u0228\b@\u0001@\u0001@\u0001@\u0001A\u0001A\u0001A\u0001A\u0003A\u0231"+
		"\bA\u0001A\u0003A\u0234\bA\u0001A\u0001A\u0001A\u0001B\u0001B\u0001B\u0001"+
		"B\u0001B\u0003B\u023e\bB\u0001B\u0001B\u0001B\u0003B\u0243\bB\u0001B\u0001"+
		"B\u0001C\u0001C\u0001C\u0001C\u0001C\u0001D\u0001D\u0001D\u0001D\u0001"+
		"D\u0001E\u0004E\u0252\bE\u000bE\fE\u0253\u0001E\u0001E\u0001E\u0001F\u0001"+
		"F\u0001F\u0005F\u025c\bF\nF\fF\u025f\tF\u0001F\u0001F\u0001G\u0001G\u0001"+
		"G\u0001G\u0004G\u0267\bG\u000bG\fG\u0268\u0001G\u0001G\u0001H\u0001H\u0001"+
		"H\u0001H\u0001H\u0001I\u0001I\u0001I\u0001I\u0001I\u0001I\u0001I\u0000"+
		"\u0000J\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080"+
		"\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0000\u0004\u0001"+
		"\u0000\n\f\u0002\u0000\u0005\u0005\r\u000f\u0001\u0000\u0010\u0014\u0001"+
		"\u0000,-\u027b\u0000\u0096\u0001\u0000\u0000\u0000\u0002\u0098\u0001\u0000"+
		"\u0000\u0000\u0004\u00b2\u0001\u0000\u0000\u0000\u0006\u00b7\u0001\u0000"+
		"\u0000\u0000\b\u00ba\u0001\u0000\u0000\u0000\n\u00c4\u0001\u0000\u0000"+
		"\u0000\f\u00c7\u0001\u0000\u0000\u0000\u000e\u00ca\u0001\u0000\u0000\u0000"+
		"\u0010\u00d4\u0001\u0000\u0000\u0000\u0012\u00dd\u0001\u0000\u0000\u0000"+
		"\u0014\u00df\u0001\u0000\u0000\u0000\u0016\u00e1\u0001\u0000\u0000\u0000"+
		"\u0018\u00e4\u0001\u0000\u0000\u0000\u001a\u00ed\u0001\u0000\u0000\u0000"+
		"\u001c\u00ef\u0001\u0000\u0000\u0000\u001e\u00f6\u0001\u0000\u0000\u0000"+
		" \u0102\u0001\u0000\u0000\u0000\"\u0104\u0001\u0000\u0000\u0000$\u0108"+
		"\u0001\u0000\u0000\u0000&\u010f\u0001\u0000\u0000\u0000(\u0111\u0001\u0000"+
		"\u0000\u0000*\u011a\u0001\u0000\u0000\u0000,\u0123\u0001\u0000\u0000\u0000"+
		".\u0125\u0001\u0000\u0000\u00000\u0127\u0001\u0000\u0000\u00002\u0129"+
		"\u0001\u0000\u0000\u00004\u012b\u0001\u0000\u0000\u00006\u012f\u0001\u0000"+
		"\u0000\u00008\u0131\u0001\u0000\u0000\u0000:\u0136\u0001\u0000\u0000\u0000"+
		"<\u0138\u0001\u0000\u0000\u0000>\u013e\u0001\u0000\u0000\u0000@\u0144"+
		"\u0001\u0000\u0000\u0000B\u014a\u0001\u0000\u0000\u0000D\u0150\u0001\u0000"+
		"\u0000\u0000F\u0155\u0001\u0000\u0000\u0000H\u015d\u0001\u0000\u0000\u0000"+
		"J\u015f\u0001\u0000\u0000\u0000L\u016c\u0001\u0000\u0000\u0000N\u0179"+
		"\u0001\u0000\u0000\u0000P\u0182\u0001\u0000\u0000\u0000R\u018b\u0001\u0000"+
		"\u0000\u0000T\u018f\u0001\u0000\u0000\u0000V\u0191\u0001\u0000\u0000\u0000"+
		"X\u019c\u0001\u0000\u0000\u0000Z\u01a5\u0001\u0000\u0000\u0000\\\u01ae"+
		"\u0001\u0000\u0000\u0000^\u01bc\u0001\u0000\u0000\u0000`\u01be\u0001\u0000"+
		"\u0000\u0000b\u01c6\u0001\u0000\u0000\u0000d\u01ce\u0001\u0000\u0000\u0000"+
		"f\u01d9\u0001\u0000\u0000\u0000h\u01db\u0001\u0000\u0000\u0000j\u01e6"+
		"\u0001\u0000\u0000\u0000l\u01e8\u0001\u0000\u0000\u0000n\u01f1\u0001\u0000"+
		"\u0000\u0000p\u01f3\u0001\u0000\u0000\u0000r\u01f6\u0001\u0000\u0000\u0000"+
		"t\u01f9\u0001\u0000\u0000\u0000v\u01fc\u0001\u0000\u0000\u0000x\u01ff"+
		"\u0001\u0000\u0000\u0000z\u0202\u0001\u0000\u0000\u0000|\u0205\u0001\u0000"+
		"\u0000\u0000~\u0211\u0001\u0000\u0000\u0000\u0080\u0220\u0001\u0000\u0000"+
		"\u0000\u0082\u022c\u0001\u0000\u0000\u0000\u0084\u0238\u0001\u0000\u0000"+
		"\u0000\u0086\u0246\u0001\u0000\u0000\u0000\u0088\u024b\u0001\u0000\u0000"+
		"\u0000\u008a\u0251\u0001\u0000\u0000\u0000\u008c\u0258\u0001\u0000\u0000"+
		"\u0000\u008e\u0262\u0001\u0000\u0000\u0000\u0090\u026c\u0001\u0000\u0000"+
		"\u0000\u0092\u0271\u0001\u0000\u0000\u0000\u0094\u0097\u0003\u0002\u0001"+
		"\u0000\u0095\u0097\u0003\u0084B\u0000\u0096\u0094\u0001\u0000\u0000\u0000"+
		"\u0096\u0095\u0001\u0000\u0000\u0000\u0097\u0001\u0001\u0000\u0000\u0000"+
		"\u0098\u0099\u0005.\u0000\u0000\u0099\u009a\u0005\u0001\u0000\u0000\u009a"+
		"\u009c\u0003\u0004\u0002\u0000\u009b\u009d\u0003\b\u0004\u0000\u009c\u009b"+
		"\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009f"+
		"\u0001\u0000\u0000\u0000\u009e\u00a0\u0003\u0010\b\u0000\u009f\u009e\u0001"+
		"\u0000\u0000\u0000\u009f\u00a0\u0001\u0000\u0000\u0000\u00a0\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a1\u00a3\u0003(\u0014\u0000\u00a2\u00a1\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a5\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a6\u0003*\u0015\u0000\u00a5\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00ad\u0001\u0000\u0000"+
		"\u0000\u00a7\u00ac\u0003|>\u0000\u00a8\u00ac\u0003~?\u0000\u00a9\u00ac"+
		"\u0003\u0080@\u0000\u00aa\u00ac\u0003\u0082A\u0000\u00ab\u00a7\u0001\u0000"+
		"\u0000\u0000\u00ab\u00a8\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000\u0000\u00ac\u00af\u0001\u0000"+
		"\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000"+
		"\u0000\u0000\u00ae\u00b0\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b1\u0005/\u0000\u0000\u00b1\u0003\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b3\u0005.\u0000\u0000\u00b3\u00b4\u0005\u0002\u0000\u0000"+
		"\u00b4\u00b5\u00051\u0000\u0000\u00b5\u00b6\u0005/\u0000\u0000\u00b6\u0005"+
		"\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005\u0003\u0000\u0000\u00b8\u00b9"+
		"\u00051\u0000\u0000\u00b9\u0007\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005"+
		".\u0000\u0000\u00bb\u00bf\u0005\u0004\u0000\u0000\u00bc\u00be\u0003\u0006"+
		"\u0003\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00be\u00c1\u0001\u0000"+
		"\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000"+
		"\u0000\u0000\u00c0\u00c2\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000"+
		"\u0000\u0000\u00c2\u00c3\u0005/\u0000\u0000\u00c3\t\u0001\u0000\u0000"+
		"\u0000\u00c4\u00c5\u0005\u0005\u0000\u0000\u00c5\u00c6\u0003\f\u0006\u0000"+
		"\u00c6\u000b\u0001\u0000\u0000\u0000\u00c7\u00c8\u00051\u0000\u0000\u00c8"+
		"\r\u0001\u0000\u0000\u0000\u00c9\u00cb\u0003\f\u0006\u0000\u00ca\u00c9"+
		"\u0001\u0000\u0000\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000\u00cd\u00d1"+
		"\u0001\u0000\u0000\u0000\u00ce\u00d0\u0003\n\u0005\u0000\u00cf\u00ce\u0001"+
		"\u0000\u0000\u0000\u00d0\u00d3\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001"+
		"\u0000\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u000f\u0001"+
		"\u0000\u0000\u0000\u00d3\u00d1\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005"+
		".\u0000\u0000\u00d5\u00d7\u0005\u0006\u0000\u0000\u00d6\u00d8\u0003\u000e"+
		"\u0007\u0000\u00d7\u00d6\u0001\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000"+
		"\u0000\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000"+
		"\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db\u00dc\u0005/\u0000"+
		"\u0000\u00dc\u0011\u0001\u0000\u0000\u0000\u00dd\u00de\u00051\u0000\u0000"+
		"\u00de\u0013\u0001\u0000\u0000\u0000\u00df\u00e0\u00051\u0000\u0000\u00e0"+
		"\u0015\u0001\u0000\u0000\u0000\u00e1\u00e2\u00050\u0000\u0000\u00e2\u0017"+
		"\u0001\u0000\u0000\u0000\u00e3\u00e5\u0003\u0016\u000b\u0000\u00e4\u00e3"+
		"\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000\u0000\u00e6\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001\u0000\u0000\u0000\u00e7\u00e8"+
		"\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005\u0005\u0000\u0000\u00e9\u00ea"+
		"\u0003\f\u0006\u0000\u00ea\u0019\u0001\u0000\u0000\u0000\u00eb\u00ee\u0003"+
		"\u0016\u000b\u0000\u00ec\u00ee\u0003\u0014\n\u0000\u00ed\u00eb\u0001\u0000"+
		"\u0000\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ee\u001b\u0001\u0000"+
		"\u0000\u0000\u00ef\u00f3\u0003\u0012\t\u0000\u00f0\u00f2\u0003\u001a\r"+
		"\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000\u00f2\u00f5\u0001\u0000\u0000"+
		"\u0000\u00f3\u00f1\u0001\u0000\u0000\u0000\u00f3\u00f4\u0001\u0000\u0000"+
		"\u0000\u00f4\u001d\u0001\u0000\u0000\u0000\u00f5\u00f3\u0001\u0000\u0000"+
		"\u0000\u00f6\u00fa\u0003\u0012\t\u0000\u00f7\u00f9\u0003\u0018\f\u0000"+
		"\u00f8\u00f7\u0001\u0000\u0000\u0000\u00f9\u00fc\u0001\u0000\u0000\u0000"+
		"\u00fa\u00f8\u0001\u0000\u0000\u0000\u00fa\u00fb\u0001\u0000\u0000\u0000"+
		"\u00fb\u001f\u0001\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000"+
		"\u00fd\u00fe\u0005.\u0000\u0000\u00fe\u00ff\u0003\u001c\u000e\u0000\u00ff"+
		"\u0100\u0005/\u0000\u0000\u0100\u0103\u0001\u0000\u0000\u0000\u0101\u0103"+
		"\u0003\u0016\u000b\u0000\u0102\u00fd\u0001\u0000\u0000\u0000\u0102\u0101"+
		"\u0001\u0000\u0000\u0000\u0103!\u0001\u0000\u0000\u0000\u0104\u0105\u0005"+
		".\u0000\u0000\u0105\u0106\u0003\u001e\u000f\u0000\u0106\u0107\u0005/\u0000"+
		"\u0000\u0107#\u0001\u0000\u0000\u0000\u0108\u0109\u0005.\u0000\u0000\u0109"+
		"\u010a\u0005\u0007\u0000\u0000\u010a\u010b\u0003 \u0010\u0000\u010b\u010c"+
		"\u0005/\u0000\u0000\u010c%\u0001\u0000\u0000\u0000\u010d\u0110\u0003 "+
		"\u0010\u0000\u010e\u0110\u0003$\u0012\u0000\u010f\u010d\u0001\u0000\u0000"+
		"\u0000\u010f\u010e\u0001\u0000\u0000\u0000\u0110\'\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\u0005.\u0000\u0000\u0112\u0114\u0005\b\u0000\u0000\u0113"+
		"\u0115\u0003\"\u0011\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0115\u0116"+
		"\u0001\u0000\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000\u0116\u0117"+
		"\u0001\u0000\u0000\u0000\u0117\u0118\u0001\u0000\u0000\u0000\u0118\u0119"+
		"\u0005/\u0000\u0000\u0119)\u0001\u0000\u0000\u0000\u011a\u011b\u0005."+
		"\u0000\u0000\u011b\u011d\u0005\t\u0000\u0000\u011c\u011e\u0003\"\u0011"+
		"\u0000\u011d\u011c\u0001\u0000\u0000\u0000\u011e\u011f\u0001\u0000\u0000"+
		"\u0000\u011f\u011d\u0001\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000"+
		"\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u0122\u0005/\u0000\u0000"+
		"\u0122+\u0001\u0000\u0000\u0000\u0123\u0124\u0007\u0000\u0000\u0000\u0124"+
		"-\u0001\u0000\u0000\u0000\u0125\u0126\u0007\u0001\u0000\u0000\u0126/\u0001"+
		"\u0000\u0000\u0000\u0127\u0128\u0007\u0002\u0000\u0000\u01281\u0001\u0000"+
		"\u0000\u0000\u0129\u012a\u00053\u0000\u0000\u012a3\u0001\u0000\u0000\u0000"+
		"\u012b\u012c\u0005\u0015\u0000\u0000\u012c5\u0001\u0000\u0000\u0000\u012d"+
		"\u0130\u00032\u0019\u0000\u012e\u0130\u00034\u001a\u0000\u012f\u012d\u0001"+
		"\u0000\u0000\u0000\u012f\u012e\u0001\u0000\u0000\u0000\u01307\u0001\u0000"+
		"\u0000\u0000\u0131\u0132\u00032\u0019\u0000\u01329\u0001\u0000\u0000\u0000"+
		"\u0133\u0137\u0003<\u001e\u0000\u0134\u0137\u0003 \u0010\u0000\u0135\u0137"+
		"\u00036\u001b\u0000\u0136\u0133\u0001\u0000\u0000\u0000\u0136\u0134\u0001"+
		"\u0000\u0000\u0000\u0136\u0135\u0001\u0000\u0000\u0000\u0137;\u0001\u0000"+
		"\u0000\u0000\u0138\u0139\u0005.\u0000\u0000\u0139\u013a\u0003.\u0017\u0000"+
		"\u013a\u013b\u0003:\u001d\u0000\u013b\u013c\u0003:\u001d\u0000\u013c\u013d"+
		"\u0005/\u0000\u0000\u013d=\u0001\u0000\u0000\u0000\u013e\u013f\u0005."+
		"\u0000\u0000\u013f\u0140\u0005\u0014\u0000\u0000\u0140\u0141\u0003 \u0010"+
		"\u0000\u0141\u0142\u00038\u001c\u0000\u0142\u0143\u0005/\u0000\u0000\u0143"+
		"?\u0001\u0000\u0000\u0000\u0144\u0145\u0005.\u0000\u0000\u0145\u0146\u0005"+
		"\u0014\u0000\u0000\u0146\u0147\u0005\u0016\u0000\u0000\u0147\u0148\u0003"+
		":\u001d\u0000\u0148\u0149\u0005/\u0000\u0000\u0149A\u0001\u0000\u0000"+
		"\u0000\u014a\u014b\u0005.\u0000\u0000\u014b\u014c\u00030\u0018\u0000\u014c"+
		"\u014d\u0003:\u001d\u0000\u014d\u014e\u0003:\u001d\u0000\u014e\u014f\u0005"+
		"/\u0000\u0000\u014fC\u0001\u0000\u0000\u0000\u0150\u0151\u0005.\u0000"+
		"\u0000\u0151\u0152\u0005\u0007\u0000\u0000\u0152\u0153\u0003B!\u0000\u0153"+
		"\u0154\u0005/\u0000\u0000\u0154E\u0001\u0000\u0000\u0000\u0155\u0156\u0005"+
		".\u0000\u0000\u0156\u0157\u0003,\u0016\u0000\u0157\u0158\u0003 \u0010"+
		"\u0000\u0158\u0159\u0003:\u001d\u0000\u0159\u015a\u0005/\u0000\u0000\u015a"+
		"G\u0001\u0000\u0000\u0000\u015b\u015e\u0003&\u0013\u0000\u015c\u015e\u0003"+
		"F#\u0000\u015d\u015b\u0001\u0000\u0000\u0000\u015d\u015c\u0001\u0000\u0000"+
		"\u0000\u015eI\u0001\u0000\u0000\u0000\u015f\u0160\u0005.\u0000\u0000\u0160"+
		"\u0166\u0005\u0017\u0000\u0000\u0161\u0167\u0003J%\u0000\u0162\u0167\u0003"+
		"L&\u0000\u0163\u0167\u0003&\u0013\u0000\u0164\u0167\u0003D\"\u0000\u0165"+
		"\u0167\u0003B!\u0000\u0166\u0161\u0001\u0000\u0000\u0000\u0166\u0162\u0001"+
		"\u0000\u0000\u0000\u0166\u0163\u0001\u0000\u0000\u0000\u0166\u0164\u0001"+
		"\u0000\u0000\u0000\u0166\u0165\u0001\u0000\u0000\u0000\u0167\u0168\u0001"+
		"\u0000\u0000\u0000\u0168\u0166\u0001\u0000\u0000\u0000\u0168\u0169\u0001"+
		"\u0000\u0000\u0000\u0169\u016a\u0001\u0000\u0000\u0000\u016a\u016b\u0005"+
		"/\u0000\u0000\u016bK\u0001\u0000\u0000\u0000\u016c\u016d\u0005.\u0000"+
		"\u0000\u016d\u0173\u0005\u0018\u0000\u0000\u016e\u0174\u0003J%\u0000\u016f"+
		"\u0174\u0003L&\u0000\u0170\u0174\u0003&\u0013\u0000\u0171\u0174\u0003"+
		"D\"\u0000\u0172\u0174\u0003B!\u0000\u0173\u016e\u0001\u0000\u0000\u0000"+
		"\u0173\u016f\u0001\u0000\u0000\u0000\u0173\u0170\u0001\u0000\u0000\u0000"+
		"\u0173\u0171\u0001\u0000\u0000\u0000\u0173\u0172\u0001\u0000\u0000\u0000"+
		"\u0174\u0175\u0001\u0000\u0000\u0000\u0175\u0173\u0001\u0000\u0000\u0000"+
		"\u0175\u0176\u0001\u0000\u0000\u0000\u0176\u0177\u0001\u0000\u0000\u0000"+
		"\u0177\u0178\u0005/\u0000\u0000\u0178M\u0001\u0000\u0000\u0000\u0179\u017a"+
		"\u0005.\u0000\u0000\u017a\u017c\u0005\u0017\u0000\u0000\u017b\u017d\u0003"+
		"H$\u0000\u017c\u017b\u0001\u0000\u0000\u0000\u017d\u017e\u0001\u0000\u0000"+
		"\u0000\u017e\u017c\u0001\u0000\u0000\u0000\u017e\u017f\u0001\u0000\u0000"+
		"\u0000\u017f\u0180\u0001\u0000\u0000\u0000\u0180\u0181\u0005/\u0000\u0000"+
		"\u0181O\u0001\u0000\u0000\u0000\u0182\u0183\u0005.\u0000\u0000\u0183\u0184"+
		"\u0005/\u0000\u0000\u0184Q\u0001\u0000\u0000\u0000\u0185\u018c\u0003J"+
		"%\u0000\u0186\u018c\u0003L&\u0000\u0187\u018c\u0003&\u0013\u0000\u0188"+
		"\u018c\u0003D\"\u0000\u0189\u018c\u0003B!\u0000\u018a\u018c\u0003P(\u0000"+
		"\u018b\u0185\u0001\u0000\u0000\u0000\u018b\u0186\u0001\u0000\u0000\u0000"+
		"\u018b\u0187\u0001\u0000\u0000\u0000\u018b\u0188\u0001\u0000\u0000\u0000"+
		"\u018b\u0189\u0001\u0000\u0000\u0000\u018b\u018a\u0001\u0000\u0000\u0000"+
		"\u018cS\u0001\u0000\u0000\u0000\u018d\u0190\u0003H$\u0000\u018e\u0190"+
		"\u0003N\'\u0000\u018f\u018d\u0001\u0000\u0000\u0000\u018f\u018e\u0001"+
		"\u0000\u0000\u0000\u0190U\u0001\u0000\u0000\u0000\u0191\u0192\u0005.\u0000"+
		"\u0000\u0192\u0196\u0005\u0017\u0000\u0000\u0193\u0197\u0003X,\u0000\u0194"+
		"\u0197\u0003Z-\u0000\u0195\u0197\u0003\\.\u0000\u0196\u0193\u0001\u0000"+
		"\u0000\u0000\u0196\u0194\u0001\u0000\u0000\u0000\u0196\u0195\u0001\u0000"+
		"\u0000\u0000\u0197\u0198\u0001\u0000\u0000\u0000\u0198\u0196\u0001\u0000"+
		"\u0000\u0000\u0198\u0199\u0001\u0000\u0000\u0000\u0199\u019a\u0001\u0000"+
		"\u0000\u0000\u019a\u019b\u0005/\u0000\u0000\u019bW\u0001\u0000\u0000\u0000"+
		"\u019c\u019d\u0005.\u0000\u0000\u019d\u01a1\u0005\u0019\u0000\u0000\u019e"+
		"\u01a2\u0003&\u0013\u0000\u019f\u01a2\u0003D\"\u0000\u01a0\u01a2\u0003"+
		"B!\u0000\u01a1\u019e\u0001\u0000\u0000\u0000\u01a1\u019f\u0001\u0000\u0000"+
		"\u0000\u01a1\u01a0\u0001\u0000\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000"+
		"\u0000\u01a3\u01a4\u0005/\u0000\u0000\u01a4Y\u0001\u0000\u0000\u0000\u01a5"+
		"\u01a6\u0005.\u0000\u0000\u01a6\u01aa\u0005\u001a\u0000\u0000\u01a7\u01ab"+
		"\u0003&\u0013\u0000\u01a8\u01ab\u0003D\"\u0000\u01a9\u01ab\u0003B!\u0000"+
		"\u01aa\u01a7\u0001\u0000\u0000\u0000\u01aa\u01a8\u0001\u0000\u0000\u0000"+
		"\u01aa\u01a9\u0001\u0000\u0000\u0000\u01ab\u01ac\u0001\u0000\u0000\u0000"+
		"\u01ac\u01ad\u0005/\u0000\u0000\u01ad[\u0001\u0000\u0000\u0000\u01ae\u01af"+
		"\u0005.\u0000\u0000\u01af\u01b3\u0005\u001b\u0000\u0000\u01b0\u01b4\u0003"+
		"&\u0013\u0000\u01b1\u01b4\u0003D\"\u0000\u01b2\u01b4\u0003B!\u0000\u01b3"+
		"\u01b0\u0001\u0000\u0000\u0000\u01b3\u01b1\u0001\u0000\u0000\u0000\u01b3"+
		"\u01b2\u0001\u0000\u0000\u0000\u01b4\u01b5\u0001\u0000\u0000\u0000\u01b5"+
		"\u01b6\u0005/\u0000\u0000\u01b6]\u0001\u0000\u0000\u0000\u01b7\u01bd\u0003"+
		"V+\u0000\u01b8\u01bd\u0003X,\u0000\u01b9\u01bd\u0003Z-\u0000\u01ba\u01bd"+
		"\u0003\\.\u0000\u01bb\u01bd\u0003P(\u0000\u01bc\u01b7\u0001\u0000\u0000"+
		"\u0000\u01bc\u01b8\u0001\u0000\u0000\u0000\u01bc\u01b9\u0001\u0000\u0000"+
		"\u0000\u01bc\u01ba\u0001\u0000\u0000\u0000\u01bc\u01bb\u0001\u0000\u0000"+
		"\u0000\u01bd_\u0001\u0000\u0000\u0000\u01be\u01bf\u0005.\u0000\u0000\u01bf"+
		"\u01c2\u0005\u0019\u0000\u0000\u01c0\u01c3\u0003&\u0013\u0000\u01c1\u01c3"+
		"\u0003F#\u0000\u01c2\u01c0\u0001\u0000\u0000\u0000\u01c2\u01c1\u0001\u0000"+
		"\u0000\u0000\u01c3\u01c4\u0001\u0000\u0000\u0000\u01c4\u01c5\u0005/\u0000"+
		"\u0000\u01c5a\u0001\u0000\u0000\u0000\u01c6\u01c7\u0005.\u0000\u0000\u01c7"+
		"\u01ca\u0005\u001c\u0000\u0000\u01c8\u01cb\u0003&\u0013\u0000\u01c9\u01cb"+
		"\u0003F#\u0000\u01ca\u01c8\u0001\u0000\u0000\u0000\u01ca\u01c9\u0001\u0000"+
		"\u0000\u0000\u01cb\u01cc\u0001\u0000\u0000\u0000\u01cc\u01cd\u0005/\u0000"+
		"\u0000\u01cdc\u0001\u0000\u0000\u0000\u01ce\u01cf\u0005.\u0000\u0000\u01cf"+
		"\u01d2\u0005\u001b\u0000\u0000\u01d0\u01d3\u0003&\u0013\u0000\u01d1\u01d3"+
		"\u0003F#\u0000\u01d2\u01d0\u0001\u0000\u0000\u0000\u01d2\u01d1\u0001\u0000"+
		"\u0000\u0000\u01d3\u01d4\u0001\u0000\u0000\u0000\u01d4\u01d5\u0005/\u0000"+
		"\u0000\u01d5e\u0001\u0000\u0000\u0000\u01d6\u01da\u0003`0\u0000\u01d7"+
		"\u01da\u0003b1\u0000\u01d8\u01da\u0003d2\u0000\u01d9\u01d6\u0001\u0000"+
		"\u0000\u0000\u01d9\u01d7\u0001\u0000\u0000\u0000\u01d9\u01d8\u0001\u0000"+
		"\u0000\u0000\u01dag\u0001\u0000\u0000\u0000\u01db\u01dc\u0005.\u0000\u0000"+
		"\u01dc\u01de\u0005\u0017\u0000\u0000\u01dd\u01df\u0003f3\u0000\u01de\u01dd"+
		"\u0001\u0000\u0000\u0000\u01df\u01e0\u0001\u0000\u0000\u0000\u01e0\u01de"+
		"\u0001\u0000\u0000\u0000\u01e0\u01e1\u0001\u0000\u0000\u0000\u01e1\u01e2"+
		"\u0001\u0000\u0000\u0000\u01e2\u01e3\u0005/\u0000\u0000\u01e3i\u0001\u0000"+
		"\u0000\u0000\u01e4\u01e7\u0003f3\u0000\u01e5\u01e7\u0003h4\u0000\u01e6"+
		"\u01e4\u0001\u0000\u0000\u0000\u01e6\u01e5\u0001\u0000\u0000\u0000\u01e7"+
		"k\u0001\u0000\u0000\u0000\u01e8\u01ec\u0005.\u0000\u0000\u01e9\u01eb\u0003"+
		"\u0018\f\u0000\u01ea\u01e9\u0001\u0000\u0000\u0000\u01eb\u01ee\u0001\u0000"+
		"\u0000\u0000\u01ec\u01ea\u0001\u0000\u0000\u0000\u01ec\u01ed\u0001\u0000"+
		"\u0000\u0000\u01ed\u01ef\u0001\u0000\u0000\u0000\u01ee\u01ec\u0001\u0000"+
		"\u0000\u0000\u01ef\u01f0\u0005/\u0000\u0000\u01f0m\u0001\u0000\u0000\u0000"+
		"\u01f1\u01f2\u00051\u0000\u0000\u01f2o\u0001\u0000\u0000\u0000\u01f3\u01f4"+
		"\u0005\u001d\u0000\u0000\u01f4\u01f5\u0003l6\u0000\u01f5q\u0001\u0000"+
		"\u0000\u0000\u01f6\u01f7\u0005\u001e\u0000\u0000\u01f7\u01f8\u0003R)\u0000"+
		"\u01f8s\u0001\u0000\u0000\u0000\u01f9\u01fa\u0005\u001f\u0000\u0000\u01fa"+
		"\u01fb\u0003^/\u0000\u01fbu\u0001\u0000\u0000\u0000\u01fc\u01fd\u0005"+
		" \u0000\u0000\u01fd\u01fe\u0003T*\u0000\u01few\u0001\u0000\u0000\u0000"+
		"\u01ff\u0200\u0005 \u0000\u0000\u0200\u0201\u0003j5\u0000\u0201y\u0001"+
		"\u0000\u0000\u0000\u0202\u0203\u0005!\u0000\u0000\u0203\u0204\u0003@ "+
		"\u0000\u0204{\u0001\u0000\u0000\u0000\u0205\u0206\u0005.\u0000\u0000\u0206"+
		"\u0207\u0005\"\u0000\u0000\u0207\u0209\u0003n7\u0000\u0208\u020a\u0003"+
		"p8\u0000\u0209\u0208\u0001\u0000\u0000\u0000\u0209\u020a\u0001\u0000\u0000"+
		"\u0000\u020a\u020c\u0001\u0000\u0000\u0000\u020b\u020d\u0003r9\u0000\u020c"+
		"\u020b\u0001\u0000\u0000\u0000\u020c\u020d\u0001\u0000\u0000\u0000\u020d"+
		"\u020e\u0001\u0000\u0000\u0000\u020e\u020f\u0003v;\u0000\u020f\u0210\u0005"+
		"/\u0000\u0000\u0210}\u0001\u0000\u0000\u0000\u0211\u0212\u0005.\u0000"+
		"\u0000\u0212\u0213\u0005#\u0000\u0000\u0213\u0215\u0003n7\u0000\u0214"+
		"\u0216\u0003p8\u0000\u0215\u0214\u0001\u0000\u0000\u0000\u0215\u0216\u0001"+
		"\u0000\u0000\u0000\u0216\u0218\u0001\u0000\u0000\u0000\u0217\u0219\u0003"+
		"z=\u0000\u0218\u0217\u0001\u0000\u0000\u0000\u0218\u0219\u0001\u0000\u0000"+
		"\u0000\u0219\u021b\u0001\u0000\u0000\u0000\u021a\u021c\u0003t:\u0000\u021b"+
		"\u021a\u0001\u0000\u0000\u0000\u021b\u021c\u0001\u0000\u0000\u0000\u021c"+
		"\u021d\u0001\u0000\u0000\u0000\u021d\u021e\u0003x<\u0000\u021e\u021f\u0005"+
		"/\u0000\u0000\u021f\u007f\u0001\u0000\u0000\u0000\u0220\u0221\u0005.\u0000"+
		"\u0000\u0221\u0222\u0005$\u0000\u0000\u0222\u0224\u0003n7\u0000\u0223"+
		"\u0225\u0003p8\u0000\u0224\u0223\u0001\u0000\u0000\u0000\u0224\u0225\u0001"+
		"\u0000\u0000\u0000\u0225\u0227\u0001\u0000\u0000\u0000\u0226\u0228\u0003"+
		"r9\u0000\u0227\u0226\u0001\u0000\u0000\u0000\u0227\u0228\u0001\u0000\u0000"+
		"\u0000\u0228\u0229\u0001\u0000\u0000\u0000\u0229\u022a\u0003v;\u0000\u022a"+
		"\u022b\u0005/\u0000\u0000\u022b\u0081\u0001\u0000\u0000\u0000\u022c\u022d"+
		"\u0005.\u0000\u0000\u022d\u022e\u0005%\u0000\u0000\u022e\u0230\u0003n"+
		"7\u0000\u022f\u0231\u0003p8\u0000\u0230\u022f\u0001\u0000\u0000\u0000"+
		"\u0230\u0231\u0001\u0000\u0000\u0000\u0231\u0233\u0001\u0000\u0000\u0000"+
		"\u0232\u0234\u0003r9\u0000\u0233\u0232\u0001\u0000\u0000\u0000\u0233\u0234"+
		"\u0001\u0000\u0000\u0000\u0234\u0235\u0001\u0000\u0000\u0000\u0235\u0236"+
		"\u0003v;\u0000\u0236\u0237\u0005/\u0000\u0000\u0237\u0083\u0001\u0000"+
		"\u0000\u0000\u0238\u0239\u0005.\u0000\u0000\u0239\u023a\u0005\u0001\u0000"+
		"\u0000\u023a\u023b\u0003\u0086C\u0000\u023b\u023d\u0003\u0088D\u0000\u023c"+
		"\u023e\u0003\u008cF\u0000\u023d\u023c\u0001\u0000\u0000\u0000\u023d\u023e"+
		"\u0001\u0000\u0000\u0000\u023e\u023f\u0001\u0000\u0000\u0000\u023f\u0240"+
		"\u0003\u008eG\u0000\u0240\u0242\u0003\u0090H\u0000\u0241\u0243\u0003\u0092"+
		"I\u0000\u0242\u0241\u0001\u0000\u0000\u0000\u0242\u0243\u0001\u0000\u0000"+
		"\u0000\u0243\u0244\u0001\u0000\u0000\u0000\u0244\u0245\u0005/\u0000\u0000"+
		"\u0245\u0085\u0001\u0000\u0000\u0000\u0246\u0247\u0005.\u0000\u0000\u0247"+
		"\u0248\u0005&\u0000\u0000\u0248\u0249\u00051\u0000\u0000\u0249\u024a\u0005"+
		"/\u0000\u0000\u024a\u0087\u0001\u0000\u0000\u0000\u024b\u024c\u0005.\u0000"+
		"\u0000\u024c\u024d\u0005\'\u0000\u0000\u024d\u024e\u00051\u0000\u0000"+
		"\u024e\u024f\u0005/\u0000\u0000\u024f\u0089\u0001\u0000\u0000\u0000\u0250"+
		"\u0252\u0003\u0014\n\u0000\u0251\u0250\u0001\u0000\u0000\u0000\u0252\u0253"+
		"\u0001\u0000\u0000\u0000\u0253\u0251\u0001\u0000\u0000\u0000\u0253\u0254"+
		"\u0001\u0000\u0000\u0000\u0254\u0255\u0001\u0000\u0000\u0000\u0255\u0256"+
		"\u0005\u0005\u0000\u0000\u0256\u0257\u0003\f\u0006\u0000\u0257\u008b\u0001"+
		"\u0000\u0000\u0000\u0258\u0259\u0005.\u0000\u0000\u0259\u025d\u0005(\u0000"+
		"\u0000\u025a\u025c\u0003\u008aE\u0000\u025b\u025a\u0001\u0000\u0000\u0000"+
		"\u025c\u025f\u0001\u0000\u0000\u0000\u025d\u025b\u0001\u0000\u0000\u0000"+
		"\u025d\u025e\u0001\u0000\u0000\u0000\u025e\u0260\u0001\u0000\u0000\u0000"+
		"\u025f\u025d\u0001\u0000\u0000\u0000\u0260\u0261\u0005/\u0000\u0000\u0261"+
		"\u008d\u0001\u0000\u0000\u0000\u0262\u0263\u0005.\u0000\u0000\u0263\u0266"+
		"\u0005)\u0000\u0000\u0264\u0267\u0003 \u0010\u0000\u0265\u0267\u0003>"+
		"\u001f\u0000\u0266\u0264\u0001\u0000\u0000\u0000\u0266\u0265\u0001\u0000"+
		"\u0000\u0000\u0267\u0268\u0001\u0000\u0000\u0000\u0268\u0266\u0001\u0000"+
		"\u0000\u0000\u0268\u0269\u0001\u0000\u0000\u0000\u0269\u026a\u0001\u0000"+
		"\u0000\u0000\u026a\u026b\u0005/\u0000\u0000\u026b\u008f\u0001\u0000\u0000"+
		"\u0000\u026c\u026d\u0005.\u0000\u0000\u026d\u026e\u0005*\u0000\u0000\u026e"+
		"\u026f\u0003R)\u0000\u026f\u0270\u0005/\u0000\u0000\u0270\u0091\u0001"+
		"\u0000\u0000\u0000\u0271\u0272\u0005.\u0000\u0000\u0272\u0273\u0005+\u0000"+
		"\u0000\u0273\u0274\u0007\u0003\u0000\u0000\u0274\u0275\u0003:\u001d\u0000"+
		"\u0275\u0276\u0005/\u0000\u0000\u0276\u0093\u0001\u0000\u0000\u00009\u0096"+
		"\u009c\u009f\u00a2\u00a5\u00ab\u00ad\u00bf\u00cc\u00d1\u00d9\u00e6\u00ed"+
		"\u00f3\u00fa\u0102\u010f\u0116\u011f\u012f\u0136\u015d\u0166\u0168\u0173"+
		"\u0175\u017e\u018b\u018f\u0196\u0198\u01a1\u01aa\u01b3\u01bc\u01c2\u01ca"+
		"\u01d2\u01d9\u01e0\u01e6\u01ec\u0209\u020c\u0215\u0218\u021b\u0224\u0227"+
		"\u0230\u0233\u023d\u0242\u0253\u025d\u0266\u0268";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}