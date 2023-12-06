(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (load_limit bot1) 4.0)
		(mount left2 bot2)
		(at item1 rooma)
		(at item4 rooma)
		(mount left1 bot1)
		(free right1)
		(= (current_load bot1) 0.0)
		(= (weight item2) 1.0)
		(door roomc rooma)
		(door rooma roomb)
		(= (weight item6) 1.0)
		(at item6 rooma)
		(free right2)
		(mount right2 bot2)
		(at item3 rooma)
		(free left1)
		(= (cost) 0.0)
		(at-bot bot2 rooma)
		(= (weight item1) 1.0)
		(= (load_limit bot2) 4.0)
		(at item2 rooma)
		(= (weight item5) 1.0)
		(= (weight item4) 1.0)
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