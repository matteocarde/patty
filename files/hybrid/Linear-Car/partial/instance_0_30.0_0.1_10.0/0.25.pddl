(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) 0.0)
	)
	(:goal
			(and
				(>= (d) 1.0)
				(<= (d) 2.0)
				(engine_stopped)
			)
	)
)