
(define (problem p01-bike)
	(:domain linear-race)
	(:objects
		bike - vehicle
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

		(= (time) 0)
		(= (final_distance) 30000)

		(= (ck) 0)
		(= (tk bike) 0)
		(= (delta bike) 15)

	)

	(:goal
		(and
			(>= (d bike) (* (final_distance) 0.99))
			(<= (d bike) (* (final_distance) 1.01))
			(engine_stopped bike)
			(engine_ok bike)
		)
	)
)