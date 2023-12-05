(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 0.0)
		(= (temp_requested r1 k1) 21.0)
		(= (temp r1) 8.0)
		(= (air_flow r1) -14.0)
		(= (temp_sa r1) 14.0)
		(= (time) 2.0)
		(= (comfort) -11.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)