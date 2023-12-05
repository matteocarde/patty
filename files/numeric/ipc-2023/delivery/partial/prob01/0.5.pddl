(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item4 rooma)
		(free left2)
		(= (weight item1) 1.0)
		(free right2)
		(at item2 rooma)
		(= (weight item2) 1.0)
		(= (weight item4) 1.0)
		(at-bot bot1 rooma)
		(at-bot bot2 rooma)
		(door roomc rooma)
		(= (cost) 0.0)
		(= (load_limit bot1) 4.0)
		(at item1 rooma)
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