(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (v_margin) 10.0)
		(= (M_min) 5000.0)
		(= (ISP) 311.0)
		(= (M) 10000.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)