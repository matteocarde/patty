(define (problem delivery-x-5)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item12 item11 item10 item9 item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (load_limit bot1) 4.0)
		(at item11 rooma)
		(door roomc rooma)
		(door rooma roomc)
		(at item10 rooma)
		(mount right2 bot2)
		(= (weight item3) 1.0)
		(free right1)
		(mount right1 bot1)
		(= (weight item7) 1.0)
	)
	(:goal
			(and
				(at item12 roomb)
				(at item11 roomb)
				(at item10 roomb)
				(at item9 roomb)
				(at item8 roomb)
				(at item7 roomb)
				(at item6 roomc)
				(at item5 roomc)
				(at item4 roomc)
				(at item3 roomc)
				(at item2 roomc)
				(at item1 roomc)
			)
	)
)