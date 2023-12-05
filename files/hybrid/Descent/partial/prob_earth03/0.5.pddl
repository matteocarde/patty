(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d) 0.0)
		(= (d_final) 300.0)
		(= (M) 10000.0)
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