(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (weight item2) 1.0)
		(= (current_load bot2) 0.0)
		(= (cost) 0.0)
		(= (load_limit bot2) 4.0)
		(at item8 rooma)
		(mount right2 bot2)
		(= (weight item8) 2.0)
		(at item3 rooma)
		(at item7 rooma)
		(= (weight item4) 2.0)
		(= (load_limit bot1) 4.0)
		(= (weight item1) 1.0)
		(at item5 rooma)
		(free right1)
		(door rooma roomb)
		(door roomc rooma)
		(= (weight item5) 1.0)
	)
	(:goal
			(and
				(at item8 roomb)
				(at item7 roomb)
				(at item6 roomb)
				(at item5 roomb)
				(at item4 roomc)
				(at item3 roomc)
				(at item2 roomc)
				(at item1 roomc)
			)
	)
)