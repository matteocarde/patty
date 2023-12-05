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
		(calibration_target camera1 objective0)
		(empty rover0store)
		(empty rover1store)
		(visible waypoint0 waypoint1)
		(can_traverse rover1 waypoint1 waypoint0)
		(equipped_for_imaging rover0)
		(channel_free general)
		(supports camera0 low_res)
		(store_of rover1store rover1)
		(visible waypoint2 waypoint0)
		(available rover1)
		(can_traverse rover1 waypoint0 waypoint1)
		(at_rock_sample waypoint0)
		(visible_from objective1 waypoint1)
		(at_lander general waypoint0)
		(visible waypoint3 waypoint0)
		(can_traverse rover1 waypoint2 waypoint3)
		(equipped_for_soil_analysis rover1)
		(visible waypoint3 waypoint1)
		(in_sun waypoint1)
		(available rover0)
		(visible_from objective0 waypoint0)
		(visible waypoint0 waypoint2)
		(= (energy rover1) 50.0)
		(store_of rover0store rover0)
		(can_traverse rover0 waypoint0 waypoint1)
		(calibration_target camera0 objective1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)