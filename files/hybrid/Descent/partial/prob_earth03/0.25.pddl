(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (ISP) 311.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)