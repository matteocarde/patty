(define (problem prob_8_5_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 4)
		(= (litres l2) 2)
		(= (litres l3) 2)
		(= (litres l4) 4)
		(= (litres l5) 12)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 4)
			(= (litres r2) 1)
			(= (litres r3) 19)
		)
	)
)