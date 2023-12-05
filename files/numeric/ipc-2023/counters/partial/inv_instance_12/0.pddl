(define (problem instance_12)
	(:domain fn-counters)
	(:objects
		c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 - counter
	)
	(:init
	)
	(:goal
			(and
				(<= (+ (value c0) 1.0) (value c1))
				(<= (+ (value c1) 1.0) (value c2))
				(<= (+ (value c2) 1.0) (value c3))
				(<= (+ (value c3) 1.0) (value c4))
				(<= (+ (value c4) 1.0) (value c5))
				(<= (+ (value c5) 1.0) (value c6))
				(<= (+ (value c6) 1.0) (value c7))
				(<= (+ (value c7) 1.0) (value c8))
				(<= (+ (value c8) 1.0) (value c9))
				(<= (+ (value c9) 1.0) (value c10))
				(<= (+ (value c10) 1.0) (value c11))
			)
	)
)