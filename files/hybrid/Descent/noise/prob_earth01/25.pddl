(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 76.0)
		(= (d_margin) 0.0)
		(= (v_margin) 15.0)
		(= (v) -9.0)
		(= (d) -25.0)
		(= (g) 26.8)
		(= (M) 10010.0)
		(= (M_min) 4985.0)
		(= (q) 64.0)
		(= (ISP) 317.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)