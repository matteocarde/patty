(define (problem prob_7_3_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 16)
		(= (litres l2) 4)
		(= (litres l3) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
		(capped r2)
		(capped r3)
		(capped r4)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 5)
			(= (litres r3) 12)
			(= (litres r4) 3)
		)
	)
)