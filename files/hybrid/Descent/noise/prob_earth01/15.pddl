(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 106.0)
		(= (d_margin) 17.0)
		(= (v_margin) 8.0)
		(= (v) -12.0)
		(= (d) 12.0)
		(= (g) -4.199999999999999)
		(= (M) 10001.0)
		(= (M_min) 5000.0)
		(= (q) 36.0)
		(= (ISP) 304.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)