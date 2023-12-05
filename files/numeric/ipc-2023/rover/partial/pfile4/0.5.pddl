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
		(in_sun waypoint2)
		(= (recharges) 0.0)
		(at_rock_sample waypoint1)
		(visible_from objective0 waypoint2)
		(supports camera0 high_res)
		(can_traverse rover1 waypoint3 waypoint2)
		(equipped_for_rock_analysis rover1)
		(visible_from objective0 waypoint1)
		(can_traverse rover1 waypoint1 waypoint2)
		(supports camera1 low_res)
		(in_sun waypoint1)
		(visible waypoint1 waypoint2)
		(calibration_target camera1 objective0)
		(supports camera1 colour)
		(visible_from objective1 waypoint0)
		(on_board camera2 rover0)
		(calibration_target camera0 objective0)
		(can_traverse rover1 waypoint2 waypoint3)
		(visible_from objective2 waypoint1)
		(at_soil_sample waypoint2)
		(at_rock_sample waypoint3)
		(visible waypoint1 waypoint0)
		(= (energy rover1) 50.0)
		(visible waypoint2 waypoint1)
		(supports camera0 colour)
		(on_board camera1 rover0)
		(store_of rover1store rover1)
		(equipped_for_imaging rover0)
		(empty rover1store)
		(equipped_for_soil_analysis rover1)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)