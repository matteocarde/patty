(define (problem instance_1_4_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 p2 p3 - person
	)
	(:init
		(= (d p0) -370.0)
		(= (x b0) -7.0)
		(= (d p2) 63.0)
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