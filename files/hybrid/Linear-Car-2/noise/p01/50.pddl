(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -29.0)
		(= (v) -14.0)
		(engine_stopped)
		(= (a) 7.0)
		(= (max_acceleration) -30.0)
		(= (min_acceleration) 13.0)
		(= (max_speed) 101.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)