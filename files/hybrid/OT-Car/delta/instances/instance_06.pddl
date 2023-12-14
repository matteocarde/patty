(define (problem instance_06)
	(:domain overtaking_car)

	(:objects car1 car2 - car)

	(:init
(= (ck) 0)
(= (delta) 1)
		(= (d car1) 0)
		(= (v car1) 0.0)
		(= (a car1) 0.0)
		(engine_stopped car1)


		(= (d car2) 30)
		(= (v car2) 0.0)
		(= (a car2) 0.0)
		(engine_stopped car2)


		(= (max_acceleration) 2)
		(= (min_acceleration) -2)
		(= (max_speed) 10)
	)

	(:goal
		(and
			(>= (d car1) 60.5 )
			(<= (d car1) 61.5 )

			(engine_stopped car1)
			(overtaking car1)
			(overtaking car2)
			(not (crash_happened))
		)
	)
)
