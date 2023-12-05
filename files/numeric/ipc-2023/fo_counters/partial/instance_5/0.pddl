(define (problem instance_5)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 c4 - counter
	)
	(:init
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
				(<= (+ (value c2) 1.0) (value c3))
				(<= (+ (value c3) 1.0) (value c4))
			)
	)
)