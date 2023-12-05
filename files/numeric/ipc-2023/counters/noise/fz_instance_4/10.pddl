(define (problem instance_4)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 - counter
	)
	(:init
		(= (max_int) -2.0)
		(= (value c0) -8.0)
		(= (value c1) 9.0)
		(= (value c2) -3.0)
		(= (value c3) -6.0)
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
				(<= (+ (value c2) 1.0) (value c3))
			)
	)
)