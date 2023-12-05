(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (q) 50.0)
		(= (d_margin) 10.0)
		(= (d_final) 300.0)
		(= (g) 9.8)
		(= (d) 0.0)
		(= (M) 10000.0)
		(= (M_min) 5000.0)
		(= (v) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)