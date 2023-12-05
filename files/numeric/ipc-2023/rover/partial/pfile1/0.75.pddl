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
		(visible_from objective0 waypoint3)
		(at_rock_sample waypoint2)
		(at_rock_sample waypoint1)
		(calibration_target camera0 objective1)
		(equipped_for_imaging rover0)
		(at_soil_sample waypoint2)
		(= (energy rover0) 50.0)
		(visible waypoint1 waypoint2)
		(visible waypoint3 waypoint1)
		(can_traverse rover0 waypoint0 waypoint3)
		(visible waypoint2 waypoint0)
		(empty rover0store)
		(can_traverse rover0 waypoint2 waypoint1)
		(can_traverse rover0 waypoint1 waypoint2)
		(supports camera0 colour)
		(can_traverse rover0 waypoint1 waypoint3)
		(visible waypoint2 waypoint3)
		(in rover0 waypoint3)
		(can_traverse rover0 waypoint3 waypoint1)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible_from objective1 waypoint1)
		(visible waypoint1 waypoint0)
		(visible waypoint0 waypoint2)
		(visible waypoint2 waypoint1)
		(visible_from objective0 waypoint1)
		(on_board camera0 rover0)
		(at_soil_sample waypoint0)
		(= (recharges) 0.0)
		(visible waypoint1 waypoint3)
		(visible waypoint0 waypoint3)
		(supports camera0 high_res)
		(store_of rover0store rover0)
		(at_soil_sample waypoint3)
		(at_rock_sample waypoint3)
		(visible_from objective0 waypoint0)
		(in_sun waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)