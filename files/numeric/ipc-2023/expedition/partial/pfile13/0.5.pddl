(define (problem instance_2_sled_2)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 wa6 - waypoint
	)
	(:init
		(at s1 wa0)
		(is_next wa0 wa1)
		(= (waypoint_supplies wa6) 0.0)
		(is_next wa2 wa3)
		(is_next wa3 wa4)
		(= (waypoint_supplies wa2) 0.0)
		(is_next wa1 wa2)
		(= (waypoint_supplies wa4) 0.0)
		(= (waypoint_supplies wa0) 1000.0)
	)
	(:goal
			(and
				(at s0 wa6)
				(at s1 wa6)
			)
	)
)