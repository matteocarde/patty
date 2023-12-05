(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M_min) 5000.0)
		(= (v) 0.0)
		(stop)
		(= (q) 50.0)
		(= (d_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)