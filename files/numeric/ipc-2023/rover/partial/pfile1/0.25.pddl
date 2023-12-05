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
		(at_soil_sample waypoint0)
		(channel_free general)
		(in rover0 waypoint3)
		(available rover0)
		(equipped_for_rock_analysis rover0)
		(at_soil_sample waypoint2)
		(visible_from objective1 waypoint1)
		(at_rock_sample waypoint2)
		(at_rock_sample waypoint3)
		(equipped_for_imaging rover0)
		(visible waypoint1 waypoint3)
		(visible waypoint0 waypoint1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint3)
				(communicated_image_data objective1 high_res)
			)
	)
)