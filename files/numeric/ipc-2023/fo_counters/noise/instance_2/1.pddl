(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) 4.0)
		(= (value c0) -1.0)
		(= (value c1) -1.0)
		(= (rate_value c0) -1.0)
		(= (rate_value c1) -1.0)
		(= (total-cost) 0.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)