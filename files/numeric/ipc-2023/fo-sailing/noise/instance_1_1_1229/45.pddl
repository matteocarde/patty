(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) 4.0)
		(= (y b0) 31.0)
		(= (v b0) -39.0)
		(= (d p0) -352.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)