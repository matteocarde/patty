(define (problem instance_04)
	(:domain overtaking_car)

	(:objects car1 - car)

	(:init
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (max_acceleration) 8)
		(= (min_acceleration) -8)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 80.5 )
			(<= (d car1) 81.5 )

			(engine_stopped car1)
			(overtaking car1)
			(not (crash_happened))
		)
	)
)
