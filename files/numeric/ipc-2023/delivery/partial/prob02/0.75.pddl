(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (weight item3) 1.0)
		(mount left2 bot2)
		(mount left1 bot1)
		(mount right1 bot1)
		(door roomb rooma)
		(= (current_load bot1) 0.0)
		(at item1 rooma)
		(= (weight item5) 1.0)
		(mount right2 bot2)
		(at item4 rooma)
		(door rooma roomc)
		(at item2 rooma)
		(= (load_limit bot1) 4.0)
		(at item3 rooma)
		(free right1)
		(= (current_load bot2) 0.0)
		(at-bot bot1 rooma)
		(door roomc rooma)
		(free left1)
		(= (weight item1) 1.0)
		(= (weight item6) 1.0)
		(at-bot bot2 rooma)
		(at item6 rooma)
	)
	(:goal
			(and
				(at item6 roomb)
				(at item5 roomb)
				(at item4 roomb)
				(at item3 roomb)
				(at item2 roomc)
				(at item1 roomc)
			)
	)
)