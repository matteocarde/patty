(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time) 0.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)