(define (problem instance_3_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (max_speed) 10.0)
		(= (d) 0.0)
		(= (v) 0.0)
		(= (a) 0.0)
		(engine_stopped)
	)
	(:goal
			(and
				(>= (d) 299.5)
				(<= (d) 300.5)
				(engine_stopped)
			)
	)
)