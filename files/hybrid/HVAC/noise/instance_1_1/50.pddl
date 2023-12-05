(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) -25.0)
		(= (temp_requested r1 k1) -17.0)
		(= (temp r1) -6.0)
		(= (air_flow r1) 19.0)
		(= (temp_sa r1) 18.0)
		(= (time) 3.0)
		(= (comfort) -32.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)