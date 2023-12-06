(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (ISP) 311.0)
		(= (M) 10000.0)
		(= (d) 0.0)
		(= (d_margin) 10.0)
		(= (v) 0.0)
		(= (v_margin) 10.0)
		(stop)
		(= (g) 9.8)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)