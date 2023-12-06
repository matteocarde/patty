(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item1 rooma)
		(door rooma roomb)
		(at-bot bot1 rooma)
		(= (weight item3) 1.0)
		(= (weight item1) 1.0)
		(door roomb rooma)
		(door roomc rooma)
		(= (weight item2) 1.0)
		(mount left2 bot2)
		(free right2)
		(at item4 rooma)
		(door rooma roomc)
		(mount right1 bot1)
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