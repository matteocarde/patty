(define (problem prob_8_5_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 4)
		(= (litres l3) 16)
		(= (litres l4) 2)
		(= (litres l5) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 11)
			(= (litres r2) 6)
			(= (litres r3) 7)
		)
	)
)