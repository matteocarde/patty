(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 102.0)
		(= (d_margin) 24.0)
		(= (v_margin) 1.0)
		(= (v) -12.0)
		(= (d) 1.0)
		(= (g) 12.8)
		(= (M) 9965.0)
		(= (M_min) 4957.0)
		(= (q) 7.0)
		(= (ISP) 359.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)