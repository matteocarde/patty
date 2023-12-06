(define (problem instance_1_2_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 p1 - person
	)
	(:init
		(= (d p0) -370.0)
	)
	(:goal
			(and
				(saved p0)
				(saved p1)
			)
	)
)