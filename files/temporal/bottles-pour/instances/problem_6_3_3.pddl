(define (problem prob_6_3_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 7)
		(= (litres l2) 6)
		(= (litres l3) 5)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
		(capped r2)
		(capped r3)
	)
	(:goal
		(and
			(= (litres r1) 8)
			(= (litres r2) 5)
			(= (litres r3) 5)
		)
	)
)