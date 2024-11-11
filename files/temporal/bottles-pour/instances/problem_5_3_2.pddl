(define (problem prob_5_3_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 9)
		(= (litres l2) 3)
		(= (litres l3) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
		(capped r2)
	)
	(:goal
		(and
			(= (litres r1) 2)
			(= (litres r2) 13)
		)
	)
)