(define (problem roverprob6232)
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
		(supports camera0 colour)
		(can_traverse rover0 waypoint3 waypoint1)
		(visible waypoint3 waypoint1)
		(can_traverse rover1 waypoint2 waypoint1)
		(at_soil_sample waypoint2)
		(on_board camera2 rover0)
		(visible waypoint1 waypoint0)
		(calibration_target camera1 objective0)
		(visible_from objective0 waypoint2)
		(equipped_for_imaging rover1)
		(store_of rover0store rover0)
		(channel_free general)
		(visible_from objective0 waypoint0)
		(equipped_for_rock_analysis rover1)
		(visible_from objective2 waypoint1)
		(on_board camera0 rover1)
		(can_traverse rover1 waypoint2 waypoint3)
		(visible waypoint3 waypoint2)
		(equipped_for_soil_analysis rover0)
		(visible_from objective1 waypoint1)
		(empty rover0store)
		(visible waypoint2 waypoint1)
		(visible waypoint1 waypoint2)
		(can_traverse rover1 waypoint3 waypoint2)
		(visible waypoint1 waypoint3)
		(= (recharges) 0.0)
		(in_sun waypoint2)
		(on_board camera1 rover0)
		(can_traverse rover1 waypoint0 waypoint1)
		(in rover0 waypoint3)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)