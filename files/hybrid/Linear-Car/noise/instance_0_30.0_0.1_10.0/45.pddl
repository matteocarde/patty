(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 37.0)
		(= (v) 40.0)
		(engine_stopped)
		(= (a) 15.0)
		(= (max_acceleration) 6.0)
		(= (min_acceleration) -14.0)
		(= (max_speed) 28.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)