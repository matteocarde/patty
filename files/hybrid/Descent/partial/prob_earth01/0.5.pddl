(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_margin) 10.0)
		(= (d) 0.0)
		(= (M) 10000.0)
		(= (d_final) 100.0)
		(= (v_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)