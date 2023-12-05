(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (temp_sa r1) 10.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)