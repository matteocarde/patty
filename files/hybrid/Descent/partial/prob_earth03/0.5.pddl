(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(= (ISP) 311.0)
		(stop)
		(= (d) 0.0)
		(= (v) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)