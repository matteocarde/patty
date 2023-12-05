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
		(store_of rover0store rover0)
		(can_traverse rover0 waypoint1 waypoint0)
		(supports camera1 high_res)
		(on_board camera0 rover0)
		(in_sun waypoint3)
		(can_traverse rover0 waypoint3 waypoint0)
		(visible waypoint0 waypoint1)
		(visible waypoint0 waypoint2)
		(calibration_target camera0 objective0)
		(equipped_for_imaging rover0)
		(visible_from objective1 waypoint1)
		(on_board camera1 rover0)
		(calibration_target camera1 objective1)
		(visible waypoint2 waypoint3)
		(in rover0 waypoint0)
		(visible waypoint3 waypoint1)
		(visible waypoint2 waypoint1)
		(in_sun waypoint1)
		(empty rover0store)
		(equipped_for_rock_analysis rover0)
		(supports camera0 low_res)
		(available rover0)
		(at_soil_sample waypoint0)
		(at_lander general waypoint1)
		(visible_from objective1 waypoint2)
		(= (recharges) 0.0)
		(visible waypoint1 waypoint0)
		(at_rock_sample waypoint0)
		(visible_from objective1 waypoint0)
		(= (energy rover0) 50.0)
		(visible waypoint3 waypoint2)
		(channel_free general)
		(visible waypoint0 waypoint3)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)