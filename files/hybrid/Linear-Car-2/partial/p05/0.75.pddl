(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (max_acceleration) 5.0)
		(= (max_speed) 100.0)
		(= (min_acceleration) -5.0)
		(= (d) 0.0)
		(= (v) 0.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)