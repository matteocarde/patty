(define (problem prob_5_3_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 7)
		(= (litres l2) 14)
		(= (litres l3) 4)
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
			(= (litres r1) 18)
			(= (litres r2) 7)
		)
	)
)