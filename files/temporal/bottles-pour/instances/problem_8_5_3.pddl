(define (problem prob_8_5_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 4)
		(= (litres l2) 13)
		(= (litres l3) 4)
		(= (litres l4) 2)
		(= (litres l5) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped r1)
		(capped r2)
		(capped r3)
	)
	(:goal
		(and
			(= (litres r1) 16)
			(= (litres r2) 3)
			(= (litres r3) 5)
		)
	)
)