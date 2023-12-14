(define (problem instance_08)
	(:domain overtaking_car)

	(:objects car1 car2 - car)

	(:init
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 90)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (max_acceleration) 4)
		(= (min_acceleration) -4)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 180.5 )
			(<= (d car1) 181.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (crash_happened))
		)
	)
)
