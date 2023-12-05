(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_margin) 10.0)
		(= (v_margin) 10.0)
		(= (M_min) 5000.0)
		(= (g) 9.8)
		(stop)
		(= (v) 0.0)
		(= (q) 50.0)
		(= (M) 10000.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)