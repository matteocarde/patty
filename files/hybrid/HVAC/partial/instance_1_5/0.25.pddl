(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 k4 k5 - request
	)
	(:init
		(= (air_flow r1) 0.0)
		(= (time) 0.0)
		(= (comfort) 2.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
				(satisfied k3)
				(satisfied k4)
				(satisfied k5)
			)
	)
)