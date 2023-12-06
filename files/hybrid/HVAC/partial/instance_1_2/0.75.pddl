(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 - request
	)
	(:init
		(= (temp_requested r1 k2) 14.0)
		(= (temp_requested r1 k1) 20.0)
		(= (air_flow r1) 0.0)
		(= (temp_sa r1) 10.0)
		(= (comfort) 2.0)
		(= (temp r1) 15.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
			)
	)
)