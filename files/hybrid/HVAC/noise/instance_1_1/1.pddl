(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 9.0)
		(= (temp_requested r1 k1) 20.0)
		(= (temp r1) 14.0)
		(= (air_flow r1) -1.0)
		(= (temp_sa r1) 10.0)
		(= (time) 0.0)
		(= (comfort) 2.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)