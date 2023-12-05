(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 - request
	)
	(:init
		(= (temp r1) 15.0)
		(= (time_requested r1 k1) 10.0)
		(= (temp_requested r1 k1) 20.0)
		(= (comfort) 2.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
			)
	)
)