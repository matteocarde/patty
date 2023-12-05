(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 k4 - request
	)
	(:init
		(= (air_flow r1) 0.0)
		(= (temp_requested r1 k2) 13.0)
		(= (temp r1) 15.0)
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