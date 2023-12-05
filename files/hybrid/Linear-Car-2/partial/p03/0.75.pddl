(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (min_acceleration) -3.0)
		(= (a) 0.0)
		(engine_stopped)
		(= (d) 0.0)
		(= (max_acceleration) 3.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)