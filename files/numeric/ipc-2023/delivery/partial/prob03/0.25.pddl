(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at-bot bot1 rooma)
		(at item8 rooma)
		(door rooma roomb)
		(= (cost) 0.0)
		(= (current_load bot1) 0.0)
		(at-bot bot2 rooma)
		(mount left2 bot2)
		(at item6 rooma)
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