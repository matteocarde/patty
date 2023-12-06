(define (problem instance_4_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (a) 0.0)
		(= (max_speed) 10.0)
		(= (max_acceleration) 4.0)
		(= (v) 0.0)
		(= (d) 0.0)
	)
	(:goal
			(and
				(>= (d) 299.5)
				(<= (d) 300.5)
				(engine_stopped)
			)
	)
)