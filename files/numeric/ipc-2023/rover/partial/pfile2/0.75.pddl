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
		(= (recharges) 0.0)
		(visible waypoint2 waypoint3)
		(supports camera0 colour)
		(visible waypoint1 waypoint3)
		(at_rock_sample waypoint0)
		(visible waypoint0 waypoint1)
		(visible waypoint3 waypoint2)
		(visible waypoint1 waypoint2)
		(supports camera0 low_res)
		(at_lander general waypoint1)
		(visible_from objective1 waypoint1)
		(visible waypoint2 waypoint0)
		(visible_from objective1 waypoint0)
		(visible waypoint1 waypoint0)
		(equipped_for_rock_analysis rover0)
		(in_sun waypoint3)
		(visible_from objective1 waypoint2)
		(available rover0)
		(= (energy rover0) 50.0)
		(empty rover0store)
		(calibration_target camera0 objective0)
		(calibration_target camera1 objective1)
		(can_traverse rover0 waypoint0 waypoint2)
		(on_board camera0 rover0)
		(can_traverse rover0 waypoint2 waypoint0)
		(equipped_for_soil_analysis rover0)
		(visible waypoint3 waypoint1)
		(in_sun waypoint1)
		(at_soil_sample waypoint0)
		(visible waypoint0 waypoint2)
		(channel_free general)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible waypoint3 waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)