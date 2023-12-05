(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 400.0)
		(= (g) 9.8)
		(= (ISP) 311.0)
		(stop)
		(= (M_min) 5000.0)
		(= (v_margin) 10.0)
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