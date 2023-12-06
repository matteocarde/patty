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
		(= (energy rover1) 50.0)
		(available rover1)
		(calibration_target camera2 objective1)
		(visible_from objective0 waypoint0)
		(can_traverse rover1 waypoint2 waypoint1)
		(at_lander general waypoint2)
		(visible_from objective2 waypoint1)
		(can_traverse rover1 waypoint1 waypoint2)
		(can_traverse rover1 waypoint1 waypoint0)
		(on_board camera0 rover1)
		(supports camera2 low_res)
		(in rover0 waypoint3)
		(available rover0)
		(= (energy rover0) 50.0)
		(visible_from objective0 waypoint2)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)