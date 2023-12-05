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
		(at_rock_sample waypoint1)
		(at_soil_sample waypoint3)
		(= (energy rover1) 50.0)
		(can_traverse rover1 waypoint1 waypoint0)
		(supports camera0 high_res)
		(on_board camera2 rover0)
		(store_of rover0store rover0)
		(equipped_for_imaging rover1)
		(visible_from objective2 waypoint0)
		(can_traverse rover0 waypoint1 waypoint3)
		(calibration_target camera1 objective0)
		(can_traverse rover1 waypoint0 waypoint1)
		(visible_from objective0 waypoint0)
		(visible_from objective1 waypoint0)
		(empty rover1store)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)