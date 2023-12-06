(define (problem instance_1_3_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 p2 - person
	)
	(:init
		(= (v b0) 1.0)
		(= (d p0) -370.0)
		(= (d p1) -58.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
				(saved p2)
			)
	)
)