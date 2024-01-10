(define (problem prob_6_5_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 10)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres r1) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 18)
		)
	)
)