
(define (problem p01-f1)
	(:domain linear-race)
	(:objects
		f1 - vehicle
	)

	(:init
		(engine_stopped f1)
		(engine_ok f1)
		(= (d f1) 0.0)
		(= (v f1) 0.0)
		(= (a f1) 0.0)
		(= (max_acceleration f1) 40)
		(= (min_acceleration f1) -80)
		(= (max_speed f1) 270.0)

		(= (time) 0)
		(= (final_distance) 30000)
	)

	(:goal
		(and
			(>= (d f1) (* (final_distance) 0.99))
			(<= (d f1) (* (final_distance) 1.01))
			(engine_stopped f1)
			(engine_ok f1)
		)
	)
)