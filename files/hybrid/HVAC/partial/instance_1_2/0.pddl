(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 - request
	)
	(:init
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
			)
	)
)