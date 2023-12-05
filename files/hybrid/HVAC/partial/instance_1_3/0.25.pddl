(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 - request
	)
	(:init
		(= (time) 0.0)
		(= (temp r1) 15.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
				(satisfied k3)
			)
	)
)