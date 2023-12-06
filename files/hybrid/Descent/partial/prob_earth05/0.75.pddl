(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(= (v) 0.0)
		(= (v_margin) 10.0)
		(= (g) 9.8)
		(= (d_margin) 10.0)
		(= (d_final) 500.0)
		(stop)
		(= (M) 10000.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)