(define (problem prob_11_1_10)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 - bottleright
	)
	(:init
		(= (litres l1) 33)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
		(= (litres r8) 0)
		(= (litres r9) 0)
		(= (litres r10) 0)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 2)
			(= (litres r3) 3)
			(= (litres r4) 3)
			(= (litres r5) 2)
			(= (litres r6) 3)
			(= (litres r7) 12)
			(= (litres r8) 3)
			(= (litres r9) 3)
			(= (litres r10) 1)
		)
	)
)