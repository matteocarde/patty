
(define (problem p01-car)
	(:domain linear-race)
	(:objects
		car - vehicle
	)

	(:init
		(engine_stopped car)
		(engine_ok car)
		(= (d car) 0.0)
		(= (v car) 0.0)
		(= (a car) 0.0)
		(= (max_acceleration car) 20)
		(= (min_acceleration car) -50)
		(= (max_speed car) 200.0)

		(= (time) 0)
		(= (final_distance) 30000)

		(= (ck) 0)
		(= (tk car) 0)
		(= (delta car) 10)

	)

	(:goal
		(and
			(>= (d car) (* (final_distance) 0.99))
			(<= (d car) (* (final_distance) 1.01))
			(engine_stopped car)
			(engine_ok car)
		)
	)
)