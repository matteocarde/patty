(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M) 10000.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)