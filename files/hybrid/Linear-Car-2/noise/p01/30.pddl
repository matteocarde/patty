(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -30.0)
		(= (v) 18.0)
		(engine_stopped)
		(= (a) -19.0)
		(= (max_acceleration) -6.0)
		(= (min_acceleration) 28.0)
		(= (max_speed) 91.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)