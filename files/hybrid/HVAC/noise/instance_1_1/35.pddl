(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 20.0)
		(= (temp_requested r1 k1) -12.0)
		(= (temp r1) 5.0)
		(= (air_flow r1) -7.0)
		(= (temp_sa r1) 18.0)
		(= (time) 18.0)
		(= (comfort) 10.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)