(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -15.0)
		(= (v) 1.0)
		(engine_stopped)
		(= (a) 8.0)
		(= (max_acceleration) -13.0)
		(= (min_acceleration) -9.0)
		(= (max_speed) 4.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)