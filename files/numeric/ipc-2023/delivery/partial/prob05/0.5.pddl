(define (problem delivery-x-5)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item12 item11 item10 item9 item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item7 rooma)
		(= (weight item9) 1.0)
		(at item10 rooma)
		(free right2)
		(= (weight item2) 1.0)
		(= (weight item12) 2.0)
		(at-bot bot1 rooma)
		(at item3 rooma)
		(= (cost) 0.0)
		(free right1)
		(at item2 rooma)
		(at item1 rooma)
		(= (weight item5) 2.0)
		(door roomc rooma)
		(free left1)
		(at item12 rooma)
		(at item4 rooma)
		(= (weight item8) 1.0)
		(door rooma roomb)
		(at item6 rooma)
		(mount left2 bot2)
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