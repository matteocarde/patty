# Generated from pddl.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pddlParser import pddlParser
else:
    from pddlParser import pddlParser

# This class defines a complete listener for a parse tree produced by pddlParser.
class pddlListener(ParseTreeListener):

    # Enter a parse tree produced by pddlParser#pddlDoc.
    def enterPddlDoc(self, ctx:pddlParser.PddlDocContext):
        pass

    # Exit a parse tree produced by pddlParser#pddlDoc.
    def exitPddlDoc(self, ctx:pddlParser.PddlDocContext):
        pass


    # Enter a parse tree produced by pddlParser#domain.
    def enterDomain(self, ctx:pddlParser.DomainContext):
        pass

    # Exit a parse tree produced by pddlParser#domain.
    def exitDomain(self, ctx:pddlParser.DomainContext):
        pass


    # Enter a parse tree produced by pddlParser#domainName.
    def enterDomainName(self, ctx:pddlParser.DomainNameContext):
        pass

    # Exit a parse tree produced by pddlParser#domainName.
    def exitDomainName(self, ctx:pddlParser.DomainNameContext):
        pass


    # Enter a parse tree produced by pddlParser#requireKey.
    def enterRequireKey(self, ctx:pddlParser.RequireKeyContext):
        pass

    # Exit a parse tree produced by pddlParser#requireKey.
    def exitRequireKey(self, ctx:pddlParser.RequireKeyContext):
        pass


    # Enter a parse tree produced by pddlParser#requirements.
    def enterRequirements(self, ctx:pddlParser.RequirementsContext):
        pass

    # Exit a parse tree produced by pddlParser#requirements.
    def exitRequirements(self, ctx:pddlParser.RequirementsContext):
        pass


    # Enter a parse tree produced by pddlParser#parentType.
    def enterParentType(self, ctx:pddlParser.ParentTypeContext):
        pass

    # Exit a parse tree produced by pddlParser#parentType.
    def exitParentType(self, ctx:pddlParser.ParentTypeContext):
        pass


    # Enter a parse tree produced by pddlParser#typeName.
    def enterTypeName(self, ctx:pddlParser.TypeNameContext):
        pass

    # Exit a parse tree produced by pddlParser#typeName.
    def exitTypeName(self, ctx:pddlParser.TypeNameContext):
        pass


    # Enter a parse tree produced by pddlParser#type.
    def enterType(self, ctx:pddlParser.TypeContext):
        pass

    # Exit a parse tree produced by pddlParser#type.
    def exitType(self, ctx:pddlParser.TypeContext):
        pass


    # Enter a parse tree produced by pddlParser#types.
    def enterTypes(self, ctx:pddlParser.TypesContext):
        pass

    # Exit a parse tree produced by pddlParser#types.
    def exitTypes(self, ctx:pddlParser.TypesContext):
        pass


    # Enter a parse tree produced by pddlParser#atomName.
    def enterAtomName(self, ctx:pddlParser.AtomNameContext):
        pass

    # Exit a parse tree produced by pddlParser#atomName.
    def exitAtomName(self, ctx:pddlParser.AtomNameContext):
        pass


    # Enter a parse tree produced by pddlParser#groundAtomParameter.
    def enterGroundAtomParameter(self, ctx:pddlParser.GroundAtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#groundAtomParameter.
    def exitGroundAtomParameter(self, ctx:pddlParser.GroundAtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#liftedAtomParameter.
    def enterLiftedAtomParameter(self, ctx:pddlParser.LiftedAtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#liftedAtomParameter.
    def exitLiftedAtomParameter(self, ctx:pddlParser.LiftedAtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#typedAtomParameter.
    def enterTypedAtomParameter(self, ctx:pddlParser.TypedAtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#typedAtomParameter.
    def exitTypedAtomParameter(self, ctx:pddlParser.TypedAtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#atomParameter.
    def enterAtomParameter(self, ctx:pddlParser.AtomParameterContext):
        pass

    # Exit a parse tree produced by pddlParser#atomParameter.
    def exitAtomParameter(self, ctx:pddlParser.AtomParameterContext):
        pass


    # Enter a parse tree produced by pddlParser#atom.
    def enterAtom(self, ctx:pddlParser.AtomContext):
        pass

    # Exit a parse tree produced by pddlParser#atom.
    def exitAtom(self, ctx:pddlParser.AtomContext):
        pass


    # Enter a parse tree produced by pddlParser#typedAtom.
    def enterTypedAtom(self, ctx:pddlParser.TypedAtomContext):
        pass

    # Exit a parse tree produced by pddlParser#typedAtom.
    def exitTypedAtom(self, ctx:pddlParser.TypedAtomContext):
        pass


    # Enter a parse tree produced by pddlParser#positiveLiteral.
    def enterPositiveLiteral(self, ctx:pddlParser.PositiveLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#positiveLiteral.
    def exitPositiveLiteral(self, ctx:pddlParser.PositiveLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#typedPositiveLiteral.
    def enterTypedPositiveLiteral(self, ctx:pddlParser.TypedPositiveLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#typedPositiveLiteral.
    def exitTypedPositiveLiteral(self, ctx:pddlParser.TypedPositiveLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#negativeLiteral.
    def enterNegativeLiteral(self, ctx:pddlParser.NegativeLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#negativeLiteral.
    def exitNegativeLiteral(self, ctx:pddlParser.NegativeLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:pddlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by pddlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:pddlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by pddlParser#predicates.
    def enterPredicates(self, ctx:pddlParser.PredicatesContext):
        pass

    # Exit a parse tree produced by pddlParser#predicates.
    def exitPredicates(self, ctx:pddlParser.PredicatesContext):
        pass


    # Enter a parse tree produced by pddlParser#functions.
    def enterFunctions(self, ctx:pddlParser.FunctionsContext):
        pass

    # Exit a parse tree produced by pddlParser#functions.
    def exitFunctions(self, ctx:pddlParser.FunctionsContext):
        pass


    # Enter a parse tree produced by pddlParser#modificator.
    def enterModificator(self, ctx:pddlParser.ModificatorContext):
        pass

    # Exit a parse tree produced by pddlParser#modificator.
    def exitModificator(self, ctx:pddlParser.ModificatorContext):
        pass


    # Enter a parse tree produced by pddlParser#operator.
    def enterOperator(self, ctx:pddlParser.OperatorContext):
        pass

    # Exit a parse tree produced by pddlParser#operator.
    def exitOperator(self, ctx:pddlParser.OperatorContext):
        pass


    # Enter a parse tree produced by pddlParser#comparator.
    def enterComparator(self, ctx:pddlParser.ComparatorContext):
        pass

    # Exit a parse tree produced by pddlParser#comparator.
    def exitComparator(self, ctx:pddlParser.ComparatorContext):
        pass


    # Enter a parse tree produced by pddlParser#number.
    def enterNumber(self, ctx:pddlParser.NumberContext):
        pass

    # Exit a parse tree produced by pddlParser#number.
    def exitNumber(self, ctx:pddlParser.NumberContext):
        pass


    # Enter a parse tree produced by pddlParser#delta.
    def enterDelta(self, ctx:pddlParser.DeltaContext):
        pass

    # Exit a parse tree produced by pddlParser#delta.
    def exitDelta(self, ctx:pddlParser.DeltaContext):
        pass


    # Enter a parse tree produced by pddlParser#constant.
    def enterConstant(self, ctx:pddlParser.ConstantContext):
        pass

    # Exit a parse tree produced by pddlParser#constant.
    def exitConstant(self, ctx:pddlParser.ConstantContext):
        pass


    # Enter a parse tree produced by pddlParser#assignmentSide.
    def enterAssignmentSide(self, ctx:pddlParser.AssignmentSideContext):
        pass

    # Exit a parse tree produced by pddlParser#assignmentSide.
    def exitAssignmentSide(self, ctx:pddlParser.AssignmentSideContext):
        pass


    # Enter a parse tree produced by pddlParser#operationSide.
    def enterOperationSide(self, ctx:pddlParser.OperationSideContext):
        pass

    # Exit a parse tree produced by pddlParser#operationSide.
    def exitOperationSide(self, ctx:pddlParser.OperationSideContext):
        pass


    # Enter a parse tree produced by pddlParser#operation.
    def enterOperation(self, ctx:pddlParser.OperationContext):
        pass

    # Exit a parse tree produced by pddlParser#operation.
    def exitOperation(self, ctx:pddlParser.OperationContext):
        pass


    # Enter a parse tree produced by pddlParser#assignment.
    def enterAssignment(self, ctx:pddlParser.AssignmentContext):
        pass

    # Exit a parse tree produced by pddlParser#assignment.
    def exitAssignment(self, ctx:pddlParser.AssignmentContext):
        pass


    # Enter a parse tree produced by pddlParser#durationAssignment.
    def enterDurationAssignment(self, ctx:pddlParser.DurationAssignmentContext):
        pass

    # Exit a parse tree produced by pddlParser#durationAssignment.
    def exitDurationAssignment(self, ctx:pddlParser.DurationAssignmentContext):
        pass


    # Enter a parse tree produced by pddlParser#comparation.
    def enterComparation(self, ctx:pddlParser.ComparationContext):
        pass

    # Exit a parse tree produced by pddlParser#comparation.
    def exitComparation(self, ctx:pddlParser.ComparationContext):
        pass


    # Enter a parse tree produced by pddlParser#negatedComparation.
    def enterNegatedComparation(self, ctx:pddlParser.NegatedComparationContext):
        pass

    # Exit a parse tree produced by pddlParser#negatedComparation.
    def exitNegatedComparation(self, ctx:pddlParser.NegatedComparationContext):
        pass


    # Enter a parse tree produced by pddlParser#modification.
    def enterModification(self, ctx:pddlParser.ModificationContext):
        pass

    # Exit a parse tree produced by pddlParser#modification.
    def exitModification(self, ctx:pddlParser.ModificationContext):
        pass


    # Enter a parse tree produced by pddlParser#ceCond.
    def enterCeCond(self, ctx:pddlParser.CeCondContext):
        pass

    # Exit a parse tree produced by pddlParser#ceCond.
    def exitCeCond(self, ctx:pddlParser.CeCondContext):
        pass


    # Enter a parse tree produced by pddlParser#ceEff.
    def enterCeEff(self, ctx:pddlParser.CeEffContext):
        pass

    # Exit a parse tree produced by pddlParser#ceEff.
    def exitCeEff(self, ctx:pddlParser.CeEffContext):
        pass


    # Enter a parse tree produced by pddlParser#ce.
    def enterCe(self, ctx:pddlParser.CeContext):
        pass

    # Exit a parse tree produced by pddlParser#ce.
    def exitCe(self, ctx:pddlParser.CeContext):
        pass


    # Enter a parse tree produced by pddlParser#forallEffect.
    def enterForallEffect(self, ctx:pddlParser.ForallEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#forallEffect.
    def exitForallEffect(self, ctx:pddlParser.ForallEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#forall.
    def enterForall(self, ctx:pddlParser.ForallContext):
        pass

    # Exit a parse tree produced by pddlParser#forall.
    def exitForall(self, ctx:pddlParser.ForallContext):
        pass


    # Enter a parse tree produced by pddlParser#exists.
    def enterExists(self, ctx:pddlParser.ExistsContext):
        pass

    # Exit a parse tree produced by pddlParser#exists.
    def exitExists(self, ctx:pddlParser.ExistsContext):
        pass


    # Enter a parse tree produced by pddlParser#effect.
    def enterEffect(self, ctx:pddlParser.EffectContext):
        pass

    # Exit a parse tree produced by pddlParser#effect.
    def exitEffect(self, ctx:pddlParser.EffectContext):
        pass


    # Enter a parse tree produced by pddlParser#effectNoCes.
    def enterEffectNoCes(self, ctx:pddlParser.EffectNoCesContext):
        pass

    # Exit a parse tree produced by pddlParser#effectNoCes.
    def exitEffectNoCes(self, ctx:pddlParser.EffectNoCesContext):
        pass


    # Enter a parse tree produced by pddlParser#inequality.
    def enterInequality(self, ctx:pddlParser.InequalityContext):
        pass

    # Exit a parse tree produced by pddlParser#inequality.
    def exitInequality(self, ctx:pddlParser.InequalityContext):
        pass


    # Enter a parse tree produced by pddlParser#andClause.
    def enterAndClause(self, ctx:pddlParser.AndClauseContext):
        pass

    # Exit a parse tree produced by pddlParser#andClause.
    def exitAndClause(self, ctx:pddlParser.AndClauseContext):
        pass


    # Enter a parse tree produced by pddlParser#orClause.
    def enterOrClause(self, ctx:pddlParser.OrClauseContext):
        pass

    # Exit a parse tree produced by pddlParser#orClause.
    def exitOrClause(self, ctx:pddlParser.OrClauseContext):
        pass


    # Enter a parse tree produced by pddlParser#andEffect.
    def enterAndEffect(self, ctx:pddlParser.AndEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#andEffect.
    def exitAndEffect(self, ctx:pddlParser.AndEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#andEffectNoCes.
    def enterAndEffectNoCes(self, ctx:pddlParser.AndEffectNoCesContext):
        pass

    # Exit a parse tree produced by pddlParser#andEffectNoCes.
    def exitAndEffectNoCes(self, ctx:pddlParser.AndEffectNoCesContext):
        pass


    # Enter a parse tree produced by pddlParser#emptyPrecondition.
    def enterEmptyPrecondition(self, ctx:pddlParser.EmptyPreconditionContext):
        pass

    # Exit a parse tree produced by pddlParser#emptyPrecondition.
    def exitEmptyPrecondition(self, ctx:pddlParser.EmptyPreconditionContext):
        pass


    # Enter a parse tree produced by pddlParser#preconditions.
    def enterPreconditions(self, ctx:pddlParser.PreconditionsContext):
        pass

    # Exit a parse tree produced by pddlParser#preconditions.
    def exitPreconditions(self, ctx:pddlParser.PreconditionsContext):
        pass


    # Enter a parse tree produced by pddlParser#effects.
    def enterEffects(self, ctx:pddlParser.EffectsContext):
        pass

    # Exit a parse tree produced by pddlParser#effects.
    def exitEffects(self, ctx:pddlParser.EffectsContext):
        pass


    # Enter a parse tree produced by pddlParser#andDurClause.
    def enterAndDurClause(self, ctx:pddlParser.AndDurClauseContext):
        pass

    # Exit a parse tree produced by pddlParser#andDurClause.
    def exitAndDurClause(self, ctx:pddlParser.AndDurClauseContext):
        pass


    # Enter a parse tree produced by pddlParser#atStartPre.
    def enterAtStartPre(self, ctx:pddlParser.AtStartPreContext):
        pass

    # Exit a parse tree produced by pddlParser#atStartPre.
    def exitAtStartPre(self, ctx:pddlParser.AtStartPreContext):
        pass


    # Enter a parse tree produced by pddlParser#overAllPre.
    def enterOverAllPre(self, ctx:pddlParser.OverAllPreContext):
        pass

    # Exit a parse tree produced by pddlParser#overAllPre.
    def exitOverAllPre(self, ctx:pddlParser.OverAllPreContext):
        pass


    # Enter a parse tree produced by pddlParser#atEndPre.
    def enterAtEndPre(self, ctx:pddlParser.AtEndPreContext):
        pass

    # Exit a parse tree produced by pddlParser#atEndPre.
    def exitAtEndPre(self, ctx:pddlParser.AtEndPreContext):
        pass


    # Enter a parse tree produced by pddlParser#durativeConditions.
    def enterDurativeConditions(self, ctx:pddlParser.DurativeConditionsContext):
        pass

    # Exit a parse tree produced by pddlParser#durativeConditions.
    def exitDurativeConditions(self, ctx:pddlParser.DurativeConditionsContext):
        pass


    # Enter a parse tree produced by pddlParser#atStartEffect.
    def enterAtStartEffect(self, ctx:pddlParser.AtStartEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#atStartEffect.
    def exitAtStartEffect(self, ctx:pddlParser.AtStartEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#overAllEffect.
    def enterOverAllEffect(self, ctx:pddlParser.OverAllEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#overAllEffect.
    def exitOverAllEffect(self, ctx:pddlParser.OverAllEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#atEndEffect.
    def enterAtEndEffect(self, ctx:pddlParser.AtEndEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#atEndEffect.
    def exitAtEndEffect(self, ctx:pddlParser.AtEndEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#durativeEffect.
    def enterDurativeEffect(self, ctx:pddlParser.DurativeEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#durativeEffect.
    def exitDurativeEffect(self, ctx:pddlParser.DurativeEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#andDurativeEffect.
    def enterAndDurativeEffect(self, ctx:pddlParser.AndDurativeEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#andDurativeEffect.
    def exitAndDurativeEffect(self, ctx:pddlParser.AndDurativeEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#durativeEffects.
    def enterDurativeEffects(self, ctx:pddlParser.DurativeEffectsContext):
        pass

    # Exit a parse tree produced by pddlParser#durativeEffects.
    def exitDurativeEffects(self, ctx:pddlParser.DurativeEffectsContext):
        pass


    # Enter a parse tree produced by pddlParser#parameters.
    def enterParameters(self, ctx:pddlParser.ParametersContext):
        pass

    # Exit a parse tree produced by pddlParser#parameters.
    def exitParameters(self, ctx:pddlParser.ParametersContext):
        pass


    # Enter a parse tree produced by pddlParser#opName.
    def enterOpName(self, ctx:pddlParser.OpNameContext):
        pass

    # Exit a parse tree produced by pddlParser#opName.
    def exitOpName(self, ctx:pddlParser.OpNameContext):
        pass


    # Enter a parse tree produced by pddlParser#opParameters.
    def enterOpParameters(self, ctx:pddlParser.OpParametersContext):
        pass

    # Exit a parse tree produced by pddlParser#opParameters.
    def exitOpParameters(self, ctx:pddlParser.OpParametersContext):
        pass


    # Enter a parse tree produced by pddlParser#opPrecondition.
    def enterOpPrecondition(self, ctx:pddlParser.OpPreconditionContext):
        pass

    # Exit a parse tree produced by pddlParser#opPrecondition.
    def exitOpPrecondition(self, ctx:pddlParser.OpPreconditionContext):
        pass


    # Enter a parse tree produced by pddlParser#opDurativeCondition.
    def enterOpDurativeCondition(self, ctx:pddlParser.OpDurativeConditionContext):
        pass

    # Exit a parse tree produced by pddlParser#opDurativeCondition.
    def exitOpDurativeCondition(self, ctx:pddlParser.OpDurativeConditionContext):
        pass


    # Enter a parse tree produced by pddlParser#opEffect.
    def enterOpEffect(self, ctx:pddlParser.OpEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#opEffect.
    def exitOpEffect(self, ctx:pddlParser.OpEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#opDurativeEffect.
    def enterOpDurativeEffect(self, ctx:pddlParser.OpDurativeEffectContext):
        pass

    # Exit a parse tree produced by pddlParser#opDurativeEffect.
    def exitOpDurativeEffect(self, ctx:pddlParser.OpDurativeEffectContext):
        pass


    # Enter a parse tree produced by pddlParser#opDuration.
    def enterOpDuration(self, ctx:pddlParser.OpDurationContext):
        pass

    # Exit a parse tree produced by pddlParser#opDuration.
    def exitOpDuration(self, ctx:pddlParser.OpDurationContext):
        pass


    # Enter a parse tree produced by pddlParser#action.
    def enterAction(self, ctx:pddlParser.ActionContext):
        pass

    # Exit a parse tree produced by pddlParser#action.
    def exitAction(self, ctx:pddlParser.ActionContext):
        pass


    # Enter a parse tree produced by pddlParser#durativeAction.
    def enterDurativeAction(self, ctx:pddlParser.DurativeActionContext):
        pass

    # Exit a parse tree produced by pddlParser#durativeAction.
    def exitDurativeAction(self, ctx:pddlParser.DurativeActionContext):
        pass


    # Enter a parse tree produced by pddlParser#event.
    def enterEvent(self, ctx:pddlParser.EventContext):
        pass

    # Exit a parse tree produced by pddlParser#event.
    def exitEvent(self, ctx:pddlParser.EventContext):
        pass


    # Enter a parse tree produced by pddlParser#process.
    def enterProcess(self, ctx:pddlParser.ProcessContext):
        pass

    # Exit a parse tree produced by pddlParser#process.
    def exitProcess(self, ctx:pddlParser.ProcessContext):
        pass


    # Enter a parse tree produced by pddlParser#constraints.
    def enterConstraints(self, ctx:pddlParser.ConstraintsContext):
        pass

    # Exit a parse tree produced by pddlParser#constraints.
    def exitConstraints(self, ctx:pddlParser.ConstraintsContext):
        pass


    # Enter a parse tree produced by pddlParser#problem.
    def enterProblem(self, ctx:pddlParser.ProblemContext):
        pass

    # Exit a parse tree produced by pddlParser#problem.
    def exitProblem(self, ctx:pddlParser.ProblemContext):
        pass


    # Enter a parse tree produced by pddlParser#problemName.
    def enterProblemName(self, ctx:pddlParser.ProblemNameContext):
        pass

    # Exit a parse tree produced by pddlParser#problemName.
    def exitProblemName(self, ctx:pddlParser.ProblemNameContext):
        pass


    # Enter a parse tree produced by pddlParser#problemDomain.
    def enterProblemDomain(self, ctx:pddlParser.ProblemDomainContext):
        pass

    # Exit a parse tree produced by pddlParser#problemDomain.
    def exitProblemDomain(self, ctx:pddlParser.ProblemDomainContext):
        pass


    # Enter a parse tree produced by pddlParser#typedObjects.
    def enterTypedObjects(self, ctx:pddlParser.TypedObjectsContext):
        pass

    # Exit a parse tree produced by pddlParser#typedObjects.
    def exitTypedObjects(self, ctx:pddlParser.TypedObjectsContext):
        pass


    # Enter a parse tree produced by pddlParser#objects.
    def enterObjects(self, ctx:pddlParser.ObjectsContext):
        pass

    # Exit a parse tree produced by pddlParser#objects.
    def exitObjects(self, ctx:pddlParser.ObjectsContext):
        pass


    # Enter a parse tree produced by pddlParser#init.
    def enterInit(self, ctx:pddlParser.InitContext):
        pass

    # Exit a parse tree produced by pddlParser#init.
    def exitInit(self, ctx:pddlParser.InitContext):
        pass


    # Enter a parse tree produced by pddlParser#goal.
    def enterGoal(self, ctx:pddlParser.GoalContext):
        pass

    # Exit a parse tree produced by pddlParser#goal.
    def exitGoal(self, ctx:pddlParser.GoalContext):
        pass


    # Enter a parse tree produced by pddlParser#metric.
    def enterMetric(self, ctx:pddlParser.MetricContext):
        pass

    # Exit a parse tree produced by pddlParser#metric.
    def exitMetric(self, ctx:pddlParser.MetricContext):
        pass



del pddlParser