(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 4.0)
		(= (v) -2.0)
		(engine_stopped)
		(= (a) -4.0)
		(= (max_acceleration) -18.0)
		(= (min_acceleration) -8.0)
		(= (max_speed) 92.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)