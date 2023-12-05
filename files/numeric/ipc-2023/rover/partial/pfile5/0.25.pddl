(define (problem roverprob2435)
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
		(supports camera0 low_res)
		(supports camera2 colour)
		(visible waypoint3 waypoint2)
		(visible waypoint0 waypoint3)
		(visible waypoint0 waypoint2)
		(visible_from objective0 waypoint2)
		(visible waypoint1 waypoint3)
		(supports camera0 high_res)
		(visible_from objective0 waypoint0)
		(visible_from objective2 waypoint2)
		(at_lander general waypoint3)
		(visible waypoint2 waypoint0)
		(visible_from objective0 waypoint1)
		(= (recharges) 0.0)
		(can_traverse rover1 waypoint0 waypoint1)
		(can_traverse rover0 waypoint0 waypoint1)
		(= (energy rover0) 50.0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint1)
				(communicated_soil_data waypoint2)
				(communicated_rock_data waypoint0)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
				(communicated_image_data objective2 high_res)
				(communicated_image_data objective0 colour)
			)
	)
)