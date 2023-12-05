(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -17.0)
		(= (y b0) -16.0)
		(= (d p0) -369.0)
		(= (d p1) -78.0)
		(= (d p2) 69.0)
		(= (d p3) 504.0)
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