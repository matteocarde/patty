(define (problem prob_8_7_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 1)
		(= (litres l3) 11)
		(= (litres l4) 2)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 2)
		(= (litres r1) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped l6)
		(capped l7)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 24)
		)
	)
)