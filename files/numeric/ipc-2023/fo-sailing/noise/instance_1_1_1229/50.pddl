(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (x b0) -26.0)
		(= (y b0) -46.0)
		(= (v b0) -20.0)
		(= (d p0) -365.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)