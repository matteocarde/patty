(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 k4 - request
	)
	(:init
		(= (temp_requested r1 k3) 20.0)
		(= (temp_requested r1 k4) 13.0)
		(= (time_requested r1 k4) 40.0)
		(= (comfort) 2.0)
		(= (time_requested r1 k3) 30.0)
		(= (air_flow r1) 0.0)
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