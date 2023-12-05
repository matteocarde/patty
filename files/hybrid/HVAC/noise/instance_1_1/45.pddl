(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 8.0)
		(= (temp_requested r1 k1) 29.0)
		(= (temp r1) 19.0)
		(= (air_flow r1) 31.0)
		(= (temp_sa r1) 8.0)
		(= (time) -22.0)
		(= (comfort) 31.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)