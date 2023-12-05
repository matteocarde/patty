(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (v) 0.0)
		(= (min_acceleration) -1.0)
		(= (max_speed) 100.0)
		(= (max_acceleration) 1.0)
		(= (d) 0.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)