(define (problem instance_3_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (max_speed) 10.0)
		(= (max_acceleration) 3.0)
		(= (a) 0.0)
	)
	(:goal
			(and
				(>= (d) 299.5)
				(<= (d) 300.5)
				(engine_stopped)
			)
	)
)