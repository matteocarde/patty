(define (problem instance_2_sled_2)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 wa6 - waypoint
	)
	(:init
		(is_next wa4 wa5)
		(= (sled_capacity s0) 4.0)
		(= (waypoint_supplies wa0) 1000.0)
		(at s0 wa0)
	)
	(:goal
			(and
				(at s0 wa6)
				(at s1 wa6)
			)
	)
)