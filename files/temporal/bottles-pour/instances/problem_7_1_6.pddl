(define (problem prob_7_1_6)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 35)
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
			(= (litres r1) 4)
			(= (litres r2) 1)
			(= (litres r3) 1)
			(= (litres r4) 5)
			(= (litres r5) 2)
			(= (litres r6) 22)
		)
	)
)