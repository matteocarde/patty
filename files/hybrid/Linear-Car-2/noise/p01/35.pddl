(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -14.0)
		(= (v) -17.0)
		(engine_stopped)
		(= (a) 16.0)
		(= (max_acceleration) -33.0)
		(= (min_acceleration) -8.0)
		(= (max_speed) 115.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)