(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (g) 9.8)
		(= (M_min) 5000.0)
		(= (ISP) 311.0)
		(= (v) 0.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)