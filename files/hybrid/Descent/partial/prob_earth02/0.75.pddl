(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (d) 0.0)
		(= (v_margin) 10.0)
		(= (M_min) 5000.0)
		(= (d_margin) 10.0)
		(= (M) 10000.0)
		(stop)
		(= (ISP) 311.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)