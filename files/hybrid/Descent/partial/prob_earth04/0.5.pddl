(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M) 10000.0)
		(= (d_final) 400.0)
		(= (d_margin) 10.0)
		(= (v_margin) 10.0)
		(= (ISP) 311.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)