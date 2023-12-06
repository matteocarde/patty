(define (problem delivery-x-1)
	(:domain delivery)
	(:objects
		rooma roomb roomc - room
		item4 item3 item2 item1 - item
		bot1 bot2 - bot
		left1 right1 left2 right2 - arm
	)
	(:init
		(= (load_limit bot1) 4.0)
		(mount left2 bot2)
		(at item2 rooma)
		(= (current_load bot2) 0.0)
		(door rooma roomc)
		(door roomc rooma)
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