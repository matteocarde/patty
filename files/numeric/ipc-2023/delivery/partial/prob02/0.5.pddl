(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item2 rooma)
		(at item3 rooma)
		(mount left2 bot2)
		(= (load_limit bot1) 4.0)
		(= (current_load bot1) 0.0)
		(mount right2 bot2)
		(= (load_limit bot2) 4.0)
		(free right1)
		(= (weight item4) 1.0)
		(free right2)
		(at item6 rooma)
		(at-bot bot1 rooma)
		(= (weight item1) 1.0)
		(= (cost) 0.0)
		(= (weight item5) 1.0)
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