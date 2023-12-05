(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 7.0)
		(= (temp_requested r1 k1) 20.0)
		(= (temp r1) 23.0)
		(= (air_flow r1) 7.0)
		(= (temp_sa r1) 14.0)
		(= (time) 1.0)
		(= (comfort) -7.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)