(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (g) 9.8)
		(= (q) 50.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)