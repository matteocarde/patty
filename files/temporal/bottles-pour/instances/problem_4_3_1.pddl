(define (problem prob_4_3_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 9)
		(= (litres l2) 2)
		(= (litres l3) 1)
		(= (litres r1) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 12)
		)
	)
)