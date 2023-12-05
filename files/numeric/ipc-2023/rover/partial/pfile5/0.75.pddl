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
		(visible waypoint3 waypoint0)
		(channel_free general)
		(can_traverse rover1 waypoint1 waypoint3)
		(can_traverse rover1 waypoint1 waypoint2)
		(at_soil_sample waypoint1)
		(in rover1 waypoint0)
		(can_traverse rover1 waypoint3 waypoint1)
		(visible waypoint0 waypoint3)
		(supports camera2 colour)
		(= (energy rover1) 50.0)
		(supports camera0 low_res)
		(visible waypoint1 waypoint3)
		(visible waypoint1 waypoint2)
		(calibration_target camera1 objective1)
		(available rover1)
		(visible_from objective1 waypoint0)
		(can_traverse rover1 waypoint0 waypoint1)
		(at_soil_sample waypoint3)
		(visible_from objective2 waypoint2)
		(equipped_for_soil_analysis rover1)
		(calibration_target camera0 objective1)
		(visible_from objective0 waypoint1)
		(supports camera2 high_res)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible_from objective0 waypoint3)
		(available rover0)
		(visible_from objective1 waypoint1)
		(visible waypoint2 waypoint1)
		(store_of rover0store rover0)
		(visible_from objective0 waypoint0)
		(can_traverse rover0 waypoint1 waypoint0)
		(visible waypoint3 waypoint1)
		(can_traverse rover1 waypoint1 waypoint0)
		(at_lander general waypoint3)
		(on_board camera1 rover1)
		(store_of rover1store rover1)
		(equipped_for_rock_analysis rover0)
		(at_rock_sample waypoint0)
		(visible_from objective1 waypoint2)
		(= (recharges) 0.0)
		(visible_from objective2 waypoint0)
		(= (energy rover0) 50.0)
		(at_soil_sample waypoint2)
		(can_traverse rover0 waypoint0 waypoint3)
		(visible_from objective2 waypoint1)
		(empty rover1store)
		(empty rover0store)
		(can_traverse rover0 waypoint0 waypoint1)
		(equipped_for_imaging rover0)
		(supports camera1 colour)
		(supports camera2 low_res)
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