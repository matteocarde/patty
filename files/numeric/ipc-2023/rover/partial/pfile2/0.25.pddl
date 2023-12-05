(define (problem roverprob4213)
	(:domain rover)
	(:objects
		general - lander
		colour high_res low_res - mode
		rover0 - rover
		rover0store - store
		waypoint0 waypoint1 waypoint2 waypoint3 - waypoint
		camera0 camera1 - camera
		objective0 objective1 - objective
	)
	(:init
		(on_board camera0 rover0)
		(can_traverse rover0 waypoint2 waypoint0)
		(calibration_target camera1 objective1)
		(visible waypoint2 waypoint1)
		(visible waypoint2 waypoint3)
		(can_traverse rover0 waypoint0 waypoint3)
		(visible waypoint0 waypoint2)
		(visible waypoint1 waypoint2)
		(visible_from objective0 waypoint0)
		(visible_from objective1 waypoint2)
		(equipped_for_soil_analysis rover0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)