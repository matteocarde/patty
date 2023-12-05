(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -46.0)
		(= (v) -41.0)
		(engine_stopped)
		(= (a) -3.0)
		(= (max_acceleration) 19.0)
		(= (min_acceleration) -16.0)
		(= (max_speed) -22.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)