(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(engine_stopped)
		(= (min_acceleration) -1.0)
	)
	(:goal
			(and
				(>= (d) 299.5)
				(<= (d) 300.5)
				(engine_stopped)
			)
	)
)