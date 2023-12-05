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
		(calibration_target camera0 objective0)
		(can_traverse rover0 waypoint0 waypoint3)
		(visible waypoint1 waypoint3)
		(visible waypoint3 waypoint1)
		(visible_from objective1 waypoint1)
		(visible waypoint2 waypoint1)
		(supports camera1 high_res)
		(calibration_target camera1 objective1)
		(visible waypoint2 waypoint3)
		(on_board camera1 rover0)
		(channel_free general)
		(in_sun waypoint1)
		(can_traverse rover0 waypoint3 waypoint0)
		(empty rover0store)
		(in rover0 waypoint0)
		(visible waypoint2 waypoint0)
		(visible waypoint3 waypoint0)
		(equipped_for_imaging rover0)
		(in_sun waypoint3)
		(visible waypoint0 waypoint2)
		(on_board camera0 rover0)
		(= (recharges) 0.0)
	)
	(:goal
			(and
				(communicated_soil_data waypoint0)
				(communicated_rock_data waypoint0)
				(communicated_image_data objective1 low_res)
			)
	)
)