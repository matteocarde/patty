(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 4.0)
		(= (value c0) 4.0)
		(= (value c1) 4.0)
		(= (rate_value c0) -3.0)
		(= (rate_value c1) 0.0)
		(= (total-cost) -5.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)