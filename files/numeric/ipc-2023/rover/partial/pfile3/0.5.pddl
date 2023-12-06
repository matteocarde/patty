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
		(equipped_for_rock_analysis rover0)
		(visible_from objective1 waypoint1)
		(supports camera1 high_res)
		(visible_from objective1 waypoint0)
		(on_board camera0 rover0)
		(equipped_for_soil_analysis rover1)
		(visible waypoint0 waypoint1)
		(visible waypoint0 waypoint3)
		(visible waypoint2 waypoint3)
		(equipped_for_imaging rover0)
		(can_traverse rover1 waypoint3 waypoint0)
		(on_board camera1 rover1)
		(store_of rover0store rover0)
		(visible waypoint1 waypoint2)
		(at_rock_sample waypoint0)
		(visible waypoint1 waypoint3)
		(in_sun waypoint0)
		(visible_from objective0 waypoint1)
		(can_traverse rover1 waypoint0 waypoint3)
		(visible waypoint3 waypoint1)
		(can_traverse rover0 waypoint1 waypoint3)
		(= (energy rover1) 50.0)
		(at_rock_sample waypoint1)
		(can_traverse rover1 waypoint1 waypoint0)
		(= (energy rover0) 50.0)
		(can_traverse rover0 waypoint1 waypoint0)
		(in rover0 waypoint1)
		(visible waypoint2 waypoint0)
		(supports camera1 low_res)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)