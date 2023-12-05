(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -23.0)
		(= (y b0) -39.0)
		(= (d p0) -364.0)
		(= (d p1) -48.0)
		(= (d p2) 90.0)
		(= (d p3) 479.0)
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