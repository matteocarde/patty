(define (problem prob_7_5_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 11)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres l4) 4)
		(= (litres l5) 4)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped r1)
		(capped r2)
	)
	(:goal
		(and
			(= (litres r1) 15)
			(= (litres r2) 6)
		)
	)
)