(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M) 10000.0)
		(= (d_final) 100.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)