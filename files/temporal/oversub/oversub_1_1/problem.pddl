(define (problem p_1_1)

	(:domain optional_goals_1_1)

	(:init
		(= (total-cost) 0)
	)

	(:goal
		(and
			(y)
			(g1)
		)
	)

	(:metric minimize
		(total-cost)
	)
)