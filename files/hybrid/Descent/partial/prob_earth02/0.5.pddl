(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (g) 9.8)
		(= (d) 0.0)
		(= (d_margin) 10.0)
		(= (ISP) 311.0)
		(= (d_final) 200.0)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)