(define (problem instance1)
	(:domain hvac)
	(:objects
		r1 - room
		k1 - request
	)
	(:init
		(= (time_requested r1 k1) 7.0)
		(= (temp_requested r1 k1) 27.0)
		(= (temp r1) 18.0)
		(= (air_flow r1) -11.0)
		(= (temp_sa r1) 24.0)
		(= (time) -17.0)
		(= (comfort) 9.0)
	)
	(:goal
			(and
				(satisfied k1)
			)
	)
)