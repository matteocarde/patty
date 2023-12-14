(define (problem instance_13)
	(:domain overtaking_car)

	(:objects car1 car2 - car)

	(:init
(= (ck) 0)
(= (delta) 1)
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 240)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (max_acceleration) 9)
		(= (min_acceleration) -9)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 480.5 )
			(<= (d car1) 481.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (crash_happened))
		)
	)
)
