(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 97.0)
		(= (d_margin) 7.0)
		(= (v_margin) 13.0)
		(= (v) 8.0)
		(= (d) 3.0)
		(= (g) 8.8)
		(= (M) 9992.0)
		(= (M_min) 4997.0)
		(= (q) 45.0)
		(= (ISP) 305.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)