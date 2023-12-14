
(define (problem p01-car)
	(:domain linear-race)
	(:objects
		bike car - vehicle
	)

	(:init

		(engine_stopped bike)
		(engine_ok bike)
		(= (d bike) 0.0)
		(= (v bike) 0.0)
		(= (a bike) 0.0)
		(= (max_acceleration bike) 3)
		(= (min_acceleration bike) -20)
		(= (max_speed bike) 55.0)

		(engine_stopped car)
		(engine_ok car)
		(= (d car) 0.0)
		(= (v car) 0.0)
		(= (a car) 0.0)
		(= (max_acceleration car) 20)
		(= (min_acceleration car) -50)
		(= (max_speed car) 200.0)

		(= (final_distance) 30000)
	)

	(:goal
		(and
			(>= (d bike) (* (final_distance) 0.99))
			(<= (d bike) (* (final_distance) 1.01))
			(engine_stopped bike)
			(engine_ok bike)
			(>= (d car) (* (final_distance) 0.99))
			(<= (d car) (* (final_distance) 1.01))
			(engine_stopped car)
			(engine_ok car)
		)
	)
)