(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 k2 - request
	)
	(:init
		(= (air_flow r1) 0.0)
		(= (temp_sa r1) 10.0)
		(= (temp r1) 15.0)
		(= (time_requested r1 k2) 20.0)
		(= (time_requested r1 k1) 10.0)
		(= (time) 0.0)
	)
	(:goal
			(and
				(satisfied k1)
				(satisfied k2)
			)
	)
)