class PDDLException:
    class GoalNotReachable(Exception):
        pass

    class InvalidPlan(Exception):
        pass
