(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 2.0)
		(= (value c0) -9.0)
		(= (value c1) -10.0)
		(= (rate_value c0) -5.0)
		(= (rate_value c1) 2.0)
		(= (total-cost) 8.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)