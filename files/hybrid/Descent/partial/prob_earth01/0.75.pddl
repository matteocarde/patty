(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (g) 9.8)
		(= (d_margin) 10.0)
		(= (d) 0.0)
		(= (d_final) 100.0)
		(= (v_margin) 10.0)
		(= (M_min) 5000.0)
		(stop)
		(= (q) 50.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)