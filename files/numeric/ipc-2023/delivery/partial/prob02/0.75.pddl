(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(mount right1 bot1)
		(mount left1 bot1)
		(= (load_limit bot1) 4.0)
		(= (weight item4) 1.0)
		(at item3 rooma)
		(= (load_limit bot2) 4.0)
		(mount right2 bot2)
		(= (weight item5) 1.0)
		(door roomb rooma)
		(door rooma roomb)
		(at-bot bot1 rooma)
		(= (current_load bot2) 0.0)
		(= (weight item3) 1.0)
		(= (weight item6) 1.0)
		(free left1)
		(at-bot bot2 rooma)
		(door roomc rooma)
		(at item5 rooma)
		(at item2 rooma)
		(= (weight item1) 1.0)
		(= (current_load bot1) 0.0)
		(at item6 rooma)
		(at item1 rooma)
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