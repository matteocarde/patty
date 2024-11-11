(define (problem prob_8_1_7)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 - bottleright
	)
	(:init
		(= (litres l1) 24)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
	)
	(:goal
		(and
			(= (litres r1) 3)
			(= (litres r2) 1)
			(= (litres r3) 10)
			(= (litres r4) 3)
			(= (litres r5) 1)
			(= (litres r6) 3)
			(= (litres r7) 3)
		)
	)
)