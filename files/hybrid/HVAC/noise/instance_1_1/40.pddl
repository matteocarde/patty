(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) -20.0)
		(= (temp_requested r1 k1) 21.0)
		(= (temp r1) 50.0)
		(= (air_flow r1) 39.0)
		(= (temp_sa r1) -23.0)
		(= (time) 36.0)
		(= (comfort) 1.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)