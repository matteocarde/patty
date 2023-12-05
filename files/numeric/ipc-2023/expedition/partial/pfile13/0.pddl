(define (problem instance_2_sled_2)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 wa6 - waypoint
	)
	(:init
	)
	(:goal
			(and
				(at s0 wa6)
				(at s1 wa6)
			)
	)
)