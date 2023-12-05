(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -3.0)
		(= (v) 6.0)
		(engine_stopped)
		(= (a) 2.0)
		(= (max_acceleration) 3.0)
		(= (min_acceleration) -6.0)
		(= (max_speed) 18.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)