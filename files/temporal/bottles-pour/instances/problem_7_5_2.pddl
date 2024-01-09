(define (problem prob_7_5_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 22)
		(= (litres l2) 4)
		(= (litres l3) 5)
		(= (litres l4) 2)
		(= (litres l5) 2)
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
			(= (litres r1) 3)
			(= (litres r2) 32)
		)
	)
)