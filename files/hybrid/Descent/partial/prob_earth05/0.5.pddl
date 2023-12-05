(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(stop)
		(= (d) 0.0)
		(= (q) 50.0)
		(= (M) 10000.0)
		(= (v_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)