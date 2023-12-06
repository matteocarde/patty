(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_margin) 10.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)