(define (problem instance_05)
	(:domain overtaking_car)

	(:objects car1 - car)

	(:init
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (max_acceleration) 10)
		(= (min_acceleration) -10)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 100.5 )
			(<= (d car1) 101.5 )

			(engine_stopped car1)
			(overtaking car1)
			(not (crash_happened))
		)
	)
)
