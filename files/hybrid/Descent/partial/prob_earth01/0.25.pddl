(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (q) 50.0)
		(= (v_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)