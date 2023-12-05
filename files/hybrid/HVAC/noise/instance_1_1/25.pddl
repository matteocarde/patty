(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 29.0)
		(= (temp_requested r1 k1) 4.0)
		(= (temp r1) 32.0)
		(= (air_flow r1) -4.0)
		(= (temp_sa r1) 3.0)
		(= (time) -24.0)
		(= (comfort) -14.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)