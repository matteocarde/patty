(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_margin) 10.0)
		(stop)
		(= (d) 0.0)
		(= (M) 10000.0)
		(= (M_min) 5000.0)
		(= (v) 0.0)
		(= (g) 9.8)
		(= (d_final) 500.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)