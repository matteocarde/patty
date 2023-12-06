(define (problem delivery-x-5)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item12 item11 item10 item9 item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (weight item7) 1.0)
		(at item4 rooma)
		(at item1 rooma)
		(= (weight item3) 1.0)
		(= (weight item11) 2.0)
		(at item3 rooma)
		(door roomb rooma)
		(at item10 rooma)
		(at item11 rooma)
		(at item12 rooma)
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