(define (problem roverprob1234)
	(:domain rover)
	(:objects
		general - lander
		colour high_res low_res - mode
		rover0 - rover
		rover0store - store
		waypoint0 waypoint1 waypoint2 waypoint3 - waypoint
		camera0 - camera
		objective0 objective1 - objective
	)
	(:init
		(at_rock_sample waypoint3)
		(channel_free general)
		(visible_from objective1 waypoint0)
		(visible_from objective1 waypoint3)
		(visible_from objective0 waypoint1)
		(= (recharges) 0.0)
		(visible_from objective0 waypoint0)
		(supports camera0 high_res)
		(visible waypoint0 waypoint3)
		(can_traverse rover0 waypoint1 waypoint2)
		(visible waypoint3 waypoint2)
		(equipped_for_imaging rover0)
		(at_soil_sample waypoint2)
		(at_rock_sample waypoint2)
		(supports camera0 colour)
		(visible_from objective0 waypoint2)
		(calibration_target camera0 objective1)
		(in_sun waypoint0)
		(visible waypoint3 waypoint0)
		(visible_from objective0 waypoint3)
		(visible waypoint2 waypoint0)
		(empty rover0store)
		(available rover0)
		(on_board camera0 rover0)
		(visible_from objective1 waypoint1)
		(equipped_for_soil_analysis rover0)
		(visible waypoint0 waypoint2)
		(visible waypoint1 waypoint3)
		(at_soil_sample waypoint3)
		(visible_from objective1 waypoint2)
		(visible waypoint1 waypoint0)
		(in rover0 waypoint3)
		(visible waypoint0 waypoint1)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible waypoint2 waypoint1)
		(at_soil_sample waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)