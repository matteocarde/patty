(define (problem instance_1_6_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 p4 p5 - person
	)
	(:init
		(= (d p5) 316.0)
		(= (d p3) 483.0)
		(= (d p1) -58.0)
		(= (d p4) 223.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
				(saved p2)
				(saved p3)
				(saved p4)
				(saved p5)
			)
	)
)