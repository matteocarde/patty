(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_margin) 10.0)
		(= (ISP) 311.0)
		(= (q) 50.0)
		(= (v) 0.0)
		(= (M_min) 5000.0)
		(= (d_final) 200.0)
		(= (M) 10000.0)
		(= (g) 9.8)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)