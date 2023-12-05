(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (weight item8) 2.0)
		(at item6 rooma)
		(at item5 rooma)
		(= (cost) 0.0)
		(free left1)
		(= (weight item4) 2.0)
		(door roomc rooma)
		(door rooma roomc)
		(free left2)
		(= (weight item1) 1.0)
		(= (current_load bot2) 0.0)
		(= (weight item3) 2.0)
		(mount right2 bot2)
		(at item7 rooma)
		(at item3 rooma)
		(at item8 rooma)
		(= (weight item6) 1.0)
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