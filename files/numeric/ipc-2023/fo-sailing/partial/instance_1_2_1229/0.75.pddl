(define (problem instance_1_2_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 - person
	)
	(:init
		(= (y b0) 0.0)
		(= (x b0) 7.0)
		(= (d p1) -58.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
			)
	)
)