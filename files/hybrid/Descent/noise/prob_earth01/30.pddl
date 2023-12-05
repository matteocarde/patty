(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 117.0)
		(= (d_margin) 18.0)
		(= (v_margin) 34.0)
		(= (v) -26.0)
		(= (d) -16.0)
		(= (g) -4.199999999999999)
		(= (M) 9989.0)
		(= (M_min) 4987.0)
		(= (q) 67.0)
		(= (ISP) 289.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)