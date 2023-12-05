(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) -16.0)
		(= (value c0) 6.0)
		(= (value c1) 24.0)
		(= (rate_value c0) 13.0)
		(= (rate_value c1) 17.0)
		(= (total-cost) -19.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)