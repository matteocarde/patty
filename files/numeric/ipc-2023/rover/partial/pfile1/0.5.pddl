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
		(= (recharges) 0.0)
		(can_traverse rover0 waypoint0 waypoint3)
		(visible waypoint1 waypoint3)
		(at_soil_sample waypoint0)
		(visible_from objective1 waypoint2)
		(visible waypoint2 waypoint1)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible waypoint0 waypoint2)
		(visible_from objective0 waypoint3)
		(equipped_for_imaging rover0)
		(can_traverse rover0 waypoint2 waypoint1)
		(supports camera0 high_res)
		(empty rover0store)
		(available rover0)
		(equipped_for_rock_analysis rover0)
		(at_rock_sample waypoint3)
		(visible_from objective1 waypoint3)
		(store_of rover0store rover0)
		(visible_from objective0 waypoint2)
		(at_rock_sample waypoint2)
		(at_soil_sample waypoint2)
		(equipped_for_soil_analysis rover0)
		(at_rock_sample waypoint1)
		(at_soil_sample waypoint3)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)