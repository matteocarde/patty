(define (problem delivery-x-3)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (current_load bot1) 0.0)
		(= (weight item4) 2.0)
		(at item8 rooma)
		(= (weight item1) 1.0)
		(mount left1 bot1)
		(at item2 rooma)
		(= (current_load bot2) 0.0)
		(door roomb rooma)
		(door roomc rooma)
		(= (weight item8) 2.0)
		(= (weight item3) 2.0)
		(at item6 rooma)
		(at item1 rooma)
		(at-bot bot2 rooma)
		(door rooma roomc)
		(door rooma roomb)
		(at item3 rooma)
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