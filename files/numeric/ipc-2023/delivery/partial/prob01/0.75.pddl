(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at-bot bot2 rooma)
		(free left2)
		(door roomc rooma)
		(door rooma roomc)
		(at item3 rooma)
		(= (load_limit bot1) 4.0)
		(at item1 rooma)
		(mount left1 bot1)
		(door roomb rooma)
		(mount right1 bot1)
		(at item2 rooma)
		(= (cost) 0.0)
		(free right2)
		(at item4 rooma)
		(= (current_load bot1) 0.0)
		(mount right2 bot2)
		(= (current_load bot2) 0.0)
		(at-bot bot1 rooma)
		(free left1)
		(= (weight item2) 1.0)
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