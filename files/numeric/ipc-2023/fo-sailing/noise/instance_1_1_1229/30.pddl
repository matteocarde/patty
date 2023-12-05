(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) -9.0)
		(= (y b0) -28.0)
		(= (v b0) 13.0)
		(= (d p0) -376.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)