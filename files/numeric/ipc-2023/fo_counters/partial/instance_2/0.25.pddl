(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (value c1) 0.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)