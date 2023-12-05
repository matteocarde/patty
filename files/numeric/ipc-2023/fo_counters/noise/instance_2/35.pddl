(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 24.0)
		(= (value c0) -10.0)
		(= (value c1) -4.0)
		(= (rate_value c0) -1.0)
		(= (rate_value c1) 18.0)
		(= (total-cost) -13.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)