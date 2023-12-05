(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (q) 50.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)