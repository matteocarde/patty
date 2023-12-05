(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 k3 - request
	)
	(:init
		(= (air_flow r1) 0.0)
		(= (time_requested r1 k3) 30.0)
		(= (temp_requested r1 k2) 14.0)
		(= (temp_requested r1 k1) 20.0)
		(= (time) 0.0)
		(= (time_requested r1 k1) 10.0)
		(= (comfort) 2.0)
		(= (temp_sa r1) 10.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
				(satisfied k3)
			)
	)
)