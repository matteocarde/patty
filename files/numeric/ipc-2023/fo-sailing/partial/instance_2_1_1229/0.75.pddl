(define (problem instance_2_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 b1 - boat
		p0 - person
	)
	(:init
		(= (y b1) 0.0)
		(= (v b0) 1.0)
		(= (v b1) 1.0)
		(= (x b0) 3.0)
		(= (y b0) 0.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)