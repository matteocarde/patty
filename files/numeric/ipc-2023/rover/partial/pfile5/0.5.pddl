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
		(can_traverse rover1 waypoint1 waypoint3)
		(visible_from objective0 waypoint3)
		(visible_from objective2 waypoint2)
		(in rover0 waypoint0)
		(can_traverse rover0 waypoint1 waypoint0)
		(supports camera1 high_res)
		(= (recharges) 0.0)
		(on_board camera0 rover1)
		(can_traverse rover0 waypoint3 waypoint0)
		(in rover1 waypoint0)
		(at_rock_sample waypoint0)
		(calibration_target camera1 objective1)
		(visible_from objective1 waypoint2)
		(can_traverse rover0 waypoint0 waypoint1)
		(visible waypoint1 waypoint3)
		(available rover0)
		(visible waypoint0 waypoint2)
		(available rover1)
		(supports camera0 low_res)
		(visible waypoint2 waypoint1)
		(calibration_target camera0 objective1)
		(= (energy rover1) 50.0)
		(can_traverse rover1 waypoint3 waypoint1)
		(can_traverse rover1 waypoint1 waypoint2)
		(equipped_for_rock_analysis rover0)
		(visible waypoint3 waypoint2)
		(in_sun waypoint0)
		(visible waypoint1 waypoint0)
		(equipped_for_imaging rover0)
		(at_soil_sample waypoint2)
		(visible_from objective2 waypoint1)
		(visible waypoint2 waypoint3)
		(visible_from objective0 waypoint2)
		(can_traverse rover1 waypoint1 waypoint0)
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