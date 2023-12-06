(define (problem instance_2_sled_1)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 - waypoint
	)
	(:init
		(is_next wa2 wa3)
		(= (waypoint_supplies wa2) 0.0)
		(at s1 wa0)
		(is_next wa4 wa5)
	)
	(:goal
			(and
				(at s0 wa5)
				(at s1 wa5)
			)
	)
)