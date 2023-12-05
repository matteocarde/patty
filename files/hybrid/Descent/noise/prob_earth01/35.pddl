(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 124.0)
		(= (d_margin) 18.0)
		(= (v_margin) 24.0)
		(= (v) 33.0)
		(= (d) -7.0)
		(= (g) 43.8)
		(= (M) 9981.0)
		(= (M_min) 5026.0)
		(= (q) 46.0)
		(= (ISP) 345.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)