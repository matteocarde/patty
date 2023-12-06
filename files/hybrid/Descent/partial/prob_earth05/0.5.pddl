(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (q) 50.0)
		(= (d_margin) 10.0)
		(= (ISP) 311.0)
		(= (d) 0.0)
		(= (M_min) 5000.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)