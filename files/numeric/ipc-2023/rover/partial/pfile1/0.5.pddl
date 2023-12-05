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
		(visible waypoint2 waypoint3)
		(equipped_for_rock_analysis rover0)
		(visible waypoint3 waypoint1)
		(supports camera0 colour)
		(on_board camera0 rover0)
		(= (energy rover0) 50.0)
		(can_traverse rover0 waypoint1 waypoint2)
		(visible_from objective1 waypoint3)
		(visible_from objective1 waypoint0)
		(can_traverse rover0 waypoint3 waypoint0)
		(store_of rover0store rover0)
		(visible waypoint0 waypoint3)
		(supports camera0 high_res)
		(visible waypoint3 waypoint0)
		(in rover0 waypoint3)
		(can_traverse rover0 waypoint0 waypoint3)
		(at_rock_sample waypoint1)
		(visible_from objective0 waypoint0)
		(= (recharges) 0.0)
		(empty rover0store)
		(calibration_target camera0 objective1)
		(can_traverse rover0 waypoint3 waypoint1)
		(channel_free general)
		(available rover0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)