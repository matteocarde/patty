(define (problem instance_3)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 - counter
	)
	(:init
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
			)
	)
)