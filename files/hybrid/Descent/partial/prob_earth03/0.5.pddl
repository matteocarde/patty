(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (M) 10000.0)
		(= (d_margin) 10.0)
		(stop)
		(= (d_final) 300.0)
		(= (v) 0.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)