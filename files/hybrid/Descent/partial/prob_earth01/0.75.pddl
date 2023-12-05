(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(stop)
		(= (d) 0.0)
		(= (d_final) 100.0)
		(= (M) 10000.0)
		(= (M_min) 5000.0)
		(= (d_margin) 10.0)
		(= (q) 50.0)
		(= (ISP) 311.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)