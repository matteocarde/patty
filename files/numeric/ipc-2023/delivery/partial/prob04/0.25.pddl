(define (problem delivery-x-4)
	(:domain delivery)
	(:objects
		rooma roomb roomc roomd - room
		item12 item11 item10 item9 item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item1 rooma)
		(= (weight item3) 1.0)
		(door roomc rooma)
		(door rooma roomc)
		(mount right1 bot1)
		(= (weight item7) 1.0)
		(= (weight item1) 1.0)
		(door rooma roomb)
		(= (weight item4) 1.0)
		(mount left2 bot2)
	)
	(:goal
			(and
				(at item10 roomb)
				(at item9 roomb)
				(at item8 roomd)
				(at item7 roomd)
				(at item6 roomd)
				(at item5 roomd)
				(at item4 roomc)
				(at item3 roomc)
				(at item2 roomc)
				(at item1 roomc)
			)
	)
)