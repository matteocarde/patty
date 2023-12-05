(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -11.0)
		(= (y b0) 13.0)
		(= (d p0) -384.0)
		(= (d p1) -18.0)
		(= (d p2) 74.0)
		(= (d p3) 491.0)
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