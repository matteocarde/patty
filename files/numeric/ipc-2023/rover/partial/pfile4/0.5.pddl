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
		(at_rock_sample waypoint3)
		(visible waypoint0 waypoint1)
		(can_traverse rover1 waypoint1 waypoint0)
		(visible waypoint3 waypoint1)
		(at_soil_sample waypoint3)
		(empty rover1store)
		(can_traverse rover0 waypoint3 waypoint1)
		(supports camera1 colour)
		(supports camera2 low_res)
		(supports camera0 high_res)
		(= (energy rover1) 50.0)
		(on_board camera1 rover0)
		(visible waypoint1 waypoint0)
		(in rover0 waypoint3)
		(at_lander general waypoint2)
		(store_of rover0store rover0)
		(visible waypoint2 waypoint3)
		(equipped_for_imaging rover0)
		(= (recharges) 0.0)
		(visible_from objective1 waypoint0)
		(visible_from objective0 waypoint0)
		(on_board camera0 rover1)
		(visible_from objective0 waypoint2)
		(visible_from objective1 waypoint1)
		(calibration_target camera0 objective0)
		(on_board camera2 rover0)
		(visible_from objective0 waypoint1)
		(visible_from objective2 waypoint0)
		(supports camera0 colour)
		(in_sun waypoint2)
	)
	(:goal
			(and
				(communicated_soil_data waypoint3)
				(communicated_rock_data waypoint1)
				(communicated_image_data objective0 high_res)
			)
	)
)