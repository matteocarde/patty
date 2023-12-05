(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) 7.0)
		(= (y b0) 6.0)
		(= (v b0) -9.0)
		(= (d p0) -380.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)