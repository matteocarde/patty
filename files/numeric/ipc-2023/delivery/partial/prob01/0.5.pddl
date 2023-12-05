(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(mount right1 bot1)
		(= (load_limit bot1) 4.0)
		(= (weight item2) 1.0)
		(= (weight item1) 1.0)
		(at-bot bot2 rooma)
		(door roomc rooma)
		(= (current_load bot1) 0.0)
		(free right2)
		(= (load_limit bot2) 4.0)
		(at item1 rooma)
		(door roomb rooma)
		(at item2 rooma)
		(= (weight item3) 1.0)
	)
	(:goal
			(and
				(at item4 roomb)
				(at item3 roomb)
				(at item2 roomc)
				(at item1 roomc)
			)
	)
)