(define (problem instance_2_sled_1)
	(:domain expedition)
	(:objects
		s0 s1 - sled
		wa0 wa1 wa2 wa3 wa4 wa5 - waypoint
	)
	(:init
		(= (sled_capacity s1) 4.0)
		(= (waypoint_supplies wa0) 1000.0)
		(= (sled_supplies s1) 1.0)
		(= (sled_supplies s0) 1.0)
		(is_next wa0 wa1)
		(is_next wa4 wa5)
		(= (waypoint_supplies wa3) 0.0)
		(at s0 wa0)
	)
	(:goal
			(and
				(at s0 wa5)
				(at s1 wa5)
			)
	)
)