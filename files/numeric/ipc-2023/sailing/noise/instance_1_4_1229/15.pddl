(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -22.0)
		(= (y b0) -3.0)
		(= (d p0) -373.0)
		(= (d p1) -56.0)
		(= (d p2) 72.0)
		(= (d p3) 484.0)
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