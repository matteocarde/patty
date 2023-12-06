(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (v_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)