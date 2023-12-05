(define (problem instance_2_sled_2)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 wa6 - waypoint
	)
	(:init
		(= (sled_supplies s1) 1.0)
		(= (waypoint_supplies wa1) 0.0)
		(= (waypoint_supplies wa6) 0.0)
		(= (waypoint_supplies wa0) 1000.0)
		(= (waypoint_supplies wa2) 0.0)
		(= (sled_supplies s0) 1.0)
		(is_next wa4 wa5)
		(= (waypoint_supplies wa4) 0.0)
		(is_next wa2 wa3)
	)
	(:goal
			(and
				(at s0 wa6)
				(at s1 wa6)
			)
	)
)