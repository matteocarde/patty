(define (problem instance_3)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 - counter
	)
	(:init
		(= (value c2) 0.0)
		(= (max_int) 6.0)
		(= (value c1) 0.0)
		(= (total-cost) 0.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
			)
	)
)