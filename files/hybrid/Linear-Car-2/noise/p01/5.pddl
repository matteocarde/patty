(define (problem instance_1_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects
	)
	(:init
		(= (d) -1.0)
		(= (v) -3.0)
		(engine_stopped)
		(= (a) -3.0)
		(= (max_acceleration) 5.0)
		(= (min_acceleration) -6.0)
		(= (max_speed) 104.0)
	)
	(:goal
			(and
				(>= (d) 1000.5)
				(<= (d) 1001.5)
				(engine_stopped)
			)
	)
)