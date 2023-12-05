(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) -17.0)
		(= (y b0) -14.0)
		(= (v b0) 16.0)
		(= (d p0) -366.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)