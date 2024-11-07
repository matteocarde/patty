(define (problem prob_9_1_8)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 - bottleright
	)
	(:init
		(= (litres l1) 27)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
		(= (litres r8) 0)
	)
	(:goal
		(and
			(= (litres r1) 11)
			(= (litres r2) 2)
			(= (litres r3) 1)
			(= (litres r4) 3)
			(= (litres r5) 3)
			(= (litres r6) 3)
			(= (litres r7) 2)
			(= (litres r8) 2)
		)
	)
)