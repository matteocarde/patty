(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) 3.0)
		(= (y b0) -28.0)
		(= (v b0) 34.0)
		(= (d p0) -397.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)