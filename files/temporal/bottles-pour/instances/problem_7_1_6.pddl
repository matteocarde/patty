(define (problem prob_7_1_6)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 21)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(capped l1)
		(capped r1)
		(capped r2)
		(capped r3)
		(capped r4)
		(capped r5)
		(capped r6)
	)
	(:goal
		(and
			(= (litres r1) 2)
			(= (litres r2) 2)
			(= (litres r3) 1)
			(= (litres r4) 3)
			(= (litres r5) 1)
			(= (litres r6) 12)
		)
	)
)