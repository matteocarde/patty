(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(= (v_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)