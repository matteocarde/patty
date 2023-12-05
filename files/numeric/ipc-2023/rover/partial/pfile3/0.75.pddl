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
		(at_rock_sample waypoint0)
		(visible waypoint3 waypoint1)
		(calibration_target camera1 objective0)
		(can_traverse rover0 waypoint1 waypoint3)
		(equipped_for_imaging rover0)
		(visible waypoint1 waypoint3)
		(visible_from objective0 waypoint0)
		(equipped_for_rock_analysis rover1)
		(on_board camera1 rover1)
		(can_traverse rover1 waypoint3 waypoint0)
		(supports camera0 low_res)
		(can_traverse rover1 waypoint2 waypoint3)
		(store_of rover1store rover1)
		(empty rover1store)
		(visible waypoint0 waypoint2)
		(visible waypoint1 waypoint0)
		(at_soil_sample waypoint2)
		(visible_from objective1 waypoint0)
		(visible waypoint2 waypoint1)
		(visible waypoint2 waypoint0)
		(empty rover0store)
		(visible waypoint2 waypoint3)
		(at_rock_sample waypoint1)
		(store_of rover0store rover0)
		(equipped_for_rock_analysis rover0)
		(channel_free general)
		(can_traverse rover0 waypoint3 waypoint1)
		(in_sun waypoint0)
		(at_lander general waypoint0)
		(at_rock_sample waypoint2)
		(supports camera1 high_res)
		(supports camera1 colour)
		(visible waypoint0 waypoint1)
		(can_traverse rover1 waypoint3 waypoint2)
		(calibration_target camera0 objective1)
		(visible waypoint1 waypoint2)
		(can_traverse rover1 waypoint0 waypoint3)
		(equipped_for_soil_analysis rover1)
		(can_traverse rover0 waypoint1 waypoint0)
		(equipped_for_imaging rover1)
		(in_sun waypoint1)
		(visible_from objective0 waypoint1)
		(= (energy rover1) 50.0)
		(can_traverse rover1 waypoint1 waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)