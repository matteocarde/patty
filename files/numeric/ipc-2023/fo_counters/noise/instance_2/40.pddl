(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 32.0)
		(= (value c0) 4.0)
		(= (value c1) 23.0)
		(= (rate_value c0) 7.0)
		(= (rate_value c1) 34.0)
		(= (total-cost) 31.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)