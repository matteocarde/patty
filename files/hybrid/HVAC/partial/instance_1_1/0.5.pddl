(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (comfort) 2.0)
		(= (air_flow r1) 0.0)
		(= (time) 0.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)