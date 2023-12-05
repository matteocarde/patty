(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 6.0)
		(= (temp_requested r1 k1) 7.0)
		(= (temp r1) -6.0)
		(= (air_flow r1) 11.0)
		(= (temp_sa r1) 24.0)
		(= (time) -20.0)
		(= (comfort) -28.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)