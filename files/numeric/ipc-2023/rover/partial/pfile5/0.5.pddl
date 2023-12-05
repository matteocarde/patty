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
		(supports camera1 high_res)
		(visible waypoint1 waypoint0)
		(= (energy rover0) 50.0)
		(empty rover1store)
		(can_traverse rover0 waypoint0 waypoint1)
		(equipped_for_soil_analysis rover1)
		(visible_from objective1 waypoint0)
		(in_sun waypoint0)
		(visible waypoint3 waypoint2)
		(= (energy rover1) 50.0)
		(empty rover0store)
		(equipped_for_rock_analysis rover0)
		(at_soil_sample waypoint3)
		(visible waypoint3 waypoint0)
		(= (recharges) 0.0)
		(can_traverse rover0 waypoint0 waypoint3)
		(in rover0 waypoint0)
		(can_traverse rover1 waypoint1 waypoint3)
		(at_rock_sample waypoint0)
		(at_soil_sample waypoint2)
		(at_rock_sample waypoint1)
		(equipped_for_imaging rover0)
		(supports camera2 low_res)
		(visible_from objective2 waypoint1)
		(available rover1)
		(supports camera1 colour)
		(visible_from objective0 waypoint3)
		(available rover0)
		(calibration_target camera0 objective1)
		(visible waypoint1 waypoint2)
		(on_board camera1 rover1)
		(supports camera0 low_res)
		(can_traverse rover1 waypoint1 waypoint0)
		(in rover1 waypoint0)
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