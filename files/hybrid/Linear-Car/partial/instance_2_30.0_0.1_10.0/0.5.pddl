(define (problem instance_2_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
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