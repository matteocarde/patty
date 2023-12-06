(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)