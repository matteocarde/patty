(define (problem instance_5)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 c4 - counter
	)
	(:init
		(= (value c1) 0.0)
		(= (value c3) 0.0)
		(= (rate_value c0) 0.0)
		(= (rate_value c1) 0.0)
		(= (rate_value c4) 0.0)
		(= (value c4) 0.0)
		(= (max_int) 10.0)
		(= (rate_value c2) 0.0)
		(= (value c0) 0.0)
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