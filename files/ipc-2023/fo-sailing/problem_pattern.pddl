(define (problem instance_1_1_1229)
	(:domain sailing_ln)
	(:objects
		b0 - boat
		p0 - person
	)
	(:init
		(= (y b0) 0.0)
		(= (d p0) -370.0)
		(turn_accelerate b0)
		(= (x b0) 3.0)
		(= (v b0) 1.0)
	)
	(:goal
			(and
				(saved p0)
			)
	)
)