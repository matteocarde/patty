(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) 0.0)
		(= (y b0) 19.0)
		(= (v b0) -2.0)
		(= (d p0) -351.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)