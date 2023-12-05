(define (problem instance_1_2_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 - person
	)
	(:init
		(= (d p1) -58.0)
		(= (d p0) -370.0)
		(= (y b0) 0.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
			)
	)
)