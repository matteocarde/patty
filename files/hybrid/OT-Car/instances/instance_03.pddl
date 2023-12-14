(define (problem instance_03)
	(:domain overtaking_car)

	(:objects car1 - car)

	(:init
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (max_acceleration) 6)
		(= (min_acceleration) -6)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 60.5 )
			(<= (d car1) 61.5 )

			(engine_stopped car1)
			(overtaking car1)
			(not (crash_happened))
		)
	)
)
