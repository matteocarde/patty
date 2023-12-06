(define (problem instance_2_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 b1 - boat
		p0 - person
	)
	(:init
		(= (y b1) 0.0)
		(= (d p0) -370.0)
		(= (v b0) 1.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)