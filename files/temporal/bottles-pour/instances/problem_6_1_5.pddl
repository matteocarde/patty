(define (problem prob_6_1_5)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 30)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(capped l1)
		(capped r1)
		(capped r2)
		(capped r3)
		(capped r4)
		(capped r5)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 16)
			(= (litres r3) 4)
			(= (litres r4) 3)
			(= (litres r5) 2)
		)
	)
)