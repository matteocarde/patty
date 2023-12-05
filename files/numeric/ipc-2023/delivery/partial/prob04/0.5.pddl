(define (problem delivery-x-4)
	(:domain delivery)
	(:objects
		rooma roomb roomc roomd - room
		item12 item11 item10 item9 item8 item7 item6 item5 item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(door rooma roomc)
		(mount right2 bot2)
		(= (current_load bot1) 0.0)
		(free left2)
		(at-bot bot2 rooma)
		(door rooma roomb)
		(at item8 rooma)
		(at item7 rooma)
		(= (weight item9) 2.0)
		(= (weight item6) 1.0)
		(= (weight item8) 1.0)
		(= (weight item3) 1.0)
		(door roomb roomd)
		(at item5 rooma)
		(= (cost) 0.0)
		(free right1)
		(at item3 rooma)
		(door roomd roomb)
		(= (weight item1) 1.0)
		(door roomb rooma)
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