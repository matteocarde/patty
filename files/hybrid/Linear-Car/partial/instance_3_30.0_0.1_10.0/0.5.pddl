(define (problem instance_3_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(engine_stopped)
		(= (max_acceleration) 3.0)
		(= (max_speed) 10.0)
	)
	(:goal
			(and
				(>= (d) 299.5)
				(<= (d) 300.5)
				(engine_stopped)
			)
	)
)