(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 9.0)
		(= (value c0) 21.0)
		(= (value c1) 19.0)
		(= (rate_value c0) 16.0)
		(= (rate_value c1) 9.0)
		(= (total-cost) -14.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)