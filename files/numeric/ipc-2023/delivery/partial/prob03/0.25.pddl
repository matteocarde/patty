(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (cost) 0.0)
		(at item4 rooma)
		(= (weight item2) 1.0)
		(door roomb rooma)
		(mount right1 bot1)
		(at-bot bot1 rooma)
		(= (current_load bot2) 0.0)
		(= (load_limit bot1) 4.0)
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