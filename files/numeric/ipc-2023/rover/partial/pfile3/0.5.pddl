(define (problem roverprob3726)
	(:domain rover)
	(:objects
		general - lander
		colour high_res low_res - mode
		rover0 rover1 - rover
		rover0store rover1store - store
		waypoint0 waypoint1 waypoint2 waypoint3 - waypoint
		camera0 camera1 - camera
		objective0 objective1 - objective
	)
	(:init
		(equipped_for_soil_analysis rover0)
		(in_sun waypoint0)
		(in_sun waypoint1)
		(visible waypoint0 waypoint1)
		(available rover0)
		(equipped_for_rock_analysis rover1)
		(equipped_for_soil_analysis rover1)
		(calibration_target camera0 objective1)
		(can_traverse rover0 waypoint3 waypoint1)
		(at_rock_sample waypoint1)
		(visible waypoint2 waypoint1)
		(in rover1 waypoint3)
		(store_of rover1store rover1)
		(= (energy rover1) 50.0)
		(visible waypoint2 waypoint3)
		(can_traverse rover0 waypoint1 waypoint3)
		(visible waypoint1 waypoint0)
		(visible waypoint1 waypoint2)
		(visible_from objective0 waypoint1)
		(equipped_for_imaging rover1)
		(equipped_for_imaging rover0)
		(on_board camera1 rover1)
		(empty rover1store)
		(visible waypoint3 waypoint2)
		(can_traverse rover1 waypoint2 waypoint3)
		(= (energy rover0) 50.0)
		(visible waypoint0 waypoint2)
		(channel_free general)
		(can_traverse rover0 waypoint0 waypoint1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)