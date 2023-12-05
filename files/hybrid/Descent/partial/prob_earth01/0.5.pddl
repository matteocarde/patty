(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (ISP) 311.0)
		(= (v_margin) 10.0)
		(= (d_final) 100.0)
		(= (d) 0.0)
		(= (d_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)