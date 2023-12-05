(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(stop)
		(= (M_min) 5000.0)
		(= (v) 0.0)
		(= (d_final) 200.0)
		(= (ISP) 311.0)
		(= (d) 0.0)
		(= (q) 50.0)
		(= (M) 10000.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)