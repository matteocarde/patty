(define (problem instance_14)
	(:domain overtaking_car)

	(:objects car1 car2 - car)

	(:init
(= (ck) 0)
(= (delta) 1)
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 270)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (max_acceleration) 10)
		(= (min_acceleration) -10)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 540.5 )
			(<= (d car1) 541.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (crash_happened))
		)
	)
)
