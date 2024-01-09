(define (problem prob_8_3_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 19)
		(= (litres l2) 12)
		(= (litres l3) 9)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(capped l1)
		(capped l2)
		(capped l3)
		(capped r1)
		(capped r2)
		(capped r3)
		(capped r4)
		(capped r5)
	)
	(:goal
		(and
			(= (litres r1) 7)
			(= (litres r2) 2)
			(= (litres r3) 4)
			(= (litres r4) 6)
			(= (litres r5) 21)
		)
	)
)