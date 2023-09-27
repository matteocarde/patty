(define (problem instance_17)
	(:domain overtaking_car)

	(:objects car1 car2 car3 - car)

	(:init
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 90)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (d car3) 180)
		(= (v car3) 0.0)
		(= (a car3) 0.0)
		(engine_stopped car3)
		(overtaking car3)


		(= (max_acceleration) 3)
		(= (min_acceleration) -3)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 270.5 )
			(<= (d car1) 271.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (overtaking car3))
			(not (crash_happened))
		)
	)
)
