(define (problem instance_02)
	(:domain overtaking_car)

	(:objects
		car1 - car
	)

	(:init
		(= (ck) 0)
		(= (delta) 1)
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)

		(= (max_acceleration) 4)
		(= (min_acceleration) -4)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 40.5)
			(<= (d car1) 41.5)

			(engine_stopped car1)
			(overtaking car1)
			(not (crash_happened))
		)
	)
)