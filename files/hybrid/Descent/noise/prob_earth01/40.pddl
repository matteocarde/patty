(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 126.0)
		(= (d_margin) 29.0)
		(= (v_margin) 24.0)
		(= (v) 5.0)
		(= (d) 30.0)
		(= (g) 8.8)
		(= (M) 10022.0)
		(= (M_min) 4972.0)
		(= (q) 75.0)
		(= (ISP) 306.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)