(define (problem instance_18)
	(:domain overtaking_car)

	(:objects car1 car2 car3 - car)

	(:init
(= (ck) 0)
(= (delta) 1)
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 120)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (d car3) 240)
		(= (v car3) 0.0)
		(= (a car3) 0.0)
		(engine_stopped car3)
		(overtaking car3)


		(= (max_acceleration) 4)
		(= (min_acceleration) -4)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 360.5 )
			(<= (d car1) 361.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (overtaking car3))
			(not (crash_happened))
		)
	)
)
