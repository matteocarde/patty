
(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	;(:objects  )

	(:init
		(= (d) 0.0)
		(= (v) 0.0)
		(= (a) 0.0)
		(= (D) -1)
		(= (A) 1)
	)

	(:goal
		(and
			(>= (d) 2)
			(<= (d) 4)
			(not (on))
		)
	)

)