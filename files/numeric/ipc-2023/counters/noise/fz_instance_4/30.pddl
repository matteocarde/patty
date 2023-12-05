(define (problem instance_4)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 - counter
	)
	(:init
		(= (max_int) 19.0)
		(= (value c0) -4.0)
		(= (value c1) -29.0)
		(= (value c2) 24.0)
		(= (value c3) -20.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
				(<= (+ (value c2) 1.0) (value c3))
			)
	)
)