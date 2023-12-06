(define (problem delivery-x-2)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(at item4 rooma)
		(mount left1 bot1)
		(free left2)
		(= (weight item2) 1.0)
		(at item3 rooma)
		(at item5 rooma)
		(at item1 rooma)
		(= (weight item5) 1.0)
		(= (weight item6) 1.0)
		(= (weight item1) 1.0)
		(mount right1 bot1)
		(free right1)
		(at item2 rooma)
		(door rooma roomc)
		(free right2)
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