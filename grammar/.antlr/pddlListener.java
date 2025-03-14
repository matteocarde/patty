// Generated from /Users/carde/Documents/Workspace/patty/grammar/pddl.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link pddlParser}.
 */
public interface pddlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link pddlParser#pddlDoc}.
	 * @param ctx the parse tree
	 */
	void enterPddlDoc(pddlParser.PddlDocContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#pddlDoc}.
	 * @param ctx the parse tree
	 */
	void exitPddlDoc(pddlParser.PddlDocContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#domain}.
	 * @param ctx the parse tree
	 */
	void enterDomain(pddlParser.DomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#domain}.
	 * @param ctx the parse tree
	 */
	void exitDomain(pddlParser.DomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#domainName}.
	 * @param ctx the parse tree
	 */
	void enterDomainName(pddlParser.DomainNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#domainName}.
	 * @param ctx the parse tree
	 */
	void exitDomainName(pddlParser.DomainNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#requireKey}.
	 * @param ctx the parse tree
	 */
	void enterRequireKey(pddlParser.RequireKeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#requireKey}.
	 * @param ctx the parse tree
	 */
	void exitRequireKey(pddlParser.RequireKeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#requirements}.
	 * @param ctx the parse tree
	 */
	void enterRequirements(pddlParser.RequirementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#requirements}.
	 * @param ctx the parse tree
	 */
	void exitRequirements(pddlParser.RequirementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#parentType}.
	 * @param ctx the parse tree
	 */
	void enterParentType(pddlParser.ParentTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#parentType}.
	 * @param ctx the parse tree
	 */
	void exitParentType(pddlParser.ParentTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#typeName}.
	 * @param ctx the parse tree
	 */
	void enterTypeName(pddlParser.TypeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#typeName}.
	 * @param ctx the parse tree
	 */
	void exitTypeName(pddlParser.TypeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(pddlParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(pddlParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#types}.
	 * @param ctx the parse tree
	 */
	void enterTypes(pddlParser.TypesContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#types}.
	 * @param ctx the parse tree
	 */
	void exitTypes(pddlParser.TypesContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atomName}.
	 * @param ctx the parse tree
	 */
	void enterAtomName(pddlParser.AtomNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atomName}.
	 * @param ctx the parse tree
	 */
	void exitAtomName(pddlParser.AtomNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#groundAtomParameter}.
	 * @param ctx the parse tree
	 */
	void enterGroundAtomParameter(pddlParser.GroundAtomParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#groundAtomParameter}.
	 * @param ctx the parse tree
	 */
	void exitGroundAtomParameter(pddlParser.GroundAtomParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#liftedAtomParameter}.
	 * @param ctx the parse tree
	 */
	void enterLiftedAtomParameter(pddlParser.LiftedAtomParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#liftedAtomParameter}.
	 * @param ctx the parse tree
	 */
	void exitLiftedAtomParameter(pddlParser.LiftedAtomParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#typedAtomParameter}.
	 * @param ctx the parse tree
	 */
	void enterTypedAtomParameter(pddlParser.TypedAtomParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#typedAtomParameter}.
	 * @param ctx the parse tree
	 */
	void exitTypedAtomParameter(pddlParser.TypedAtomParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atomParameter}.
	 * @param ctx the parse tree
	 */
	void enterAtomParameter(pddlParser.AtomParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atomParameter}.
	 * @param ctx the parse tree
	 */
	void exitAtomParameter(pddlParser.AtomParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(pddlParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(pddlParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#typedAtom}.
	 * @param ctx the parse tree
	 */
	void enterTypedAtom(pddlParser.TypedAtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#typedAtom}.
	 * @param ctx the parse tree
	 */
	void exitTypedAtom(pddlParser.TypedAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#positiveLiteral}.
	 * @param ctx the parse tree
	 */
	void enterPositiveLiteral(pddlParser.PositiveLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#positiveLiteral}.
	 * @param ctx the parse tree
	 */
	void exitPositiveLiteral(pddlParser.PositiveLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#typedPositiveLiteral}.
	 * @param ctx the parse tree
	 */
	void enterTypedPositiveLiteral(pddlParser.TypedPositiveLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#typedPositiveLiteral}.
	 * @param ctx the parse tree
	 */
	void exitTypedPositiveLiteral(pddlParser.TypedPositiveLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#negativeLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNegativeLiteral(pddlParser.NegativeLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#negativeLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNegativeLiteral(pddlParser.NegativeLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(pddlParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(pddlParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#predicates}.
	 * @param ctx the parse tree
	 */
	void enterPredicates(pddlParser.PredicatesContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#predicates}.
	 * @param ctx the parse tree
	 */
	void exitPredicates(pddlParser.PredicatesContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#functions}.
	 * @param ctx the parse tree
	 */
	void enterFunctions(pddlParser.FunctionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#functions}.
	 * @param ctx the parse tree
	 */
	void exitFunctions(pddlParser.FunctionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#modificator}.
	 * @param ctx the parse tree
	 */
	void enterModificator(pddlParser.ModificatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#modificator}.
	 * @param ctx the parse tree
	 */
	void exitModificator(pddlParser.ModificatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(pddlParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(pddlParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#comparator}.
	 * @param ctx the parse tree
	 */
	void enterComparator(pddlParser.ComparatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#comparator}.
	 * @param ctx the parse tree
	 */
	void exitComparator(pddlParser.ComparatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(pddlParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(pddlParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#delta}.
	 * @param ctx the parse tree
	 */
	void enterDelta(pddlParser.DeltaContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#delta}.
	 * @param ctx the parse tree
	 */
	void exitDelta(pddlParser.DeltaContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(pddlParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(pddlParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#assignmentSide}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentSide(pddlParser.AssignmentSideContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#assignmentSide}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentSide(pddlParser.AssignmentSideContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#operationSide}.
	 * @param ctx the parse tree
	 */
	void enterOperationSide(pddlParser.OperationSideContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#operationSide}.
	 * @param ctx the parse tree
	 */
	void exitOperationSide(pddlParser.OperationSideContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterOperation(pddlParser.OperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitOperation(pddlParser.OperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(pddlParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(pddlParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#durationAssignment}.
	 * @param ctx the parse tree
	 */
	void enterDurationAssignment(pddlParser.DurationAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#durationAssignment}.
	 * @param ctx the parse tree
	 */
	void exitDurationAssignment(pddlParser.DurationAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#comparation}.
	 * @param ctx the parse tree
	 */
	void enterComparation(pddlParser.ComparationContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#comparation}.
	 * @param ctx the parse tree
	 */
	void exitComparation(pddlParser.ComparationContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#negatedComparation}.
	 * @param ctx the parse tree
	 */
	void enterNegatedComparation(pddlParser.NegatedComparationContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#negatedComparation}.
	 * @param ctx the parse tree
	 */
	void exitNegatedComparation(pddlParser.NegatedComparationContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#modification}.
	 * @param ctx the parse tree
	 */
	void enterModification(pddlParser.ModificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#modification}.
	 * @param ctx the parse tree
	 */
	void exitModification(pddlParser.ModificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#ceCond}.
	 * @param ctx the parse tree
	 */
	void enterCeCond(pddlParser.CeCondContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#ceCond}.
	 * @param ctx the parse tree
	 */
	void exitCeCond(pddlParser.CeCondContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#ceEff}.
	 * @param ctx the parse tree
	 */
	void enterCeEff(pddlParser.CeEffContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#ceEff}.
	 * @param ctx the parse tree
	 */
	void exitCeEff(pddlParser.CeEffContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#ce}.
	 * @param ctx the parse tree
	 */
	void enterCe(pddlParser.CeContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#ce}.
	 * @param ctx the parse tree
	 */
	void exitCe(pddlParser.CeContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#forallEffect}.
	 * @param ctx the parse tree
	 */
	void enterForallEffect(pddlParser.ForallEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#forallEffect}.
	 * @param ctx the parse tree
	 */
	void exitForallEffect(pddlParser.ForallEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#forall}.
	 * @param ctx the parse tree
	 */
	void enterForall(pddlParser.ForallContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#forall}.
	 * @param ctx the parse tree
	 */
	void exitForall(pddlParser.ForallContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#exists}.
	 * @param ctx the parse tree
	 */
	void enterExists(pddlParser.ExistsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#exists}.
	 * @param ctx the parse tree
	 */
	void exitExists(pddlParser.ExistsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#effect}.
	 * @param ctx the parse tree
	 */
	void enterEffect(pddlParser.EffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#effect}.
	 * @param ctx the parse tree
	 */
	void exitEffect(pddlParser.EffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#effectNoCes}.
	 * @param ctx the parse tree
	 */
	void enterEffectNoCes(pddlParser.EffectNoCesContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#effectNoCes}.
	 * @param ctx the parse tree
	 */
	void exitEffectNoCes(pddlParser.EffectNoCesContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#inequality}.
	 * @param ctx the parse tree
	 */
	void enterInequality(pddlParser.InequalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#inequality}.
	 * @param ctx the parse tree
	 */
	void exitInequality(pddlParser.InequalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#andClause}.
	 * @param ctx the parse tree
	 */
	void enterAndClause(pddlParser.AndClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#andClause}.
	 * @param ctx the parse tree
	 */
	void exitAndClause(pddlParser.AndClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#orClause}.
	 * @param ctx the parse tree
	 */
	void enterOrClause(pddlParser.OrClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#orClause}.
	 * @param ctx the parse tree
	 */
	void exitOrClause(pddlParser.OrClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#andEffect}.
	 * @param ctx the parse tree
	 */
	void enterAndEffect(pddlParser.AndEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#andEffect}.
	 * @param ctx the parse tree
	 */
	void exitAndEffect(pddlParser.AndEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#andEffectNoCes}.
	 * @param ctx the parse tree
	 */
	void enterAndEffectNoCes(pddlParser.AndEffectNoCesContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#andEffectNoCes}.
	 * @param ctx the parse tree
	 */
	void exitAndEffectNoCes(pddlParser.AndEffectNoCesContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#emptyPrecondition}.
	 * @param ctx the parse tree
	 */
	void enterEmptyPrecondition(pddlParser.EmptyPreconditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#emptyPrecondition}.
	 * @param ctx the parse tree
	 */
	void exitEmptyPrecondition(pddlParser.EmptyPreconditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#preconditions}.
	 * @param ctx the parse tree
	 */
	void enterPreconditions(pddlParser.PreconditionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#preconditions}.
	 * @param ctx the parse tree
	 */
	void exitPreconditions(pddlParser.PreconditionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#effects}.
	 * @param ctx the parse tree
	 */
	void enterEffects(pddlParser.EffectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#effects}.
	 * @param ctx the parse tree
	 */
	void exitEffects(pddlParser.EffectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#andDurClause}.
	 * @param ctx the parse tree
	 */
	void enterAndDurClause(pddlParser.AndDurClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#andDurClause}.
	 * @param ctx the parse tree
	 */
	void exitAndDurClause(pddlParser.AndDurClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atStartPre}.
	 * @param ctx the parse tree
	 */
	void enterAtStartPre(pddlParser.AtStartPreContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atStartPre}.
	 * @param ctx the parse tree
	 */
	void exitAtStartPre(pddlParser.AtStartPreContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#overAllPre}.
	 * @param ctx the parse tree
	 */
	void enterOverAllPre(pddlParser.OverAllPreContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#overAllPre}.
	 * @param ctx the parse tree
	 */
	void exitOverAllPre(pddlParser.OverAllPreContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atEndPre}.
	 * @param ctx the parse tree
	 */
	void enterAtEndPre(pddlParser.AtEndPreContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atEndPre}.
	 * @param ctx the parse tree
	 */
	void exitAtEndPre(pddlParser.AtEndPreContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#durativeConditions}.
	 * @param ctx the parse tree
	 */
	void enterDurativeConditions(pddlParser.DurativeConditionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#durativeConditions}.
	 * @param ctx the parse tree
	 */
	void exitDurativeConditions(pddlParser.DurativeConditionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atStartEffect}.
	 * @param ctx the parse tree
	 */
	void enterAtStartEffect(pddlParser.AtStartEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atStartEffect}.
	 * @param ctx the parse tree
	 */
	void exitAtStartEffect(pddlParser.AtStartEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#overAllEffect}.
	 * @param ctx the parse tree
	 */
	void enterOverAllEffect(pddlParser.OverAllEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#overAllEffect}.
	 * @param ctx the parse tree
	 */
	void exitOverAllEffect(pddlParser.OverAllEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#atEndEffect}.
	 * @param ctx the parse tree
	 */
	void enterAtEndEffect(pddlParser.AtEndEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#atEndEffect}.
	 * @param ctx the parse tree
	 */
	void exitAtEndEffect(pddlParser.AtEndEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#durativeEffect}.
	 * @param ctx the parse tree
	 */
	void enterDurativeEffect(pddlParser.DurativeEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#durativeEffect}.
	 * @param ctx the parse tree
	 */
	void exitDurativeEffect(pddlParser.DurativeEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#andDurativeEffect}.
	 * @param ctx the parse tree
	 */
	void enterAndDurativeEffect(pddlParser.AndDurativeEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#andDurativeEffect}.
	 * @param ctx the parse tree
	 */
	void exitAndDurativeEffect(pddlParser.AndDurativeEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#durativeEffects}.
	 * @param ctx the parse tree
	 */
	void enterDurativeEffects(pddlParser.DurativeEffectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#durativeEffects}.
	 * @param ctx the parse tree
	 */
	void exitDurativeEffects(pddlParser.DurativeEffectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(pddlParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(pddlParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opName}.
	 * @param ctx the parse tree
	 */
	void enterOpName(pddlParser.OpNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opName}.
	 * @param ctx the parse tree
	 */
	void exitOpName(pddlParser.OpNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opParameters}.
	 * @param ctx the parse tree
	 */
	void enterOpParameters(pddlParser.OpParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opParameters}.
	 * @param ctx the parse tree
	 */
	void exitOpParameters(pddlParser.OpParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opPrecondition}.
	 * @param ctx the parse tree
	 */
	void enterOpPrecondition(pddlParser.OpPreconditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opPrecondition}.
	 * @param ctx the parse tree
	 */
	void exitOpPrecondition(pddlParser.OpPreconditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opDurativeCondition}.
	 * @param ctx the parse tree
	 */
	void enterOpDurativeCondition(pddlParser.OpDurativeConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opDurativeCondition}.
	 * @param ctx the parse tree
	 */
	void exitOpDurativeCondition(pddlParser.OpDurativeConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opEffect}.
	 * @param ctx the parse tree
	 */
	void enterOpEffect(pddlParser.OpEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opEffect}.
	 * @param ctx the parse tree
	 */
	void exitOpEffect(pddlParser.OpEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opDurativeEffect}.
	 * @param ctx the parse tree
	 */
	void enterOpDurativeEffect(pddlParser.OpDurativeEffectContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opDurativeEffect}.
	 * @param ctx the parse tree
	 */
	void exitOpDurativeEffect(pddlParser.OpDurativeEffectContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#opDuration}.
	 * @param ctx the parse tree
	 */
	void enterOpDuration(pddlParser.OpDurationContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#opDuration}.
	 * @param ctx the parse tree
	 */
	void exitOpDuration(pddlParser.OpDurationContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(pddlParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(pddlParser.ActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#durativeAction}.
	 * @param ctx the parse tree
	 */
	void enterDurativeAction(pddlParser.DurativeActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#durativeAction}.
	 * @param ctx the parse tree
	 */
	void exitDurativeAction(pddlParser.DurativeActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#event}.
	 * @param ctx the parse tree
	 */
	void enterEvent(pddlParser.EventContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#event}.
	 * @param ctx the parse tree
	 */
	void exitEvent(pddlParser.EventContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#process}.
	 * @param ctx the parse tree
	 */
	void enterProcess(pddlParser.ProcessContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#process}.
	 * @param ctx the parse tree
	 */
	void exitProcess(pddlParser.ProcessContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#constraints}.
	 * @param ctx the parse tree
	 */
	void enterConstraints(pddlParser.ConstraintsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#constraints}.
	 * @param ctx the parse tree
	 */
	void exitConstraints(pddlParser.ConstraintsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#problem}.
	 * @param ctx the parse tree
	 */
	void enterProblem(pddlParser.ProblemContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#problem}.
	 * @param ctx the parse tree
	 */
	void exitProblem(pddlParser.ProblemContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#problemName}.
	 * @param ctx the parse tree
	 */
	void enterProblemName(pddlParser.ProblemNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#problemName}.
	 * @param ctx the parse tree
	 */
	void exitProblemName(pddlParser.ProblemNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#problemDomain}.
	 * @param ctx the parse tree
	 */
	void enterProblemDomain(pddlParser.ProblemDomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#problemDomain}.
	 * @param ctx the parse tree
	 */
	void exitProblemDomain(pddlParser.ProblemDomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#typedObjects}.
	 * @param ctx the parse tree
	 */
	void enterTypedObjects(pddlParser.TypedObjectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#typedObjects}.
	 * @param ctx the parse tree
	 */
	void exitTypedObjects(pddlParser.TypedObjectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#objects}.
	 * @param ctx the parse tree
	 */
	void enterObjects(pddlParser.ObjectsContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#objects}.
	 * @param ctx the parse tree
	 */
	void exitObjects(pddlParser.ObjectsContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#init}.
	 * @param ctx the parse tree
	 */
	void enterInit(pddlParser.InitContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#init}.
	 * @param ctx the parse tree
	 */
	void exitInit(pddlParser.InitContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#goal}.
	 * @param ctx the parse tree
	 */
	void enterGoal(pddlParser.GoalContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#goal}.
	 * @param ctx the parse tree
	 */
	void exitGoal(pddlParser.GoalContext ctx);
	/**
	 * Enter a parse tree produced by {@link pddlParser#metric}.
	 * @param ctx the parse tree
	 */
	void enterMetric(pddlParser.MetricContext ctx);
	/**
	 * Exit a parse tree produced by {@link pddlParser#metric}.
	 * @param ctx the parse tree
	 */
	void exitMetric(pddlParser.MetricContext ctx);
}