(define (problem instance_2)
	(:domain fn-counters)
	(:objects
		c0 c1 - counter
	)
	(:init
		(= (max_int) -28.0)
		(= (value c0) -9.0)
		(= (value c1) 10.0)
		(= (rate_value c0) 7.0)
		(= (rate_value c1) -44.0)
		(= (total-cost) -12.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
			)
	)
)