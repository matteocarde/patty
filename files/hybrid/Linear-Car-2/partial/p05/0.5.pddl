(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (a) 0.0)
		(= (max_speed) 100.0)
		(engine_stopped)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)