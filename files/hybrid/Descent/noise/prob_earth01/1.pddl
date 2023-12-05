(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 99.0)
		(= (d_margin) 9.0)
		(= (v_margin) 10.0)
		(= (v) -1.0)
		(= (d) -1.0)
		(= (g) 8.8)
		(= (M) 9999.0)
		(= (M_min) 5000.0)
		(= (q) 49.0)
		(= (ISP) 311.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)