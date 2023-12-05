(define (problem roverprob3726)
	(:domain rover)
	(:objects
		general - lander
		colour high_res low_res - mode
		rover0 rover1 - rover
		rover0store rover1store - store
		waypoint0 waypoint1 waypoint2 waypoint3 - waypoint
		camera0 camera1 - camera
		objective0 objective1 - objective
	)
	(:init
		(equipped_for_imaging rover1)
		(visible_from objective1 waypoint0)
		(at_lander general waypoint0)
		(visible_from objective1 waypoint1)
		(can_traverse rover1 waypoint3 waypoint2)
		(can_traverse rover1 waypoint0 waypoint1)
		(can_traverse rover1 waypoint2 waypoint3)
		(calibration_target camera0 objective1)
		(visible waypoint0 waypoint3)
		(equipped_for_rock_analysis rover1)
		(equipped_for_rock_analysis rover0)
		(equipped_for_soil_analysis rover1)
		(visible_from objective0 waypoint0)
		(visible waypoint2 waypoint1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)