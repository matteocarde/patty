(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 4.0)
		(= (v) -26.0)
		(engine_stopped)
		(= (a) -2.0)
		(= (max_acceleration) -34.0)
		(= (min_acceleration) -12.0)
		(= (max_speed) 23.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)