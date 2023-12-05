(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 17.0)
		(= (value c0) -8.0)
		(= (value c1) 8.0)
		(= (rate_value c0) 6.0)
		(= (rate_value c1) 0.0)
		(= (total-cost) 2.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)