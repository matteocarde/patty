
(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	;(:objects  )

	(:init
		(= (d) 0.0)
		(= (v) 0.0)
		(engine_stopped)
		(= (a) 0.0)
		(= (max_acceleration) 1)
		(= (min_acceleration) -1)
		(= (max_speed) 10.0)
	)

	(:goal
		(and
			(>= (d) 1)
			(<= (d) 2)
			(engine_stopped)
		)
	)

)