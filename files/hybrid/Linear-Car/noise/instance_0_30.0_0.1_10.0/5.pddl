(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -1.0)
		(= (v) -3.0)
		(engine_stopped)
		(= (a) -5.0)
		(= (max_acceleration) 4.0)
		(= (min_acceleration) 0.0)
		(= (max_speed) 9.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)