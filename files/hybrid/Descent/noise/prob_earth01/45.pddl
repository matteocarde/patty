(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 126.0)
		(= (d_margin) 29.0)
		(= (v_margin) 6.0)
		(= (v) 18.0)
		(= (d) -19.0)
		(= (g) -0.1999999999999993)
		(= (M) 10033.0)
		(= (M_min) 4975.0)
		(= (q) 80.0)
		(= (ISP) 273.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)