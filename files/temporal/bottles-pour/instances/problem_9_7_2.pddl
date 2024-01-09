(define (problem prob_9_7_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 32)
		(= (litres l2) 2)
		(= (litres l3) 2)
		(= (litres l4) 4)
		(= (litres l5) 2)
		(= (litres l6) 2)
		(= (litres l7) 1)
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
			(= (litres r1) 4)
			(= (litres r2) 41)
		)
	)
)