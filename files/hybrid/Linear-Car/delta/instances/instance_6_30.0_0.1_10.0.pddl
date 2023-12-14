
(define (problem instance_6_300_01_100)
	(:domain car_linear_mt_sc)
	(:objects

	)

	(:init
		(= (time) 0)
		(= (tk) 0)
		(= (delta) 1)
		(= (d) 0.0)
		(= (v) 0.0)
		(engine_stopped)
		(= (a) 0.0)
		(= (max_acceleration) 6)
		(= (min_acceleration) -6)
		(= (max_speed) 10.0)
	)

	(:goal
		(and
			(>= (d) 299.5)
			(<= (d) 300.5)
			(engine_stopped)
		)
	)
)