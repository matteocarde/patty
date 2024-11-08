(define (problem prob_9_7_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 14)
		(= (litres l2) 1)
		(= (litres l3) 2)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped l4)
		(capped l5)
		(capped l6)
		(capped l7)
		(capped r1)
		(capped r2)
	)
	(:goal
		(and
			(= (litres r1) 12)
			(= (litres r2) 15)
		)
	)
)