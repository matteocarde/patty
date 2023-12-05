(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (max_speed) 10.0)
		(= (max_acceleration) 1.0)
		(= (a) 0.0)
		(= (min_acceleration) -1.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)