(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 96.0)
		(= (d_margin) 12.0)
		(= (v_margin) 10.0)
		(= (v) 2.0)
		(= (d) 4.0)
		(= (g) 6.800000000000001)
		(= (M) 9996.0)
		(= (M_min) 4995.0)
		(= (q) 45.0)
		(= (ISP) 308.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)