(define (problem roverprob2435)
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
		(at_lander general waypoint3)
		(= (energy rover1) 50.0)
		(can_traverse rover0 waypoint1 waypoint0)
		(at_rock_sample waypoint0)
		(can_traverse rover1 waypoint1 waypoint3)
		(store_of rover1store rover1)
		(channel_free general)
		(can_traverse rover1 waypoint1 waypoint2)
		(can_traverse rover1 waypoint0 waypoint1)
		(empty rover0store)
		(equipped_for_imaging rover0)
		(supports camera2 colour)
		(empty rover1store)
		(visible_from objective1 waypoint0)
		(at_rock_sample waypoint1)
		(visible waypoint2 waypoint1)
		(visible waypoint3 waypoint2)
		(calibration_target camera2 objective1)
		(visible waypoint2 waypoint3)
		(supports camera1 high_res)
		(visible_from objective0 waypoint2)
		(can_traverse rover0 waypoint0 waypoint1)
		(equipped_for_soil_analysis rover1)
		(calibration_target camera0 objective1)
		(visible waypoint2 waypoint0)
		(visible_from objective2 waypoint2)
		(visible waypoint1 waypoint0)
		(equipped_for_imaging rover1)
		(visible_from objective0 waypoint0)
		(visible waypoint3 waypoint1)
		(in rover1 waypoint0)
		(in rover0 waypoint0)
		(visible waypoint0 waypoint1)
		(available rover0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint1)
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
				(communicated_image_data objective2 high_res)
				(communicated_image_data objective0 colour)
			)
	)
)