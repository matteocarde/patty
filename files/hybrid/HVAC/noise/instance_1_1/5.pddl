(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 11.0)
		(= (temp_requested r1 k1) 21.0)
		(= (temp r1) 16.0)
		(= (air_flow r1) -4.0)
		(= (temp_sa r1) 5.0)
		(= (time) -3.0)
		(= (comfort) 1.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)