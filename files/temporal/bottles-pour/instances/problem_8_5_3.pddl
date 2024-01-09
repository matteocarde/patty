(define (problem prob_8_5_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 5)
		(= (litres l2) 8)
		(= (litres l3) 6)
		(= (litres l4) 3)
		(= (litres l5) 18)
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
			(= (litres r1) 24)
			(= (litres r2) 9)
			(= (litres r3) 7)
		)
	)
)