(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(door rooma roomc)
		(door roomb rooma)
		(= (weight item5) 1.0)
		(at item4 rooma)
		(at-bot bot1 rooma)
		(mount left1 bot1)
		(= (current_load bot2) 0.0)
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