(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 - request
	)
	(:init
		(= (time_requested r1 k2) 20.0)
		(= (time) 0.0)
		(= (temp_requested r1 k1) 20.0)
		(= (time_requested r1 k1) 10.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
			)
	)
)