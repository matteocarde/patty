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
		(= (energy rover0) 50.0)
		(visible waypoint2 waypoint1)
		(store_of rover1store rover1)
		(visible waypoint1 waypoint3)
		(equipped_for_imaging rover1)
		(visible_from objective1 waypoint0)
		(supports camera1 low_res)
		(visible waypoint0 waypoint1)
		(at_soil_sample waypoint2)
		(visible waypoint0 waypoint2)
		(in_sun waypoint0)
		(can_traverse rover1 waypoint0 waypoint1)
		(on_board camera0 rover0)
		(supports camera1 colour)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective0 colour)
			)
	)
)