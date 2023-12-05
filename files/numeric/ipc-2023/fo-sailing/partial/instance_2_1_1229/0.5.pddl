(define (problem instance_2_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 b1 - boat
		p0 - person
	)
	(:init
		(= (v b1) 1.0)
		(= (d p0) -370.0)
		(= (y b0) 0.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)