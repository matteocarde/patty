
(define (problem p03-bike-car-f1)
	(:domain linear-race)
	(:objects
		bike car f1 - vehicle
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

		(engine_stopped f1)
		(engine_ok f1)
		(= (d f1) 0.0)
		(= (v f1) 0.0)
		(= (a f1) 0.0)
		(= (max_acceleration f1) 40)
		(= (min_acceleration f1) -80)
		(= (max_speed f1) 270.0)

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
			(>= (d f1) (* (final_distance) 0.99))
			(<= (d f1) (* (final_distance) 1.01))
			(engine_stopped f1)
			(engine_ok f1)
		)
	)
)