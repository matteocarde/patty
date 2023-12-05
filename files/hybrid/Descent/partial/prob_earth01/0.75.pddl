(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v_margin) 10.0)
		(= (v) 0.0)
		(= (ISP) 311.0)
		(= (M) 10000.0)
		(stop)
		(= (M_min) 5000.0)
		(= (g) 9.8)
		(= (d) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)