(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) -2.0)
		(= (value c0) 45.0)
		(= (value c1) -12.0)
		(= (rate_value c0) 23.0)
		(= (rate_value c1) -46.0)
		(= (total-cost) -24.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)