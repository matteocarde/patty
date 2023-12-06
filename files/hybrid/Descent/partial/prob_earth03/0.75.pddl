(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d) 0.0)
		(= (v_margin) 10.0)
		(= (d_final) 300.0)
		(= (g) 9.8)
		(= (q) 50.0)
		(= (M) 10000.0)
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