(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (current_load bot2) 0.0)
		(mount left1 bot1)
		(door roomc rooma)
		(= (weight item1) 1.0)
		(door roomb rooma)
		(= (cost) 0.0)
		(free right2)
		(at item2 rooma)
		(= (weight item3) 1.0)
		(= (current_load bot1) 0.0)
		(mount left2 bot2)
		(free left2)
		(= (load_limit bot1) 4.0)
		(at item4 rooma)
		(door rooma roomc)
		(free left1)
		(free right1)
		(at-bot bot1 rooma)
		(= (load_limit bot2) 4.0)
		(at-bot bot2 rooma)
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