(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 400.0)
		(= (v_margin) 10.0)
		(= (g) 9.8)
		(= (q) 50.0)
		(stop)
		(= (ISP) 311.0)
		(= (d_margin) 10.0)
		(= (v) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)