(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(free left2)
		(= (load_limit bot2) 4.0)
		(mount left1 bot1)
		(at item2 rooma)
		(= (current_load bot1) 0.0)
		(at item1 rooma)
		(mount right1 bot1)
		(mount left2 bot2)
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