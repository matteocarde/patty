(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 36.0)
		(= (v) -3.0)
		(engine_stopped)
		(= (a) 35.0)
		(= (max_acceleration) 14.0)
		(= (min_acceleration) 37.0)
		(= (max_speed) 78.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)