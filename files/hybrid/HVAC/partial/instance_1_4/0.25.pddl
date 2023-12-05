(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 k4 - request
	)
	(:init
		(= (time_requested r1 k2) 20.0)
		(= (time_requested r1 k1) 10.0)
		(= (time_requested r1 k3) 30.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
				(satisfied k3)
				(satisfied k4)
			)
	)
)