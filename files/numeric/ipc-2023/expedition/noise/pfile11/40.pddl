(define (problem instance_2_sled_1)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 - waypoint
	)
	(:init
		(at s0 wa0)
		(= (sled_capacity s0) -32.0)
		(= (sled_supplies s0) 12.0)
		(= (waypoint_supplies wa0) 1012.0)
		(= (waypoint_supplies wa1) 24.0)
		(= (waypoint_supplies wa2) 0.0)
		(= (waypoint_supplies wa3) -19.0)
		(= (waypoint_supplies wa4) -38.0)
		(= (waypoint_supplies wa5) 16.0)
		(is_next wa0 wa1)
		(is_next wa1 wa2)
		(is_next wa2 wa3)
		(is_next wa3 wa4)
		(is_next wa4 wa5)
		(at s1 wa0)
		(= (sled_capacity s1) 9.0)
		(= (sled_supplies s1) 39.0)
	)
	(:goal
			(and
				(at s0 wa5)
				(at s1 wa5)
			)
	)
)