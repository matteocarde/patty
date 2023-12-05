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
		(in_sun waypoint0)
		(at_lander general waypoint0)
		(visible waypoint3 waypoint1)
		(on_board camera0 rover0)
		(visible waypoint0 waypoint2)
		(at_rock_sample waypoint2)
		(visible waypoint3 waypoint0)
		(empty rover0store)
		(can_traverse rover0 waypoint1 waypoint3)
		(can_traverse rover0 waypoint2 waypoint1)
		(store_of rover0store rover0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)