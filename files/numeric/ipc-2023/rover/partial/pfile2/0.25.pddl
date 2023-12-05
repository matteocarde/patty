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
		(supports camera0 low_res)
		(equipped_for_rock_analysis rover0)
		(visible waypoint3 waypoint0)
		(channel_free general)
		(can_traverse rover0 waypoint2 waypoint0)
		(available rover0)
		(can_traverse rover0 waypoint3 waypoint0)
		(empty rover0store)
		(on_board camera0 rover0)
		(in rover0 waypoint0)
		(at_lander general waypoint1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)