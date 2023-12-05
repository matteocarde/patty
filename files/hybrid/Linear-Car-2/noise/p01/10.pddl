(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 3.0)
		(= (v) 9.0)
		(engine_stopped)
		(= (a) 3.0)
		(= (max_acceleration) 6.0)
		(= (min_acceleration) 7.0)
		(= (max_speed) 109.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)