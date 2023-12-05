(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) 17.0)
		(= (y b0) 30.0)
		(= (v b0) 35.0)
		(= (d p0) -347.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)