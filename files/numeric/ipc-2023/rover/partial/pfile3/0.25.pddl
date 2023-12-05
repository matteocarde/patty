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
		(in_sun waypoint0)
		(on_board camera1 rover1)
		(can_traverse rover1 waypoint3 waypoint0)
		(can_traverse rover0 waypoint1 waypoint3)
		(at_rock_sample waypoint2)
		(available rover0)
		(equipped_for_imaging rover0)
		(at_lander general waypoint0)
		(at_rock_sample waypoint0)
		(equipped_for_soil_analysis rover1)
		(visible waypoint1 waypoint2)
		(supports camera1 low_res)
		(empty rover1store)
		(visible waypoint0 waypoint3)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)