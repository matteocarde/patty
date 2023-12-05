(define (problem descent_prob)
	(:domain descent)
	(:objects
	)
	(:init
		(= (d_final) 93.0)
		(= (d_margin) -1.0)
		(= (v_margin) 3.0)
		(= (v) -8.0)
		(= (d) -12.0)
		(= (g) -5.199999999999999)
		(= (M) 9993.0)
		(= (M_min) 5002.0)
		(= (q) 36.0)
		(= (ISP) 293.0)
		(stop)
	)
	(:goal
			(and
				(landed)
				(not (block))
			)
	)
)