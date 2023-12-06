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
		(on_board camera1 rover0)
		(= (energy rover0) 50.0)
		(visible waypoint3 waypoint1)
		(can_traverse rover0 waypoint0 waypoint2)
		(can_traverse rover0 waypoint3 waypoint0)
		(calibration_target camera0 objective0)
		(available rover0)
		(visible_from objective1 waypoint1)
		(visible waypoint0 waypoint1)
		(store_of rover0store rover0)
		(can_traverse rover0 waypoint2 waypoint0)
		(visible_from objective1 waypoint2)
		(visible waypoint2 waypoint3)
		(in_sun waypoint1)
		(visible waypoint3 waypoint0)
		(can_traverse rover0 waypoint1 waypoint0)
		(can_traverse rover0 waypoint0 waypoint3)
		(equipped_for_soil_analysis rover0)
		(at_soil_sample waypoint0)
		(supports camera1 high_res)
		(equipped_for_rock_analysis rover0)
		(visible_from objective0 waypoint0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)