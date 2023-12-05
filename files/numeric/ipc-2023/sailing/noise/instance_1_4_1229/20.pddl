(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -8.0)
		(= (y b0) 14.0)
		(= (d p0) -353.0)
		(= (d p1) -70.0)
		(= (d p2) 75.0)
		(= (d p3) 473.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
				(saved p2)
				(saved p3)
			)
	)
)