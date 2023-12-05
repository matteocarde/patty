(define (problem instance_1_5_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 p4 - person
	)
	(:init
		(= (d p2) 63.0)
		(= (d p4) 223.0)
		(= (d p0) -370.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
				(saved p2)
				(saved p3)
				(saved p4)
			)
	)
)