(define (problem instance_1_4_1229)
	(:domain sailing)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -35.0)
		(= (y b0) -11.0)
		(= (d p0) -373.0)
		(= (d p1) -93.0)
		(= (d p2) 75.0)
		(= (d p3) 508.0)
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