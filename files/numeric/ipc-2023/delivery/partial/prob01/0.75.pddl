(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(free right1)
		(at-bot bot2 rooma)
		(at item1 rooma)
		(at-bot bot1 rooma)
		(mount right1 bot1)
		(= (weight item1) 1.0)
		(free left2)
		(free right2)
		(= (current_load bot2) 0.0)
		(= (load_limit bot1) 4.0)
		(door roomc rooma)
		(= (weight item2) 1.0)
		(mount left1 bot1)
		(= (current_load bot1) 0.0)
		(= (weight item4) 1.0)
		(= (load_limit bot2) 4.0)
		(at item2 rooma)
		(door roomb rooma)
		(free left1)
		(mount left2 bot2)
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