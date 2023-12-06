(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (v_margin) 10.0)
		(= (d) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)