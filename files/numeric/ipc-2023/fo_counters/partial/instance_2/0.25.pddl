(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (rate_value c0) 0.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)