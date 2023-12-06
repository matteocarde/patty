(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (v b0) 1.0)
		(= (y b0) 0.0)
		(= (x b0) 3.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)