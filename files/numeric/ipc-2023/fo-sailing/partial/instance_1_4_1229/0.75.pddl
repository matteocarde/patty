(define (problem instance_1_4_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (x b0) -7.0)
		(= (d p1) -58.0)
		(= (d p3) 483.0)
		(= (y b0) 0.0)
		(= (v b0) 1.0)
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