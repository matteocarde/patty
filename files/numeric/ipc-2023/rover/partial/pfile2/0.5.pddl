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
		(visible waypoint3 waypoint0)
		(visible_from objective1 waypoint0)
		(store_of rover0store rover0)
		(visible waypoint2 waypoint0)
		(at_soil_sample waypoint0)
		(supports camera0 colour)
		(in_sun waypoint1)
		(supports camera0 low_res)
		(available rover0)
		(visible waypoint0 waypoint2)
		(in rover0 waypoint0)
		(equipped_for_soil_analysis rover0)
		(on_board camera0 rover0)
		(at_lander general waypoint1)
		(visible waypoint1 waypoint0)
		(can_traverse rover0 waypoint1 waypoint0)
		(channel_free general)
		(visible waypoint0 waypoint3)
		(= (recharges) 0.0)
		(calibration_target camera1 objective1)
		(in_sun waypoint3)
		(visible waypoint1 waypoint2)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)