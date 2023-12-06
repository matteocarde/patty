(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d) 0.0)
		(= (v) 0.0)
		(= (d_final) 400.0)
		(= (g) 9.8)
		(= (d_margin) 10.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)