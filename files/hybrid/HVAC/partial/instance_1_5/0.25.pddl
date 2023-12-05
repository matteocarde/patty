(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 k4 k5 - request
	)
	(:init
		(= (time_requested r1 k1) 10.0)
		(= (temp_requested r1 k2) 14.0)
		(= (temp_sa r1) 10.0)
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