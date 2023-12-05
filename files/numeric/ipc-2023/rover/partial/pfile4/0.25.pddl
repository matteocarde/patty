(define (problem roverprob6232)
	(:domain rover)
	(:objects
		general - lander
		colour high_res low_res - mode
		rover0 rover1 - rover
		rover0store rover1store - store
		waypoint0 waypoint1 waypoint2 waypoint3 - waypoint
		camera0 camera1 camera2 - camera
		objective0 objective1 objective2 - objective
	)
	(:init
		(channel_free general)
		(visible_from objective0 waypoint0)
		(visible waypoint1 waypoint2)
		(on_board camera2 rover0)
		(store_of rover0store rover0)
		(equipped_for_imaging rover0)
		(supports camera0 high_res)
		(supports camera0 colour)
		(at_soil_sample waypoint2)
		(at_rock_sample waypoint1)
		(calibration_target camera0 objective0)
		(supports camera2 low_res)
		(visible waypoint1 waypoint3)
		(= (energy rover1) 50.0)
		(visible_from objective1 waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)