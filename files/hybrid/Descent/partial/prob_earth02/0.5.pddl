(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(= (ISP) 311.0)
		(= (g) 9.8)
		(= (v_margin) 10.0)
		(= (q) 50.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)