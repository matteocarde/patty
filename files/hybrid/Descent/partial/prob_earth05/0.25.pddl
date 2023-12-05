(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 500.0)
		(= (q) 50.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)